class Sql:
    recipe_insert = """INSERT INTO recipe (r_id,rc_id, u_id, r_regdate, r_name, r_cooktime, r_mimage, r_detail, r_dimage, r_recommend, r_view, r_public)  VALUE (%d,%d,'%s','%s','%s','%s','%s','%s','%s',%d,%d,%d)"""

    recipe_select = """SELECT JSON_VALUE(r_detail,"$.%s") FROM recipe"""
    recipe_selectall = """SELECT * FROM recipe
                            WHERE r_id = %d"""
    recipe_ingr_insert = """INSERT INTO recipe_ingr VALUE (%d,%d,'%s')"""
    ingr_insert = """INSERT INTO ingr VALUE (%d,%d,'%s')"""

    ingr_select = """SELECT i_name FROM ingr"""
    ingr_id_select = """SELECT i_id from ingr
                        WHERE i_name ='%s'"""
    # recipe_select_rid = """select r_id from recipe
    #                         where r_name = '%s'"""





    # ======================================================우림코드================================================
    # 현재 디비에 있는 모든 레시피 목록을 가져오는 쿼리문
    # recipe.html에서 레시피 리스트에 레시피를 뿌려주기 위해 사용된다
    recipeall= """select r.*, ifnull(AVG(re.r_num),0), count(r.r_id) from recipe as r
	                LEFT OUTER JOIN review re ON r.r_id = re.r_id group by r.r_id;"""

    recipe_rid = """select r.*, ifnull(AVG(re.r_num),0), count(re.r_id) from recipe as r
	                LEFT OUTER JOIN review re ON r.r_id = re.r_id where r.r_id=%d group by re.r_id;"""