import json
from datetime import datetime
import pandas as pd


def generate_metadata(df: pd.DataFrame, config: dict) -> str:
    metadata = {
        "dataset_name": config["dataset_name"],
        "row_count": len(df),
        "column_count": len(df.columns),
        "columns": list(df.columns),
        "source_files": config["source_files"],
        "generated_at": datetime.utcnow().isoformat()
    }
    return json.dumps(metadata, indent=2)