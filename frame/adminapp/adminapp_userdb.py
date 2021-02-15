from frame.adminapp.adminapp_db import Db
from frame.adminapp.adminapp_sql import Sql
from frame.adminapp.adminapp_value import Recipe


class UsersDb(Db):
    def select(self,num1,num2):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.users_counter % (num1,num2));
        u = cursor.fetchone();
        super().close(conn,cursor);
        return u[0];

    def recipe_select(self):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.recipe_select);
        result = cursor.fetchall();
        all = [];
        for u in result:
            recipe = Recipe(u[0],u[1],u[2],u[3],u[4]);
            all.append(recipe);
        super().close(conn,cursor);
        return all;





# userlist Test Function ..........
# def userlist_test():
#     users = ReviewDb().select_review();
#     for u in users:
#         print(u);

def users_counter_test(num1,num2):
    counter = UsersDb().select(num1,num2);
    print(counter)

def recipe_select_test():
    recipe = UsersDb().recipe_select();
    for r in recipe:
        print(r)
#
#
#
if __name__ == '__main__':
    # users_counter_test(10,20)
    recipe_select_test()
