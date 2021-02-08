class Sql:
    user_ingrlist = """SELECT ui.ui_id,ui.ui_regdate, ifnull(icp.ic_name, ' '),ic.ic_name,i.i_name,ui.ui_exdate From users_ingr ui
                    INNER JOIN ingr i ON ui.i_id = i.i_id
                    INNER JOIN ingr_ct ic ON i.ic_id = ic.ic_id
                    LEFT OUTER JOIN ingr_ct icp ON ic.icp_id = icp.ic_id
                    WHERE ui.u_id = '%s'""";

    user_avoidlist = """SELECT icp.ic_name, ic.ic_name, i.i_name,ui.ui_exdate FROM users_avoid ua
                    INNER JOIN users_ingr ui ON ua.i_id = ui.i_id
                    INNER JOIN ingr i ON ua.i_id = i.i_id
                    INNER JOIN ingr_ct ic ON i.ic_id = ic.ic_id
                    INNER JOIN ingr_ct icp ON ic.icp_id = icp.ic_id
                    WHERE ui.u_id = '%s'""";

    user_ingrinsert = "INSERT INTO users_ingr (u_id,i_id,ui_regdate,ui_exdate) VALUE ('%s',%d,'%s','%s')";
    user_ingrdelete = "DELETE FROM users_ingr WHERE i_id=%d AND u_id='%s' AND ui_exdate='%s'";
    user_ingrupdate = "UPDATE users_ingr SET i_id=%d, ui_exdate='%s' WHERE ui_id=%d";

    ingr_id = "SELECT i_id FROM ingr WHERE i_name='%s'";
    i_name_ingrlist = """SELECT i_name FROM ingr
                        group by i_name""";


    # ingr_ctlist = "SELECT * FROM ingr_ct";
    # ingr_ctlistone = "SELECT * FROM ingr_ct WHERE id=%d";
    # ingr_ctinsert = "INSERT INTO ingr_ct VALUE (%d,'%s',%d)"