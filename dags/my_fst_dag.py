from datetime import datetime, timedelta #_, for retry_delay

from airflow import DAG
from airflow.operators.bash import BashOperator ## To creat Bash cmd, PythonOperator, etc


default_args ={
    'owner': 'Shubham',
    'retries': 5,
    'retry_delay': timedelta(minutes= 1) ## retry after every 1 min
}

''' 1 '''
# with DAG(                       ## Creatong DAG function and its's parameters (instance)
#     dag_id = 'my_fst_dag',
#     default_args= default_args,
#     description = 'Fst DAG at 22-06-23; 22:33',
#     start_date= datetime(2023, 6, 12, 12), ## Start (year, month, date, time(24hr), mins, secs)
#     schedule_interval= '@daily'
# ) as dag:                       ## Creating simple TASK using Bash cmd
#     task1 = BashOperator(
#         task_id= 'Fst_task',
#         bash_command= "echo Printing first Task using bash cmd-echo"       ## Use Bash Language
#     )

#     ## Setting the tasks:
#     task1

''' 2 '''
# with DAG(                       ## Creatong DAG function and its's parameters (instance)
#     dag_id = 'my_fst_dag-with-Scnd_task',
#     default_args= default_args,
#     description = 'Fst DAG at 22-06-23; 22:33',
#     start_date= datetime(2023, 6, 12, 12), ## Start (year, month, date, time(24hr), mins, secs)
#     schedule_interval= '@daily'
# ) as dag:                       ## Creating simple TASK using Bash cmd
#     task1 = BashOperator(
#         task_id= 'Fst_task',
#         bash_command= "echo --Printing first Task using bash cmd-echo--"       ## Use Bash Language
#     )
    
#     task2 = BashOperator(       ## It'll we be executed after successfull run of task1
#         task_id= 'Scnd_task',
#         bash_command= "echo --This is 2nd task which will be executed after successfull run of task1--"
#     )

#     ## Setting the stream of the tasks:
#     task1.set_downstream(task2)

''' 3 '''
with DAG(                       ## Creatong DAG function and its's parameters (instance)
    dag_id = 'my_fst_dag-v3',
    default_args= default_args,
    description = 'Fst DAG at 22-06-23; 22:33',
    start_date= datetime(2023, 6, 12, 12), ## Start (year, month, date, time(24hr), mins, secs)
    schedule_interval= '@daily'
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

    ## Setting the stream of the tasks:
    '1'
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)
    '2'
    # task1 >> task2
    # task1 >> task3
    '3'
    task1 >> [task2, task3]