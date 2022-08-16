# Import libraries
import unittest
from datecalc import when
from datetime import datetime, timedelta

# Create class that inherits TestCase class
class Test_datecalc(unittest.TestCase):
    
    # Create method to assert when function calculates the correct value for the end date
    def test_when(self):
        # Create test date and days variables
        test_date = datetime(2022, 1, 31)
        test_days = 90
        # Create actual and expected variables
        actual = when(test_date, test_days)
        expected = datetime(2022, 5, 1)
        # Create assertion using self.assertEqual() method to test whether actual and expected are equal
        self.assertEqual(actual, expected, 'Should be datetime.datetime(2022, 5, 1, 0, 0)')

# Call unittest.main() when running script from the command-line
if __name__ == '__main__':
    unittest.main()
