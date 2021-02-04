# from frame.sql import Sql
# from frame.db import Db
# from frame.value import User
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
from frame.recipeapp.recipeapp_db import Db
from frame.recipeapp.recipeapp_sql import Sql
from frame.recipeapp.recipeapp_value import User_Ingr


class User_IngrDb(Db):

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