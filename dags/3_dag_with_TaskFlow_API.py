## API one needs less lines of code as compared to non-API one
from datetime import datetime, timedelta

from airflow.decorators import dag, task

default_args ={
    'owner': 'Shubham',
    'retries': 5,
    'retry_delay': timedelta(minutes= 1)  ## retry after every 1 min
}

'''1'''
# @dag(dag_id='3_dag_with_TaskFlow_API_v1',  ## To define DAG API
#      default_args= default_args,
#      start_date= datetime(2023, 7, 26),
#      schedule_interval= '@daily')

# def dag_API():

#     @task
#     def task1():
#         return 'task1_value'
    
#     @task
#     def task2():
#         return 'task2_value'

#     @task
#     def get_t1t2_value(t1_v, t2_v):
#         print(f"This is: {t1_v} and this is: {t2_v}")

#     t1_v = task1()
#     t2_v = task2()
#     get_t1t2_value(t1_v, t2_v)

'''2'''  ## Pass Multiple parameters
@dag(dag_id='dag_with_TaskFlow_API_v2',  ## To define DAG API
     default_args= default_args,
     start_date= datetime(2023, 7, 26),
     schedule_interval= '@daily')

def dag_API():

    @task(multiple_outputs=True)
    def task1():
        return {
            'o/p_1': 'output_value_1',
            'o/p_2': 'output_value_2'
        }
    
    @task
    def task2():
        return 'task2_value'

    @task
    def get_t1t2_value(op1, op2, t2_v):
        print(f"This is: {op1} - {op2} and this is: {t2_v}")

    t1_v = task1()
    t2_v = task2()
    get_t1t2_value(t1_v['o/p_1'], t1_v['o/p_2'], t2_v)


## we not need to create task1>>tas2 connections it connects itself
call_API = dag_API() ## create the estance of the dag