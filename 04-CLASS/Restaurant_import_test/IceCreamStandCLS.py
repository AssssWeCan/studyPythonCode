import restaurantCLS

class IceCreamStand(restaurantCLS.Restaurant):
    '''创建Restaurant子类'''
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.tastes = ['strawberry','coconut','vanilla']

    def output_taste(self):
        '''展示冰淇淋店的口味'''
        print('WE HAVB :')
        for taste in self.tastes:
            print(taste)