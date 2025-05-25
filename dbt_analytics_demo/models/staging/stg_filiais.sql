{{ config(materialized='ephemeral') }}

SELECT
    id AS filial_id,
    nome AS filial_nome,
    estado
FROM {{ source('public', 'filiais') }}
