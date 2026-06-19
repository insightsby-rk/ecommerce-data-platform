\# Ecommerce Data Platform



\## Overview



This project demonstrates an end-to-end Data Engineering pipeline using PySpark, dbt, Airflow, Docker, DuckDB, and Medallion Architecture.



\## Architecture



Raw CSV Data

↓

Bronze Layer

↓

Silver Layer (PySpark Transformations)

↓

Gold Layer (Business Aggregations)

↓

dbt Models

↓

Airflow Orchestration



\## Tech Stack



\* Python 3.11

\* PySpark

\* dbt Core

\* DuckDB

\* Apache Airflow

\* Docker

\* GitHub

\* Floci (Local Cloud Services)



\## Features



\* ETL Pipeline Development

\* Data Modeling with dbt

\* Workflow Orchestration with Airflow

\* Bronze, Silver, Gold Architecture

\* Automated Documentation

\* Dockerized Deployment



\## Project Structure



ecommerce-data-platform/

├── data/

├── pyspark/

├── ecommerce\_dbt/

├── airflow-docker/

├── README.md

└── .gitignore



\## Future Enhancements



\* Delta Lake

\* Databricks Integration

\* Azure Data Lake Storage

\* Data Quality Monitoring

\* Incremental Processing



