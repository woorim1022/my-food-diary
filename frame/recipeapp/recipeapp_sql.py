class Sql:
    recipe = """SELECT r.*, ig.i_name, rv.rv_review, rv.r_num, ui.i_id, rv.rv_regdate FROM recipe AS r
                        INNER JOIN users_ingr ui ON r.u_id = ui.u_id
                        INNER JOIN ingr ig ON ui.i_id = ig.i_id
                        INNER JOIN ingr_ct ic ON ig.ic_id = ic.ic_id
                        INNER JOIN review rv ON r.u_id = rv.u_id
                        INNER JOIN favorite fv ON r.r_id = fv.r_id
                        INNER JOIN recipe_ingr ri ON r.r_id = ri.r_id""";

    # userlist = "SELECT * FROM users";
    # userlistone = "SELECT * FROM users WHERE id='%s'";
    # userinsert = "INSERT INTO users VALUE ('%s','%s','%s','%s',%d)";