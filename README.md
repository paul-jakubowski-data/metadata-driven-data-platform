# Metadata-Driven Data Platform

A Python-based simulation of a governed data product pipeline.

## Purpose
This project demonstrates core data platform concepts:
- ingestion of raw source data
- transformation into curated business-ready outputs
- data validation checks
- metadata generation
- lineage documentation

## Tech Stack
- Python
- pandas
- CSV-based source data

# Metadata-Driven Data Platform

A Python-based simulation of a governed data platform that ingests raw business data, transforms it into curated analytics-ready outputs, and generates validation, metadata, and lineage artifacts.

## Why I Built This
I wanted to create a small but realistic portfolio project that demonstrates how modern data platform patterns can be applied to business data products. This project simulates concepts commonly found in enterprise analytics environments, including governed ingestion, transformation, validation, metadata capture, and lineage documentation.

## Business Scenario
This project uses a simple ecommerce-style order pipeline. Raw order and customer files are loaded, standardized, joined, validated, and published as a curated dataset for downstream analytics use.

## What This Project Demonstrates
- ingestion of raw source data
- transformation into curated business-ready outputs
- validation of business and data quality rules
- metadata generation for published datasets
- lineage documentation from source to target
- clear project structure and modular pipeline design

## Tech Stack
- Python
- pandas
- CSV files for source simulation

## Pipeline Flow
1. Load raw orders and customer data
2. Transform and enrich records into a curated orders dataset
3. Run validation checks on the curated output
4. Generate metadata and lineage artifacts
5. Save outputs for downstream analytics and governance use

## Repository Structure
```
metadata-driven-data-platform/
├── data/
│   ├── raw/
│   └── curated/
├── src/
├── config/
├── docs/
├── outputs/
├── main.py
├── requirements.txt
└── README.md
```

## Outputs
- Curated orders dataset
- Validation report
- Metadata summary
- Lineage document