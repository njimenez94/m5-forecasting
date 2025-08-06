import polars as pl
import gc
import logging

from src.utils.logger import create_logger

#from src.etl.etl_calendar import load_calendar

create_logger()

def load_sales(input_file):
    sales_data_dtype = {
       'state_id': pl.Categorical,
       'store_id': pl.Categorical,
       'cat_id': pl.Categorical,
       'dept_id': pl.Categorical,
       'id': pl.Categorical,
       'item_id': pl.Categorical,
       }

    logging.info(f"Loading sales data: {input_file}")
    sales_data = pl.read_csv(
        input_file,
        schema_overrides=sales_data_dtype,
        infer_schema_length=0
    )
    
    logging.info("Unpivot data")
    sales_data = sales_data.unpivot(
        index=['state_id', 'store_id', 'cat_id', 'dept_id', 'id', 'item_id'],
        variable_name='d',
        value_name='sales'
    )

    logging.info("Change type data")
    sales_data = sales_data.with_columns([
        pl.col("d").cast(pl.Categorical),
        pl.col("sales").cast(pl.Int16),
    ])

    return sales_data