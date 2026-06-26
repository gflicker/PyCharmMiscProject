import unittest
from name_function import get_formatted_name

class NamesTest(unittest.TestCase):
    """Tests for name_function.py."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Do names like 'Janis Joplin Flicker' work?"""
        formatted_name = get_formatted_name('janis', 'joplin', 'flicker')
        self.assertEqual(formatted_name, 'Janis Flicker Joplin')

if __name__ == '__main__':
    unittest.main()