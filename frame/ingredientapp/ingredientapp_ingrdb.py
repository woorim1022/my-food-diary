from datetime import date, timedelta

from frame.ingredientapp.ingredientapp_db import Db
from frame.ingredientapp.ingredientapp_sql import Sql
from frame.ingredientapp.ingredientapp_value import User_Ingr, User_Avoid


class User_IngrDb(Db):
    # def selectone(self,i_id):
    #     conn = super().getConnection();
    #     cursor = conn.cursor();
    #     cursor.execute(Sql.user_ingrlistone % i_id);
    #     u = cursor.fetchone();
    #     ingr = User_Ingr(u[0],u[1],u[2]);
    #     super().close(conn,cursor);
    #     return ingr;

    def select(self):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.user_ingrlist);
        result = cursor.fetchall();
        all = [];
        for u in result:
            user_ingr = User_Ingr(u[0],u[1],u[2],u[3],u[4],u[5]);
            all.append(user_ingr);
        super().close(conn,cursor);
        return all;

#     def insert(self,i_id,ic_id,i_name):
#         try:
#             conn = super().getConnection();
#             cursor = conn.cursor();
#             cursor.execute(Sql.ingrinsert % (i_id,ic_id,i_name));
#             conn.commit();
#         except:
#             conn.rollback();
#             raise Exception;
#         finally:
#             super().close(conn, cursor);
#
# class Ingr_ctDb(Db):
#     def selectone(self,ic_id):
#         conn = super().getConnection();
#         cursor = conn.cursor();
#         cursor.execute(Sql.ingr_ctlistone % ic_id);
#         u = cursor.fetchone();
#         ingr_ct = Ingr_ct(u[0],u[1],u[2]);
#         super().close(conn,cursor);
#         return ingr_ct;
#
#     def select(self):
#         conn = super().getConnection();
#         cursor = conn.cursor();
#         cursor.execute(Sql.ingr_ctlist);
#         result = cursor.fetchall();
#         all = [];
#         for u in result:
#             ingr_ct = Ingr_ct(u[0],u[1],u[2]);
#             all.append(ingr_ct);
#         super().close(conn,cursor);
#         return all;
#
#     def insert(self,ic_id,ic_name,icp_id):
#         try:
#             conn = super().getConnection();
#             cursor = conn.cursor();
#             cursor.execute(Sql.ingr_ctinsert % (ic_id,ic_name,icp_id));
#             conn.commit();
#         except:
#             conn.rollback();
#             raise Exception;
#         finally:
#             super().close(conn, cursor);

class User_AvoidDb(Db):
    def select(self):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.user_avoidlist);
        result = cursor.fetchall();
        all = [];
        for u in result:
            user_avoid = User_Avoid(u[0],u[1],u[2],u[3]);
            all.append(user_avoid);
        super().close(conn,cursor);
        return all;

# userlist Test Function ..........
def user_ingrlist_test():
    user_ingrlist = User_IngrDb().select();
    today = date.today()
    ex = timedelta(days=5)
    list = [];
    for u in user_ingrlist:
         list.append(u)
         # print(type(u))
    for l in list:
        print(l.ui_exdate)
        # print(u.ui_exdate)
        # if u.ui_exdate - today > ex:
        #     print(u.ui_exdate)

def user_avoidlist_test():
    user_avoidlist = User_AvoidDb().select();
    today = date.today()
    ex = timedelta(days=5)
    list = [];
    for u in user_avoidlist:
         list.append(u)
         print(u)
         # print(type(u))
    # for l in list:
    #     print(l.ui_exdate)

# def userlistone_test():
#     users = UserDb().selectone('id01');
#     print(users);

if __name__ == '__main__':
    # user_ingrlist_test();
    user_avoidlist_test();