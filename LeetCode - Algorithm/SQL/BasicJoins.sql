-- https://leetcode.com/studyplan/top-sql-50/

-- 1068. Product Sales Analysis I
-- https://leetcode.com/problems/product-sales-analysis-i/

SELECT P.product_name, S.year, S.price
FROM Product AS P
JOIN Sales AS S
ON P.product_id = S.product_id

-- 197. Rising Temperature
-- https://leetcode.com/problems/rising-temperature/

SELECT W1.id
FROM Weather AS W1
JOIN Weather AS W2
ON W1.recordDate = W2.recordDate + INTERVAL '1 day'
WHERE W1.temperature > W2.temperature;

-- 1661. Average Time of Process per Machine
-- https://leetcode.com/problems/average-time-of-process-per-machine/

SELECT A1.machine_id, ROUND(CAST(AVG(A2.timestamp - A1.timestamp) AS NUMERIC), 3) AS processing_time
FROM Activity as A1
JOIN Activity as A2
ON A1.machine_id = A2.machine_id AND A1.process_id = A2.process_id AND A1.activity_type = 'start' AND A2.activity_type = 'end'
GROUP BY A1.machine_id;

-- 577. Employee Bonus
-- https://leetcode.com/problems/employee-bonus/

SELECT E.name, B.bonus
FROM Employee AS E
LEFT OUTER JOIN Bonus AS B
ON E.empId = B.empId
WHERE B.bonus < 1000 OR B.bonus IS NULL;

-- 1280. Students and Examinations
-- https://leetcode.com/problems/students-and-examinations/

SELECT S.student_id, S.student_name, Sub.subject_name, COUNT(E.student_id) AS attended_exams
FROM Students AS S
CROSS JOIN Subjects AS Sub
LEFT OUTER JOIN Examinations AS E
ON S.student_id = E.student_id AND Sub.subject_name = E.subject_name
GROUP BY S.student_id, S.student_name, Sub.subject_name
ORDER BY S.student_id, Sub.subject_name;