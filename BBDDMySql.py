import mysql.connector
from pony.orm import *

db = Database()
db.bind('mysql',host= 'localhost',user='root',
password = 'root',db = 'PruebaMysql')

class Person(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    age = Required(int)

class Coche(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    puertas = Required(int)

#Para mostrar por consola
sql_debug(True)
#Crea la tabla sino esta creada
db.generate_mapping(create_tables=True)

#Mete a john en la tabla person de la bbdd PruebaMysql
#uso with aunque podria usar @db_session
with db_session:
    p1 = Person(name='John', age=20)
    p2 = Person(name='Mike', age=18)
    #para guardarlo
    commit()

with db_session:
    c1 = Coche(name='Opel', puertas=4)
    c2 = Coche(name='BMW', puertas=2)
    commit()
