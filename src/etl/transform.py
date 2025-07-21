import pandas as pd

def long_format_transform(df: pd.DataFrame) -> pd.DataFrame:
    df_long = df.melt(
        id_vars=['id', 'item_id', 'dept_id', 'cat_id', 'store_id', 'state_id'],
        var_name='d',
        value_name='sales'
    )

    return df_long

def convert_columns_to_category(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    for col in cols:
        df[col] = df[col].astype('category')
    return df

def transform_sales_train_validation(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform sales_train_validation DataFrame to long format and convert
    specified columns to category type.

    Parameters:
    - df: DataFrame containing sales data

    Returns:
    - Transformed DataFrame
    """
    df = long_format_transform(df)
    cols_to_category = ['dept_id', 'cat_id', 'store_id', 'state_id']
    df = convert_columns_to_category(df, cols_to_category)

    df['sales'] = df['sales'].astype('int16')
    
    return df


