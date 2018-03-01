
#bultin library
import os

#external libraries
import pony.orm as pony
from datetime import date

basedir = os.path.abspath(os.path.dirname(__file__))
PONY_DATABASE_URI = os.path.join(basedir, 'pony.db')

database = pony.Database(
    "sqlite",
    PONY_DATABASE_URI,
    create_db=True
)

class Person(database.Entity):
    name = pony.Required(str)
    age = pony.Required(int)
    dob = pony.Required(date)


# enciende el debug
pony.sql_debug(True)

# crea la tabla si no existe
database.generate_mapping(create_tables=True)


@pony.db_session
def create_entities():
    Person(name='John', age=30, dob=date(1986, 1, 1))
    Person(name='Mike', age=32, dob=date(1984, 5, 20))
    Person(name='Mary', age=20, dob=date(1996, 2, 15))

create_entities()
