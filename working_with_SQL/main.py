import sqlite3

path = "/Users/danilbuslaev/Desktop/test_db"
con = sqlite3.connect(path)  # создание БД и подключение к ней
cur = con.cursor()  # "курсор" для отправки запросов и получения результатов

cur.execute("CREATE TABLE IF NOT EXISTS Note(number INTEGER, content TEXT)")
data = [(1, "Some text for note 1"),
        (2, "Some text for note 2"),
        (3, "Some text for note 3"),
        (4, "Some text for note 4")]

cur.executemany("INSERT INTO Note VALUES (?, ?)", data)
con.commit()
res = cur.execute("SELECT number, content FROM Note")
notes_data = res.fetchall()
for note in data:
    print(f"Note {note[0]} content: {note[1]}")
