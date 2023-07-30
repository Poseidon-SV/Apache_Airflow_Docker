from datetime import datetime, timedelta #_, for retry_delay

from airflow import DAG
from airflow.operators.python import PythonOperator ## To creat Bash cmd, PythonOperator, etc

default_args ={
    'owner': 'Shubham',
    'retries': 5,
    'retry_delay': timedelta(minutes= 1)  ## retry after every 1 min
}

def get_sklearn():
    import sklearn
    print(f"Scikit-learn with version: {sklearn.__version__}")

with DAG(
    default_args= default_args,
    dag_id= '7_dag_with_python_pkgs-v1',
    start_date= datetime(2023, 7, 25, 12),
    schedule_interval='@daily'
) as dag:
    get_sklearn_task = PythonOperator(
        task_id='get_sklearn_task',
        python_callable= get_sklearn
    )

    get_sklearn_task

# RUN docker-compose up -d --no-deps --build airflow-webserver airflow-scheduler

## Login and trigger newly created DAG
## Whenever we change the requiments.txt file we have to rebuild the docker image