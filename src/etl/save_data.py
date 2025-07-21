import pandas as pd

def save_processed_data(df: pd.DataFrame,
                        path: str) -> None:
    """
    Guarda un DataFrame en formato Parquet.

    Parámetros:
    - df: DataFrame a guardar
    """

    try:
        df.to_parquet(path, index=False)
        print(f"Datos guardados exitosamente en {path}")
    except Exception as e:
        print(f"Error al guardar los datos: {e}")
        raise