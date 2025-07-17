from pathlib import Path
import pandas as pd
from src.utils.config import (
    SALES_TRAIN_VALIDATION_FILE,
    CALENDAR_FILE,
    SELL_PRICES_FILE
)

FILES = [
    SALES_TRAIN_VALIDATION_FILE,
    CALENDAR_FILE,
    SELL_PRICES_FILE
]

def load_data(path: Path) -> pd.DataFrame:
    """
    Carga un archivo en formato CSV o Parquet según su extensión.

    Parámetros:
    - path: ruta al archivo (Path object)

    Retorna:
    - DataFrame con los datos cargados
    """
    try:
        if path.suffix == ".csv":
            return pd.read_csv(path)
        elif path.suffix == ".parquet":
            return pd.read_parquet(path)
        else:
            raise ValueError(f"Formato no soportado: {path.suffix}")
    except Exception as e:
        print(f"Error al cargar {path.name}: {e}")
        raise

def load_all_data() -> list[pd.DataFrame]:
    """
    Carga todos los archivos definidos en la lista FILES.

    Retorna:
    - Lista de DataFrames en el mismo orden que FILES
    """
    return [load_data(file) for file in FILES]

def load_raw_data() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Carga los tres archivos base de la competencia M5.

    Retorna:
    - sales_train_validation, calendar, sell_prices
    """
    return (
        load_data(SALES_TRAIN_VALIDATION_FILE),
        load_data(CALENDAR_FILE),
        load_data(SELL_PRICES_FILE),
    )
