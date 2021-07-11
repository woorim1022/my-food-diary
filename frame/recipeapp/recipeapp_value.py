# =====================================송현님 코드============================================================
# =====================================송현님 코드============================================================
class Review:
    def __init__(self, rc_id,r_name,u_id,r_id,r_num,rv_review,rv_regdate):
        self.rc_id = rc_id;
        self.r_name = r_name;
        self.u_id = u_id;
        self.r_id = r_id;
        self.r_num = r_num;
        self.rv_review = rv_review;
        self.rv_regdate = rv_regdate;


    def __str__(self):
        return str(self.rc_id) + ' ' +\
               self.r_name + ' ' + self.u_id + ' ' +\
               str(self.r_id) + ' ' + str(self.r_num) + ' ' +\
               str(self.rv_review) + str(self.rv_regdate) + ' ';


class Ingr:
    def __init__(self,i_name,ri_q):
        self.i_name = i_name;
        self.ri_q = ri_q;

    def __str__(self):
        return self.i_name + ' ' + self.ri_q + ' ';



class Recipe:
    def __init__(self, r_id, rc_id, u_id, r_regdate, r_name, r_cooktime, r_mimage, r_detail, r_dimage, r_recommend,
                 r_view, r_public,rc_name):
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
        self.rc_name = rc_name;

    def __str__(self):
        return str(self.r_id) + ' ' + str(self.rc_id) + ' ' + \
               self.u_id + ' ' + str(self.r_regdate) + ' ' + self.r_name + ' ' + \
               str(self.r_cooktime) + ' ' + str(self.r_mimage) + ' ' + str(self.r_detail) + ' ' + \
               str(self.r_dimage) + ' ' + \
               str(self.r_recommend) + ' ' + str(self.r_view) + ' ' + \
               str(self.r_public) + ' ' + str(self.r_public) + ' ';
# ==============================송현님 코드========================================================================
# ==============================송현님 코드========================================================================

















# =============================우림 코드==============================================================
# =============================우림 코드==============================================================

# 우림이가 만든 레시피 클래스
class Recipe_woorim:
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


    def map(self):
        return self.r_id,self.rc_id,self.u_id,self.r_regdate,self.r_name,self.r_cooktime,self.r_detail,self.r_image1,self.r_image2,self.r_image3,self.r_image4,self.r_image5,self.r_video,self.r_recommend,self.r_view,self.r_public;

# 현재 로그인한 사용자가 가지고 있는 식재료를 담을 클래스
class UserIngredient:
    def __init__(self, ui_id, u_id, i_id, ui_regdate, ui_exdate, i_name, ic_name, icp_name):
        self.ui_id = ui_id;
        self.u_id = u_id;
        self.i_id = i_id;
        self.ui_regdate = ui_regdate;
        self.ui_exdate = ui_exdate;
        self.i_name = i_name;
        self.ic_name = ic_name;
        self.icp_name = icp_name;

# 데이터베이스에 존재하는 모든 식재료를 담을 클래스
class Ingredient:
    def __init__(self, i_id, ic_id, i_name, ic_name, icp_name):
        self.i_id = i_id;
        self.ic_id = ic_id;
        self.i_name = i_name;
        self.ic_name = ic_name;
        self.icp_name = icp_name;

class Ingredient_2:
    def __init__(self, i_id, ic_id, i_name):
        self.i_id = i_id;
        self.ic_id = ic_id;
        self.i_name = i_name;

class Recipe_review:
    def __init__(self, r_id,rc_id,u_id,r_regdate,r_name,r_cooktime,r_mimage,r_detail,r_dimage,r_recommend,r_view,r_public,r_num, re_count):
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
        self.r_num = r_num;
        self.re_count = re_count;

class Favorite:
    def __init__(self, u_id, r_id):
        self.u_id = u_id;
        self.r_id = r_id;


# =============================우림 코드==========================================================
# =============================우림 코드==========================================================
