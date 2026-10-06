-- Write your query below
select email from(select email , count(*) as cnt from person  group by email) where cnt>1