# variables
from variables import *
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
import mysql.connector

# Resources
from resources.SystemParameter import SystemParameterList, SystemParameter
from resources.Student import Student, StudentMaleFaculty, StudentFemaleFaculty, StudentSexFaculty, StudentUndergraduateSex
from resources.Student import StudentEthnicGroupFaculty, StudentDisabilityFaculty, StudentInternacionalFaculty, StudentNacionalFaculty 
from resources.Student import StudentNationalityFaculty, StudentProfessionFaculty, StudentProfessionConstantsFaculty, StudentInternacional 
from resources.Student import StudentFaculty, StudentUndergraduateNacionality, StudentPerYear, StudentYearFaculty
from resources.TeacherPublication import TeacherPublication, TeacherPublicationFaculty, TeacherCiteFaculty, TeacherCitePublication
from resources.Teacher import Teacher, TeacherSexFaculty, TeacherScale, TeacherNacionalityFaculty, TeacherWithDoctorateFaculty, TeacherGradeFaculty, TeacherWithDoctorate, TeacherInternacionals, TeacherNational
from resources.TeacherTitle import TeacherTitle, TeacherTitleFaculty
from resources.TeacherStudent import TeacherStudent
from resources.TeacherPrize import TeacherPrize
from resources.TeacherProject import TeacherProject
from resources.TeacherOtherStudios import TeacherOtherStudios
from resources.GraduatePatents import GraduatePatents
from resources.GraduateJobs import GraduateJobs
from resources.GraduateCourses import GraduateCourses
from resources.GraduateCertification import GraduateCertification
from resources.GraduateEducation import GraduateEducation
from resources.GraduateStudiosUc import GraduateFaculty, GraduatePerYear, GraduateFacultyYear
from resources.GraduateVolunteering import GraduateVolunteering
from resources.Carga import Carga
from resources.Full import Year, Faculty
# metodos
from etl import etl_process

def sensor():
	#print(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) # Se obtiene local para la actualizacion de la data cuando se ejecute el job
	print("Scheduler esta vivo!000000000000000000000")

def sensor1():
	print(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) # Se obtiene local para la actualizacion de la data cuando se ejecute el job
	print("Scheduler esta vivo11111111111111111111111!")



# sched = BackgroundScheduler(deamon=True)
# sched.add_job(extraction, 'interval', minutes=60)
# sched.start()

#sched.add_job(sensor, trigger='interval', seconds=10)
#sched.add_job(sensor1, 'interval', seconds=20)


app = Flask(__name__)
api = Api(app, prefix="/api/v1")
# enable CORS
CORS(app)

@app.route('/')
def extraction():
	etl_process()
	return "Hola mundo"

# route para parametros del sistema
api.add_resource(SystemParameterList, '/parametroSistema')
api.add_resource(SystemParameter, '/parametroSistema/<systemParameter_id>')
api.add_resource(Year, '/year')
api.add_resource(Faculty, '/faculty')

