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
    dag_id='dbt_test_dag',
    default_args=default_args,
    description='Executa dbt test via Airflow e envia notificações',
    schedule_interval=None,
    start_date=days_ago(1),
    catchup=False,
    tags=['dbt', 'test']
) as dag:

    notify_start = EmailOperator(
        task_id='notify_start_test',
        to=EMAIL_TO,
        subject='Airflow DBT Test DAG Iniciada 🧪',
        html_content='A DAG dbt_test_dag foi iniciada.',
        from_email=EMAIL_FROM
    )

    run_dbt_test = BashOperator(
        task_id='run_dbt_test',
        bash_command='cd /opt/airflow/dbt_analytics_demo && dbt test',
    )

    notify_success = EmailOperator(
        task_id='notify_success_test',
        to=EMAIL_TO,
        subject='DBT Test Finalizado com Sucesso ✅',
        html_content='Todos os testes do dbt foram concluídos com sucesso.',
        from_email=EMAIL_FROM,
        trigger_rule=TriggerRule.ALL_SUCCESS
    )

    notify_failure = EmailOperator(
        task_id='notify_failure_test',
        to=EMAIL_TO,
        subject='Erro ao Rodar dbt test ❌',
        html_content='Um ou mais testes do dbt falharam.',
        from_email=EMAIL_FROM,
        trigger_rule=TriggerRule.ONE_FAILED
    )

    notify_start >> run_dbt_test >> [notify_success, notify_failure]
