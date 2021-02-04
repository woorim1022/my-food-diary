class Sql:
    user_ingrlist = """SELECT ui.ui_id,ui.ui_regdate,icp.ic_name,ic.ic_name,i.i_name,ui.ui_exdate From users_ingr ui
                        INNER JOIN ingr i ON ui.i_id = i.i_id
                        INNER JOIN ingr_ct ic ON i.ic_id = ic.ic_id
                        INNER JOIN ingr_ct icp ON ic.icp_id = icp.ic_id""";

    # userlist = "SELECT * FROM users";
    # userlistone = "SELECT * FROM users WHERE id='%s'";
    # userinsert = "INSERT INTO users VALUE ('%s','%s','%s','%s',%d)";