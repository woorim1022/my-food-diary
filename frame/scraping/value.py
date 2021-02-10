class Recipe:
    def __init__(self, r_id,rc_id,u_id,r_regdate,r_name,r_cooktime,r_mimage,r_detail,r_dimage,r_recommend,r_view,r_public):
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

    def __str__(self):
        return str(self.r_id) + ' ' + str(self.rc_id) + ' ' +\
               self.u_id + ' ' + str(self.r_regdate) + ' ' + self.r_name + ' ' +\
               str(self.r_cooktime) + ' ' + str(self.r_mimage) + ' ' + str(self.r_detail) + ' ' +\
               str(self.r_dimage) + ' ' +\
               str(self.r_recommend) + ' ' + str(self.r_view) + ' ' +\
               str(self.r_public) + ' ';

class Ingr:
    def __init__(self, i_name):
        self.i_name = i_name;

    def __str__(self):
        self.i_name + ' ';


class Recipe_Test:
    def __init__(self, r_detail):
        self.r_detail = r_detail;

    def __str__(self):
        self.r_detail + ' ';