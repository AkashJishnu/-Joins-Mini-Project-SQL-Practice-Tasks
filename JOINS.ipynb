-- Joins Mini Project: SQL Practice Tasks
-- Author: Akash Jishnu Vasudevan
-- Description: A collection of SQL JOIN tasks from basic to advanced.

-- DROP TABLES (safe cleanup for re-runs)
DROP TABLE IF EXISTS enrollments;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS departments;

-- CREATE TABLES
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100)
);

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    course_name VARCHAR(100),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

-- INSERT SAMPLE DATA
INSERT INTO departments (department_id, department_name) VALUES
(1, 'Computer Science'),
(2, 'Physics'),
(3, 'Literature'),
(4, 'Business');

INSERT INTO students (student_id, name, department_id) VALUES
(1, 'Akash', 1),
(2, 'Priya', 2),
(3, 'Meera', NULL),
(4, 'Rahul', 1),
(5, 'Daniel', 3);

INSERT INTO enrollments (enrollment_id, student_id, course_name) VALUES
(1, 1, 'Data Structures'),
(2, 2, 'Quantum Physics'),
(3, 1, 'Algorithms'),
(4, 4, 'Business Analytics'),
(5, 5, 'World Literature'),
(6, NULL, 'Artificial Intelligence');

-- TASK 1: Students with their departments
SELECT s.name, d.department_name
FROM students s
LEFT JOIN departments d ON s.department_id = d.department_id;

-- TASK 2: Students with their courses
SELECT s.name, e.course_name
FROM students s
LEFT JOIN enrollments e ON s.student_id = e.student_id;

-- TASK 3: Courses with enrolled student names
SELECT e.course_name, s.name
FROM enrollments e
LEFT JOIN students s ON e.student_id = s.student_id;

-- TASK 4: Departments with students (even if none)
SELECT d.department_name, s.name
FROM departments d
LEFT JOIN students s ON d.department_id = s.department_id;

-- TASK 5: Students with no course enrollments
SELECT s.name
FROM students s
LEFT JOIN enrollments e ON s.student_id = e.student_id
WHERE e.course_name IS NULL;

-- TASK 6: Courses not linked to any student
SELECT e.course_name
FROM enrollments e
LEFT JOIN students s ON e.student_id = s.student_id
WHERE s.name IS NULL;

-- TASK 7: All students and all courses (even unmatched)
(SELECT s.name, e.course_name
 FROM students s
 LEFT JOIN enrollments e ON s.student_id = e.student_id)
UNION
(SELECT s.name, e.course_name
 FROM enrollments e
 RIGHT JOIN students s ON e.student_id = s.student_id);

-- TASK 8: Students with department and course
SELECT s.name, d.department_name, e.course_name
FROM students s
LEFT JOIN departments d ON s.department_id = d.department_id
LEFT JOIN enrollments e ON s.student_id = e.student_id;

-- TASK 9: Departments with no students and no enrollments
SELECT d.department_name
FROM departments d
LEFT JOIN students s ON d.department_id = s.department_id
LEFT JOIN enrollments e ON s.student_id = e.student_id
WHERE s.student_id IS NULL AND e.enrollment_id IS NULL;

-- TASK 10: Each course with the student's department
SELECT e.course_name, d.department_name
FROM enrollments e
LEFT JOIN students s ON e.student_id = s.student_id
LEFT JOIN departments d ON s.department_id = d.department_id;
