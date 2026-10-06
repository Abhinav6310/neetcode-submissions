-- Write your query below
select customer_number from (select customer_number, count(*) as total_order from orders group by customer_number) order by total_order desc limit 1