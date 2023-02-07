from flask import Flask, render_template, request, flash, redirect, url_for
import sqlite3
from tabulate import tabulate
import logging
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
db.init_app(app)

# with app.app_context():
#     flats_table = db.Table('Flats', db.metadata, autoload=True, autoload_with=db.engine)
#     buildings_table = db.Table('Buildings', db.metadata, autoload=True, autoload_with=db.engine)
with app.app_context():
    db.reflect()


class Flats:
    __table__ = db.metadata.tables["Flats"]


class Buildings:
    __table__ = db.metadata.tables['Buildings']


def get_db_connection():
    db_path = app.config['DB_PATH']
    conn = sqlite3.connect(db_path)
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
    header = ["Номер квартиры", "Адрес"]
    conn.close()
    return render_template('linked_table.html', elements=flats, header=header)


@app.route('/flats/<number>')
def flat(number):
    result = db.session.execute(db.select(Flats).where(Flats.number == number)).scalars()
    # result=db.get_or_404(flats_table, number)
    header = ["Идентификатор квартиры", "Идентификатор здания", "Номер"]
    return render_template('flats.html', elements=[result.id, result.building_id, result.number], header=header)


@app.route('/flats/')
def flats():
    # results = db.session.query(flats_table).all()
    results = db.session.execute(db.select(Flats).order_by(Flats.id)).scalars()
    elements = []
    for flat in results:
        elements.append([flat.id, flat.building_id, flat.number])
    header = ["Идентификатор квартиры", "Идентификатор здания", "Номер"]
    return render_template('flats.html', elements=elements, header=header)


@app.route('/buildings/')
def buildings():
    results = db.session.execute(db.select(Buildings).order_by(Buildings.id)).scalars()
    elements = []
    for building in results:
        elements.append([building.id, building.Adress])
    header = ["Идентификатор здания", "Адрес здания"]
    return render_template('buildings.html', elements=elements, header=header)


@app.route('/buildings/<id>')
def building(id):
    result = db.get_or_404(Buildings, id)
    header = ["Идентификатор здания", "Адрес здания"]
    return render_template('buildings.html', elements=[result.id, result.Adress], header=header)


@app.route('/flats/new')
def new_flat():
    conn = get_db_connection()
    res = conn.execute("""SELECT Adress FROM buildings""")
    adresses = res.fetchall()
    conn.close()
    return render_template('new_flat.html', adresses=adresses)


@app.route('/addflat', methods=['POST', 'GET'])
def addflat():
    if request.method == 'POST':
        conn = get_db_connection()
        try:
            building_adress = request.form['building_adress']
            number = request.form['number']

            res = conn.execute("""SELECT id FROM buildings WHERE Adress = ?;
            """, (building_adress,))
            building_id = res.fetchall()
            conn.execute("""INSERT INTO flats (building_id, number)
                VALUES(?, ?)""", (building_id[0][0], number))
            conn.commit()
            flash('Квартира успешно добавлена')
            conn.close()
            return redirect(url_for('flats'))
        except:
            conn.rollback()
            flash('Такая запись уже существует')
            logging.exception('')
            conn.close()
            return redirect(url_for('new_flat'))


@app.route('/buildings/new')
def new_building():
    return render_template('new_building.html')


@app.route('/addbuilding', methods=['POST', 'GET'])
def addbuilding():
    if request.method == 'POST':
        conn = get_db_connection()
        Adress = request.form['Adress']

        conn.execute("""INSERT INTO buildings (Adress)
            VALUES (?)""", (Adress,))
        conn.commit()
        conn.close()
        flash('Здание успешно добавлено')
        conn.close()
        return redirect(url_for('buildings'))


@app.route('/deletebuilding', methods=['POST', 'GET'])
def deletebuilding():
    if request.method == 'POST':
        conn = get_db_connection()
        building_id = request.form['building_id']
        conn.execute("""DELETE FROM buildings
            WHERE id = ?""", (building_id,))
        conn.commit()
        conn.close()
        flash('Запись удалена')
        return redirect(url_for('buildings'))


@app.route('/deleteflat', methods=['POST', 'GET'])
def deleteflat():
    if request.method == 'POST':
        conn = get_db_connection()
        flat_id = request.form['flat_id']
        conn.execute("""DELETE FROM flats
            WHERE id = ?""", (flat_id,))
        conn.commit()
        conn.close()
        flash('Запись удалена')
        return redirect(url_for('flats'))


if __name__ == '__main__':
    app.run()
