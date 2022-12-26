from flask import Flask
import sqlite3
from tabulate import tabulate

app = Flask(__name__)

@app.route("/")
def hello_world():
    path = "/Users/danilbuslaev/Desktop/test_db"
    con = sqlite3.connect(path)  # создание БД и подключение к ней
    cur = con.cursor()  # "курсор" для отправки запросов и получения результатов

    res = cur.execute("""SELECT number, adress
                            FROM flats
                            INNER JOIN buildings on buildings.id = flats.building_id;
                            """)
    list_of_flats = res.fetchall()
    table = tabulate(list_of_flats, tablefmt="html")
    return table


