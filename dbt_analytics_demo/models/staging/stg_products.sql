{{ config(materialized='ephemeral') }}

SELECT
    id AS product_id,
    name AS product_name,
    category,
    price::NUMERIC AS price
FROM {{ source('raw_data', 'products') }}
