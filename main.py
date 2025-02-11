# Import necessary modules
import os  # Provides functions for interacting with the operating system
import json  # Used to read and write JSON data

# Import custom modules from the src directory
from src.data_loader import DataLoader  # Handles loading CSV data
from src.data_processor import DataProcessor  # Processes and transforms the data
from src.data_validator import DataValidator  # Validates data using expectations

# Define the path to the configuration file
CONFIG_PATH = "config/config.json"

# Load configuration settings from the JSON file
with open(CONFIG_PATH, "r") as file:
    config = json.load(file)  # Read and parse the configuration file into a dictionary

# Load data from the specified CSV file (path is retrieved from config)
data = DataLoader.load_csv(config["input_data_file"])

# Process the loaded data (e.g., convert data types, clean values)
processed_data = DataProcessor.transform_data(data)

# Create a validator object and pass the processed data along with the expectation suite
validator = DataValidator(processed_data, config["expectation_suite"])

# Run data validation against the defined expectations
validation_results = validator.run_validation()

# Ensure the "logs" directory exists; create it if necessary
os.makedirs("logs", exist_ok=True)

# Save the validation results to a JSON file inside the "logs" directory
with open("logs/validation_results.json", "w") as result_file:
    json.dump(validation_results.to_json_dict(), result_file, indent=4)  # Convert results to JSON format

# Print a message to indicate that ETL testing is completed
print("ETL Testing Completed. Check logs/validation_results.json for details.")

