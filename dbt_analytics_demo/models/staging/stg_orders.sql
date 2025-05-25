{{ config(materialized='ephemeral') }}

SELECT
    id AS order_id,
    customer_id,
    order_date,
    status,
    total_value::NUMERIC AS total_value
FROM {{ source('raw_data', 'orders') }}
