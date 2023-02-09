from flask import Flask, render_template, request, flash, redirect, url_for
import sqlite3
from tabulate import tabulate
import logging
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
db.init_app(app)

with app.app_context():
    flats_table = db.Table('Flats', db.metadata, autoload=True, autoload_with=db.engine)
    buildings_table = db.Table('Buildings', db.metadata, autoload=True, autoload_with=db.engine)

    db.session.execute("PRAGMA foreign_keys = ON;")


def get_db_connection():
    db_path = app.config['DB_PATH']
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def show_linked_table():
    results = db.session.execute(
        db.select(flats_table.c.number, buildings_table.c.Adress).join_from(flats_table, buildings_table))
    header = ["Номер квартиры", "Адрес"]
    return render_template('linked_table.html', elements=results, header=header)


@app.route('/flats/<number>')
def flat(number):
    result = db.session.execute(db.select(flats_table).where(flats_table.c.number == number))
    header = ["Идентификатор квартиры", "Идентификатор здания", "Номер"]
    return render_template('flats.html', elements=result, header=header)


@app.route('/flats/')
def flats():
    results = db.session.execute(db.select(flats_table))
    header = ["Идентификатор квартиры", "Идентификатор здания", "Номер"]
    return render_template('flats.html', elements=results, header=header)


@app.route('/buildings/')
def buildings():
    results = db.session.execute(db.select(buildings_table))
    header = ["Идентификатор здания", "Адрес здания"]
    return render_template('buildings.html', elements=results, header=header)


@app.route('/buildings/<id>')
def building(id):
    result = db.session.execute(db.select(buildings_table).where(buildings_table.c.id == id))
    header = ["Идентификатор здания", "Адрес здания"]
    return render_template('buildings.html', elements=result, header=header)


@app.route('/flats/new')
def new_flat():
    adresses = db.session.execute(db.select(buildings_table.c.Adress))
    return render_template('new_flat.html', adresses=adresses)


@app.route('/addflat', methods=['POST', 'GET'])
def addflat():
    if request.method == 'POST':
        try:
            building_adress = request.form['building_adress']
            number = request.form['number']

            building_id = db.session.execute(
                db.select(buildings_table.c.id).where(buildings_table.c.Adress == building_adress)).scalar()
            db.session.execute(db.insert(flats_table).values(building_id=building_id, number=number))
            db.session.commit()
            flash('Квартира успешно добавлена')

            return redirect(url_for('flats'))
        except:
            flash('Такая запись уже существует')
            logging.exception('')
            return redirect(url_for('new_flat'))


@app.route('/buildings/new')
def new_building():
    return render_template('new_building.html')


@app.route('/addbuilding', methods=['POST', 'GET'])
def addbuilding():
    if request.method == 'POST':
        adress = request.form['Adress']
        db.session.execute(db.insert(buildings_table).values(Adress=adress))
        db.session.commit()

        flash('Здание успешно добавлено')

        return redirect(url_for('buildings'))


@app.route('/deletebuilding', methods=['POST', 'GET'])
def deletebuilding():
    if request.method == 'POST':
        building_id = request.form['building_id']
        db.session.execute(db.delete(buildings_table).where(buildings_table.c.id == building_id))
        db.session.commit()

        flash('Запись удалена')
        return redirect(url_for('buildings'))


@app.route('/deleteflat', methods=['POST', 'GET'])
def deleteflat():
    if request.method == 'POST':
        flat_id = request.form['flat_id']
        db.session.execute(db.delete(flats_table).where(flats_table.c.id == flat_id))
        db.session.commit()

        flash('Запись удалена')
        return redirect(url_for('flats'))


if __name__ == '__main__':
    app.run()
