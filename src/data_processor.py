import pandas as pd

class DataProcessor:
    """Processes and transforms data."""
    
    @staticmethod
    def transform_data(df):
        df["processed_date"] = pd.to_datetime(df["date"], errors="coerce")
        return df
