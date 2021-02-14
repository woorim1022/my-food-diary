class Sql:
    selectall = "SELECT * FROM users";
    selectid = "SELECT * FROM users WHERE u_id='%s'";
    selectnick = "SELECT * FROM users WHERE u_nick='%s'";
    userinsert = "INSERT INTO users VALUE ('%s','%s','%s','%s',%d)";
    selectallrecipe = "select * from recipe ORDER BY RAND() LIMIT 8;";

    select_recent = """select re.re_regdate as visittime, r.* from recent as re
                        inner JOIN recipe r ON re.r_id = r.r_id
	                    where re.u_id='%s'
	                    ORDER BY re.re_regdate DESC LIMIT 4;""";

    select_review = """select u.u_nick, rv.r_num, rv.rv_review, rv.rv_regdate, r.* from review as rv
	                    INNER JOIN recipe r ON rv.r_id = r.r_id
	                    INNER JOIN users u ON rv.u_id = u.u_id
                        ORDER BY rv.rv_regdate DESC LIMIT 6;"""


    select_toprecommend = """select *
                            from recipe 
                            ORDER BY r_recommend desc
                            LIMIT 3;
                            """