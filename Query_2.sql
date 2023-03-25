SELECT students.name, AVG(marks.mark) as avg_mark
FROM students
JOIN marks ON students.id = marks.student_id
WHERE marks.subject_id = 5
GROUP BY students.id
ORDER BY avg_mark DESC
LIMIT 1;