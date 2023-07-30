from datetime import datetime, timedelta #_, for retry_delay

from airflow import DAG
from airflow.operators.python import PythonOperator ## To creat Bash cmd, PythonOperator, etc

### Info
# - Max size of the __Xcoms__ is `48KB` only

def greet():  ## Define py function which'll be scheduled for execution
    print("Hello World!!")

def peraFunc(para_1, para_2):  ## Funnction with operator (Argument)
    # Using op_kwargs we can unpack the paramerters in the dictanory
    print("Python operator using parameter function:",para_1)
    print("this is the second parameter:",para_2)

def return_to_Xcoms():
    return "value returned to Xcoms"

def pull_from_Xcoms(ti):  ## ti is the only var that will pull from Xcoms
    pulled = ti.xcom_pull(task_ids='return_to_Xcoms_task') ## from which task to pull
    print("This is the pulled Xcoms value:", pulled)

def multi_push_Xcoms(ti):
    ti.xcom_push(key='para_1', value='value_1')
    ti.xcom_push(key='para_2', value='value_2')

def multi_pull_Xcoms(ti):
    para_1 = ti.xcom_pull(key='para_1', task_ids='multi_push_Xcoms_task')
    para_2 = ti.xcom_pull(key='para_2', task_ids='multi_push_Xcoms_task')
    print(f"--Value_1 = {para_1}\n--Value_2 = {para_2}")

default_args ={
    'owner': 'Shubham',
    'retries': 5,
    'retry_delay': timedelta(minutes= 1)  ## retry after every 1 min
}

'''1'''
# with DAG(
#     default_args= default_args,
#     dag_id= 'pyOp_dag-v1',
#     description= 'Fst PyOp DAG 28-07-23; 21:42',
#     start_date= datetime(2023, 7, 2, 12),
#     schedule_interval='@daily'
# ) as dag:
#     task1 = PythonOperator(
#         task_id='greet',
#         python_callable=greet
#     )

#     task1

'''2'''
# with DAG(
#     default_args= default_args,
#     dag_id= 'pyOp_dag-v2',
#     description= 'Fst PyOp DAG 28-07-23; 21:42',
#     start_date= datetime(2023, 7, 2, 12),
#     schedule_interval='@daily'
# ) as dag:
#     task1 = PythonOperator(
#         task_id='parameter_task',
#         python_callable=peraFunc,
#         op_kwargs={'para_1': '1st Parameter',
#                    'para_2': '2nd Parameter'}
#     )

#     task1

'''3'''
# with DAG(
#     default_args= default_args,
#     dag_id= 'pyOp_dag-v3',
#     description= 'Fst PyOp DAG 28-07-23; 21:42',
#     start_date= datetime(2023, 7, 2, 12),
#     schedule_interval='@daily'
# ) as dag:
#     # task1 = PythonOperator(
#     #     task_id='parameter_task',
#     #     python_callable=peraFunc,
#     #     op_kwargs={'para_1': '1st Parameter',  ##  From here the function peraFunc will get its values (arguments)
#     #                'para_2': '2nd Parameter'}
#     # )
    
#     task2 = PythonOperator(
#         task_id= 'retun_to_Xcoms_task',
#         python_callable= return_to_Xcoms
#     )

#     # task1
#     task2

'''4'''
# with DAG(
#     default_args= default_args,
#     dag_id= 'pyOp_dag-v4',
#     description= 'Fst PyOp DAG 28-07-23; 21:42',
#     start_date= datetime(2023, 7, 22, 12),
#     schedule_interval='@daily'
# ) as dag:
#     task1 = PythonOperator(
#         task_id='return_to_Xcoms_task',
#         python_callable=return_to_Xcoms
#     )
    
#     task2 = PythonOperator(
#         task_id= 'pull_from_Xcoms_task',
#         python_callable= pull_from_Xcoms
#     )

#     task1 >> task2

'''5'''  ## Multiple values in one function
with DAG(
    default_args= default_args,
    dag_id= 'pyOp_dag-v5',
    description= 'Fst PyOp DAG 28-07-23; 21:42',
    start_date= datetime(2023, 7, 25, 12),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='multi_push_Xcoms_task',
        python_callable= multi_push_Xcoms
    )
    
    task2 = PythonOperator(
        task_id= 'multi_pull_Xcoms_task',
        python_callable= multi_pull_Xcoms
    )

    task1 >> task2