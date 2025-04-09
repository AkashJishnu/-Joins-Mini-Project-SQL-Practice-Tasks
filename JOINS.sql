TASKS

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
