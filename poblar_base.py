from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date

from configuracion import cadena_base_datos
from crear_base_entidades import Facultad, Carrera, Profesor, RecursoAcademico

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()



fac1 = Facultad(
    nombre ="Facultad de Medicina",
    ubicacion = "Zona A",
    decano = "Jose Ortiz"
)

fac2 = Facultad(
    nombre = "Facultad de Odontologia",
    ubicacion = "Zona B",
    decano = "Maria Estrella"
)

fac3 = Facultad(
    nombre = "Facultad de Ingenieria",
    ubicacion = "Zona C",
    decano = "Roberto Mena"
)

carr1 = Carrera(
    nombre = "Fisioterapia",
    codigo = "FS01",
    facultad = fac1
)

carr2 = Carrera(
    nombre = "Laboratorio Clinico",
    codigo = "LC03",
    facultad = fac1
)

carr3 = Carrera(
    nombre = "Ortodoncia",
    codigo = "OR05",
    facultad = fac2
)

carr4 = Carrera(
    nombre = "Ingeniería en Sistemas",
    codigo = "IS010",
    facultad = fac3
)

carr5 = Carrera(
    nombre = "Neurologia",
    codigo = "NE01",
    facultad = fac1
)



prof1 = Profesor(
    nombres = "Alexander",
    apellidos = "Cruz",
    correo = "alcruz@universidad.edu",
    especialidad ="Fisioterapia Deportiva",
    carrera = carr1
)

prof2 = Profesor(
    nombres = "Daniela",
    apellidos = "Centeno",
    correo = "dacenteno@universidad.edu",
    especialidad = "Genetica",
    carrera = carr2
)

prof3 = Profesor(
    nombres = "Carlos",
    apellidos = "Ortiz",
    correo = "caortiz@universidad.edu",
    especialidad = "ortodoncista",
    carrera = carr3
)

prof4 = Profesor(
    nombres = "Miguel",
    apellidos = "Torres",
    correo = "mitorres@universidad",
    especialidad = "Programacion",
    carrera = carr4
)
prof5 = Profesor(
    nombres = "Carla",
    apellidos = "Sanchez",
    correo = "casanchez@universidad",
    especialidad = "Neurologo",
    carrera = carr5
)

rec1 = RecursoAcademico(
    titulo = "Terapia Deportiva",
    fecha_publicacion = date(2024,7,8),
    tipo = "Articulo",
    url = "https://www.fisioedu.com/rehabilitacion",
    profesor = prof1 
)

rec2 = RecursoAcademico(
    titulo = "Bioseguridad Clinica",
    fecha_publicacion = date(2023,1,18),
    tipo ="Guia",
    url = "https://www.labmedico.com/bioseguridad",
    profesor = prof2
)

rec3 = RecursoAcademico(
    titulo = "Ortodoncia Correctiva",
    fecha_publicacion = date(2023,4,10),
    tipo = "libro",
    url = "https://www.odontouni.com/correctiva",
    profesor = prof3
)

rec4 = RecursoAcademico(
    titulo = "Programacion en Pyhton",
    fecha_publicacion = date(2025,3,12),
    tipo = "libro",
    url = "htpps://uni.edu/pyhton",
    profesor = prof4
)

rec5 = RecursoAcademico(
    titulo = "Introduccion a la neurologia clinica",
    fecha_publicacion = date(2024,4,15),
    tipo = "libro",
    url = "htpps://universidad.edu/neurologia",
    profesor = prof5
)

session.add_all([
    fac1, fac2, fac3,
    carr1, carr2, carr3, carr4, carr5,
    prof1, prof2, prof3, prof4, prof5,
    rec1, rec2, rec3, rec4, rec5
])

session.commit()
print("Datos ingresados correctamente")