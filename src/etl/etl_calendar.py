import polars as pl
import gc
import logging

from src.utils.logger import create_logger

create_logger()

def load_calendar(input_file = "data/raw/calendar.csv"):
   logging.info("Cargando calendario")
   calendar = (
       pl.read_csv(
           input_file,
           schema_overrides={"date": pl.Date}
       )
       .with_columns([
           pl.col('wm_yr_wk').cast(pl.UInt32),
           pl.col("d").cast(pl.Categorical, strict=False),
           pl.col("date").dt.weekday().cast(pl.UInt8).alias("wday"),
           pl.col("date").dt.week().cast(pl.UInt8).alias("week"),
           pl.col("date").dt.day().cast(pl.UInt8).alias("mday"),
           pl.col("date").dt.month().cast(pl.UInt8).alias("month"),
           pl.col("date").dt.quarter().cast(pl.UInt8).alias("quarter"),
           pl.col("date").dt.year().cast(pl.UInt16).alias("year"),
       ])
       .select(['d', 'wm_yr_wk', 'date', 'year', 'month','quarter', 'week', 'wday', 'mday'])
   )

   return calendar