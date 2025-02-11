# ETL Testing Framework with Great Expectations

## 📌 Objective
This framework is designed to validate ETL pipelines using **Great Expectations** in Python. It ensures **data quality, transformation correctness, and integrity** before loading into the data warehouse. The framework enables automated **data validation, profiling, and transformation checks** in a structured and scalable manner.

---

## 📖 User Story
As a **Data Engineer**, I need to validate and test the ETL pipeline to ensure:
- No missing or corrupted data.
- Data conforms to the expected format.
- Transformation rules are correctly applied before the final load.

This ensures **data integrity** and prevents **downstream errors** in the analytics layer.

---

## 📦 Dependencies & Installation
This framework requires the following Python libraries:

### **🔧 Required Libraries**
- `pandas` - For data manipulation.
- `great_expectations` - For data validation.
- `pytest` / `unittest` - For test execution.

### **📥 Installation Steps**
1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/etl-testing-framework.git
   cd etl-testing-framework
   ```
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 💡 Proposed Solution
This framework follows a **modular architecture** with separate modules for:
- **Data Loading** (`data_loader.py`)
- **Data Processing/Transformation** (`data_processor.py`)
- **Data Validation** (`data_validator.py`)

Data validation is performed using **Great Expectations**, and results are logged in `logs/validation_results.json`.

---

## 📂 Project Folder Structure
```
etl_testing_project/
│── data/                           # Raw and processed data files
│   ├── input_data.csv
│── expectations/                    # Great Expectations expectations
│   ├── my_expectations.json
│── logs/                            # Logs for test execution
│   ├── validation_results.json
│── config/                          # Configuration files
│   ├── config.json
│── src/                             # Source code
│   ├── __init__.py
│   ├── data_loader.py               # Module for data loading
│   ├── data_processor.py            # Module for data transformation
│   ├── data_validator.py            # Module for data validation
│── tests/                           # Test cases for different scenarios
│   ├── test_data_quality.py
│   ├── test_data_validation.py
│   ├── test_data_transformation.py
│── main.py                          # Main execution script
│── requirements.txt                  # Dependencies
│── README.md                         # Documentation
```

---

## 📜 Module Breakdown

### `config/config.json`
Stores configuration parameters, such as input data paths and validation rules.

### `data_loader.py`
Loads data from CSV files into a Pandas DataFrame.

### `data_processor.py`
Applies transformations, such as converting date fields into the correct format.

### `data_validator.py`
Uses **Great Expectations** to validate:
- Missing values
- Correct data types
- Date format compliance
- Range validation (e.g., non-negative amounts)

### `tests/test_data_validation.py`
Tests that:
- Required columns are present.
- No null values exist in mandatory fields.
- Data adheres to expected formats.

### `tests/test_data_transformation.py`
Tests that:
- Date fields are properly transformed.
- Invalid dates are handled correctly.

### `main.py`
The execution script that:
1. Loads data.
2. Transforms it.
3. Runs validation tests.
4. Stores validation results in `logs/validation_results.json`.

---

## 🚀 How to Run the Framework

### **1️⃣ Run Data Validation & Transformation Tests**
Execute all test cases using `unittest`:
```bash
python -m unittest discover tests
```
Or use `pytest`:
```bash
pytest tests/
```

### **2️⃣ Run the Full ETL Validation Pipeline**
```bash
python main.py
```
This loads, processes, and validates the data, logging results in `logs/validation_results.json`.

---

## 📊 Logging & Reporting
- **Validation results** are stored in `logs/validation_results.json`.
- Errors and warnings can be checked to diagnose failing cases.

---

## 📌 Additional Notes
- You can modify `expectations/my_expectations.json` to define your own validation rules.
- Future improvements include **database integration** and **CI/CD automation**.

---

## 🛠️ Future Enhancements
✅ Support for **database validation** (e.g., PostgreSQL, MySQL).  
✅ Integration with **Apache Airflow** for automated pipeline validation.  
✅ CI/CD integration to **run tests in GitHub Actions**.  

---

## 📝 Conclusion
This **ETL Testing Framework** ensures that extracted and transformed data adheres to defined rules before final storage. By leveraging **Great Expectations**, it simplifies **data validation** and improves **data pipeline reliability**.

🚀 **Ready to test?** Run `python main.py` and validate your ETL pipeline!
