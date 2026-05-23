from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker

from configuracion import cadena_base_datos
from crear_base_entidades import RecursoAcademico

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

recursos = session.query(RecursoAcademico).filter(
    or_(
        RecursoAcademico.tipo == "Articulo",
        RecursoAcademico.tipo == "Guia",
        RecursoAcademico.tipo == "libro"
    )
).all()

print("Recursos Academicos")
print("----------------------")

for r in recursos:
    print(r)