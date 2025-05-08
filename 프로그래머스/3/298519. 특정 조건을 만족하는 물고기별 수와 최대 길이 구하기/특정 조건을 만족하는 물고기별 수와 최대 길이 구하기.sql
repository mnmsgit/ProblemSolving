-- 코드를 작성해주세요
select count(ID) as FISH_COUNT, max(IFNULL(LENGTH,10)) as MAX_LENGTH, FISH_TYPE
from FISH_INFO as A
group by FISH_TYPE
having avg(IFNULL(LENGTH,10)) >=33
order by FISH_TYPE;

