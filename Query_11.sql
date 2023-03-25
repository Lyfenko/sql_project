SELECT AVG(marks.mark) as avg_mark
FROM marks
JOIN subjects ON subjects.id = marks.subject_id
JOIN teachers ON teachers.id = subjects.teacher_id
JOIN students ON students.id = marks.student_id
WHERE teachers.id = 1 AND students.id = 10;
