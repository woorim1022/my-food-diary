from frame.recipeapp.recipeapp_db import Db
from frame.recipeapp.recipeapp_sql import Sql
from frame.recipeapp.recipeapp_value import Recipe, Recipe_woorim, UserIngredient, Ingredient, Review, Recipe_review, Favorite, Ingr


# from recipeapp.views import recipe


# =============================================송현님 코드==========================================
# ================================================송현님 코드==========================================

class ReviewDb(Db):
    def select(self, r_id):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.review % (r_id));
        result = cursor.fetchall();
        all = [];
        for u in result:
            review = Review(u[0],u[1],u[2],u[3],u[4],u[5],u[6]);
            all.append(review);
        super().close(conn,cursor);
        return all;


class IngrDb(Db):
    def select(self, r_id):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.ingr % (r_id));
        result = cursor.fetchall();
        all = [];
        for r in result:
            ingr = Ingr(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9],r[10]);
            all.append(ingr);
        super().close(conn, cursor);
        return all;



class RecipeDb(Db):
    def selectall2(self,r_id):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.recipe_selectall % (r_id));
        result = cursor.fetchall();
        all = [];
        for u in result:
            user_ingr = Recipe(u[0], u[1], u[2], u[3], u[4], u[5],u[6],u[7],u[8],u[9],u[10],u[11]);
            all.append(user_ingr);
        super().close(conn, cursor);
        return all;



# ===============================송현님 코드========================================================
# ===============================송현님 코드========================================================

# ================================================우림코드===================================================
# ====================================================================================================================
    def selectall(self, num):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.recipeall % (num));
        result = cursor.fetchall();
        all = [];
        for u in result:
            recipe = Recipe_review(u[0],u[1],u[2],u[3],u[4],u[5],u[6],u[7],u[8],u[9],u[10],u[11],u[12],u[13]);
            all.append(recipe);
        super().close(conn,cursor);
        return all;

    def recipepage(self):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.recipe_page);
        result = cursor.fetchall();
        all = [];
        for u in result:
            all= u[0];
        super().close(conn, cursor);
        return all;

    def select_recipe_with_ingr(self, i_id):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.recipe_ingr % (i_id));
        result = cursor.fetchall();
        all = [];
        for r in result:
            recipe = Recipe_woorim(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9],r[0],r[11]);
            all.append(recipe);
        super().close(conn, cursor);
        return all;

    def select_with_r_id(self, r_id_list, num):
        conn = super().getConnection();
        cursor = conn.cursor();
        # r_id 를 리스트로 받아와서 map으로 모양 맞춰서 sql 에 포맷에 넣
        format_strings = ",".join( map(str, r_id_list) )
        cursor.execute(Sql.recipe_rid % (format_strings, num));
        result = cursor.fetchall();
        all = [];
        for u in result:
            recipe = Recipe_review(u[0],u[1],u[2],u[3],u[4],u[5],u[6],u[7],u[8],u[9],u[10],u[11],u[12],u[13]);
            all.append(recipe);
        super().close(conn,cursor);
        return all;

    def select_f_with_u(self, u_id):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.select_f_with_u % (u_id));
        result = cursor.fetchall();
        all = [];
        for f in result:
            all.append(f[1]);
        super().close(conn, cursor);
        return all;

    def insert_fav(self, u_id, r_id):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.insert_fav % (u_id, r_id));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(conn, cursor);

    def delete_fav(self, u_id, r_id):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.delete_fav % (u_id, r_id));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(conn, cursor);

    def insert_recent(self, u_id, r_id):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.insert_recent % (u_id, r_id));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(conn, cursor);

    def update_r_view(self, r_id):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.update_r_view % (r_id));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(conn, cursor);


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
            all.append(ingredient.i_name);
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
    # RecipeDb().insert_fav('id01', 1);
    RecipeDb().select_with_r_id([1,2,3,4,5], 20);

if __name__ == '__main__':
     review_test();
# =================================송현님 코드===========================================================
# =================================송현님 코드===========================================================