from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args ={
    'owner': 'Shubham',
    'retries': 5,
    'retry_delay': timedelta(minutes= 1)
}

with DAG(                       ## Creatong DAG function and its's parameters (instance)
    dag_id = 'dag_with_catchup_and_backfill-v1',
    default_args= default_args,
    start_date= datetime(2023, 7, 26, 12), ## Start (year, month, date, time(24hr), mins, secs)
    # https://crontab.guru/ to change `schedule_interval` to desired time
    schedule_interval= '0 0 * * *', # same as @daily
    catchup=False  # Default True (it runs from the date given to the current date)
) as dag:                       ## Creating simple TASK using Bash cmd
    task1 = BashOperator(
        task_id= 'Fst_task',
        bash_command= "echo --Simple Task--"       ## Use Bash Language
    )
    