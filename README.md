
# 🔗 SQL Joins Mini Project

A hands-on SQL mini project to practice and master SQL `JOIN`s — from beginner to advanced.  
Created by **Akash Jishnu Vasudevan** as part of his Data Analyst learning journey.

---

## 🧠 What You'll Practice

- `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, `FULL JOIN`
- Anti-joins using `LEFT JOIN` + `WHERE IS NULL`
- Combining data from multiple tables
- `UNION` as a substitute for `FULL JOIN`
- Complex multi-table joins

---

## 🗂️ Tables & Sample Data

### `students`

| student_id | name     | department_id |
|------------|----------|---------------|
| 1          | Akash    | 1             |
| 2          | Priya    | 2             |
| 3          | Meera    | NULL          |
| 4          | Rahul    | 1             |
| 5          | Daniel   | 3             |

### `departments`

| department_id | department_name     |
|---------------|---------------------|
| 1             | Computer Science    |
| 2             | Physics             |
| 3             | Literature          |
| 4             | Business            |

### `enrollments`

| enrollment_id | student_id | course_name            |
|---------------|------------|------------------------|
| 1             | 1          | Data Structures        |
| 2             | 2          | Quantum Physics        |
| 3             | 1          | Algorithms             |
| 4             | 4          | Business Analytics     |
| 5             | 5          | World Literature       |
| 6             | NULL       | Artificial Intelligence|

---

## ✅ Tasks

| Task # | Description                                                                 |
|--------|-----------------------------------------------------------------------------|
| 1      | List all students with their departments                                    |
| 2      | List all students and any course they’re enrolled in                       |
| 3      | List all courses and student names enrolled in them                        |
| 4      | Show all departments and students in them (include empty departments)      |
| 5      | Find students who haven’t enrolled in any course                           |
| 6      | Find courses that don’t have any student enrolled                          |
| 7      | Show all students and all courses (even if unmatched)                      |
| 8      | List all students with their department and enrolled course                |
| 9      | Find departments with no students and no enrollments                       |
| 10     | List each course with the department of the student enrolled (if any)      |

---

## 🚀 How to Use

1. Download and run `joins-mini-project.sql` in any SQL environment (MySQL, PostgreSQL, SQLite, etc.)
2. It will:
   - Drop & recreate the schema
   - Insert sample data
   - Execute all 10 practice tasks

---

## 👨‍💻 Author

**Akash Jishnu Vasudevan**  
Learning to become a Data Analyst 💼

---

## 📊 Progress Visual

![Progress](progress_chart.png) <!-- Replace with your visual if uploaded -->

---

## 🌟 License

Feel free to fork and practice — contributions and suggestions welcome!
