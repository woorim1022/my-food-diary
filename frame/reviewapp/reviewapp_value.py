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

    def __str__(self):
        return str(self.r_id) + ' ' + str(self.rc_id) + ' ' + \
               self.u_id + ' ' + str(self.r_regdate) + ' ' + self.r_name + ' ' + \
               str(self.r_cooktime) + ' ' + self.r_detail + ' ' + str(self.r_image1) + ' ' + \
               str(self.r_image2) + ' ' + str(self.r_image3) + ' ' + str(self.r_image4) + ' ' + str(
            self.r_image5) + ' ' + \
               str(self.r_video) + ' ' + str(self.r_recommend) + ' ' + str(self.r_view) + ' ' + \
               str(self.r_public) + ' ' + self.i_name + ' ' + self.rv_review + ' ' + \
               str(self.r_num) + ' ' + str(self.i_id) + ' ' + str(self.rv_regdate) + ' ';

class Review:
    def __init__(self,u_id,r_id,r_num,rv_review,rv_regdate,r_name,r_image1):
        self.u_id = u_id;
        self.r_id = r_id;
        self.r_num = r_num;
        self.rv_review = rv_review;
        self.rv_regdate = rv_regdate;
        self.r_name = r_name;
        self.r_image1 = r_image1;

    def __str__(self):
        return self.u_id + ' ' + str(self.r_id) + ' ' + str(self.r_num) + ' ' +\
               self.rv_review + str(self.rv_regdate) + ' ' +\
               self.r_name + ' ' + self.r_image1 + ' ';

class ReviewPage:
    def __init__(self,cnt):
        self.cnt = cnt;

    def __str__(self):
        return str(self.cnt) + ' ';