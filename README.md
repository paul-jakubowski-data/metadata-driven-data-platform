# Metadata-Driven Data Platform

A Python-based simulation of a governed data platform that ingests raw business data, transforms it into curated analytics-ready outputs, and applies configurable validation, metadata, and lineage tracking.

---

## 🚀 Overview

This project demonstrates how modern data platform patterns can be implemented in a modular, scalable way using Python.

It simulates key concepts found in enterprise environments such as:
- Azure Data Factory pipelines
- Microsoft Fabric data workflows
- dbt-style transformations and testing
- governed analytics data products

---

## 🧠 Key Design Principles

### Modular Pipeline Architecture
The pipeline is broken into discrete components:
- ingestion
- transformation
- validation
- metadata generation
- lineage tracking

### Config-Driven Design
All inputs, outputs, and validation rules are externalized in configuration:
- no hardcoded file paths
- no hardcoded validation logic
- easy to extend without modifying code

### Rule-Based Validation Framework
Validation rules are defined in config and executed dynamically, similar to:
- dbt tests
- data quality frameworks (e.g., Great Expectations)

---

## 📊 Business Scenario

The pipeline simulates an ecommerce analytics workflow:

1. Raw order and customer data is ingested
2. Data is joined and transformed into a curated dataset
3. Business rules and data quality checks are applied
4. Metadata and lineage artifacts are generated
5. Outputs are published for downstream analytics use

---

## 🛠️ Tech Stack

- Python
- pandas
- JSON configuration
- CSV (as a stand-in for raw data sources)

---

## 🔄 Pipeline Flow

```
Raw Data → Ingestion → Transformation → Validation → Metadata → Lineage → Outputs
```

---

## 📁 Repository Structure
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