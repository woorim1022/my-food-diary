from frame.reviewapp.reviewapp_db import Db
from frame.reviewapp.reviewapp_sql import Sql
from frame.reviewapp.reviewapp_value import Recipe, Review


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

class ReviewPageDb(Db):
    def select_user(self,u_id,num):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.review % (u_id,num));
        result = cursor.fetchall();
        all = [];
        for u in result:
            review = Review(u[0],u[1],u[2],u[3],u[4],u[5],u[6]);
            all.append(review);
        super().close(conn,cursor);
        return all;

    def reviewpage(self,u_id):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.reviewpage % (u_id));
        result = cursor.fetchall();
        all = [];
        for u in result:
            all= u[0];
        super().close(conn, cursor);
        return all;


