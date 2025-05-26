# Projeto dbt_analytics_demo

Este projeto demonstra como utilizar o **dbt** integrado ao **Apache Airflow** usando **Docker**, ideal para pipelines analíticos reproduzíveis e automatizados.

## 🔧 Tecnologias Utilizadas
- [dbt (Data Build Tool)](https://www.getdbt.com/)
- [Apache Airflow](https://airflow.apache.org/)
- [Docker](https://www.docker.com/)
- PostgreSQL
- Python 3.11

---

## 📁 Estrutura de Pastas

```
📦 dbt_analytics_demo/
├── dbt_project.yml
├── models/
├── seeds/
├── macros/
├── tests/
├── target/                   # gerado pelo dbt build
├── profiles.yml              # opcional, se necessário
├── Docker/
│   ├── docker-compose.yml    # stack do Airflow com Postgres
│   ├── .env                  # variáveis de ambiente (emails, senhas, etc)
│   ├── dags/
│   │   ├── dbt_run_dag.py
│   │   ├── dbt_test_dag.py
│   │   └── outros_dags.py
│   ├── plugins/              # plugins customizados (opcional)
│   ├── logs/                 # gerado pelo Airflow
│   └── requirements.txt      # opcional: dependências extras
```

---

## 🚀 Como Rodar com Docker

```bash
# Vá até o diretório Docker
cd Docker

# Inicie os serviços do Airflow
docker compose up airflow-init

# Depois de inicializado, suba o ambiente completo
docker compose up -d
```

Acesse a interface do Airflow em: [http://localhost:8080](http://localhost:8080)

Usuário padrão:
```
Login: admin@example.com
Senha: admin
```

---

## 📦 Comandos úteis dbt (dentro do container)

```bash
# Acesse o container do scheduler ou webserver
docker exec -it docker-scheduler-1 bash

# Execute comandos dbt dentro do container
cd /opt/airflow/dbt_analytics_demo

# Rodar tudo
$ dbt build

# Rodar testes
$ dbt test

# Gerar documentação
$ dbt docs generate
```

---

## 📧 Configuração de e-mails no .env

```
EMAIL_SENDER=seuemail@gmail.com
EMAIL_RECEIVER=seuemail@gmail.com
AIRFLOW_ADMIN_EMAIL=admin@example.com
AIRFLOW_ADMIN_PASSWORD=admin
AIRFLOW__CORE__FERNET_KEY=gerado_com_fernet
```

---

## 🧪 DAGs disponíveis

- `dbt_run_dag`: Executa `dbt build` e notifica por e-mail.
- `dbt_test_dag`: Executa `dbt test` e notifica por e-mail.

---

## 🧠 Dicas finais

- Para reiniciar tudo: `docker compose down -v`
- Para resetar Airflow: apagar `postgres-db-volume`
- Para adicionar novas DAGs: edite ou adicione arquivos na pasta `Docker/dags/`

---

Para dúvidas ou melhorias, abra uma issue ou contribua com PRs! 🚀
