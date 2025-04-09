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
