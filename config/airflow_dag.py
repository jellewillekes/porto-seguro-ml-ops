from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
    "owner": "airflow",
    "start_date": datetime(2023, 1, 1),
}

with DAG("porto_seguro_pipeline",
         default_args=default_args,
         schedule_interval="@daily") as dag:
    preprocess = BashOperator(
        task_id="preprocess_data",
        bash_command="python /opt/airflow/dags/../scripts/preprocess_data.py "
    )

    train = BashOperator(
        task_id="train_xgb",
        bash_command="python /opt/airflow/dags/../scripts/train_model.py "
    )

    evaluate = BashOperator(
        task_id="evaluate_model",
        bash_command="python /opt/airflow/dags/../scripts/evaluate_model.py "
    )

    # Example pipeline sequence
    preprocess >> train >> evaluate
