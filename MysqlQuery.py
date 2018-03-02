from pony.orm import *
import pony.orm as pony
from BBDDMySql import Person, Coche


@pony.db_session
def ejecutor_queries():
    #muestra todos los mike
    #query1 = select(p for p in Person if p.name == 'Mike').show()
    #muestra todos los usuarios pero sin redundancias
    #query1 = select(p.name for p in Person).show()
    #Muestra todo el contenido de la tabla persona
    #Con esta query se cargan varios datos en las tablas
    query1 = select(p for p in Person).show()
    print(query1)

#ejecutor_queries()

@pony.db_session
def ejecutor_queries2():
    #Con esta query el dato se carga tres datos
    query2 = pony.select(c for c in Coche).show()
    print(query2)

ejecutor_queries2()
