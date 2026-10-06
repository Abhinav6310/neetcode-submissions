-- Write your query below
select c.customer_id,d.name from (
    select a.* , b.* , 'june' as mon from orders a left join product b on a.product_id = b.product_id where a.order_date >= '2020-06-1' and a.order_date < '2020-07-1' 
union all 
select a.* , b.* ,'july' as mon from orders a left join product b on a.product_id = b.product_id where a.order_date >= '2020-07-1' and a.order_date < '2020-08-1') c left join customers d on c.customer_id = d.customer_id group by  c.customer_id,d.name having sum(case when mon='june' then quantity * price else 0 end) >= 100 and sum(case when mon='july' then quantity * price else 0 end) >= 100