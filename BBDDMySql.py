import mysql.connector
from pony.orm import *

db = Database()
db.bind('mysql',host= 'localhost',user='root',
password = 'root',db = 'PruebaMysql')

class Person(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    age = Required(int)

sql_debug(True)
db.generate_mapping(create_tables=True)
