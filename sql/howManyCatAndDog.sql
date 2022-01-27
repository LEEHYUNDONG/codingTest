select animal_type, count(animal_type) 
from animal_ins
group by animal_type
order by animal_type

-- mysql에서 유형별로 갯수를 가져오고 싶을때, 단순히 count함수로 데이터를 조회하면
-- 전체 갯수만을 가져온다.
-- 이렇게 유형별로 갯수를 알고싶을떄는 컬럼에 데이터를 그룹화할 수 있는 group by를 
-- 사용한다.

-- 특정 컬럼을 그룹화 group by
-- 특정 컬럼을 그룹화한 결과에 조건을 거는 것 having

