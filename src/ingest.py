import pandas as pd


def load_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Load raw source datasets for orders and customers.
    """
    try:
        orders_df = pd.read_csv("data/raw/orders.csv")
        customers_df = pd.read_csv("data/raw/customers.csv")
        return orders_df, customers_df
    except Exception as e:
        print(f"Data load failed: {e}")
        raise