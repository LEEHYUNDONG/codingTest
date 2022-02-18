-- 코드를 입력하세요
SELECT o.animal_id, o.animal_type, o.name
from animal_ins as i
right join animal_outs as o
on i.animal_id = o.animal_id
where (i.sex_upon_intake not like 'Neutered%' and i.sex_upon_intake not like 'Spayed%') and (o.sex_upon_outcome like 'Neutered%' or o.sex_upon_outcome like 'Spayed%')
order by o.animal_id