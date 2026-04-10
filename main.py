from src.config_loader import load_config
from src.ingest import load_data
from src.transform import transform_data
from src.validate import run_validations
from src.metadata import generate_metadata
from src.lineage import generate_lineage


def main() -> None:
    try:
        config = load_config()

        orders_df, customers_df = load_data(config)
        curated_df = transform_data(orders_df, customers_df)

        validation_df = run_validations(curated_df)
        metadata = generate_metadata(curated_df, config)
        lineage = generate_lineage(config)

        curated_df.to_csv(config["outputs"]["curated_orders"], index=False)
        validation_df.to_csv(config["outputs"]["validation_report"], index=False)

        with open(config["outputs"]["metadata_summary"], "w", encoding="utf-8") as f:
            f.write(metadata)

        with open(config["outputs"]["lineage"], "w", encoding="utf-8") as f:
            f.write(lineage)

        print("Pipeline completed successfully.")

    except Exception as e:
        print(f"Pipeline failed: {e}")
        raise


if __name__ == "__main__":
    main()