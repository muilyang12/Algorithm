-- https://leetcode.com/studyplan/top-sql-50/

-- 584. Find Customer Referee
-- https://leetcode.com/problems/find-customer-referee/

SELECT name
FROM Customer AS C
WHERE C.referee_id != 2 OR C.referee_id IS NULL;

-- 595. Big Countries
-- https://leetcode.com/problems/big-countries/

SELECT name, population, area
FROM World as W
WHERE W.area >= 3000000 OR W.population >= 25000000;

-- 1683. Invalid Tweets
-- https://leetcode.com/problems/invalid-tweets/

SELECT tweet_id
FROM Tweets AS T
WHERE LENGTH(T.content) > 15;