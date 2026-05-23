from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from configuracion import cadena_base_datos
from crear_base_entidades import Carrera

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

carreras = session.query(Carrera).order_by(
    Carrera.nombre
).all()

print("Carreras")
print("------------")

for c in carreras:
    print(c)