-- Write your query below
--select a.* , b.* , substring(b.phone_number,1,3) as country_code from calls a left join person b on a.

select d.name as country from  (select a.* , b.* , substring(b.phone_number,1,3) as country_code from  (select caller_id as person_id, duration  from calls union all select callee_id as person_id, duration  from calls) a left join person b on a.person_id = b.id) c inner join country d on c.country_code = d.country_code  group by d.name having avg(duration) > (
    SELECT AVG(duration)
    FROM calls
)