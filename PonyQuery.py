from pony.orm import *
import pony.orm as pony
from BBDD2 import Person

@pony.db_session
def ejecutor_queries():
    #muestra todos los mike
    #query1 = select(p for p in Person if p.name == 'Mike').show()
    #muestra todos los usuarios pero sin redundancias
    #query1 = select(p.name for p in Person).show()
    #Muestra todo el contenido de la tabla persona
    query1 = select(p for p in Person).show()
    print(query1)

ejecutor_queries()
