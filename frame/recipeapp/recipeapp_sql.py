class Sql:
    # ================================================송현님코드======================================
    recipe_selectall = """SELECT * FROM recipe
                                    WHERE r_id = %d"""

    # 레시피 리뷰
    review = """SELECT r.rc_id, r.r_name, rv.* FROM recipe AS r
                                INNER JOIN review rv ON r.u_id = rv.u_id
                                WHERE r.r_id=%d"""

    # 레시피 식재료
    ingr = """SELECT re.*, ig.i_name, r.rc_id, r.r_name, r.r_regdate, r.r_cooktime, r.r_view, r.r_recommend, rc.rc_name from recipe_ingr as re
                    INNER JOIN ingr ig ON re.i_id = ig.i_id
                    INNER JOIN recipe r ON re.r_id = r.r_id
                    INNER JOIN recipe_ct rc ON rc.rc_id = r.rc_id
                    WHERE re.r_id=%d"""

    # JSON
    json = """SELECT p.id, p.img, r.r_image1 FROM productdb p
                  INNER JOIN recipe r ON p.id = r.r_id
                  WHERE p.id=%d"""
    json1 = """SELECT JSON_VALUE(img,"$.'%s'") FROM productdb"""

    # userlist = "SELECT * FROM users";
    # userlistone = "SELECT * FROM users WHERE id='%s'";
    # userinsert = "INSERT INTO users VALUE ('%s','%s','%s','%s',%d)";
    # ================================================송현님코드===================================










    # ======================================================우림코드================================================
    # 현재 디비에 있는 모든 레시피 목록을 가져오는 쿼리문
    # recipe.html에서 레시피 리스트에 레시피를 뿌려주기 위해 사용된다
    recipeall= """select r.*, ifnull(AVG(re.r_num),0), count(r.r_id) from recipe as r
	                LEFT OUTER JOIN review re ON r.r_id = re.r_id group by r.r_id;"""

    recipe_rid = """select r.*, ifnull(AVG(re.r_num),0), count(re.r_id) from recipe as r
	                LEFT OUTER JOIN review re ON r.r_id = re.r_id where r.r_id=%d group by re.r_id;"""

    select_f_with_u = "select * from favorite where u_id = '%s';"

    insert_fav = "INSERT INTO favorite VALUE ('%s',%d);"
    delete_fav = "DELETE FROM favorite WHERE u_id='%s' AND r_id=%d";

    # 현재 로그인한 사용자가 가지고 있는 식재료를 전부 가져오는 쿼리문
    # recipe.html의 위쪽에 ㅇㅇ님이 가진 식재료 고르기 영역에 ㅇㅇ이 가지고 있는 식재료를 뿌려주기 위해 사용된다
    usres_ingr =  """select ui.*, ig.i_name, ic.ic_name, ifnull(icp.ic_name, ' ') as icp_name from users_ingr as ui
                        INNER JOIN ingr ig ON ui.i_id = ig.i_id
                        INNER JOIN ingr_ct ic ON ig.ic_id = ic.ic_id
                        LEFT OUTER JOIN ingr_ct icp ON ic.icp_id = icp.ic_id 
                    where u_id='%s';"""

    # 현재 디비에 있는 모든 식재료료 목록 가져오는 쿼리문
    ingredientall = """select ig.*, ic.ic_name, ifnull(icp.ic_name, ' ') as icp_name from ingr as ig
                            INNER JOIN ingr_ct ic ON ig.ic_id = ic.ic_id
                            LEFT OUTER JOIN ingr_ct icp ON ic.icp_id = icp.ic_id;"""


    recipe_ingr = """select re.*, ig.i_name, r.* from recipe_ingr as re
                        INNER JOIN ingr ig ON re.i_id = ig.i_id
                        INNER JOIN recipe r ON re.r_id = r.r_id
                    where re.i_id=%d;"""

    insert_recent = "INSERT INTO recent VALUE ('%s',%d, NOW());"

    update_r_view = "UPDATE recipe SET r_view = r_view + 1 WHERE r_id=%d;"
    # =====================================================우림코드=============================================

