{{ config(materialized='ephemeral') }}

SELECT
    vendedor_id,
    mes,
    meta_vendas::NUMERIC
FROM {{ source('public', 'metas_vendas') }}
