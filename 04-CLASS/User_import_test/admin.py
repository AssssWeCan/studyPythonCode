import Admin_PrivilegesCLS

admin_1 = Admin_PrivilegesCLS.Admin('tong','zhou','Hanzhong','20')
admin_1.describe_user()
admin_1.privileges.up_date_privilege('play games')
admin_1.privileges.show_privileges()