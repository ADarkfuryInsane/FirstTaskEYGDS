-- Active: 1760677919389@@127.0.0.1@3306
-- Create courses table
CREATE TABLE IF NOT EXISTS courses (
    CourseID TEXT PRIMARY KEY,
    Title TEXT,
    Category TEXT,
    Duration INTEGER
);
 
-- Insert course data
INSERT INTO courses (CourseID, Title, Category, Duration) VALUES
('C101', 'Python for Beginners', 'Programming', 40),
('C102', 'Machine Learning Basics', 'AI', 60),
('C103', 'Data Visualization with Power BI', 'Analytics', 30),
('C104', 'Cloud Fundamentals', 'Cloud', 50);
 
-- Create students table
CREATE TABLE IF NOT EXISTS students (
    StudentID TEXT PRIMARY KEY,
    Name TEXT,
    Email TEXT,
    Country TEXT
);
 
-- Insert student data
INSERT INTO students (StudentID, Name, Email, Country) VALUES
('S001', 'Neha', 'neha@example.com', 'India'),
('S002', 'Arjun', 'arjun@example.com', 'UAE'),
('S003', 'Sophia', 'sophia@example.com', 'UK'),
('S004', 'Ravi', 'ravi@example.com', 'India'),
('S005', 'Meena', 'meena@example.com', 'USA');
 
# DROP TABLE courses;
SELECT * FROM courses;
SELECT * FROM students;
 
INSERT INTO courses (CourseID, Title, Category, Duration) VALUES
('C105', 'DEEP LEARNING ADVANCED', 'AI', 70);
 
UPDATE courses SET "Duration" = 80 WHERE "CourseID" = 'C102';
 
# DELETE FROM courses WHERE "CourseID" = 'C105';
 
# DROP TABLE students;
 
INSERT INTO students (StudentID, Name, Email, Country) VALUES
('S006', 'Liam', 'liam@example.com', 'Canada');
 
SELECT * FROM students;
 
#UPDATE students SET "Country" = 'Australia' WHERE "StudentID" = 'S004';
 
DELETE FROM students WHERE "StudentID" = 'S006';
 
SELECT * FROM students WHERE "Country" = 'India';
 
