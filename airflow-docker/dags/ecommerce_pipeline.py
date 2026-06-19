from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="ecommerce_pipeline",
    start_date=datetime(2026, 6, 19),
    schedule=None,
    catchup=False,
) as dag:

    ingest = BashOperator(
        task_id="ingest",
        bash_command="echo Running Ingestion"
    )

    transform = BashOperator(
        task_id="transform",
        bash_command="echo Running Transformation"
    )

    gold = BashOperator(
        task_id="gold_layer",
        bash_command="echo Creating Gold Layer"
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command="echo Running dbt Models"
    )

    ingest >> transform >> gold >> dbt_run