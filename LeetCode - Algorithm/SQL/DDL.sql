-- DDL

CREATE TABLE Students (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    grade FLOAT,
    email VARCHAR(100) UNIQUE
);

ALTER TABLE Students
ADD age INT;

ALTER TABLE Students
MODIFY grade DECIMAL(5, 2);

ALTER TABLE Students
CHANGE grade gpa DECIMAL(3, 2);

ALTER TABLE Students
ADD CONSTRAINT CHECK_UTD_EMAIL
CHECK (email LIKE '%@utdallas.edu');

ALTER TABLE Students
DROP COLUMN age;

ALTER TABLE Students
DROP CONSTRAINT CHECK_UTD_EMAIL;

DROP TABLE Students;

TRUNCATE TABLE Students;

-- DML

SELECT name, gpa
FROM Students
WHERE gpa > 3.2
ORDER BY gpa DESC;

SELECT gpa, COUNT(*) AS student_count
FROM Students
GROUP BY gpa;

INSERT INTO Students (.....)
VALUES
(.....)
(.....);

UPDATE Students
SET gpa = 3.5
WHERE name = "Muil Yang";

UPDATE Students
SET gpa = gpa + 0.1, age = age + 1
WHERE id = 1;

DELETE FROM Students
WHERE gpa < 3.0;

DELETE FROM Students;