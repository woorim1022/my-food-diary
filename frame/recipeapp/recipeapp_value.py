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

class User_Ingr:
    def __init__(self,ui_id,ui_regdate,icp_name,ic_name,i_name,ui_exdate):
        self.ui_id = ui_id;
        self.ui_regdate = ui_regdate;
        self.icp_name = icp_name;
        self.ic_name = ic_name;
        self.i_name = i_name;
        self.ui_exdate = ui_exdate;

    def __str__(self):
        return str(self.ui_id) + ' ' + str(self.ui_regdate) + ' ' +\
               self.icp_name + ' ' + self.ic_name + ' ' + self.i_name + ' ' +\
               str(self.ui_exdate) + ' ';