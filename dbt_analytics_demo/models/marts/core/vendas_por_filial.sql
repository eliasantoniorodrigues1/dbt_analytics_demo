{{ config(materialized='table') }}

SELECT
    f.filial_id,
    f.filial_nome,
    f.estado,
    COUNT(o.order_id) AS total_pedidos,
    SUM(o.total_value) AS receita_total
FROM {{ ref('stg_orders') }} o
JOIN {{ ref('stg_vendedores') }} v ON o.customer_id = v.vendedor_id
JOIN {{ ref('stg_filiais') }} f ON v.filial_id = f.filial_id
GROUP BY f.filial_id, f.filial_nome, f.estado
