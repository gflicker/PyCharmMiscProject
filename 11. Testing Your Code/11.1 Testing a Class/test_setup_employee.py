import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.my_employee = Employee("Rose", "Zulu")

    def test_give_default(self):
       self.assertEqual(self.my_employee.give_default(), 'Rose Zulu 5000')

    def test_give_custom_raise(self):
        self.assertEqual(self.my_employee.give_raise(3000), 'Rose Zulu 8000')

if __name__ == '__main__':
    unittest.main()

