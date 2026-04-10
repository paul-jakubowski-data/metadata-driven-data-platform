import pandas as pd


def load_data(config: dict) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Load raw source datasets for orders and customers.
    """
    try:
        orders_df = pd.read_csv(config["source_files"]["orders"])
        customers_df = pd.read_csv(config["source_files"]["customers"])
        return orders_df, customers_df
    except Exception as e:
        print(f"Data load failed: {e}")
        raise