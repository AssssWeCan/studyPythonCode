from unittest import TestCase
from employeeCLS import Employee


class TestEmployee(TestCase):
    """测试employeeCLS是否成功运行"""
    def setUp(self):
        self.sample_employee = Employee('Tong', 'Zhou', 10000)
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
