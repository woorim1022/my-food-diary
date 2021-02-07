class Sql:
    selectall = "SELECT * FROM users";
    selectid = "SELECT * FROM users WHERE u_id='%s'";
    selectnick = "SELECT * FROM users WHERE u_nick='%s'";
    userinsert = "INSERT INTO users VALUE ('%s','%s','%s','%s',%d)";
    selectallrecipe = "select * from recipe";

    #리뷰 데이터 가져오기
    review = """select rv.*,r.r_name,r.r_image1 from review rv
                INNER JOIN recipe r ON rv.r_id = r.r_id
                WHERE rv.u_id = '%s'
                ORDER BY rv_regdate DESC
                LIMIT 5
                OFFSET %d""";
    # ORDER BY로 순서 지정(리뷰 작성날짜순)
    # LIMIT으로 1페이지에 몇개 가져올지 지정
    # OFFSET으로 몇번째부터 가져올건지 지정(0일시 1~5,5일시 6~10)

    #총 페이지 수 확인
    reviewpage = """SELECT COUNT(*) DIV 5 FROM review
                    WHERE u_id = '%s'"""
    #COUNT로 로우 총 갯수 가져오기
    #5개 기준으로 1페이지이므로 DIV 5(나눈 정수값을 가져오는 함수)
    #(시작값이 0이여서 추후에 +1 해줘야함)
