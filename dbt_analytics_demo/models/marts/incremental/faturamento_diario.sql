{{ config(
  materialized='incremental',
  unique_key='data'
) }}

SELECT
    order_date AS data,
    SUM(total_value) AS faturamento
FROM {{ ref('stg_orders') }}
{% if is_incremental() %}
WHERE order_date > (SELECT MAX(data) FROM {{ this }})
{% endif %}
GROUP BY order_date
