{{ config(materialized='view') }}

SELECT
    m.vendedor_id,
    v.vendedor_nome,
    m.mes,
    m.meta_vendas,
    COALESCE(SUM(o.total_value), 0) AS vendas_mes,
    CASE
        WHEN SUM(o.total_value) >= m.meta_vendas THEN 'atingida'
        ELSE 'não atingida'
    END AS status_meta
FROM {{ ref('stg_metas') }} m
JOIN {{ ref('stg_vendedores') }} v ON m.vendedor_id = v.vendedor_id
LEFT JOIN {{ ref('stg_orders') }} o ON o.customer_id = v.vendedor_id AND to_char(o.order_date, 'YYYY-MM') = m.mes
GROUP BY m.vendedor_id, v.vendedor_nome, m.mes, m.meta_vendas
