import polars as pl
import gc
import logging

from src.utils.logger import create_logger

from src.etl.etl_calendar import load_calendar
from src.etl.etl_sales import load_sales
from src.etl.etl_prices import load_prices

create_logger()

def etl_data(sales_file, output_file):
    logging.info(f"Loading {sales_file}")
    sales_data = load_sales(sales_file)

    logging.info("Loading calendar")
    calendar = load_calendar()

    logging.info("Loading prices")
    sell_prices = load_prices()

    logging.info("Joining calendar")
    sales_data = sales_data.join(calendar,on='d', how='left')

    logging.info("Joining prices")
    sales_data = sales_data.join(sell_prices, on=['wm_yr_wk', 'store_id', 'item_id'], how='left')
    
    logging.info("Sorting data")
    sales_data = sales_data.sort(["state_id", "store_id", "cat_id", "dept_id", "item_id", "date"])

    logging.info("Selecting columns")
    sales_data = sales_data.select([
           "id", "state_id", "store_id", "cat_id", "dept_id", "item_id", 
           "date", "year", "quarter", "month", "week", "wday", "mday", "sell_price", "sales"
       ])
    
    logging.info("Saving data")
    sales_data.write_parquet(output_file)

    logging.info(f"Data processed save in: {output_file}")