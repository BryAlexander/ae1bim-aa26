from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker

from configuracion import cadena_base_datos
from crear_base_entidades import Profesor

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

profesores = session.query(Profesor).filter(
    and_(
        Profesor.especialidad == "Fisioterapia Deportiva",
        Profesor.correo == "alcruz@universidad.edu"
    )
 ).all()

print("Profesores por especialidad y correo")
print("--------------------------------------")

for p in profesores:
    print(p)