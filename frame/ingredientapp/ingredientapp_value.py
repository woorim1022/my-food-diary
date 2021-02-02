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

class User_Avoid:
    def __init__(self,icp_name,ic_name,i_name,ui_exdate):
        self.icp_name = icp_name;
        self.ic_name = ic_name;
        self.i_name = i_name;
        self.ui_exdate = ui_exdate;

    def __str__(self):
        return self.icp_name + ' ' + self.ic_name + ' ' + self.i_name + ' ' +\
               str(self.ui_exdate) + ' ';
# class Ingr_ct:
#     def __init__(self, ic_id, ic_name, icp_id):
#         self.ic_id = ic_id;
#         self.ic_name = ic_name;
#         self.icp_id = icp_id;
#
#     def __str__(self):
#         return str(self.ic_id) + ' ' + str(self.icp_id) + ' ' + self.ic_name + ' ';