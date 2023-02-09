from flask import Flask, render_template, request, flash, redirect, url_for
import sqlite3
from tabulate import tabulate
import logging
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
db.init_app(app)


class Buildings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Adress = db.Column(db.String(60))


class Flats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    building_id = db.Column(db.Integer, db.ForeignKey(Buildings.id))
    number = db.Column(db.Integer)


with app.app_context():
    db.create_all()


def get_db_connection():
    db_path = app.config['DB_PATH']
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def show_linked_table():
    results = db.session.execute(
        db.select(Flats.number, Buildings.Adress).join_from(Flats, Buildings)).all()
    header = ["Номер квартиры", "Адрес"]
    return render_template('linked_table.html', elements=results, header=header)


@app.route('/flats/<number>')
def flat(number):
    result = db.session.execute(
        db.select(Flats.id, Flats.building_id, Flats.number).where(Flats.number == number)).all()
    header = ["Идентификатор квартиры", "Идентификатор здания", "Номер"]
    return render_template('flats.html', elements=result, header=header)


@app.route('/flats/')
def flats():
    result = db.session.execute(db.select(Flats.id, Flats.building_id, Flats.number)).all()
    header = ["Идентификатор квартиры", "Идентификатор здания", "Номер"]
    return render_template('flats.html', elements=result, header=header)


@app.route('/buildings/')
def buildings():
    result = db.session.execute(db.select(Buildings.id, Buildings.Adress)).all()
    header = ["Идентификатор здания", "Адрес здания"]
    return render_template('buildings.html', elements=result, header=header)


@app.route('/buildings/<id>')
def building(id):
    result = db.session.execute(db.select(Buildings.id, Buildings.Adress).where(Buildings.id == id)).all()
    header = ["Идентификатор здания", "Адрес здания"]
    return render_template('buildings.html', elements=result, header=header)


@app.route('/flats/new')
def new_flat():
    adresses = db.session.execute(db.select(Buildings.Adress)).all()
    return render_template('new_flat.html', adresses=adresses)


@app.route('/addflat', methods=['POST', 'GET'])
def addflat():
    if request.method == 'POST':
        try:
            building_adress = request.form['building_adress']
            number = request.form['number']

            building_id = db.session.execute(
                db.select(Buildings.id).where(Buildings.Adress == building_adress)).scalar()

            flat = Flats(building_id=building_id, number=number)
            db.session.add(flat)
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

        building = Buildings(Adress=adress)

        db.session.add(building)
        db.session.commit()

        flash('Здание успешно добавлено')

        return redirect(url_for('buildings'))


@app.route('/deletebuilding', methods=['POST', 'GET'])
def deletebuilding():
    if request.method == 'POST':
        building_id = request.form['building_id']

        building = db.session.execute(db.select(Buildings).filter_by(id=building_id)).scalars().one()

        db.session.delete(building)
        db.session.commit()

        flash('Запись удалена')
        return redirect(url_for('buildings'))


@app.route('/deleteflat', methods=['POST', 'GET'])
def deleteflat():
    if request.method == 'POST':
        flat_id = request.form['flat_id']

        flat = db.session.execute(db.select(Flats).filter_by(id=flat_id)).scalars().one()

        db.session.delete(flat)
        db.session.commit()

        flash('Запись удалена')
        return redirect(url_for('flats'))


if __name__ == '__main__':
    app.run()
