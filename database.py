from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists
from sqlalchemy_utils import create_database
from sqlalchemy_utils import drop_database
from elios_app.models import User, Address, CriminalRecord, Base

engine = create_engine('postgresql+psycopg2://flask_dev:letmein123@localhost/elios')

if database_exists(engine.url):
    print("Dropping DB before creating")
    drop_database(engine.url)

print("Creating new DB")
create_database(engine.url)

print("DB Created? %s at URL: %s  " % (database_exists(engine.url), engine.url))
Base.metadata.create_all(engine)