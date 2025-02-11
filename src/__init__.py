# src/__init__.py
"""
ETL Testing Framework
Modules:
- data_loader: Handles data ingestion
- data_processor: Applies transformations
- data_validator: Uses Great Expectations for validation
"""

from .data_loader import DataLoader
from .data_processor import DataProcessor
from .data_validator import DataValidator
