import pandas as pd


def load_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    orders_df = pd.read_csv("data/raw/orders.csv")
    customers_df = pd.read_csv("data/raw/customers.csv")
    return orders_df, customers_df