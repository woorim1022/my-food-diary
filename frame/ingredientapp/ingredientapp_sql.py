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

    user_ingrinsert = "INSERT INTO users_ingr VALUE (%d,'%s',%d,'%s','%s')"
    user_ingrdelete = "DELETE FROM users_ingr WHERE i_id=%d AND ui_exdate='%s'";


    ingr_id = "SELECT i_id FROM ingr WHERE i_name='%s'";
    ingrlist = """SELECT icp.ic_name, icp.ic_id, ic.ic_name, ic.ic_id, i.i_name, i.i_id  FROM ingr i
                INNER JOIN ingr_ct ic ON i.ic_id = ic.ic_id
                INNER JOIN ingr_ct icp ON ic.icp_id = icp.ic_id""";
    icp_name_ingrlist = """SELECT icp.ic_name FROM ingr i
                INNER JOIN ingr_ct ic ON i.ic_id = ic.ic_id
                INNER JOIN ingr_ct icp ON ic.icp_id = icp.ic_id
                group by icp.ic_name""";
    ic_name_ingrlist = """SELECT ic.ic_name FROM ingr i
                INNER JOIN ingr_ct ic ON i.ic_id = ic.ic_id
                INNER JOIN ingr_ct icp ON ic.icp_id = icp.ic_id
                group by ic.ic_name""";
    i_name_ingrlist = """SELECT i_name FROM ingr
                        group by i_name""";


    ingr_ctlist = "SELECT * FROM ingr_ct";
    ingr_ctlistone = "SELECT * FROM ingr_ct WHERE id=%d";
    ingr_ctinsert = "INSERT INTO ingr_ct VALUE (%d,'%s',%d)"