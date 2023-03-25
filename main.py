import sqlite3
from faker import Faker

fake = Faker('uk_UA')

# Підключення до бази даних
conn = sqlite3.connect('sqlite_homework.sqlite')
cur = conn.cursor()

# Створення таблиці студентів
cur.execute('''CREATE TABLE students (
               id INTEGER PRIMARY KEY,
               name TEXT,
               group_id INTEGER,
               FOREIGN KEY(group_id) REFERENCES groups(id))''')

# Створення таблиці груп
cur.execute('''CREATE TABLE groups (
               id INTEGER PRIMARY KEY,
               name TEXT)''')

# Створення таблиці викладачів
cur.execute('''CREATE TABLE teachers (
               id INTEGER PRIMARY KEY,
               name TEXT)''')

# Створення таблиці предметів
cur.execute('''CREATE TABLE subjects (
               id INTEGER PRIMARY KEY,
               name TEXT,
               teacher_id INTEGER,
               FOREIGN KEY(teacher_id) REFERENCES teachers(id))''')

# Створення таблиці оцінок студентів
cur.execute('''CREATE TABLE marks (
               id INTEGER PRIMARY KEY,
               subject_id INTEGER,
               student_id INTEGER,
               mark INTEGER,
               date TEXT,
               FOREIGN KEY(subject_id) REFERENCES subjects(id),
               FOREIGN KEY(student_id) REFERENCES students(id))''')

# Генерація даних для таблиць
groups = [(1, '11-T'), (2, '12-T'), (3, '13-T')]
cur.executemany('INSERT INTO groups VALUES (?, ?)', groups)

teachers = [(1, 'Лифенко Дмитро'), (2, 'Приймак Альона'), (3, 'Мугер Жанна')]
cur.executemany('INSERT INTO teachers VALUES (?, ?)', teachers)

subjects = [(1, 'Математика', 1), (2, 'Фізика', 2), (3, 'Історія', 3), (4, 'Хімія', 1), (5, 'Англійська мова', 2)]
cur.executemany('INSERT INTO subjects VALUES (?, ?, ?)', subjects)

students = []
for i in range(50):
    students.append((i+1, fake.name(), fake.random_int(min=1, max=3)))
cur.executemany('INSERT INTO students VALUES (?, ?, ?)', students)

# Генерація оцінок для студентів
marks = []
for i in range(50):
    for j in range(5):
        for k in range(4):
            mark = fake.random_int(min=60, max=100)
            date = fake.date_this_year()
            marks.append((len(marks)+1, j+1, i+1, mark, date))
cur.executemany('INSERT INTO marks VALUES (?, ?, ?, ?, ?)', marks)

conn.commit()
conn.close()
