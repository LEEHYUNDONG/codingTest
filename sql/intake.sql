-- 코드를 입력하세요
SELECT animal_id, name, case 
            when sex_upon_intake like 'spayed%' or sex_upon_intake like 'Neutered%' then 'O' 
            else 'X'
            END 중성화
from animal_ins
order by animal_id