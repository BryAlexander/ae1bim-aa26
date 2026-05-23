from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from configuracion import cadena_base_datos
from crear_base_entidades import Facultad

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

facultades = session.query(Facultad).all()

print("Facultades")
print("-------------")

for f in facultades:
    print(f)