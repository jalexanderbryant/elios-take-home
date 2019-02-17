from elios_app import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from elios_app.models import Base, Address, CriminalRecord, User
from flask import request, redirect, jsonify, url_for
import json

## Setup DB Session
engine = create_engine('postgresql+psycopg2://flask_dev:letmein123@localhost/elios')
session = sessionmaker(bind=engine)()

@app.route('/')
@app.route('/home/')
def home():
    return "Hello, world!"

@app.route('/users/')
def show_users():
  """ List all users - Will return a table"""
  users = session.query(User).all()
  return jsonify(users = [u.serialize for u in users])

@app.route('/users/<int:user_id>/')
def list_single_user(user_id):
  """ Return a user profile """
  return "User profile for USER=%s" % user_id

@app.route('/users/<int:user_id>/edit')
def edit_user_name(user_id):
  """Edit a single user's name """
  return "Edit user's fullname for USER=%s" % user_id