
import logging
from datetime import datetime


def create_logger():
    # Timestamp para el archivo de log
    #timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    #log_filename = f"logs/{timestamp}_etl_sales_train_validation.log"

    # Configuración de logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            #logging.FileHandler(log_filename),
            logging.StreamHandler()
        ]
    )

    