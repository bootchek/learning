from flask import Flask, render_template
import sqlite3
from tabulate import tabulate

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("/Users/danilbuslaev/Desktop/test_db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def hello_world():
    conn = get_db_connection()
    res = conn.execute("""SELECT number, adress
                            FROM flats
                            INNER JOIN buildings on buildings.id = flats.building_id;
                            """)
    list_of_flats = res.fetchall()
    table = tabulate(list_of_flats, tablefmt="html")
    conn.close()
    return render_template('index.html', flats = list_of_flats)


@app.route('/flats/<number>')
def flat(number):
    conn = get_db_connection()
    res = conn.execute("""SELECT number FROM flats WHERE number = ?;
                            """, (number,))
    flat = res.fetchone()
    conn.close()
    return render_template('flat.html', number=flat)


if __name__ == '__main__':
    app.run(debug=True)
