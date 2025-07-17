from pathlib import Path

BASE_DIR = Path(__file__).resolve()
while BASE_DIR.name != "m5-forecasting":
    BASE_DIR = BASE_DIR.parent

# Definición de rutas
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
FEATURES_DIR = DATA_DIR / "features"

SALES_TRAIN_VALIDATION_FILE = RAW_DIR / "sales_train_validation.csv"
CALENDAR_FILE = RAW_DIR / "calendar.csv"
SELL_PRICES_FILE = RAW_DIR / "sell_prices.csv"
