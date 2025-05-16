SELECT
  e.ID,
  CASE
    -- 상위 0%~25%
    WHEN (
      SELECT COUNT(*) 
      FROM ECOLI_DATA x 
      WHERE x.SIZE_OF_COLONY > e.SIZE_OF_COLONY
    ) < (
      SELECT COUNT(*) 
      FROM ECOLI_DATA
    ) / 4
    THEN 'CRITICAL'

    -- 상위 26%~50%
    WHEN (
      SELECT COUNT(*) 
      FROM ECOLI_DATA x 
      WHERE x.SIZE_OF_COLONY > e.SIZE_OF_COLONY
    ) < (
      SELECT COUNT(*) 
      FROM ECOLI_DATA
    ) / 2
    THEN 'HIGH'

    -- 상위 51%~75%
    WHEN (
      SELECT COUNT(*) 
      FROM ECOLI_DATA x 
      WHERE x.SIZE_OF_COLONY > e.SIZE_OF_COLONY
    ) < (
      SELECT COUNT(*) 
      FROM ECOLI_DATA
    ) * 3 / 4
    THEN 'MEDIUM'

    -- 상위 76%~100%
    ELSE 'LOW'
  END AS COLONY_NAME
FROM ECOLI_DATA e
ORDER BY e.ID;
