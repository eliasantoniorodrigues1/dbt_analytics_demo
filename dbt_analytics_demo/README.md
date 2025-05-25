# dbt_analytics_demo

Projeto completo com dbt (Data Build Tool), focado em boas práticas de engenharia analítica, integração de múltiplas fontes de dados e execução automatizada em servidor Linux.

---

## ⚙️ Tecnologias e ferramentas

- **DBT Core 1.7.x**
- PostgreSQL (local e remoto)
- Shell Script (deploy automatizado)
- Python (para carga auxiliar de dados)
- CSV, Excel e JSON como fontes simuladas

---

## 📁 Estrutura do Projeto

```
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
└── dbt_project.yml
```

---

## 🚀 Como executar localmente

### 1. Clone o projeto e instale o ambiente

```bash
git clone git@seu_repo/dbt_analytics_demo.git
cd dbt_analytics_demo
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure seu `profiles.yml`

Arquivo padrão do DBT (em `~/.dbt/profiles.yml`):

```yaml
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
```

### 3. Carregue os dados

```bash
dbt seed                      # Carrega os seeds CSV
python scripts/load_extras.py  # Carrega Excel e JSON no banco
```

### 4. Execute o pipeline DBT

```bash
dbt run                       # Executa os modelos
dbt test                      # Roda testes automáticos
dbt docs generate && dbt docs serve  # Gera a documentação
```

---

## ⚡ Automação com Git e post-receive

- Repositório bare: `/home/usuario/repos/dbt_analytics_demo.git`
- Working directory: `/home/usuario/projetos/dbt_analytics_demo`
- `post-receive`:
  - Faz o `checkout` automático
  - Ativa ou cria o `venv`
  - Instala pacotes via `requirements.txt`
  - Executa `dbt run`, `test`, `docs`

---

## ✅ Funcionalidades implementadas

- [x] Seeds CSV (vendedores)
- [x] Leitura de Excel (.xlsx) com pandas
- [x] Leitura de JSON com Python
- [x] Camada staging com materialização `ephemeral`
- [x] Marts com `view`, `table` e `incremental`
- [x] Snapshots de alterações (ex: status de clientes)
- [x] Macros reutilizáveis em Jinja
- [x] Testes automatizados
- [x] Deploy automático com Git + Bash
- [x] Execução agendada com cron

---

## 📚 Recursos úteis

- [DBT Docs – Macros](https://docs.getdbt.com/docs/building-a-dbt-project/jinja-macros)
- [dbt-utils Package](https://github.com/dbt-labs/dbt-utils)
- [Jinja Filters](https://jinja.palletsprojects.com/en/3.1.x/templates/#list-of-builtin-filters)
- [Curso gratuito oficial](https://learn.getdbt.com/)

---

## ✨ Autor

**Elias Rodrigues (earlog.dev)**  
Analista de Dados Sênior | Python + SQL | Engenharia de Dados  
GitHub: [github.com/eliasantoniorodrigues1](https://github.com/eliasantoniorodrigues1)  
LinkedIn: [linkedin.com/in/ear-345-](https://www.linkedin.com/in/ear-345-/)

---

## Licença

MIT
