import json
from collections import OrderedDict

from frame.userapp.userapp_sql import Sql
from frame.userapp.userapp_db import Db
from frame.userapp.userapp_value import User, PopIngr, Allergy, Recipe
import datetime


class UserDb(Db):
    def update(self, u_id, u_nick, u_pwd, u_name, u_age):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.userupdate % (u_nick, u_pwd, u_name, u_age, u_id));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(conn, cursor);

    def select(self):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.userlist)
        result = cursor.fetchall();
        all = [];
        for u in result:
            user = User(u[0], u[1], u[2], u[3], u[4]);
            all.append(user);
        super().close(conn, cursor);
        return all;

    def nickselect(self):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.userlist)
        result = cursor.fetchall();
        all = [];
        for n in result:
            all.append(n[1]);
        super().close(conn, cursor);
        return all


class RecipeDb(Db):
    def rselect_fav(self, u_id):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.selectfavoritewithuid % u_id);
        result = cursor.fetchall();
        r_id_list = [];
        for r_id in result:
            # r_id[0] 로 레시피 테이블에서 레시피 정보 가져오자
            # select * from recipe where r_id = 2;
            r_id_list.append(r_id[0])
        format_strings = ",".join(map(str, r_id_list))
        cursor.execute(Sql.recipelist % (format_strings));
        result = cursor.fetchall();
        r_list = [];
        for u in result:
            recipe = Recipe(u[0], u[1], u[2], u[3], u[4], u[5], u[6], u[7], u[8], u[9], u[10], u[11]);
            r_list.append(recipe);
        super().close(conn, cursor);
        return r_list;

    def insert(self, rc_id, u_id, r_regdate, r_name, r_cooktime, r_mimage, r_detail, r_dimage, r_recommend,
               r_view, r_public):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.recipeinsert % (
            rc_id, u_id, r_regdate, r_name, r_cooktime, r_mimage, r_detail, r_dimage, r_recommend,
            r_view, r_public));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(conn, cursor);

    def rselectone(self, u_id):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.ridselect % u_id);
        result = cursor.fetchone()
        result = result[0];
        super().close(conn, cursor);
        return result;


class IngrDb(Db):
    def selectone(self, i_name):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.iidselect % i_name)
        result = cursor.fetchone()
        result = result[0];
        super().close(conn, cursor);
        return result;


class RecipeIngrDb(Db):
    def insert(self, r_id, i_id, ri_q):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.recingrinsert % (r_id, i_id, ri_q));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(conn, cursor);


class PopIngrDb(Db):
    def select(self):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.ingrselect);
        result = cursor.fetchall();
        all = [];
        for u in result:
            item = PopIngr(u[0], u[1], u[2]);
            all.append(item)
        super().close(conn, cursor);
        return all;

    def selectone(self, iname):
        iname = iname + '%';

        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.ingrselectone % iname);
        result = cursor.fetchall();
        all = [];
        for u in result:
            item = PopIngr(u[0], u[1], u[2]);
            all.append(item)
        super().close(conn, cursor);
        return all;

    def popselect(self, num):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.popselect % (num));
        result = cursor.fetchall();
        all = [];
        for u in result:
            item = PopIngr(u[0], u[1], u[2]);
            all.append(item);
        super().close(conn, cursor);
        return all;

    def poppage(self):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.poppage);
        result = cursor.fetchall();
        all = [];
        for u in result:
            all = u[0];
        super().close(conn, cursor);
        return all;


class AllergyDb(Db):
    def select(self):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.allergyselect);
        result = cursor.fetchall();
        all = [];
        for a in result:
            alg = Allergy(a[0], a[1], a[2], a[3]);
            all.append(alg);
        super().close(conn, cursor);
        return all;

    def allergylist(self):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.allergyselect);
        result = cursor.fetchall();
        all = [];
        for a in result:
            all.append(a[1]);
        super().close(conn, cursor);
        return all;

    def delete(self, i_id):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.allergydelete % (i_id));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(conn, cursor);


class UsersAvoidDb(Db):
    def insert(self, u_id, i_id):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.allergyinsert % (u_id, i_id));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(conn, cursor);


def allergyselect_test(name):
    result = PopIngrDb().selectone(name);
    for i in result:
        print(i);
