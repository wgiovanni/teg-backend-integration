# variables
from variables import *
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from flask import Flask, request
from flask_cors import CORS
from flask_restful import Api
import mysql.connector
import simplejson as json
import requests
import mysql.connector
from db_credentials import datawarehouse_db_config
from sql_queries import systemParameter

# Resources
from resources.SystemParameter import SystemParameterList, SystemParameter, SystemParameterTaskStudents, SystemParameterUpdateDateStudens, SystemParameterUpdateDateTeachers 
from resources.SystemParameter import SystemParameterUpdateDateGraduate, SystemParameterTaskTeachers, SystemParameterTaskGraduates, SystemParameterTaskAll 
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
from resources.Year import Year
from resources.Faculty import FacultyReport, Faculty, FacultyId
from resources.Profession import Profession, ProfessionId
from resources.MicroservicesError import MicroservicesError

from constants import CONTENT_TYPE, SCHEDULED_TASK_GRADUATES, SCHEDULED_TASK_TEACHERS, SCHEDULED_TASK_STUDENTS

# metodos
from etl import etl_process_students, etl_process_teachers, etl_process_graduates

def taskGraduates():
	target_cnx = mysql.connector.connect(**datawarehouse_db_config)
	target_cursor = target_cnx.cursor(buffered=True)
	target_cursor.execute("USE {}".format(datawarehouse_name))
	target_cursor.execute(systemParameter.get_query, [SCHEDULED_TASK_GRADUATES])
	row = target_cursor.fetchone()
	# print(row)
	if row is not None:
		if (row[4] == "1"):
			print("Activa sensor")
			etl_process_graduates()
		else:
			print("Inactiva sensor")


# def sensor1():
# 	# print(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) # Se obtiene local para la actualizacion de la data cuando se ejecute el job
# 	# print("Scheduler esta vivo11111111111111111111111!")
# 	target_cnx = mysql.connector.connect(**datawarehouse_db_config)
# 	target_cursor = target_cnx.cursor(buffered=True)
# 	target_cursor.execute("USE {}".format(datawarehouse_name))
# 	target_cursor.execute(systemParameter.get_query, ["TAREA_PROGRAMADA"])
# 	row = target_cursor.fetchone()
# 	# print(row)
# 	if (row[4] == "1"):
# 		print("Activa Sensor 1")
# 		# print("Sensor 1")
# 		# sched.resume()
# 		# etl_process()
# 	else:
# 		print("Inactiva Sensor 1")
# 		# print("Scheduler esta vivo!000000000000000000000")

def taskTeachers():
	target_cnx = mysql.connector.connect(**datawarehouse_db_config)
	target_cursor = target_cnx.cursor(buffered=True)
	target_cursor.execute("USE {}".format(datawarehouse_name))
	target_cursor.execute(systemParameter.get_query, [SCHEDULED_TASK_TEACHERS])
	row = target_cursor.fetchone()
	# print(row)
	if row is not None:
		if (row[4] == "1"):
			print("Activa Sensor 2")
			etl_process_teachers()
		else:
			print("Inactiva Sensor 2")

def taskStudents():
	target_cnx = mysql.connector.connect(**datawarehouse_db_config)
	target_cursor = target_cnx.cursor(buffered=True)
	target_cursor.execute("USE {}".format(datawarehouse_name))
	target_cursor.execute(systemParameter.get_query, [SCHEDULED_TASK_STUDENTS])
	row = target_cursor.fetchone()
	# print(row)
	if row is not None:
		if (row[4] == "1"):
			print("Activa")
			etl_process_students()
		else:
			print("Inactiva")



# sched.add_job(sensor, 'interval', seconds=10, id='my_job_id')
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

# @app.route('/pause/<id>')
# def taskPause(id):
# 	message= ""
# 	# print("id:"+id)
# 	if id == "1":
# 		sched.add_job(sensor, 'interval', seconds=5)
# 		sched.start()
# 		message="inicio"
# 	elif id == "2":
# 		sched.resume()
# 		message ="reanudado"
# 	else:
# 		sched.pause()
# 		message= "pausado"
# 	return message
# class pauseTask(id):

# route para parametros del sistema
api.add_resource(SystemParameterList, '/parametroSistema')
api.add_resource(SystemParameter, '/parametroSistema/<systemParameter_id>')
api.add_resource(SystemParameterUpdateDateStudens, '/fecha-estudiantes')
api.add_resource(SystemParameterUpdateDateTeachers, '/fecha-docentes')
api.add_resource(SystemParameterUpdateDateGraduate, '/fecha-egresados')
api.add_resource(SystemParameterTaskStudents, '/taskSchedulerStudents')
api.add_resource(SystemParameterTaskTeachers, '/taskSchedulerTeachers')
api.add_resource(SystemParameterTaskGraduates, '/taskSchedulerGraduates')
api.add_resource(SystemParameterTaskAll, '/taskSchedulerAll')
api.add_resource(Year, '/year')
api.add_resource(FacultyReport, '/faculty')
api.add_resource(Faculty, '/facultad')
api.add_resource(FacultyId, '/facultad/<faculty_id>')
api.add_resource(Profession, '/carrera')
api.add_resource(ProfessionId, '/carrera/<profession_id>')
api.add_resource(MicroservicesError, '/microservices')

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
api.add_resource(GraduateVolunteering, '/egresado-voluntariado')
api.add_resource(GraduateCourses, '/egresado-cursos')
api.add_resource(GraduateCertification, '/egresado-certificacion')
api.add_resource(GraduateEducation, '/egresado-educacion')

# cantidad de egresados por facultad
api.add_resource(GraduateFaculty, '/egresado-facultad')
# cantidad de egresados por año
api.add_resource(GraduatePerYear, '/egresado-ano')
# cantidad de egresados por facultad y año
api.add_resource(GraduateFacultyYear, '/egresado-ano-facultad')
# trabajos de los egresados
api.add_resource(GraduateJobs, '/egresado-trabajos')

if __name__ == "__main__":
	sched = BackgroundScheduler(daemon=True)
	sched.add_job(taskStudents, 'interval', seconds=30)

	sched1 = BackgroundScheduler(daemon=True)
	sched1.add_job(taskTeachers, 'interval', seconds=60)

	sched2 = BackgroundScheduler(daemon=True)
	sched2.add_job(taskGraduates, 'interval', seconds=90)

	sched.start()
	sched1.start()
	sched2.start()

	app.run(debug=True, use_reloader=False)
	
