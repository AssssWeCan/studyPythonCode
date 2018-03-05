import UserCLS

class Privileges():
    def __init__(self):
        '''初始化权限'''
        self.privileges = ['CAN ADD POST','CAN DELETE POST','CAN BAN USERS']

    def show_privileges(self):
        '''展示权限'''
        print('ADMIN has the privilege')
        for privileges in self.privileges:
            print(privileges)

    def up_date_privilege(self,message):
        '''增加权限'''
        self.privileges.append(message)

class Admin(UserCLS.User):
    '''创建User子类'''
    def __init__(self,first_name,last_name,user_location,age):
        super().__init__(first_name,last_name,user_location,age)
        self.privileges = Privileges()
