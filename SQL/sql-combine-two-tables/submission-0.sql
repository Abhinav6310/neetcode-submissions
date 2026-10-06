-- Write your query below
select first_name,last_name,city,state from person a left join address b on a.person_id = b.person_id