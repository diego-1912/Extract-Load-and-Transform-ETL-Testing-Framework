# Import the unittest module for creating and running tests
import unittest

# Import pandas for handling data structures
import pandas as pd

# Import the DataProcessor class from the src directory to test its functionality
from src.data_processor import DataProcessor

class TestDataTransformation(unittest.TestCase):
    """Test cases for data transformation using DataProcessor"""

    def setUp(self):
        """Set up sample test data before each test case runs"""
        # Creating a sample DataFrame to simulate input data
        self.raw_data = pd.DataFrame({
            "id": [1, 2, 3, 4],  # Sample integer IDs
            "date": ["2023-10-01", "2023-10-02", "invalid_date", "2023-10-04"]  # Date column with a mix of valid and invalid values
        })
    
    def test_date_transformation(self):
        """Test if the 'date' column is correctly converted to datetime format"""
        # Transform the raw data using DataProcessor
        transformed_data = DataProcessor.transform_data(self.raw_data)

        # Check if the 'processed_date' column is recognized as a datetime type
        self.assertTrue(
            pd.api.types.is_datetime64_any_dtype(transformed_data["processed_date"]), 
            "Date conversion failed"  # Error message in case the test fails
        )

    def test_invalid_date_handling(self):
        """Test if invalid date values are handled properly"""
        # Transform the raw data using DataProcessor
        transformed_data = DataProcessor.transform_data(self.raw_data)

        # Ensure that invalid dates are converted to NaT (Not a Time)
        self.assertTrue(
            transformed_data["processed_date"].isnull().sum() > 0, 
            "Invalid date should result in NaT values"  # Error message in case the test fails
        )

# Run the test cases when the script is executed
if __name__ == "__main__":
    unittest.main()
