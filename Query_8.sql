SELECT teachers.name, AVG(marks.mark) as avg_mark
FROM teachers
JOIN subjects ON teachers.id = subjects.teacher_id
JOIN marks ON subjects.id = marks.subject_id
GROUP BY teachers.id
HAVING teachers.name = 'Лифенко Дмитро'