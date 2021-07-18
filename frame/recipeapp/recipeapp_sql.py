class Sql:
    # ================================================송현님코드======================================

    # 레시피 테이블에 있는 것과 레시피 대표항목 가져오기
    recipe_selectall = """SELECT r.*, rc.rc_name FROM recipe AS r
                        INNER JOIN recipe_ct rc ON rc.rc_id = r.rc_id
                        WHERE r_id = %d"""

    # 리뷰 데이터 가져오기
    review = """SELECT r.rc_id, r.r_name, rv.* FROM recipe AS r
                    INNER JOIN review rv ON r.r_id = rv.r_id
                    WHERE r.r_id=%d
                    ORDER BY rv_regdate DESC
                    LIMIT 5
                    OFFSET %d""";
    # ORDER BY로 순서 지정(리뷰 작성날짜순)
    # LIMIT으로 1페이지에 몇개 가져올지 지정
    # OFFSET으로 몇번째부터 가져올건지 지정(0일시 1~5,5일시 6~10)

    # 총 페이지 수 확인
    reviewpage = """SELECT COUNT(*) DIV 5 FROM review
                        WHERE r_id = %d"""
    # COUNT로 로우 총 갯수 가져오기
    # 5개 기준으로 1페이지이므로 DIV 5(나눈 정수값을 가져오는 함수)
    # (시작값이 0이여서 추후에 +1 해줘야함)

    # 레시피 식재료
    # ig.i_name = 레시피식재료 이름 re.ri_q = 레시피재료 량
    ingr = """SELECT ig.i_name,re.ri_q from recipe_ingr as re
                    INNER JOIN ingr ig ON re.i_id = ig.i_id
                    WHERE re.r_id=%d"""

    # 리뷰저장
    review_insert = "INSERT INTO review VALUE ('%s',%d,%d,'%s',NOW())";

    # ======================================================우림코드================================================
    # 현재 디비에 있는 모든 레시피 목록을 가져오는 쿼리문
    # recipe.html에서 레시피 리스트에 레시피를 뿌려주기 위해 사용된다
    recipeall= """select r.*, ifnull(AVG(re.r_num),0), count(r.r_id) from recipe as r
	                LEFT OUTER JOIN review re ON r.r_id = re.r_id group by r.r_id
                    LIMIT 20
                	OFFSET %d;"""


    recipe_page = "SELECT COUNT(*) DIV 20 FROM recipe;"

    ingr_page = "SELECT COUNT(*) DIV 18 FROM ingr;"

    recipe_rid = """select r.*, ifnull(AVG(re.r_num),0), count(re.r_id) from recipe as r
	                        LEFT OUTER JOIN review re ON r.r_id = re.r_id 
	                        where r.r_id IN (%s) group by r.r_id
	                        LIMIT 20
                	        OFFSET %d;"""




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
                            LEFT OUTER JOIN ingr_ct icp ON ic.icp_id = icp.ic_id
                            ORDER BY ig.i_name;"""

    # ingredientall = """select ig.*, ic.ic_name, ifnull(icp.ic_name, ' ') as icp_name from ingr as ig
    #                             INNER JOIN ingr_ct ic ON ig.ic_id = ic.ic_id
    #                             LEFT OUTER JOIN ingr_ct icp ON ic.icp_id = icp.ic_id
    #                             LIMIT 18
    #                             OFFSET %d;"""

    ingr_checked = """select * from ingr as i where i.i_id IN (%s)"""


    recipe_ingr = """select r.* from recipe_ingr as re
                        INNER JOIN ingr ig ON re.i_id = ig.i_id
                        INNER JOIN recipe r ON re.r_id = r.r_id
                    where re.i_id=%d;"""

    insert_recent = "INSERT INTO recent VALUE ('%s',%d, NOW());"

    update_r_view = "UPDATE recipe SET r_view = r_view + 1 WHERE r_id=%d;"


    delete = "delete from recipe where r_id=%d;"
    # =====================================================우림코드=============================================

