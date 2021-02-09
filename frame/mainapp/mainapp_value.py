class User:
    def __init__(self, u_id, u_nick, u_pwd, u_name, u_age):
        self.u_id = u_id;
        self.u_nick = u_nick;
        self.u_pwd = u_pwd;
        self.u_name = u_name;
        self.u_age = u_age;

    def __str__(self):
        return self.u_id + ' ' + self.u_pwd + ' ' + self.u_name + ' '\
                +self.u_name + ' ' + str(self.u_age) + ' ';






class Recipe:
    def __init__(self, r_id, rc_id, u_id, r_regdate, r_name, r_cooktime, r_mimage, r_detail, r_dimage, r_recommend,r_view, r_public):
        self.r_id = r_id;
        self.rc_id = rc_id;
        self.u_id = u_id;
        self.r_regdate = r_regdate;
        self.r_name = r_name;
        self.r_cooktime = r_cooktime;
        self.r_mimage = r_mimage;
        self.r_detail = r_detail;
        self.r_dimage = r_dimage;
        self.r_recommend = r_recommend;
        self.r_view = r_view;
        self.r_public = r_public;
    #
    # def __str__(self):
    #     return self.u_id + ' ' + self.u_pwd + ' ' + self.u_name + ' '\
    #             +self.u_name + ' ' + str(self.u_age) + ' ';



class Recipe_recent:
    def __init__(self, visittime, r_id, rc_id, u_id, r_regdate, r_name, r_cooktime, r_mimage, r_detail, r_dimage, r_recommend,r_view, r_public):
        self.visittime = visittime
        self.r_id = r_id;
        self.rc_id = rc_id;
        self.u_id = u_id;
        self.r_regdate = r_regdate;
        self.r_name = r_name;
        self.r_cooktime = r_cooktime;
        self.r_mimage = r_mimage;
        self.r_detail = r_detail;
        self.r_dimage = r_dimage;
        self.r_recommend = r_recommend;
        self.r_view = r_view;
        self.r_public = r_public;


class Review:
    def __init__(self,rv_u_nick, r_num, rv_review, rv_regdate, r_id, rc_id, u_id, r_regdate, r_name, r_cooktime, r_mimage, r_detail, r_dimage, r_recommend,r_view, r_public):
        self.rv_u_nick = rv_u_nick
        self.r_num = r_num
        self.rv_review = rv_review
        self.rv_regdate = rv_regdate
        self.r_id = r_id;
        self.rc_id = rc_id;
        self.u_id = u_id;
        self.r_regdate = r_regdate;
        self.r_name = r_name;
        self.r_cooktime = r_cooktime;
        self.r_mimage = r_mimage;
        self.r_detail = r_detail;
        self.r_dimage = r_dimage;
        self.r_recommend = r_recommend;
        self.r_view = r_view;
        self.r_public = r_public;