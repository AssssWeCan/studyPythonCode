import unittest
from cityAndCountryFUNCTION import city_and_country

class NameTestCase(unittest.TestCase):
    """测试是否能正确运行"""

    def test_city_and_country(self):
        """测试city_and_country"""
        formatted_name = city_and_country('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago , Chile')

    def test_city_and_country_population(self):
        """测试函数是否可以成功运行population"""
        formatted_name = city_and_country('xian','china', population_number= 50000)
        self.assertEqual(formatted_name,'Xian , China  --  population 50000')

unittest.main