from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists
from sqlalchemy_utils import create_database
from sqlalchemy_utils import drop_database
from elios_app.models import Person, Address, CriminalRecord, Base

engine = create_engine('postgresql+psycopg2://developer:letmein123@flask-test.cjqpvm7upos7.us-east-2.rds.amazonaws.com:5432/flask-test')

if database_exists(engine.url):
    print("Dropping DB before creating")
    drop_database(engine.url)

print("Creating new DB")
create_database(engine.url)

print("DB Created? %s at URL: %s  " % (database_exists(engine.url), engine.url))
Base.metadata.create_all(engine)