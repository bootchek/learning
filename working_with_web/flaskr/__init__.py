from flask import Flask, render_template, request
import sqlite3
from tabulate import tabulate

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("/home/budulay/test_db")
    # conn = sqlite3.connect("/Users/danilbuslaev/Desktop/test_db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def show_linked_table():
    conn = get_db_connection()
    res = conn.execute("""SELECT number, adress
                            FROM flats
                            INNER JOIN buildings on buildings.id = flats.building_id;
                            """)
    flats = res.fetchall()
    header = ["Идентификатор квартиры", "Адрес"]
    conn.close()
    return render_template('elements.html', elements=flats, header=header)


@app.route('/flats/<number>')
def flat(number):
    conn = get_db_connection()
    res = conn.execute("""SELECT id, building_id, number FROM flats WHERE number = ?;
                            """, (number,))
    flat = res.fetchall()
    conn.close()
    header = ["Идентификатор квартиры", "Идентификатор здания", "Номер"]
    return render_template('elements.html', elements=flat, header=header)


@app.route('/flats/')
def flats():
    conn = get_db_connection()
    res = conn.execute("""SELECT id, building_id, number FROM flats;""")
    flats = res.fetchall()
    conn.close()
    header = ["Идентификатор квартиры", "Идентификатор здания", "Номер"]
    return render_template('elements.html', elements=flats, header=header)


@app.route('/buildings/')
def buildings():
    conn = get_db_connection()
    res = conn.execute("""SELECT id, Adress FROM buildings;""")
    buildings = res.fetchall()
    conn.close()
    header = ["Идентификатор здания", "Адрес здания"]
    return render_template('elements.html', elements=buildings, header=header)


@app.route('/buildings/<id>')
def building(id):
    conn = get_db_connection()
    res = conn.execute("""SELECT id, Adress FROM buildings WHERE id = ?;
                            """, (id,))
    building = res.fetchall()
    conn.close()
    header = ["Идентификатор здания", "Адрес здания"]
    return render_template('elements.html', elements=building, header=header)


@app.route('/flats/new')
def new_flat():
    return render_template('new_flat.html')


@app.route('/addflat', methods=['POST', 'GET'])
def addflat():
    if request.method == 'POST':
        conn = get_db_connection()
        try:
            id = request.form['id']
            building_id = request.form['building_id']
            number = request.form['number']

            conn.execute("""INSERT INTO flats (id, building_id, number)
                VALUES(?, ?, ?)""", (id, building_id, number))
            conn.commit()
            msg = "Запись добавлена"
        except:
            conn.rollback()
            msg = "Такая запись уже существует"
        finally:
            return render_template("result.html", msg=msg)
            conn.close()


@app.route('/buildings/new')
def new_building():
    return render_template('new_building.html')


@app.route('/addbuilding', methods=['POST', 'GET'])
def addbuilding():
    if request.method == 'POST':
        conn = get_db_connection()
        try:
            id = request.form['id']
            Adress = request.form['Adress']

            conn.execute("""INSERT INTO buildings (id, Adress)
                VALUES(?, ?)""", (id, Adress))
            conn.commit()
            msg = "Запись добавлена"
        except:
            conn.rollback()
            msg = "Такая запись уже существует"
        finally:
            return render_template("result.html", msg=msg)
            conn.close()


if __name__ == '__main__':
    app.run(host='95.216.213.239')
