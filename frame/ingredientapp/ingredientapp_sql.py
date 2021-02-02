class Sql:
    user_ingrlist = """SELECT ui.ui_id,ui.ui_regdate,icp.ic_name,ic.ic_name,i.i_name,ui.ui_exdate From users_ingr ui
                    INNER JOIN ingr i ON ui.i_id = i.i_id
                    INNER JOIN ingr_ct ic ON i.ic_id = ic.ic_id
                    INNER JOIN ingr_ct icp ON ic.icp_id = icp.ic_id""";
    user_avoidlist = """SELECT icp.ic_name, ic.ic_name, i.i_name,ui.ui_exdate FROM users_avoid ua
                    INNER JOIN users_ingr ui ON ua.i_id = ui.i_id
                    INNER JOIN ingr i ON ua.i_id = i.i_id
                    INNER JOIN ingr_ct ic ON i.ic_id = ic.ic_id
                    INNER JOIN ingr_ct icp ON ic.icp_id = icp.ic_id""";

    ingrlistone = "SELECT * FROM ingr WHERE id=%d";
    ingrinsert = "INSERT INTO ingr VALUE (%d,%d,'%s')"

    ingr_ctlist = "SELECT * FROM ingr_ct";
    ingr_ctlistone = "SELECT * FROM ingr_ct WHERE id=%d";
    ingr_ctinsert = "INSERT INTO ingr_ct VALUE (%d,'%s',%d)"
