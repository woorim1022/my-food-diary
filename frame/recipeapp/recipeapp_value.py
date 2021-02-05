# =====================================송현님 코드============================================================
# =====================================송현님 코드============================================================
# class User:
#     def __init__(self, u_id, u_nick, u_pwd, u_name, u_age):
#         self.u_id = u_id;
#         self.u_nick = u_nick;
#         self.u_pwd = u_pwd;
#         self.u_name = u_name;
#         self.u_age = u_age;
#
#     def __str__(self):
#         return self.u_id + ' ' + self.u_pwd + ' ' + self.u_name + ' '\
#                 +self.u_name + ' ' + str(self.u_age) + ' ';

class Recipe:
    def __init__(self, r_id,rc_id,u_id,r_regdate,r_name,r_cooktime,r_detail,r_image1,r_image2,r_image3,r_image4,r_image5,r_video,r_recommend,r_view,r_public,i_name,rv_review,r_num,i_id,rv_regdate):
        self.r_id = r_id;
        self.rc_id = rc_id;
        self.u_id = u_id;
        self.r_regdate = r_regdate;
        self.r_name = r_name;
        self.r_cooktime = r_cooktime;
        self.r_detail = r_detail;
        self.r_image1 = r_image1;
        self.r_image2 = r_image2;
        self.r_image3 = r_image3;
        self.r_image4 = r_image4;
        self.r_image5 = r_image5;
        self.r_video = r_video;
        self.r_recommend = r_recommend;
        self.r_view = r_view;
        self.r_public = r_public;
        self.i_name = i_name;
        self.rv_review = rv_review;
        self.r_num = r_num;
        self.i_id = i_id;
        self.rv_regdate = rv_regdate;

    def __str__(self):
        return str(self.r_id) + ' ' + str(self.rc_id) + ' ' +\
               self.u_id + ' ' + str(self.r_regdate) + ' ' + self.r_name + ' ' +\
               str(self.r_cooktime) + ' ' + self.r_detail + ' ' + str(self.r_image1) + ' ' +\
               str(self.r_image2) + ' ' + str(self.r_image3) + ' ' + str(self.r_image4) + ' ' + str(self.r_image5) + ' ' +\
               str(self.r_video) + ' ' + str(self.r_recommend) + ' ' + str(self.r_view) + ' ' +\
               str(self.r_public) + ' ' + self.i_name + ' ' + self.rv_review + ' ' +\
               str(self.r_num) + ' ' + str(self.i_id) + ' ' + str(self.rv_regdate) + ' ';



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




# class User_Ingr:
#     def __init__(self,ui_id,ui_regdate,icp_name,ic_name,i_name,ui_exdate):
#         self.ui_id = ui_id;
#         self.ui_regdate = ui_regdate;
#         self.icp_name = icp_name;
#         self.ic_name = ic_name;
#         self.i_name = i_name;
#         self.ui_exdate = ui_exdate;
#
#     def __str__(self):
#         return str(self.ui_id) + ' ' + str(self.ui_regdate) + ' ' +\
#                self.icp_name + ' ' + self.ic_name + ' ' + self.i_name + ' ' +\
#                str(self.ui_exdate) + ' ';

# ==============================송현님 코드========================================================================
# ==============================송현님 코드========================================================================

















# =============================우림 코드==============================================================
# =============================우림 코드==============================================================

# 우림이가 만든 레시피 클래스
class Recipe_woorim:
    def __init__(self, r_id,rc_id,u_id,r_regdate,r_name,r_cooktime,r_detail,r_image1,r_image2,r_image3,r_image4,r_image5,r_video,r_recommend,r_view,r_public):
        self.r_id = r_id;
        self.rc_id = rc_id;
        self.u_id = u_id;
        self.r_regdate = r_regdate;
        self.r_name = r_name;
        self.r_cooktime = r_cooktime;
        self.r_detail = r_detail;
        self.r_image1 = r_image1;
        self.r_image2 = r_image2;
        self.r_image3 = r_image3;
        self.r_image4 = r_image4;
        self.r_image5 = r_image5;
        self.r_video = r_video;
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


# =============================우림 코드==========================================================
# =============================우림 코드==========================================================
