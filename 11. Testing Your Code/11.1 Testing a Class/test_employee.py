import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def test_give_default(self):
        my_employee = Employee("Larry", "Nasa")
        self.assertEqual(my_employee.give_default(), 'Larry Nasa 5000')

    def test_give_custom_raise(self):
        my_employee = Employee("Rose", "Zulu")
        self.assertEqual(my_employee.give_raise(3000), 'Rose Zulu 8000')

if __name__ == '__main__':
    unittest.main()

