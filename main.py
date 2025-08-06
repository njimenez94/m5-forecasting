import logging
import os

from src.utils.logger import create_logger
from src.etl.etl_data import etl_data
create_logger()
    
RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"
SALES_FILES = [
        ("sales_train_validation.csv", "sales_train_validation.parquet"),
        ("sales_train_evaluation.csv", "sales_train_evaluation.parquet"), 
        ("sample_submission.csv", "sample_submission.parquet")
    ]

def process_sales_data():
    for raw_file, processed_file in SALES_FILES:
        etl_data(
            sales_file=os.path.join(RAW_DIR, raw_file),
            output_file=os.path.join(PROCESSED_DIR, processed_file)
        )

if __name__ == "__main__":
    process_sales_data()