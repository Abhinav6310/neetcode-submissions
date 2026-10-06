-- Write your query below

select team_id,team_name,COALESCE(num_points, 0) AS num_points  from (select team , sum(points) as num_points from ((select  host_team as team , 
case when host_goals > guest_goals then 3 
when host_goals = guest_goals then 1
else 0 end as points
from matches)
UNION ALL
(select  guest_team as team, 
case when host_goals < guest_goals then 3 
when host_goals = guest_goals then 1
else 0 end as points
from matches
)) group by team) a right join teams b on a.team=b.team_id order by num_points desc
