{{ config(materialized='view') }}

SELECT
    c.customer_id,
    c.full_name,
    c.email,
    o.order_id,
    o.order_date,
    o.status,
    o.total_value
FROM {{ ref('stg_customers') }} c
LEFT JOIN {{ ref('stg_orders') }} o ON c.customer_id = o.customer_id
