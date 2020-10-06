import unittest

from more_functions.string_functions import multiply_string


class MyTestCase(unittest.TestCase):
    def test_string_functions(self):
        self.assertEqual(multiply_string("mark", 3), "markmarkmark")


if __name__ == '__main__':
    unittest.main()
