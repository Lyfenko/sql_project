SELECT students.group_id, AVG(marks.mark) as avg_mark
FROM students
JOIN marks ON students.id = marks.student_id
WHERE marks.subject_id = 4
GROUP BY students.group_id;