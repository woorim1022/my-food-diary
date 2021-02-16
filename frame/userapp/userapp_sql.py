class Sql:
    userlist = "SELECT * FROM users";
    userlistone = "SELECT * FROM users WHERE id='%s'";
    userinsert = "INSERT INTO users VALUE ('%s','%s','%s','%s',%d)";
    userupdate = "UPDATE users SET u_nick = '%s', u_pwd = '%s', u_name = '%s', u_age = %d WHERE u_id='%s'"

    ingrselect = """SELECT a.i_id, b.ic_name, a.i_name FROM ingr a
                    INNER JOIN ingr_ct b
                    ON a.ic_id = b.ic_id
                    ORDER BY b.ic_id"""

    ingrselectone = """SELECT a.i_id,  b.ic_name, a.i_name FROM ingr a
                    INNER JOIN ingr_ct b
                    ON a.ic_id = b.ic_id
                    WHERE a.i_name LIKE '%s'
                    ORDER BY b.ic_id"""

    popselect = """SELECT a.i_id, b.ic_name, a.i_name FROM ingr a
                    INNER JOIN ingr_ct b
                    ON a.ic_id = b.ic_id
                    ORDER BY b.ic_id
                    LIMIT 15
                    OFFSET %d"""

    poppage = """SELECT COUNT(*) DIV 15 from ingr a
                    INNER JOIN ingr_ct b
                    ON a.ic_id = b.ic_id"""

    recipeinsert = """INSERT INTO recipe VALUES (null, %d, '%s', '%s', '%s', '%s', '%s', '%s', '%s', %d, %d, %d)"""

    ridselect = """SELECT r_id from recipe
                    WHERE u_id = '%s'
                    ORDER BY r_regdate DESC
                    LIMIT 1"""

    iidselect = """SELECT i_id from ingr
                    WHERE i_name = '%s'"""

    recingrinsert = """INSERT INTO recipe_ingr VALUES (%d, %d, '%s')"""

    allergyselect = """SELECT a.u_id,a.i_id,c.ic_name,b.i_name FROM users_avoid a
                        INNER JOIN ingr b
                        ON a.i_id = b.i_id
                        INNER JOIN ingr_ct c
                        ON b.ic_id = c.ic_id"""

    allergyinsert = """INSERT INTO users_avoid VALUES ('%s', %d)"""

    allergydelete = """DELETE FROM users_avoid WHERE i_id = %d"""