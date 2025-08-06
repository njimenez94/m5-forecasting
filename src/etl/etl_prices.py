import polars as pl
import gc
import logging

from src.utils.logger import create_logger

#from src.etl.etl_calendar import load_calendar

create_logger()

def load_prices(input_file='data/raw/sell_prices.csv'):
    sell_price_dtype = {
       'store_id': pl.Categorical,
       'item_id': pl.Categorical,
       'wm_yr_wk': pl.UInt32,
       'sell_price': pl.Float32
   }

    logging.info(f"Loading sales data: {input_file}")
    sell_prices = pl.read_csv(
       input_file,
       schema_overrides=sell_price_dtype,
       infer_schema_length=0
   ) 

    return sell_prices