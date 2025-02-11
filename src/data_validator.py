import great_expectations as ge
import json

class DataValidator:
    """Validates data using Great Expectations."""
    
    def __init__(self, dataframe, expectation_suite_file):
        self.df = ge.from_pandas(dataframe)
        with open(expectation_suite_file, "r") as file:
            self.expectation_suite = json.load(file)
    
    def run_validation(self):
        results = self.df.validate(expectation_suite=self.expectation_suite, only_return_failures=True)
        return results
