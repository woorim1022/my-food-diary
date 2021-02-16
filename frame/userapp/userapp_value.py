

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

class PopIngr:
    def __init__(self,ic_id, ic_name, i_name):
        self.ic_id = ic_id;
        self.ic_name = ic_name;
        self.i_name = i_name;
    def __str__(self):
        return str(self.ic_id)+' '+self.ic_name+' '+self.i_name;

class PopPage:
    def __init__(self, cnt):
        self.cnt = cnt;

    def __str__(self):
        return str(self.cnt)+' ';

class Recipe:
    def __init__(self, r_id, rc_id, u_id, r_regdate, r_name, r_cooktime, r_mimage, r_detail, r_dimage, r_recommend,
                 r_view, r_public):
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
        return str(self.r_id) + ' ' + str(self.rc_id) + ' ' + \
               self.u_id + ' ' + str(self.r_regdate) + ' ' + self.r_name + ' ' + \
               str(self.r_cooktime) + ' ' + str(self.r_mimage) + ' ' + str(self.r_detail) + ' ' + \
               str(self.r_dimage) + ' ' + \
               str(self.r_recommend) + ' ' + str(self.r_view) + ' ' + \
               str(self.r_public) + ' ';

class RecipeIngr:
    def __init__(self,r_id, i_id, ri_q):
        self.r_id = r_id;
        self.i_id = i_id;
        self.ri_q = ri_q;

    def __str__(self):
        return str(self.r_id)+' '+str(self.i_id)+' '+self.ri_q;

class Ingr:
    def __init__(self, i_id, ic_id, i_name):
        self.i_id = i_id;
        self.ic_id = ic_id;
        self.i_name = i_name;

    def __str__(self):
        return str(self.i_id)+' '+str(self.ic_id)+' '+self.i_name;

class Allergy:
    def __init__(self, u_id, i_id, ic_name,i_name):
        self.u_id = u_id;
        self.i_id = i_id;
        self.ic_name = ic_name;
        self.i_name = i_name;
    def __str__(self):
        return self.u_id+' '+str(self.i_id)+' '+self.ic_name+' '+self.i_name;

class UsersAvoid:
    def __init__(self,u_id,i_id):
        self.u_id = u_id;
        self.i_id = i_id;
    def __str__(self):
        return self.u_id+' '+str(self.i_id);