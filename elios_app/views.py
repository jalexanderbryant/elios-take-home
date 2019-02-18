from elios_app import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from elios_app.models import Base, Address, CriminalRecord, Person
from flask import request, redirect, jsonify, url_for, render_template
import json

## Setup DB Session
engine = create_engine('postgresql+psycopg2://flask_dev:letmein123@localhost/elios')
session = sessionmaker(bind=engine)()

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/home/')
def home():
    return "Hello, world!"

@app.route('/person/')
def showAllPersons():
    """ List all persons - Will return a table"""
    people = session.query(Person).all()
    return jsonify(people = [p.serialize_summary for p in people])

@app.route('/list/')
def list():
    return json.dumps(["item1", "item2", "item3"])

@app.route('/person/<int:person_id>/')
def showPerson(person_id):
    """ Return a person profile """
    person = session.query(Person).filter_by(id = person_id).one()
    addresses = person.addresses
    return jsonify(person = person.serialize_full)

@app.route('/person/<int:person_id>/edit', methods=['GET', 'POST'])
def editPersonName(person_id):
    """Edit a single person's name """
    person_to_edit = session.query(Person).filter_by(id = person_id).one()

    if request.method == 'POST':
        person_to_edit.full_name = request.form['name']        
        session.add(person_to_edit)
        session.commit()
        # return "person_to_edit new name: %s" % person_to_edit.full_name
        return redirect(url_for('showPerson', person_id = person_to_edit.id))
    else:
        return "Form for editing user's name"
    return "Edit person's fullname for person=%s" % person_id