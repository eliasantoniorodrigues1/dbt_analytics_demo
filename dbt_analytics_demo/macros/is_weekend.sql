{% macro is_weekend(date_field) %}
(EXTRACT(DOW FROM {{ date_field }}) IN (0, 6))
{% endmacro %}
