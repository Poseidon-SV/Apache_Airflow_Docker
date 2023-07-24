from datetime import datetime, timedelta #_, for retry_delay

from airflow import DAG
from airflow.operators.python import PythonOperator ## To creat Bash cmd, PythonOperator, etc


default_args ={
    'owner': 'Shubham',
    'retries': 5,
    'retry_delay': timedelta(minutes= 1) ## retry after every 1 min
}

with DAG(
    default_args= default_args
    dag_id= ''
) as dag: