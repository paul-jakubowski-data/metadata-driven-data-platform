import json


def load_config(config_path: str = "config/pipeline_config.json") -> dict:
    """
    Load pipeline configuration from a JSON file.
    """
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)