import json
from datetime import datetime
import pandas as pd


def generate_metadata(df: pd.DataFrame, dataset_name: str) -> str:
    metadata = {
        "dataset_name": dataset_name,
        "row_count": len(df),
        "column_count": len(df.columns),
        "columns": list(df.columns),
        "generated_at": datetime.utcnow().isoformat()
    }
    return json.dumps(metadata, indent=2)