import datetime

from frame.scraping.db import Db
from frame.scraping.sql import Sql
from frame.scraping.value import Recipe


class RecipeDb(Db):
    def insert(self,r_id,rc_id, u_id, r_regdate, r_name, r_cooktime, r_mimage, r_detail, r_dimage, r_recommend, r_view, r_public):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.recipe_insert % (r_id, rc_id, u_id, r_regdate, r_name, r_cooktime, r_mimage, r_detail, r_dimage, r_recommend, r_view, r_public));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(conn, cursor);

    def ingr_insert(self, r_id, i_id, ri_q):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.recipe_ingr_insert % (r_id, i_id, ri_q));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(conn, cursor);

    def select(self, r_detail):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.recipe_select % (r_detail));
        result = cursor.fetchall();
        all = [];
        for u in result:
            all.append(u[0]);
        super().close(conn, cursor);
        return all;

    def selectall(self,r_id):
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

    def update(self,r_detail,r_name):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.recipe_update % (r_detail,r_name,));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(conn, cursor);


class IngrDb(Db):
    def insert(self,i_id,ic_id,i_name):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.ingr_insert % (i_id,ic_id,i_name));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(conn, cursor);

    def select(self):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.ingr_select);
        result = cursor.fetchall();
        all = [];
        for u in result:
            all.append(u[0]);
        super().close(conn, cursor);
        return all;

    def select_id(self, i_name):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.ingr_id_select % (i_name));
        result = cursor.fetchall();
        for u in result:
            num =u[0];
        super().close(conn, cursor);
        return num;


def recipe_insert_test(r_id, rc_id, u_id, r_regdate, r_name, r_cooktime, r_mimage, r_detail, r_dimage, r_recommend, r_view, r_public):
    RecipeDb().insert(r_id, rc_id, u_id, r_regdate, r_name, r_cooktime, r_mimage, r_detail, r_dimage, r_recommend, r_view, r_public)

def recipe_select_test(r_detail):
    test = RecipeDb().select(r_detail)
    for i in test:
        print(i)

def recipe_selectall_test(r_id):
    test = RecipeDb().selectall(r_id)
    for i in test:
        r_detail = eval(i.r_detail)
        r_dimage = eval(i.r_dimage)

def ingr_insert_test(r_id,i_id,ri_q):
    RecipeDb().ingr_insert(r_id,i_id,ri_q)

# def select_rid_test(r_name):
#     test = RecipeDb().select_rid(r_name)
#     print(test)

def in_insert_test(i_id,ic_id,i_name):
    IngrDb().insert(i_id,ic_id,i_name)

def ingr_select_test():
    print(IngrDb().select());

def ingr_select_id_test(i_name):
    test = IngrDb().select_id(i_name)
    print(test)
    print(type(test))
if __name__ == '__main__':
#     # now = datetime.datetime.now().strftime('%Y-%m-%d %I:%M:%S')
#     # print(now.strftime('%Y-%m-%d %I:%M:%S'))
#     # recipe_insert_test(10,3,None,'2021-02-09 10:55:48','떡갈비',30,'1.jpg','{"1":"손씻기","2":"재료다듬기","3":"요리하기"}','{"1":"1.jpg","2":"2.jpg","3":"3.jpg"}',1,1,1)
#     # recipe_select_test('3')
#     # recipe_selectall_test(1)
#     # time.strftime('%Y-%m-%d %I:%M:%S %p'
     ingr_insert_test(1,1,"2개반")
#     # select_rid_test("단짠단짠의 대패덮밥")
#     in_insert_test(1,1,"갈비살")
#     ingr_select_test()
#     ingr_select_id_test("갈비살")