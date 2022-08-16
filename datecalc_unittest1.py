# Import libraries
import unittest
from datecalc import duration
from datetime import datetime, timedelta

# Create class that inherits TestCase class
class Test_datecalc(unittest.TestCase):
    
    # Create methods to assert duration function calculates the correct value for the difference between two dates
    def test_duration(self):
        # Create test date variables
        test_date1 = datetime(1920, 12, 31)
        test_date2 = datetime(1999, 3, 2)
        # Create actual and expected variables
        actual = duration(test_date1, test_date2)
        expected = 28550
        # Create assertion using self.assertEqual() method to test whether actual and expected are equal
        self.assertEqual(actual, expected, 'Should be 28550')

    def test_duration2(self):
        # Create test date variables
        test_date1 = datetime(3112, 9, 10)
        test_date2 = datetime(5846, 1, 27)
        # Create actual and expected variables
        actual = duration(test_date1, test_date2)
        expected = 998347
        # Create assertion using self.assertEqual() method to test whether actual and expected are equal
        self.assertEqual(actual, expected, 'Should be 998347')

    def test_duration3(self):
        # Create test date variables
        test_date1 = datetime(2023, 2, 8)
        test_date2 = datetime(2022, 7, 19)
        # Create actual and expected variables
        actual = duration(test_date1, test_date2)
        expected = 204
        # Create assertion using self.assertEqual() method to test whether actual and expected are equal
        self.assertEqual(actual, expected, 'Should be 204')

# Call unittest.main() when running script from the command-line
if __name__ == '__main__':
    unittest.main()
