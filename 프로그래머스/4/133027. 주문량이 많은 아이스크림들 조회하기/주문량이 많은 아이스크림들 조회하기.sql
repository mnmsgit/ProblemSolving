-- 코드를 입력하세요
SELECT A.FLAVOR
FROM JULY as A
GROUP BY FLAVOR
ORDER BY sum(A.TOTAL_ORDER) + (SELECT TOTAL_ORDER
                                      FROM FIRST_HALF as B
                                      WHERE A.FLAVOR = B.FLAVOR) DESC
limit 3


