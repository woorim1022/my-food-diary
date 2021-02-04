from frame.recipeapp.recipeapp_db import Db
from frame.recipeapp.recipeapp_sql import Sql
from frame.recipeapp.recipeapp_value import Recipe
# from recipeapp.views import recipe



class RecipeDb(Db):
    def select(self):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.recipe);
        result = cursor.fetchall();
        all = [];
        for u in result:
            recipe = Recipe(u[0],u[1],u[2],u[3],u[4],u[5],u[6],u[7],u[8],u[9],u[10],u[11],u[12],u[13],u[14],u[15],u[16],u[17],u[18],u[19],u[20]);
            all.append(recipe);
        super().close(conn,cursor);
        return all;



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
# # recipe Test Function ..........
def recipe_test():
    recipe_test = RecipeDb().select();
    for u in recipe_test:
        print(u);

if __name__ == '__main__':
     recipe_test();
