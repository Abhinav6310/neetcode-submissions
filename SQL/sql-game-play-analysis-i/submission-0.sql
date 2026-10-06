-- Write your query below
select player_id , event_date as first_login from (select * , rank() over (partition by player_id order by event_date) as rn from activity ) where rn=1