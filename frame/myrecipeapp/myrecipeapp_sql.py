class Sql:
     selectall = """select *
                    from recipe 
                    where u_id='%s'
                    ORDER BY r_id
                    LIMIT 12
                    OFFSET %d;"""

     selectall_2 = """select *
                         from recipe 
                         where u_id='%s'
                         ORDER BY r_id;"""

     recipepage = """SELECT COUNT(*) DIV 12 FROM recipe
                         WHERE u_id = '%s'"""

     select_maxregdate = """select *
                                from recipe 
                                where u_id='%s'
                                ORDER BY r_regdate desc
                                LIMIT 1;"""

     select_maxrecommend = """select *
                                from recipe 
                                where u_id='%s'
                                ORDER BY r_recommend desc
                                LIMIT 1;
                                """

     select_maxview = """select *
                        from recipe 
                        where u_id='%s'
                        ORDER BY r_view desc
                        LIMIT 1;"""