import sqlite3
from datetime import datetime

path = "/Users/danilbuslaev/Desktop/test_db"
con = sqlite3.connect(path)  # создание БД и подключение к ней
cur = con.cursor()  # "курсор" для отправки запросов и получения результатов

res = cur.execute("SELECT number, content, created FROM Note")
notes_data = res.fetchall()
for note in notes_data:
    print(f"Note {note[0]} date: {note[2][:10]}, time:{note[2][10:]}, content: {note[1]}")