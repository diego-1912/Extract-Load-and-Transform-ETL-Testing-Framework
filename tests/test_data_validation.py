# Import the unittest module for creating and executing test cases
import unittest

# Import pandas to handle tabular data
import pandas as pd

# Import the DataValidator class from the src directory to perform validation
from src.data_validator import DataValidator

class TestDataValidation(unittest.TestCase):
    """Test cases for data validation using Great Expectations"""

    def setUp(self):
        """Set up test data before each test case runs"""
        # Creating a sample DataFrame to simulate input data with potential validation issues
        self.test_data = pd.DataFrame({
            "id": [1, 2, None, 4],  # Contains a missing value (None)
            "date": ["2023-10-01", "invalid_date", "2023-10-03", "2023-10-04"],  # One invalid date format
            "amount": [100.5, 200.0, -50, 300.75]  # Contains a negative value (invalid)
        })

        # Initialize DataValidator with test data and an expectation suite file
        self.validator = DataValidator(self.test_data, "expectations/my_expectations.json")

    def test_missing_values(self):
        """Test if the validation detects missing values in the dataset"""
        # Run validation against the defined expectations
        results = self.validator.run_validation()

        # Filter results for missing values (unexpected nulls)
        missing_values = [res for res in results["results"] if "unexpected_index_list" in res]

        # Ensure that at least one validation failure is recorded due to missing values
        self.assertGreater(
            len(missing_values), 
            0, 
            "Missing values should be detected."  # Error message if the test fails
        )

    def test_invalid_date_format(self):
        """Test if the validation detects incorrect date formats"""
        # Run validation against the defined expectations
        results = self.validator.run_validation()

        # Filter results where expectation checks for date formatting issues
        invalid_dates = [
            res for res in results["results"] 
            if "expectation_type" in res and res["expectation_type"] == "expect_column_values_to_match_strftime_format"
        ]

        # Ensure that at least one validation failure is recorded for incorrect date formats
        self.assertGreater(
            len(invalid_dates), 
            0, 
            "Invalid date formats should be detected."  # Error message if the test fails
        )

    def test_negative_amounts(self):
        """Test if the validation detects negative values in the 'amount' column"""
        # Run validation against the defined expectations
        results = self.validator.run_validation()

        # Filter results where expectation checks for values within a valid range
        negative_values = [
            res for res in results["results"] 
            if "expectation_type" in res and res["expectation_type"] == "expect_column_values_to_be_between"
        ]

        # Ensure that at least one validation failure is recorded for negative values
        self.assertGreater(
            len(negative_values), 
            0, 
            "Negative values should be detected."  # Error message if the test fails
        )

# Run the test cases when the script is executed
if __name__ == "__main__":
    unittest.main()
