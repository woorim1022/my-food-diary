
from frame.userapp.userapp_sql import Sql
from frame.userapp.userapp_db import Db
from frame.userapp.userapp_value import User


class UserDb(Db):
    def update(self, id, nick, pwd, name, age):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.userupdate % (nick,pwd,name,age,id));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(conn, cursor);

# from frame.userapp.userapp_sql import Sql
# from frame.userapp.userapp_db import Db
# from frame.userapp.userapp_value import User
#
#
# class UserDb(Db):

#     def selectone(self,id):
#         conn = super().getConnection();
#         cursor = conn.cursor();
#         cursor.execute(Sql.userlistone % id);
#         u = cursor.fetchone();
#         user = User(u[0],u[1],u[2],u[3],u[4]);
#         super().close(conn,cursor);
#         return user;
#
#     def select(self):
#         conn = super().getConnection();
#         cursor = conn.cursor();
#         cursor.execute(Sql.userlist);
#         result = cursor.fetchall();
#         all = [];
#         for u in result:
#             user = User(u[0],u[1],u[2],u[3],u[4]);
#             all.append(user);
#         super().close(conn,cursor);
#         return all;
#
#     def insert(self,u_id,u_nick,u_pwd,u_name,u_age):
#         try:
#             conn = super().getConnection();
#             cursor = conn.cursor();
#             cursor.execute(Sql.userinsert % (u_id,u_nick,u_pwd,u_name,u_age));
#             conn.commit();
#         except:
#             conn.rollback();
#             raise Exception;
#         finally:
#             super().close(conn, cursor);
#
#
# # userlist Test Function ..........
# def userlist_test():
#     users = UserDb().select();
#     for u in users:
#         print(u);
#
# def userlistone_test():
#     users = UserDb().selectone('id01');
#     print(users);
#
# if __name__ == '__main__':
#     userlistone_test();