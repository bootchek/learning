import sqlite3
from datetime import datetime
import re

path = "/Users/danilbuslaev/Desktop/test_db"
con = sqlite3.connect(path)  # создание БД и подключение к ней
cur = con.cursor()  # "курсор" для отправки запросов и получения результатов

res = cur.execute("SELECT number, content, created FROM Note")
notes_data = res.fetchall()
for note in notes_data:
    match = re.search(r'\d{2}/\d{2}/\d{4}', note[2])
    date = datetime.strptime(match.group(), '%d/%m/%Y').date()
    match = re.search(r'\d{2}:\d{2}:\d{2}', note[2])
    time = datetime.strptime(match.group(), '%H:%M:%S').time()
    print(f"Note {note[0]} date: {date}, time:{time}, content: {note[1]}")