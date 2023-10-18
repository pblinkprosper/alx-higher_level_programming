-- Lists all records of second_table showing only score and name
-- In descending score excluding rows withot name
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
