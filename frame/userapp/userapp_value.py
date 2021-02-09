

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
        return str(self.ic_id)+' '+self.ic_name+' '+self.i_name

class Recateg:
    def __init__(self,rc_id, rcp_name,rc_name):
        self.rc_id = rc_id;
        self.rcp_name = rcp_name;
        self.rc_name = rc_name;

    def __str__(self):
        return str(self.rc_id)+' '+self.rcp_name+' '+self.rc_name
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

