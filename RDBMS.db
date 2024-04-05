--Create a new MySQL database named "UniversityDB"
CREATE DATABASE IF NOT EXISTS UniversityDB;

--Switch to the UniversityDB database
USE UniversityDB;

--Create the "Students" table with specified attributes
CREATE TABLE IF NOT EXISTS Students (
    StudentID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Age INT,
    Major VARCHAR(50)
);

--Insert at least 5 records into the "Students" table
INSERT INTO Students (StudentID, FirstName, LastName, Age, Major) 
VALUES 
    (1, 'John', 'Doe', 20, 'Computer Science'),
    (2, 'Jane', 'Smith', 21, 'Mathematics'),
    (3, 'Alice', 'Johnson', 19, 'Physics'),
    (4, 'Bob', 'Williams', 22, 'Biology'),
    (5, 'Emily', 'Brown', 20, 'English');

--Alter the "Students" table to add a new column named "GPA"
ALTER TABLE Students
ADD GPA DECIMAL(3, 2);

--Insert GPA values for the existing records in the "Students" table
-- For illustration purposes, setting arbitrary GPA values
UPDATE Students 
SET GPA = ROUND(RAND() * 4, 2); -- Generating random GPA values between 0 and 4

--Rename the table from "Students" to "EnrolledStudents"
ALTER TABLE Students
RENAME TO EnrolledStudents;

--Create a new table named "Courses" with specified attributes
CREATE TABLE IF NOT EXISTS Courses (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(100),
    Instructor VARCHAR(100),
    Credits INT
);

--Insert at least 3 records into the "Courses" table
INSERT INTO Courses (CourseID, CourseName, Instructor, Credits) 
VALUES 
    (1, 'Introduction to Computer Science', 'Dr. Smith', 3),
    (2, 'Calculus I', 'Prof. Johnson', 4),
    (3, 'Physics for Engineers', 'Dr. White', 3);

--Drop the "EnrolledStudents" table from the database
DROP TABLE IF EXISTS EnrolledStudents;

Design decisions:
- Used INT data type for primary keys and other integer fields for simplicity.
- Used VARCHAR data type with appropriate maximum lengths for string fields.
- Used DECIMAL data type for GPA to store decimal values with precision.
- Included sample data for demonstration purposes, assuming basic information for students and courses.
- Renamed the "Students" table to "EnrolledStudents" to better reflect its purpose and differentiate it from potential other tables related to students.
- Included comments in SQL code for clarity and documentation purposes.

