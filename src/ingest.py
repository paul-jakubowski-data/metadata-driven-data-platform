import pandas as pd
import logging

logger = logging.getLogger(__name__)

def load_data(config: dict) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Load raw source datasets for orders and customers.
    """
    try:
        logger.info("Loading source data")

        orders_df = pd.read_csv(config["source_files"]["orders"])
        customers_df = pd.read_csv(config["source_files"]["customers"])
        
        logger.info("Source data loaded successfully")
        
        return orders_df, customers_df
    except Exception as e:
        logger.error(f"Data load failed: {e}")
        raise