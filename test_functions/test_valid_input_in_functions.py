import unittest
from more_functions.validate_input_in_functions import score_input


class MyTestCase(unittest.TestCase):
    def test_score_input_test_score_valid(self):
        self.assertEqual(score_input("pythonTest"), "pythonTest: 0")

    def test_score_input_test_score_below_range(self):
        self.assertEqual(score_input("pythonTest", -50), 'Invalid test score, try again!')
        self.assertEqual(score_input("pythonTest", -10), 'Invalid test score, try again!')

    def test_score_input_test_score_above_range(self):
        self.assertEqual(score_input("pythonTest", 160), 'Invalid test score, try again!')
        self.assertEqual(score_input("pythonTest", 101), 'Invalid test score, try again!')

    def test_test_score_non_numeric(self):
        self.assertEqual(score_input("pythonTest", "me"), 'Invalid test score, try again!')
        self.assertEqual(score_input("pythonTest", "Avery Tilley"), 'Invalid test score, try again!')

    def test_score_input_invalid_message(self):
        self.assertEqual(score_input("pythonTest", 86, "New Invalid"), "pythonTest: 86")
        self.assertEqual(score_input("pythonTest", -55, "New Invalid"), "New Invalid")


if __name__ == '__main__':
    unittest.main()
