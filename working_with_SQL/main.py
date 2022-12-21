import sqlite3
from datetime import datetime

path = "/Users/danilbuslaev/Desktop/test_db"
con = sqlite3.connect(path)  # создание БД и подключение к ней
cur = con.cursor()  # "курсор" для отправки запросов и получения результатов

# cur.execute("CREATE TABLE IF NOT EXISTS Note(number INTEGER, content TEXT)")
cur.execute("""ALTER TABLE Note
  ADD created TEXT""")

now = datetime.now()
current_time = now.strftime("%d/%m/%Y %H:%M:%S")

data = [(5, "Some text for note 5", current_time),
        (6, "Some text for note 6", current_time),
        (7, "Some text for note 7", current_time),
        (8, "Some text for note 8", current_time)]

cur.executemany("INSERT INTO Note VALUES (?, ?, ?)", data)
con.commit()
res = cur.execute("SELECT number, content, created FROM Note")
notes_data = res.fetchall()
for note in data:
    print(f"Note {note[0]} content: {note[1]}")
