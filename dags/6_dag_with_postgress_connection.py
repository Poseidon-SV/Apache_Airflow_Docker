## From docker-compose.yaml (README.md)

from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

default_args ={
    'owner': 'Shubham',
    'retries': 5,
    'retry_delay': timedelta(minutes= 1)
}

with DAG(
    dag_id = 'dag_with_postgress_connection-v1',
    default_args= default_args,
    start_date= datetime(2023, 7, 26, 12),
    schedule_interval= '0 0 * * *', #@daily
) as dag: 
    task1 = PostgresOperator(
        task_id= 'create_postgres_table',
        postgres_conn_id='', # Then Create Connection in Admin and fill the form
        sql="""
            create table if not exists dag_runs (
            dt date,
            dag_id character varying,
            primary key (dt, dag_id)
            )
        """
    )
    # task1
    ## See DBeaver to confirm

    task2 = PostgresOperator(
        task_id='insert_into_table',
        postgres_conn_id='postgres_localhost',
        sql="""
            insert into dag_runs (dt, dag_id) values ('{{ ds }}', '{{ dag.dag_id }}')
        """
    )

    # task1>>task2    
    ## then see log to confirm 1 row insterted

    task3 = PostgresOperator(  ## Alwasy delete before execution to avoid data duplication and error
        task_id='delete_data_from_table',
        postgres_conn_id='postgres_localhost',
        sql="""
            delete from dag_runs where dt = '{{ ds }}' and dag_id = '{{ dag.dag_id }}'
        """
    )

    task1>>task3>>task2

    