

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
    def __init__(self,ic_name, i_name):
        self.ic_name = ic_name;
        self.i_name = i_name;
    def __str__(self):
        return self.ic_name+' '+self.i_name

class Recateg:
    def __init__(self,rc_id, rc_name,rcp_id):
        self.rc_id = rc_id;
        self.rc_name = rc_name;
        self.rcp_id = rcp_id;

    def __str__(self):
        return str(self.rc_id)+' '+self.rc_name+' '+str(self.rcp_id)
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

