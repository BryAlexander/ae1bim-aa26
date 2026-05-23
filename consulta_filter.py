from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from configuracion import cadena_base_datos
from crear_base_entidades import Profesor

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

profesores = session.query(Profesor).filter(
    Profesor.especialidad == "Genetica"
).all()

print("Profesores por Especialidad")
print("--------------")

for p in profesores:
    print(p)