select
    c.customer_id,
    c.name,
    count(o.order_id) as total_orders,
    sum(o.amount) as total_amount,
    avg(o.amount) as avg_order_value
from {{ ref('stg_customers') }} c
join {{ ref('stg_orders') }} o
    on c.customer_id = o.customer_id
group by
    c.customer_id,
    c.name
