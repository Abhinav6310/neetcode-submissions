-- Write your query below
select a.name from customers a  left join orders b on a.id = b.customer_id where b.customer_id IS NULL