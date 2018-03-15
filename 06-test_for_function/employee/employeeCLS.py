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