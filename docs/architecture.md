# Architecture Overview

This project simulates a small governed data pipeline.

## Flow
1. Raw source data is loaded from CSV files
2. Order and customer data are joined into a curated dataset
3. Validation checks are performed on the curated output
4. Metadata and lineage artifacts are generated
5. Outputs are written for downstream analytics use