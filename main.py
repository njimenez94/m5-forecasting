import logging
import datetime

from src.etl.load_data import load_raw_data
from src.etl.transform import transform_sales_train_validation
from src.etl.save_data import save_processed_data
from src.utils.logger import create_logger


def log_dataframe_stats(df, nombre: str):
    """Log de tamaño y uso de memoria de un DataFrame."""
    logging.info("Computando estadísticas ...")
    rows, cols = df.shape
    mem_usage_gb = df.memory_usage(deep=True).sum() / (1024 ** 3)
    logging.info(f"     📊 DataFrame '{nombre}': {rows:,} filas × {cols:,} columnas")
    logging.info(f"     📦 Uso de memoria: {mem_usage_gb:,.1f} GB")


# Configuración del logger
create_logger()

def main():
    logging.info("🔁 Iniciando proceso de ETL...")

    logging.info("📥 Cargando datos crudos...")
    sales_train_validation, calendar, sell_prices = load_raw_data()
    logging.info("✅ Datos cargados exitosamente.")
    
    logging.info("🧮 Estadísticas de los DataFrames cargados:")
    log_dataframe_stats(sales_train_validation, "sales_train_validation")
    log_dataframe_stats(calendar, "calendar")
    log_dataframe_stats(sell_prices, "sell_prices")

    logging.info("🛠️  Transformando datos: sales_train_validation...")
    sales_train_validation = transform_sales_train_validation(sales_train_validation)
    logging.info("✅ Transformación de datos completa.")

    logging.info("🧮 Estadísticas después de transformación:")
    log_dataframe_stats(sales_train_validation, "sales_train_validation (transformado)")

    logging.info("💾 Guardando datos procesados en Parquet...")
    save_processed_data(df=sales_train_validation,
                        path='data/processed/sales_train_validation.parquet')
    logging.info("✅ Datos guardados exitosamente.")

if __name__ == "__main__":
    main()
