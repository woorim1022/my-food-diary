class Sql:
    userlist = "SELECT * FROM users";
    userlistone = "SELECT * FROM users WHERE id='%s'";
    userinsert = "INSERT INTO users VALUE ('%s','%s','%s','%s',%d)";
    userupdate = "UPDATE users SET u_nick = '%s', u_pwd = '%s', u_name = '%s', u_age = %d WHERE u_id='%s'"

    ingrselect = """SELECT i.ic_id, c.ic_name, i.i_name 
                    FROM ingr i INNER JOIN ingr_ct c
                    ON i.ic_id = c.ic_id"""

    recategselect = """SELECT a.rc_id,b.rc_name,a.rc_name 
                        FROM recipe_ct a INNER JOIN recipe_ct b
                        ON a.rcp_id = b.rc_id"""

    supcselect = """SELECT * FROM recipe_ct
                    WHERE rcp_id is NULL"""

    subcselect = """SELECT distinct rc_name FROM recipe_ct
                    WHERE rcp_id is NOT NULL"""
