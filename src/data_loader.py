import os
import pandas as pd

class DataLoader:
    """Loads data from different sources."""
    
    @staticmethod
    def load_csv(file_path):
        return pd.read_csv(file_path)
