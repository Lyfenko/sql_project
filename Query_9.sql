SELECT students.name, subjects.name
FROM students
JOIN marks ON students.id = marks.student_id
JOIN subjects ON marks.subject_id = subjects.id
WHERE students.name = 'Вікторія Мазепа'