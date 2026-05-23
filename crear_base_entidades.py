from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from configuracion import cadena_base_datos

engine =create_engine(cadena_base_datos, echo=False)

Base = declarative_base()

class Facultad(Base):
    __tablename__ = "facultad"

    id = Column(Integer, primary_key=True)
    nombre= Column(String(100))
    ubicacion=Column(String(100))
    decano= Column(String(100))

    carreras= relationship("Carrera", back_populates="facultad")

    def __repr__(self):
        return f"{self.nombre}"
    

class Carrera(Base):
    __tablename__ = "carrera"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    codigo = Column(String(20))

    facultad_id = Column(Integer, ForeignKey("facultad.id"))

    facultad = relationship("Facultad", back_populates="carreras")
    profesores = relationship("Profesor", back_populates="carrera")

    def __repr__(self):
        return f"{self.nombre}"
    

class Profesor(Base):
    __tablename__ = "profesor"

    id = Column(Integer,primary_key=True)
    nombres= Column(String(100))
    apellidos= Column(String(100))
    correo= Column(String(100))
    especialidad= Column(String(100))

    carrera_id = Column(Integer, ForeignKey("carrera.id"))

    carrera= relationship("Carrera", back_populates="profesores")
    recursos = relationship("RecursoAcademico", back_populates="profesor")

    def __repr__(self):
        return f"{self.nombres} {self.apellidos}"


class RecursoAcademico(Base):
    __tablename__="recurso_academico"

    id= Column(Integer, primary_key=True)
    titulo=Column(String(200))
    fecha_publicacion= Column(Date)
    tipo= Column(String(100))
    url = Column(String(200))

    profesor_id = Column(Integer, ForeignKey("profesor.id"))

    profesor = relationship("Profesor", back_populates="recursos")

    def __repr__(self):
        return f"{self.titulo}"


Base.metadata.create_all(engine)