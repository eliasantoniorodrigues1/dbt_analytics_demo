from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.email import EmailOperator
from airflow.utils.dates import days_ago
from airflow.utils.trigger_rule import TriggerRule
import os

EMAIL_FROM = os.getenv("EMAIL_SENDER")
EMAIL_TO = os.getenv("EMAIL_RECEIVER")

default_args = {
    'owner': 'airflow',
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0
}

with DAG(
    dag_id='dbt_run_dag',
    default_args=default_args,
    description='Executa dbt build via Airflow e notifica por email',
    schedule_interval=None,
    start_date=days_ago(1),
    catchup=False,
    tags=['dbt', 'example']
) as dag:

    notify_start = EmailOperator(
        task_id='notify_start',
        to=EMAIL_TO,
        subject='Airflow DBT DAG Iniciada 🚀',
        html_content='A DAG dbt_run_dag foi iniciada.',
        from_email=EMAIL_FROM
    )

    run_dbt = BashOperator(
        task_id='run_dbt_build',
        bash_command='cd /opt/airflow/dbt_analytics_demo && dbt build',
    )

    notify_success = EmailOperator(
        task_id='notify_success',
        to=EMAIL_TO,
        subject='Airflow DBT DAG Finalizada com Sucesso ✅',
        html_content='A execução do dbt_build foi concluída com sucesso.',
        from_email=EMAIL_FROM,
        trigger_rule=TriggerRule.ALL_SUCCESS
    )

    notify_failure = EmailOperator(
        task_id='notify_failure',
        to=EMAIL_TO,
        subject='Erro na DAG dbt_run_dag ❌',
        html_content='A DAG encontrou um erro durante a execução do dbt.',
        from_email=EMAIL_FROM,
        trigger_rule=TriggerRule.ONE_FAILED
    )

    notify_start >> run_dbt >> [notify_success, notify_failure]
