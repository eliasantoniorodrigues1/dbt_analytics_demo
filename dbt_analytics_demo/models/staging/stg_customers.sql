-- ephemeral nao gera tabelas fisicas e referencia suas respectivas
-- tabelas no banco source
{{ config(materialized='ephemeral') }}

SELECT
    id AS customer_id,
    full_name,
    LOWER(email) AS email,
    created_at,
    is_active
FROM {{ source('raw_data', 'customers') }}
