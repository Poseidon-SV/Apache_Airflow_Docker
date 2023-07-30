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
    schedule_interval= '@daily',
    catchup=False  # Default True (it runs from the date given to the current date)
) as dag:                       ## Creating simple TASK using Bash cmd
    task1 = BashOperator(
        task_id= 'Fst_task',
        bash_command= "echo --Printing first Task using bash cmd-echo--"       ## Use Bash Language
    )
    
    task2 = BashOperator(       ## It'll we be executed after successfull run of task1
        task_id= 'Scnd_task',
        bash_command= "echo --This is 2nd task which will be executed after successfull run of task1--"
    )

    ## Task dependences Added
    task3 = BashOperator(       ## It'll we be executed after successfull run of task2
        task_id= 'Third_task',
        bash_command= "echo --This is 3rd task which will be executed after successfull run of task1 with task2--"
    )


    task1 >> [task2, task3]

    ## Now for the dackfill
    # docker -ps    ## to get container ID of the schedular
    # docker exec -t b2b4f75fcf01fd3ac47f747d1846928ca8a8e780762c77e1706b7cf2a8b169f7 bash
    ## default@b2b4f75fcf01:/opt/airflow$   ## Loged in as a user
    ## start_date  end_date  Dag_ID
    # airflow dags backfill -s 2023-07-12 -e 2023-07-26 dag_with_catchup_and_backfill
    ## it then runs and fill the given date and it can be seen in the DAG localhost