# cantidad de estudiantes totales
api.add_resource(Student, '/estudiantes-total')
# cantidad de estudiantes por facultad
api.add_resource(StudentFaculty, '/estudiantes-facultad')
# cantidad de estudiantes masculinos por facultad
api.add_resource(StudentMaleFaculty, '/estudiantes-masculinos-facultad')
# cantidad de estudiantes femeninos por facultad
api.add_resource(StudentFemaleFaculty, '/estudiantes-femeninos-facultad')
# cantidad de estudiantes por sexo y por facultad
api.add_resource(StudentSexFaculty, '/estudiantes-sexo-facultad')
# cantidad de estudiantes internacionales
api.add_resource(StudentInternacional, '/estudiantes-internacionales-proporcion') 
# cantidad de estudiantes internacionales por facultad
api.add_resource(StudentInternacionalFaculty, '/estudiantes-internacional-facultad')
# cantidad de estudiantes nacionales por facultad
api.add_resource(StudentNacionalFaculty, '/estudiantes-nacional-facultad')
# cantidad de estudiantes por nacionalidad y por facultad
api.add_resource(StudentNationalityFaculty, '/estudiantes-nacionalidad-facultad')
# cantidad de estudiantes por carrera y por facultad
api.add_resource(StudentProfessionFaculty, '/estudiantes-carrera-facultad')
# cantidad de estudiantes por carrera, dada la facultad
api.add_resource(StudentProfessionConstantsFaculty, '/estudiantes-carrera/<facultad_codigo>')
# cantidad de estudiantes con discapacidad por facultad
api.add_resource(StudentDisabilityFaculty, '/estudiantes-discapacidad-facultad')
# cantidad de estudiantes con etnia por facultad 
api.add_resource(StudentEthnicGroupFaculty, '/estudiantes-etnia-facultad')
# matricula de pregredo por sexo
api.add_resource(StudentUndergraduateSex, '/estudiantes-pregrado-sexo')
# matricula de pregrado por nacionalidad
api.add_resource(StudentUndergraduateNacionality, '/estudiantes-pregrado-nacionalidad')
# cantidad de estudiantes por año
api.add_resource(StudentPerYear, '/estudiantes-ano')
# cantidad de estudiantes por facultad y por año
api.add_resource(StudentYearFaculty, '/estudiantes-ano-facultad')


# docentes
# Número de personal académico empleado en relación al número de alumnos matriculados.
api.add_resource(TeacherStudent, '/profesor-estudiante-proporcion')
# total de docentes empleado
api.add_resource(Teacher,'/profesor-total')
# pulicaciones por docente
api.add_resource(TeacherPublication, '/profesor-publicacion')
# cantidad de publicaciones por facultad
api.add_resource(TeacherPublicationFaculty, '/profesor-publicacion-facultad')
# cantidad de citas por facultad
api.add_resource(TeacherCiteFaculty, '/citas-facultad')
# cantidad de citas por publicación
api.add_resource(TeacherCitePublication, '/citas-publicacion')
# cantidad de profesores con doctorado o phd por facultad
api.add_resource(TeacherTitleFaculty, '/profesor-doctorado-facultad')
# cantidad de profesores por facultad, dado un grado
api.add_resource(TeacherGradeFaculty, '/profesor-grado-facultad/<grado_codigo>')
# proporcion docentes internacioles / total de docentes
api.add_resource(TeacherInternacionals, '/profesores-internacionales-proporcion')
# cantidad de profesores nacionales 
api.add_resource(TeacherNational, '/profesor-nacional')
# cantidad de profesores por sexo por facultad
api.add_resource(TeacherSexFaculty, '/profesores-sexo-facultad')
# cantidad de profesores por nacionalidad por facultad
api.add_resource(TeacherNacionalityFaculty, '/profesores-nacionalidad-facultad')
# Proporción de profesor con escalafon/ total de profesores
api.add_resource(TeacherScale, '/profesores-escalafon-proporcion')
# proporcion de profesores con doctorado/ total de profesores
api.add_resource(TeacherTitle, '/profesor-doctorado-proporcion')

# premios
api.add_resource(TeacherPrize, '/profesores-premios')
# proyectos
api.add_resource(TeacherProject, '/profesores-proyectos')
# otros estudios
api.add_resource(TeacherOtherStudios, '/profesores-otrosestudios')




# egresados
api.add_resource(GraduatePatents, '/egresado-patentes')
api.add_resource(GraduateJobs, '/egresado-trabajos')
api.add_resource(GraduateCourses, '/egresado-cursos')
api.add_resource(GraduateCertification, '/egresado-certificacion')
api.add_resource(GraduateEducation, '/egresado-educacion')
# cantidad de egresados por facultad
api.add_resource(GraduateFaculty, '/egresado-facultad')
# cantidad de egresados por año
api.add_resource(GraduatePerYear, '/egresado-ano')
# cantidad de egresados por facultad y año
api.add_resource(GraduateFacultyYear, '/egresado-ano-facultad')

api.add_resource(GraduateVolunteering, '/egresado-voluntariado')

api.add_resource(Carga, '/carga')


if __name__ == "__main__":
	app.run(debug=True)