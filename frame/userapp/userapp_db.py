
import MySQLdb

config = {
    'database': 'my_food_diary',
    'userapp': 'root',
    'password': '111111',
    'host':'127.0.0.1',
    'port': 3306,
    'charset':'utf8',
    'use_unicode':True
}
class Db:
    def getConnection(self):
        conn = MySQLdb.connect(**config);
        return conn;

    def close(self, conn, cursor):
        if cursor != None:
            cursor.close();
        if conn != None:
            cursor.close();

# import MySQLdb
#
# config = {
#     'database': 'myfooddiary',
#     'userapp': 'root',
#     'password': '111111',
#     'host':'127.0.0.1',
#     'port': 3306,
#     'charset':'utf8',
#     'use_unicode':True
# }
# class Db:
#     def getConnection(self):
#         conn = MySQLdb.connect(**config);
#         return conn;
#
#     def close(self, conn, cursor):
#         if cursor != None:
#             cursor.close();
#         if conn != None:
#             cursor.close();

