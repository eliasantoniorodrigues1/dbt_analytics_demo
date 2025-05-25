# ✅ load_extras.py
import pandas as pd
import json
import psycopg2
import os

BASE_DIR = os.path.dirname(os.path.abspath('.'))

conn = psycopg2.connect(
    dbname="dbt_demo",
    user="postgres",
    password="231916",
    host="localhost",
    port=5432
)
cursor = conn.cursor()

# Excel: metas_vendas
df_metas = pd.read_excel(os.path.join(BASE_DIR, "extras/metas_vendas.xlsx"), sheet_name="metas_2023")
cursor.execute("DROP TABLE IF EXISTS metas_vendas")
cursor.execute("""
    CREATE TABLE metas_vendas (
        vendedor_id INT,
        mes TEXT,
        meta_vendas NUMERIC
    )
""")
cursor.executemany(
    "INSERT INTO metas_vendas VALUES (%s, %s, %s)",
    df_metas.itertuples(index=False, name=None)
)

# JSON: filiais
with open(os.path.join(BASE_DIR, "extras/filiais.json")) as f:
    filiais = json.load(f)

cursor.execute("DROP TABLE IF EXISTS filiais")
cursor.execute("""
    CREATE TABLE filiais (
        id INT PRIMARY KEY,
        nome TEXT,
        estado TEXT
    )
""")
cursor.executemany(
    "INSERT INTO filiais VALUES (%s, %s, %s)",
    [(f["id"], f["nome"], f["estado"]) for f in filiais]
)

conn.commit()
cursor.close()
conn.close()
