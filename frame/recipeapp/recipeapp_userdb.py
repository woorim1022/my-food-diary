from frame.recipeapp.recipeapp_db import Db
from frame.recipeapp.recipeapp_sql import Sql
from frame.recipeapp.recipeapp_value import Recipe, Recipe_woorim, UserIngredient, Ingredient, Review
# from recipeapp.views import recipe


# =============================================송현님 코드==========================================
# ================================================송현님 코드==========================================

class ReviewDb(Db):
    def select(self):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.review);
        result = cursor.fetchall();
        all = [];
        for u in result:
            review = Review(u[0],u[1],u[2],u[3],u[4],u[5],u[6]);
            all.append(review);
        super().close(conn,cursor);
        return all;

# 레시피디테일 이렇게...... 레시피디테일 for문 제거하기
    # def selectone(self,id):
    #     conn = super().getConnection();
    #     cursor = conn.cursor();
    #     cursor.execute(Sql.userlistone % id );
    #     u = cursor.fetchone();
    #     user = User(u[0],u[1],u[2]);
    #     super().close(conn, cursor);
    #     return user;

# # recipe Test Function ..........
# def recipe_test():
#     recipe_test = RecipeDb().select();
#     for u in recipe_test:
#         print(u);
#
# if __name__ == '__main__':
#      recipe_test();









class RecipeDb(Db):
    def select(self):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.recipe);
        result = cursor.fetchall();
        all = [];
        for u in result:
            recipe = Recipe(u[0], u[1], u[2], u[3], u[4], u[5], u[6], u[7], u[8], u[9], u[10], u[11], u[12], u[13],
                            u[14], u[15], u[16], u[17], u[18], u[19], u[20]);
            all.append(recipe);
        super().close(conn, cursor);
        return all;

# ===============================송현님 코드========================================================
# ===============================송현님 코드========================================================

# ================================================우림코드===================================================
# ====================================================================================================================
    def selectall(self):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.recipeall);
        result = cursor.fetchall();
        all = [];
        for u in result:
            recipe = Recipe_woorim(u[0],u[1],u[2],u[3],u[4],u[5],u[6],u[7],u[8],u[9],u[10],u[11],u[12],u[13],u[14],u[15]);
            all.append(recipe);
        super().close(conn,cursor);
        return all;


    def select_recipe_with_ingr(self, i_id):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.recipe_ingr % (i_id));
        result = cursor.fetchall();
        all = [];
        for r in result:
            recipe = Recipe_woorim(r[3],r[4],r[5],r[6],r[7],r[8],r[9],r[10],r[11],r[12],r[13],r[14],r[15],r[16],r[17],r[18]);
            all.append(recipe);
        super().close(conn, cursor);
        return all;

    def select_with_r_id(self, r_id):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.recipe_rid % (r_id));
        result = cursor.fetchall();
        all = [];
        for u in result:
            recipe = Recipe(u[0],u[1],u[2],u[3],u[4],u[5],u[6],u[7],u[8],u[9],u[10],u[11],u[12],u[13],u[14],u[15],u[16],u[17],u[18],u[19],u[20]);
            all.append(recipe);
        super().close(conn,cursor);
        return all;


class IngredientDb(Db):
    # 현재 로그인한 사용자의 식재료"만" 가져오기 위한 함수
    # 매개변수의 u_id는 현재 로그인한 사용자의 아이디
    def selectusersingr(self, u_id):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.usres_ingr % (u_id));
        result = cursor.fetchall();
        all = [];
        for i in result:
            ingredient = UserIngredient(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]);
            all.append(ingredient);
        super().close(conn,cursor);
        return all;

    # 데이터베이스에 존재하는 모든 식재료를 가져오기 위한 함수
    def selectall(self):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.ingredientall);
        result = cursor.fetchall();
        all = [];
        for i in result:
            ingredient = Ingredient(i[0], i[1], i[2], i[3], i[4]);
            all.append(ingredient);
        super().close(conn, cursor);
        return all;
# ==================================================우림코드=================================================
# ==================================================우림코드=================================================















# =============================송현님 코드======================================================
# =============================송현님 코드======================================================
def review_test():
    review_test = ReviewDb().select();
    for u in review_test:
        print(u);

if __name__ == '__main__':
     review_test();
# =================================송현님 코드===========================================================
# =================================송현님 코드===========================================================