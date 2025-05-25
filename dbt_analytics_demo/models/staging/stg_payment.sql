{{ config(materialized='ephemeral') }}

SELECT
    id AS payment_id,
    order_id,
    payment_date,
    amount::NUMERIC AS amount,
    payment_method
FROM {{ source('raw_data', 'payments') }}
