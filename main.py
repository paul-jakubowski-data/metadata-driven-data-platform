from src.ingest import load_data
from src.transform import transform_data
from src.validate import run_validations
from src.metadata import generate_metadata
from src.lineage import generate_lineage


def main() -> None:
    orders_df, customers_df = load_data()
    curated_df = transform_data(orders_df, customers_df)

    validation_df = run_validations(curated_df)
    metadata = generate_metadata(curated_df, "curated_orders")
    lineage = generate_lineage()

    curated_df.to_csv("data/curated/curated_orders.csv", index=False)
    validation_df.to_csv("outputs/validation_report.csv", index=False)

    with open("outputs/metadata_summary.json", "w", encoding="utf-8") as f:
        f.write(metadata)

    with open("outputs/lineage.json", "w", encoding="utf-8") as f:
        f.write(lineage)

    print("Pipeline completed successfully.")


if __name__ == "__main__":
    main()