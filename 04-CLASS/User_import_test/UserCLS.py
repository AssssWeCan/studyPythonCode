class User():
    '''实例化用户'''
    def __init__(self,first_name,last_name,user_location,age):
        '''初始化用户信息'''
        self.first_name = first_name
        self.last_name = last_name
        self.location = user_location
        self.age = age
        self.login = 0

    def describe_user(self):
        '''描述用户'''
        print( self.first_name.title() + ' ' + self.last_name + ' is a ' + self.age  +  ' years old ' + self.location.title()+ ' people ')

    def greet(self):
        '''打印问候语'''
        print('HELLO, ' + self.first_name + ' ' + self.last_name)

    def login_attempt(self):
        '''打印登陆过的用户人数'''
        print(self.login)

    def set_login_attempt(self,number):
        '''设置登陆过的人数'''
        if number >= self.login:
            self.login  = number
        else:
            print('WRONG')

    def increase_login_attempt(self,number):
        '''增加登陆过的人数'''
        if number >= 0:
            self.login += number
        else:
            print('WRONG')

    def reset_login_attempt(self):
        '''重置登陆人数'''
        self.login = 0
