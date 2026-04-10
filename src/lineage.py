import json


def generate_lineage() -> str:
    lineage = {
        "target_dataset": "curated_orders",
        "source_datasets": [
            "data/raw/orders.csv",
            "data/raw/customers.csv"
        ],
        "transformations": [
            "joined orders to customers on customer_id",
            "calculated sales_amount as quantity * unit_price"
        ]
    }
    return json.dumps(lineage, indent=2)