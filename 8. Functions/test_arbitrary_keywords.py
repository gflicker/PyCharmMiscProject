import unittest
from arbitrary_keywords import build_profile

class TestArbitraryKeywords(unittest.TestCase):
    def test_build_profile(self):
        tested_build = build_profile('John', 'Doe', age = 27, location = 'mazabuka')
        self.assertEqual(tested_build, 'John Doe 27 Mazabuka')

if __name__ == '__main__':
    unittest.main()