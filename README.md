dbt_analytics_demo

Projeto completo com dbt (Data Build Tool), focado em boas práticas de engenharia analítica, integração de múltiplas fontes de dados e execução automatizada em servidor Linux ou Docker com Apache Airflow.


---

⚙️ Tecnologias e ferramentas

DBT Core 1.7.x

Apache Airflow 2.8.1 (via Docker)

PostgreSQL (local e remoto)

Shell Script (deploy automatizado)

Python (para carga auxiliar de dados)

CSV, Excel e JSON como fontes simuladas

Docker + Docker Compose



---

📁 Estrutura do Projeto

dbt_analytics_demo/
├── models/
│   ├── staging/           # Camada de preparação (ephemeral)
│   ├── marts/             # Camada analítica (view/table/incremental)
├── macros/                # Macros reutilizáveis em Jinja
├── snapshots/             # Snapshots de mudança histórica
├── seeds/                 # Dados estáticos (vendedores.csv)
├── extras/                # Fontes externas (metas.xlsx, filiais.json)
├── scripts/               # Script de carga auxiliar
├── requirements.txt
├── dbt_project.yml
├── Docker/
│   ├── docker-compose.yml
│   ├── .env
│   ├── dags/
│   │   ├── dbt_run_dag.py
│   │   ├── dbt_test_dag.py
│   ├── plugins/
│   ├── logs/               # logs gerados pelo Airflow
│   └── requirements.txt


---

🚀 Como executar localmente (modo tradicional)

1. Clone o projeto e instale o ambiente

git clone git@seu_repo/dbt_analytics_demo.git
cd dbt_analytics_demo
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

2. Configure seu profiles.yml

Arquivo padrão do DBT (em ~/.dbt/profiles.yml):

dbt_analytics_demo:
  target: dev
  outputs:
    dev:
      type: postgres
      host: localhost
      user: postgres
      password: sua_senha
      port: 5432
      dbname: dbt_demo
      schema: public
      threads: 4

3. Carregue os dados

dbt seed                      # Carrega os seeds CSV
python scripts/load_extras.py  # Carrega Excel e JSON no banco

4. Execute o pipeline DBT

dbt run                       # Executa os modelos
dbt test                      # Roda testes automáticos
dbt docs generate && dbt docs serve  # Gera a documentação


---

🐳 Como executar via Docker com Airflow

1. Acesse o diretório do Docker

cd Docker

2. Crie o arquivo .env

EMAIL_SENDER=seuemail@gmail.com
EMAIL_RECEIVER=seuemail@gmail.com
AIRFLOW_ADMIN_EMAIL=admin@example.com
AIRFLOW_ADMIN_PASSWORD=admin
AIRFLOW__CORE__FERNET_KEY=sua_chave_fernet

Gere a chave com:

python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"

3. Suba o Airflow

docker compose up airflow-init
docker compose up -d

Acesse: http://localhost:8080

Usuário: admin@example.com
Senha: admin

4. Execução de comandos dbt dentro do container

docker exec -it airflow-scheduler bash
cd /opt/airflow/dbt_analytics_demo
dbt build
dbt test
dbt docs generate


---

✅ Funcionalidades implementadas

[x] Seeds CSV (vendedores)

[x] Leitura de Excel (.xlsx) com pandas

[x] Leitura de JSON com Python

[x] Camada staging com materialização ephemeral

[x] Marts com view, table e incremental

[x] Snapshots de alterações (ex: status de clientes)

[x] Macros reutilizáveis em Jinja

[x] Testes automatizados

[x] Deploy automático com Git + Bash

[x] Execução agendada com cron ou Airflow

[x] Airflow com DAGs para dbt build e dbt test



---

📚 Recursos úteis

DBT Docs – Macros

dbt-utils Package

Jinja Filters

Curso gratuito oficial



---

✨ Autor

Elias Rodrigues (earlog.dev)
Analista de Dados Sênior | Python + SQL | Engenharia de Dados
GitHub: github.com/eliasantoniorodrigues1
LinkedIn: linkedin.com/in/ear-345-


---

Licença

MIT

