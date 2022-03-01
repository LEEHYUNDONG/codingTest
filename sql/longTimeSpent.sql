-- 코드를 입력하세요
SELECT ins.animal_id, ins.name
from animal_ins ins
join animal_outs outs on outs.animal_id = ins.animal_id
order by outs.datetime-ins.datetime desc, ins.animal_id limit 2
