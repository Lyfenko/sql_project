SELECT students.name, subjects.name, teachers.name
FROM students
JOIN marks ON students.id = marks.student_id
JOIN subjects ON marks.subject_id = subjects.id
JOIN teachers ON subjects.teacher_id = teachers.id
WHERE students.name = 'Ярослава Деряжний' AND teachers.name = 'Лифенко Дмитро'
