#用类的实例化提高效率
##一、类简介
模拟一家餐厅，餐厅有**名字**`restaurant_name`、**菜的类型**`cuisine_type`
```python
class Restaurant():
    '''模拟一家餐馆'''
    def __init__(self,restaurant_name,cuisine_type):
        '''初始化name，type'''
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        '''打印餐厅基本信息'''
        print(self.name.title() +  ' sells ' + self.type.title() + ' dishes')

    def open_restaurant(self):
        '''描述餐厅状态'''
        print('OPENING, WELCOME!')

    def number_served(self):
        '''打印来过餐厅的人数'''
        print(str(self.served) + ' people have been ' + self.name.title())
```
文件存储为*restaurantCLS.py*   
现在要增加一个餐厅光顾总数的属性,添加`self.served = 0`于
   ` def __init__(self,restaurant_name,cuisine_type):`
此时，我们要增加餐厅光顾过的总数，而且餐厅中来过人数是不能减少的，于是有：
```python
class Restaurant():
    '''模拟一家餐馆'''
    def __init__(self,restaurant_name,cuisine_type):
        '''初始化name，type'''
        self.name = restaurant_name
        self.type = cuisine_type
        self.served = 0
        #增加了self.served属性·····································<<<<<<<<<<<<<<<<<<<<<<<<<<

    def describe_restaurant(self):
        '''打印餐厅基本信息'''
        print(self.name.title() +  ' sells ' + self.type.title() + ' dishes')

    def open_restaurant(self):
        '''描述餐厅状态'''
        print('OPENING, WELCOME!')
```
增加：
```python
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

```
#####小结
* 创建每个类，必须经过初始化，即`__init__`必须存在self，后面的形参根据所需实参调整。  
* 可以在初始化中增加另外的属性`self.served = 0`，且可以在类中通过函数对其做出调整，如`def set_number_served(self,number):`  
  其中主函数调用`set_number_served`传参，通过`number`，进行修改`self.served = 0`  
* 类中的函数是很重要的功能，实例化后可对其进行调用
##二、继承和导入类
```python
import restaurantCLS

class IceCreamStand(restaurantCLS.Restaurant):
    '''创建Restaurant子类'''
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        #super()声明参数············································<<<<<<<<<<<<<<<<<<<<
        self.tastes = ['strawberry','coconut','vanilla']

    def output_taste(self):
        '''展示冰淇淋店的口味'''
        print('WE HAVB :')
        for taste in self.tastes:
            print(taste)
```
存储为*IceCreamStandCLS*
导入类和导入函数基本一致，包括
1.  `from restaurantCLS import Restaurant`(或`from restaurantCLS import Restaurant,others,or_something`)  
&nbsp;不需要声明模块名
2.  `from restaurantCLS import Restaurant as RES`  
&nbsp;不需要声明模块名,且函数名在此程序中替换为 RES
3.  `import restaurantCLS as RESCLS`  
&nbsp;需要声明模块名，但模块名在此程序中替换为RESCLS 
4.  `from restaurantCLS import *`  
&nbsp;引入此模块中所有的函数  (2、3、4并不推荐使用，只为能看懂别人的代码)  
#####小结    
* 继承的父类应写在子类class名后的括号中
* 需要继承父类中的所有属性,并在`super()`中声明，(和父类保持一致的形参父类中`__init__()`中添加的属性，如`self.served = 0`)  
* 导入类后，即可实用化类或继承等操作。
##三、主函数中类的导入
```python
from IceCreamStandCLS import IceCreamStand

my_restaurant = IceCreamStand('Ice Castle','cool')
my_restaurant.set_number_served(44)
my_restaurant.describe_restaurant()
my_restaurant.number_served()
```
当只导入子类`IceCreamStand()`，未导入`Restaurant()`时，函数正常运行，可能是子类中已经导入了父类，所以只导入子类文件时，父类文件也随子类一并导入  

![](http://p4ihydscy.bkt.clouddn.com/blog/180305/Kdmf5KdEi0.png?imageslim)