#import grades.txt as a table and answer the following:
#1) write a query to find the average of the grades
#2) add 2 values: 99 and 72 to the list of grades. what is the new average, with SQL?
#3) Change the last 2 values to 90 and 70, what is the new average? (Hint: use auto-increment)
#4) Write a script to add columns for name, school, and city. How would you populate these new columns?

create schema Grades;

select * from Grades.grades;

SELECT AVG(Grades) AS average_grade
FROM Grades.grades;
-- 82.7

INSERT INTO Grades.grades (Grades) VALUES (99), (72);

SELECT AVG(Grades) AS new_average_grade
FROM Grades.grades;
-- 81.6

ALTER TABLE Grades.grades
ADD id INT AUTO_INCREMENT PRIMARY KEY;

UPDATE Grades.grades
SET Grades = CASE
    WHEN id = (SELECT MAX(id) FROM Grades.grades) THEN 70
    WHEN id = (SELECT MAX(id) - 1 FROM Grades.grades) THEN 90
    ELSE Grades
END;

SELECT AVG(Grades) AS new_average_grades
FROM Grades.grades;

ALTER TABLE Grades.grades
ADD name VARCHAR(100),
ADD school VARCHAR(100),
ADD city VARCHAR(100);

UPDATE Grades.grades
SET name = 'John Doe', school = 'High School', city = 'New York'
WHERE id = 1; 








