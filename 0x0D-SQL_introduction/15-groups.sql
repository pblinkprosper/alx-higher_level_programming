-- Lists number of records with same score in second_table
-- Column name is number
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY score DESC;
