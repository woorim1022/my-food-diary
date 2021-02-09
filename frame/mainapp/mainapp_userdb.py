from frame.mainapp.mainapp_sql import Sql
from frame.mainapp.mainapp_db import Db
from frame.mainapp.mainapp_value import User, Recipe, Recipe_recent, Review


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


class RecipeDb(Db):
    def select(self):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.selectallrecipe);
        result = cursor.fetchall();
        all = [];
        for r in result:
            recipe = Recipe(r[0], r[1], r[2], r[3], r[4], r[5],r[6],r[7],r[8],r[9],r[10],r[11]);
            all.append(recipe);
        super().close(conn, cursor);
        return all;

    def select_recent(self, u_id):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.select_recent % (u_id));
        result = cursor.fetchall();
        all = [];
        for r in result:
            recipe = Recipe_recent(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10], r[11], r[12]);
            all.append(recipe);
        super().close(conn, cursor);
        return all;


class ReviewDb(Db):
    def select_review(self):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.select_review);
        result = cursor.fetchall();
        all = [];
        for r in result:
            review_r = Review(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10], r[11], r[12],r[13], r[14], r[15]);
            all.append(review_r);
        super().close(conn, cursor);
        return all;





# userlist Test Function ..........
def userlist_test():
    users = ReviewDb().select_review();
    for u in users:
        print(u);


# def userlistone_test():
#     users = UserDb().selectone('id01');
#     print(users);

if __name__ == '__main__':
    userlist_test();
