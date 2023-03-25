SELECT s.name AS student_name, m.mark AS student_mark
FROM students AS s
JOIN marks AS m ON s.id = m.student_id
WHERE s.group_id = 1
  AND m.subject_id = 1
  AND m.date = (SELECT MAX(date) FROM marks WHERE subject_id = 1)