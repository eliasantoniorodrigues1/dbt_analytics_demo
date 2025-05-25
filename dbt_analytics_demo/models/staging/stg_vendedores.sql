{{ config(materialized='ephemeral') }}

SELECT
    id AS vendedor_id,
    nome AS vendedor_nome,
    LOWER(email) AS vendedor_email,
    filial_id
FROM {{ ref('vendedores') }}
