#使用代码来测试代码
Python标准库中的`unittest`模块提供了代码的测试工具，单元测试用于核实函数的某个方面没有问题，使用时需要先导入模块、要测试的函数，再创建一个继承`unittest.TestCase`的类
##测试函数
```python
import unittest

def city_and_country(city_name,country_name,population_number = 0):
    """创建对应格式的"城市，国家",并返回"""
    if population_number:
        full_name = city_name.title() + ' , ' + country_name.title() + '  --  population ' + str(population_number)
    else:
        full_name = city_name.title() + ' , ' + country_name.title()
    return full_name

class NameTestCase(unittest.TestCase):
    """测试是否能正确运行"""

    def test_city_and_country(self):
        """测试city_and_country"""
        formatted_name = city_and_country('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago , Chile')

    def test_city_and_country_population(self):
        """测试函数是否可以成功运行population"""
        formatted_name = city_and_country('xian','china',  population_number= 50000)
        self.assertEqual(formatted_name,'Xian , China  --  population 50000')

unittest.main()
```
* 函数`city_and_country()`创建接收一个城市`'santiago'`和所在国家`'chile'`，并返回其整合的信息`'Santiago , Chile'`。当传参中有population信息`population_number= 50000`时，增加一条关于population的信息`'Santiago , Chile  --  population 50000'`  
* 使用继承`unittest.TestCase`的类来测试，类中每一个函数就是一个测试，每个测试函数的开头都应该是**test**,在对`city_and_country`传参后，使用`assertEqual()`可以比较`formatted_name`是否和想象中的相同。
结果为：![结果](http://p4ihydscy.bkt.clouddn.com/blog/180315/gFJm4Jlb4e.png?imageslim)

##测试类
常用断言方法
1.assertEqual(self, first, second, msg=None)  
--判断两个参数相等：first == second  
2.assertNotEqual(self, first, second, msg=None)  
--判断两个参数不相等：first ！= second  
3.assertIn(self, member, container, msg=None)  
--判断是字符串是否包含：member in container  
4.assertNotIn(self, member, container, msg=None)  
--判断是字符串是否不包含：member not in container  
5.assertTrue(self, expr, msg=None)  
--判断是否为真：expr is True  
6.assertFalse(self, expr, msg=None)  
--判断是否为假：expr is False  
7.assertIsNone(self, obj, msg=None)  
--判断是否为None：obj is None  
8.assertIsNotNone(self, obj, msg=None)  
--判断是否不为None：obj is not None  
  
测试类和函数的方法基本一致，但是需要注意测试类需要*实例化*。
###使用setUp()方法测试类（至需要实例化一次）
```python
from unittest import TestCase

class Employee():
    """创建员工信息的类"""
    def __init__(self, first_name, last_name, salary):
        """初始化员工的姓、名、年薪"""
        self.firs_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, others_salary = 0):
        """默认每年增加5000$薪水，也可以自定增加量"""
        if others_salary == 0:
            self.salary += 5000
        else:
            self.salary += others_salary
        return self.salary

class TestEmployee(TestCase):
    """测试employeeCLS是否成功运行"""
    def setUp(self):
        self.sample_employee = Employee('Van', 'Dark', 10000)
        self.increase_salary = 7000

    def test_give_raise(self):
        """测试不输入增加薪水量是否正确"""
        self.sample_employee.give_raise()
        self.assertEqual(self.sample_employee.salary, 15000)

    def test_give_actual_raise(self):
        """测试输入明确的薪水量是否正确"""
        self.sample_employee.give_raise(self.increase_salary)
        self.assertEqual(self.sample_employee.salary, 17000)

if __name__ == '__main__':
    TestCase
```
* 类`Emploryee()`初始化员工姓名、薪水，方法`give_raise()`默认每年增加5000$,现测试默认情况下的类运行情况和自定义薪水增加量的情况。  
* 创建`TestEmployee()`中的函数`setUp()`，并在这个函数中将`Employee()`使用`self`实例化`self.sample_employee`，这样在下面的函数都可以使用这个实例来测试

##另，pycharm中的特殊情况
1. 在实行`unittest()`时出现了*No tests were found*情况，这时需要去掉括号，即`unittest`就可以成功运行，原因我暂时还没弄明白23333333，有机会找大佬指点一下
2. 使用pycharm简便操作可以快速实现*单位测试*，具体为：选定要测试的函数（类），按住**ctrl+shift+T**,弹出选择框，选择*creat new test...*，即可快速生成模版。eg：
![快速生成模版](http://p4ihydscy.bkt.clouddn.com/blog/180315/hg1CKc9hk0.png?imageslim)
3. 也可使用另一种方法代替`unittest.main`
```python
if __name__ == '__main__':
    TestCase
```
输入`TestCase.main`,选择第一个衍生出的框
![另一种执行测试操作](http://p4ihydscy.bkt.clouddn.com/blog/180315/gF940e4F4f.png?imageslim)