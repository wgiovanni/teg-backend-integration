LOAD_INITIAL_UPDATE = "CARGA_INICIAL_ACTUALIZACION"
ENDPOINT_LOAD_STUDENTS = "RUTA_CARGA_ESTUDIANTES"
ENDPOINT_LOAD_TEACHERS = "RUTA_CARGA_DOCENTES"
ENDPOINT_LOAD_GRADUATES = "RUTA_CARGA_EGRESADOS"
DATE_UPDATE = "FECHA_ACTUALIZACION"

CONTENT_TYPE = {'content-type': 'application/json'}

DIMENSION = "dim-"
FACT = "hechos-"

ITEMS = "items"
STUDENT = "estudiante"
PROFESSION = "carrera"
FACULTY = "facultad"
STUDENT_PROFESSION_FACULTY = "estudiante-carrera-facultad"
TEACHER = "docente"
SCALE = "escalafon"
GRADE = "grado"
PUBLICATION = "publicacion"
TEACHER_PUBLICATION = "docente-publicacion"
TEACHER_FACULTY = "docente-facultad"
GRADUATE = "egresado"
STUDIOS_UC = "estudiosuc"

NACIONALITY_ATTRIBUTE = "nacionalidad"
SEX_ATTRIBUTE = "sexo"
IDENTIFICATION_CARD = "cedula"
FIRST_NAME_ATRIBUTE = "nombre"
LAST_NAME_ATRIBUTE = "apellido"
BIRTH_DATE_ATTRIBUTE = "fecha_nacimiento"
PHONE_ONE_ATTRIBUTE = "telefono1"
PHONE_TWO_ATTRIBUTE = "telefono2"
EMAIL_ATTRIBUTE = "correo"
STATE_PROVENANCE_ATTRIBUTE = "edo_procedencia"
USER_NAME_ATTRIBUTE = "nombre_usuario"

WORK_AREA_ATTRIBUTE = "areadeinvestigacion"
CITE_ATTRIBUTE = "citas"

MALE = "Masculino"
FEMALE = "Femenino"
NATIONAL = "Venezolano"
INTERNACIONAL = "Extranjero"

ROLE_USER_STUDENT = "facultad_estudiante"
ROLE_USER_TEACHER = "facultad_docente"


# constantes de tablas precargadas
STATUS_ACTIVE = "Active"
STATUS_INACTIVE = "Inactivo"

ETNIA_FALSE = "NO PERTENEZCO A UN PUEBLO INDIGENA"
ETNIA_TRUE = "SI PERTENEZCO A UN PUEBLO INDIGENA"

DISABILITY_FALSE = "NO POSEO NINGUNA DISCAPACIDAD"
DISABILITY_TRUE = "SI POSEO DISCAPACIDAD"

UNDERGRADUATE = "Pregrado"
POSTGRADUATE = "Postgrado"

TYPE_TEACHER = [
    {
        "codigo": "Investigador"
    },
    {
        "codigo": "Contratado"
    },
    {
        "codigo": "Normal"
    }
]

FACULTIES = [
    {
        "codigo": "INGENIERIA",
        "nombre": "Ingeniería"
    },
    {
        "codigo": "FCJP",
        "nombre": "Ciencias Jurídicas y Políticas"
    },
    {
        "codigo": "FCS",
        "nombre": "Ciencias de la Salud"
    },
    {
        "codigo": "FACES",
        "nombre": "Ciencias de la Educación"
    },
    {
        "codigo": "ODONTOLOGIA",
        "nombre": "Odontología"
    },
    {
        "codigo": "FACYT",
        "nombre": "Ciencias y Tecnología"
    }
]

LIST_SCALE = [
    {
        "nombre": "Instructor"
    },
    {
        "nombre": "Asistente"
    },
    {
        "nombre": "Agregado"
    },
    {
        "nombre": "Asociado"
    },
    {
        "nombre": "Titular"
    }
]