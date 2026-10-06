-- Write your query below
-- select a.* from exam_results a right join (select student_id , max(score) as score ,rank() over(partition by student_id order by exam_id) as rn  from exam_results ) b on a.student_id = b.student_id and a.score=b.score where rn=1


select student_id,exam_id,score from (select student_id , exam_id ,score ,rank() over(partition by student_id order by score desc,exam_id) as rn  from exam_results) where rn=1