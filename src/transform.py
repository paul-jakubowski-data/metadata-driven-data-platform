import pandas as pd


def transform_data(orders_df: pd.DataFrame, customers_df: pd.DataFrame) -> pd.DataFrame:
    df = orders_df.merge(customers_df, on="customer_id", how="left")
    df["sales_amount"] = df["quantity"] * df["unit_price"]
    return df