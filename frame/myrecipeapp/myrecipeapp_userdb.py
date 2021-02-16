from frame.myrecipeapp.myrecipeapp_sql import Sql
from frame.myrecipeapp.myrecipeapp_db import Db
from frame.myrecipeapp.myrecipeapp_value import Recipe


class RecipeDb(Db):
    def selectall(self, u_id, num):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.selectall % (u_id, num));
        result = cursor.fetchall();
        all = [];
        for r in result:
            recipe = Recipe(r[0], r[1], r[2], r[3], r[4], r[5],r[6],r[7],r[8],r[9],r[10],r[11]);
            all.append(recipe);
        super().close(conn, cursor);
        return all;

    def selectall_2(self, u_id):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.selectall_2 % (u_id));
        result = cursor.fetchall();
        all = [];
        for r in result:
            recipe = Recipe(r[0], r[1], r[2], r[3], r[4], r[5],r[6],r[7],r[8],r[9],r[10],r[11]);
            all.append(recipe);
        super().close(conn, cursor);
        return all;

    def select_maxregdate(self, u_id):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.select_maxregdate % (u_id));
        result = cursor.fetchall();
        all = [];
        for r in result:
            recipe = Recipe(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10], r[11]);
            all.append(recipe);
        super().close(conn, cursor);
        return all;

    def select_maxrecommend(self, u_id):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.select_maxrecommend % (u_id));
        result = cursor.fetchall();
        all = [];
        for r in result:
            recipe = Recipe(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10], r[11]);
            all.append(recipe);
        super().close(conn, cursor);
        return all;

    def select_maxview(self, u_id):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.select_maxview % (u_id));
        result = cursor.fetchall();
        all = [];
        for r in result:
            recipe = Recipe(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10], r[11]);
            all.append(recipe);
        super().close(conn, cursor);
        return all;

    def recipepage(self, u_id):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.recipepage % (u_id));
        result = cursor.fetchall();
        all = [];
        for u in result:
            all = u[0];
        super().close(conn, cursor);
        return all;




# userlist Test Function ..........
def userlist_test():
    users = RecipeDb().select_maxregdate('woorim');
    for u in users:
        print(u.u_id,u.r_name);


# def userlistone_test():
#     users = UserDb().selectone('id01');
#     print(users);

if __name__ == '__main__':
    userlist_test();
