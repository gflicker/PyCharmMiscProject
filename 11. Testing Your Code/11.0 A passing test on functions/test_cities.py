import unittest

from city_functions import city_country
class TestCities(unittest.TestCase):
    """Unit test for city_functions"""
    def test_city_country(self):
        formatted_city_name = city_country('lusaka', 'zambia')
        self.assertEqual(formatted_city_name, 'Lusaka, Zambia')

    def test_city_population(self):
        formatted_city_name = city_country('lusaka', 'zambia', population=100000)
        self.assertEqual(formatted_city_name, 'Lusaka, Zambia -- Population: 100000')

if __name__ == '__main__':
    unittest.main()