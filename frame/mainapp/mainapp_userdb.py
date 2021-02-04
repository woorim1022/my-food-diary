from frame.mainapp.mainapp_sql import Sql
from frame.mainapp.mainapp_db import Db
from frame.mainapp.mainapp_value import User


class UserDb(Db):
    def selectid(self,id):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.selectid % id);
        u = cursor.fetchone();
        user = User(u[0],u[1],u[2],u[3],u[4]);
        super().close(conn,cursor);
        return user;

    def selectnick(self,nickname):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.selectnick % nickname);
        u = cursor.fetchone();
        user = User(u[0],u[1],u[2],u[3],u[4]);
        super().close(conn,cursor);
        return user;

    def select(self):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.selectall);
        result = cursor.fetchall();
        all = [];
        for u in result:
            user = User(u[0],u[1],u[2],u[3],u[4]);
            all.append(user);
        super().close(conn,cursor);
        return all;

    def insert(self,u_id,u_nick,u_pwd,u_name,u_age):
        try:
            conn = super().getConnection();
            print(conn)
            cursor = conn.cursor();
            cursor.execute(Sql.userinsert % (u_id,u_nick,u_pwd,u_name,u_age));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(conn, cursor);


# userlist Test Function ..........
def userlist_test():
    users = UserDb().select();
    for u in users:
        print(u);

# def userlistone_test():
#     users = UserDb().selectone('id01');
#     print(users);

if __name__ == '__main__':
    userlist_test();