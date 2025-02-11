# Import the unittest module to create and execute test cases
import unittest

# Import pandas for data handling
import pandas as pd

# Import the DataValidator class from the src directory to validate data quality
from src.data_validator import DataValidator

class TestDataQuality(unittest.TestCase):
    """Test cases for validating data quality using DataValidator"""

    def setUp(self):
        """Set up sample test data and initialize DataValidator before each test"""
        # Creating a sample DataFrame to simulate input data with missing values
        self.df = pd.DataFrame({
            "id": [1, 2, 3, None],  # The last row contains a missing ID (None)
            "date": ["2023-10-01", "2023-10-02", None, "2023-10-04"]  # One missing date value (None)
        })

        # Initialize DataValidator with the test DataFrame and expectation suite file
        self.validator = DataValidator(self.df, "expectations/my_expectations.json")
    
    def test_missing_values(self):
        """Test if the validation catches missing values in the dataset"""
        # Run validation checks based on expectations
        results = self.validator.run_validation()

        # Ensure that the validation results contain failures due to missing values
        self.assertGreater(
            len(results["results"]), 
            0, 
            "There should be validation failures for missing values."  # Error message if the test fails
        )

# Run the test cases when the script is executed
if __name__ == "__main__":
    unittest.main()
