import json


def generate_lineage(config: dict) -> str:
    lineage = {
            "target_dataset": config["dataset_name"],
            "source_datasets": [
                config["source_files"]["orders"],
                config["source_files"]["customers"]
            ],
            "transformations": [
                "joined orders to customers on customer_id",
                "calculated sales_amount as quantity * unit_price"
            ]
        }
    return json.dumps(lineage, indent=2)