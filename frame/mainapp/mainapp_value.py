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
    def __init__(self,  r_id,rc_id,u_id,r_regdate,r_name,r_cooktime,r_detail,r_image1,r_image2,r_image3,r_image4,r_image5,r_video,r_recommend,r_view,r_public):
        self.r_id=r_id
        self.rc_id=rc_id
        self.u_id=u_id
        self.r_regdate=r_regdate
        self.r_name=r_name
        self.r_cooktime=r_cooktime
        self.r_detail=r_detail
        self.r_image1=r_image1
        self.r_image2=r_image2
        self.r_image3=r_image3
        self.r_image4=r_image4
        self.r_image5=r_image5
        self.r_video=r_video
        self.r_recommend=r_recommend
        self.r_view=r_view
        self.r_public=r_public
    #
    # def __str__(self):
    #     return self.u_id + ' ' + self.u_pwd + ' ' + self.u_name + ' '\
    #             +self.u_name + ' ' + str(self.u_age) + ' ';

