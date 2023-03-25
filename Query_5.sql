SELECT groups.name
FROM groups
JOIN students ON groups.id = students.group_id
JOIN subjects ON students.group_id = subjects.teacher_id
WHERE subjects.teacher_id = 2;