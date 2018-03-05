class Restaurant():
    '''模拟一家餐馆'''
    def __init__(self,restaurant_name,cuisine_type):
        '''初始化name，type'''
        self.name = restaurant_name
        self.type = cuisine_type
        self.served = 0

    def describe_restaurant(self):
        '''打印餐厅基本信息'''
        print(self.name.title() +  ' sells ' + self.type.title() + ' dishes')

    def open_restaurant(self):
        '''描述餐厅状态'''
        print('OPENING, WELCOME!')

    def number_served(self):
        '''打印来过餐厅的人数'''
        print(str(self.served) + ' people have been ' + self.name.title())

    def set_number_served(self,number):
        '''设置就餐过的人数'''
        if number >= self.served :
            self.served = number
        else:
            print('Please check yor number')

    def increase_number_served(self,number):
        '''增加就餐人数'''
        if number>= 0:
            self.served += number
        else:
            print('you can\'t decrease this number')