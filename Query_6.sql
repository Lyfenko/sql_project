SELECT students.name
FROM students
JOIN groups ON students.group_id = groups.id
WHERE groups.name = '11-T';