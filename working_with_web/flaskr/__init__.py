from flask import Flask
import sqlite3
from tabulate import tabulate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

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


# # change to name of your database; add path if necessary
# db_name = '/Users/danilbuslaev/Desktop/test_db'
#
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
#
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#
# # this variable, db, will be used for all SQLAlchemy commands
# db = SQLAlchemy(app)


# # NOTHING BELOW THIS LINE NEEDS TO CHANGE
# # this route will test the database connection and nothing more
# @app.route('/')
# def testdb():
#     try:
#         db.session.query(text('1')).from_statement(text('SELECT 1')).all()
#         return '<h1>It works.</h1>'
#     except Exception as e:
#         # e holds description of the error
#         error_text = "<p>The error:<br>" + str(e) + "</p>"
#         hed = '<h1>Something is broken.</h1>'
#         return hed + error_text


@app.route('/flats/<number>')
def user(number):
    path = "/Users/danilbuslaev/Desktop/test_db"
    con = sqlite3.connect(path)  # создание БД и подключение к ней
    cur = con.cursor()  # "курсор" для отправки запросов и получения результатов

    # res = cur.execute("""SELECT * FROM flats WHERE number = ?;
    #                         """, ({number},))
    # list_of_flats = res.fetchall()
    # table = tabulate(list_of_flats, tablefmt="html")
    return f'<h1>Hello, {number}!</h1>'


if __name__ == '__main__':
    app.run(debug=True)
