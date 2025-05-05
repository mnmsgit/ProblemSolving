-- 코드를 작성해주세요

select count(ID) as FISH_COUNT
from FISH_INFO as f_i
where f_i.FISH_TYPE in (
    select FISH_TYPE 
    from FISH_NAME_INFO as n_i
    where FISH_NAME = 'BASS' or FISH_NAME = 'SNAPPER');
