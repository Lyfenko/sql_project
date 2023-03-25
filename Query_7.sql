SELECT students.name, marks.mark
FROM students
JOIN groups ON students.group_id = groups.id
JOIN marks ON students.id = marks.student_id
WHERE groups.name = '12-T' AND marks.subject_id = 3;