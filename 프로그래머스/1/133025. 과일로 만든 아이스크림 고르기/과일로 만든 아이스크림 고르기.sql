-- 코드를 입력하세요
SELECT FLAVOR
FROM FIRST_HALF AS f
WHERE f.TOTAL_ORDER >3000 and f.FLAVOR in (SELECT FLAVOR
                                               FROM ICECREAM_INFO as i
                                               WHERE i.INGREDIENT_TYPE= 'fruit_based');
