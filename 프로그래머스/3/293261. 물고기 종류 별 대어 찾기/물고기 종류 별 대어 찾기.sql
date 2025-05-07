-- 코드를 작성해주세요
SELECT ID,FISH_NAME,LENGTH
FROM FISH_INFO AS A
JOIN FISH_NAME_INFO AS B ON A.FISH_TYPE = B.FISH_TYPE
WHERE (A.FISH_TYPE,A.LENGTH) IN (SELECT C.FISH_TYPE, MAX(C.LENGTH) as LENGTH
                                FROM FISH_INFO as C
                                WHERE C.LENGTH is not NULL
                                GROUP BY FISH_TYPE);