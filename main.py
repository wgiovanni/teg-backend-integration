# variables
from variables import *
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from flask import Flask, request, make_response
from flask_cors import CORS
from flask_restful import Api, Resource, abort
import mysql.connector
import simplejson as json
import requests
from common.BD import BD
from db_credentials import datawarehouse_db_config
from sql_queries import systemParameter
from pymysql import DatabaseError
from flask_apscheduler import APScheduler
from apscheduler.triggers.cron import CronTrigger
 
import time

# Resources
from resources.SystemParameter import SystemParameterList, SystemParameter, SystemParameterUpdateDateStudens, SystemParameterUpdateDateTeachers 
from resources.SystemParameter import SystemParameterUpdateDateGraduate
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
from resources.GraduateStudiosUc import GraduateFaculty, GraduatePerYear, GraduateFacultyYear, GraduateTrust
from resources.GraduateVolunteering import GraduateVolunteering
from resources.Year import Year
from resources.Faculty import FacultyReport, Faculty, FacultyId
from resources.Profession import Profession, ProfessionId
from resources.MicroservicesError import MicroservicesError

from constants import CONTENT_TYPE, SCHEDULED_TASK_GRADUATES, SCHEDULED_TASK_TEACHERS, SCHEDULED_TASK_STUDENTS, LOG_ACTIVITY_MICROSERVICES
from constants import CRON_TAB_GRADUATES, CRON_TAB_STUDENTS, CRON_TAB_TEACHERS
# metodos
from etl import etl_process_students, etl_process_teachers, etl_process_graduates


# def sensor1():
# # 	# print(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) # Se obtiene local para la actualizacion de la data cuando se ejecute el job
# 	print("Scheduler esta vivo11111111111111111111111!")
# # 	target_cnx = mysql.connector.connect(**datawarehouse_db_config)
# # 	target_cursor = target_cnx.cursor(buffered=True)
# # 	target_cursor.execute("USE {}".format(datawarehouse_name))
# # 	target_cursor.execute(systemParameter.get_query, ["TAREA_PROGRAMADA"])
# # 	row = target_cursor.fetchone()
# # 	# print(row)
# # 	if (row[4] == "1"):
# # 		print("Activa Sensor 1")
# # 		# print("Sensor 1")
# # 		# sched.resume()
# # 		# etl_process()
# # 	else:
# # 		print("Inactiva Sensor 1")
# # 		# print("Scheduler esta vivo!000000000000000000000")


def taskStudents1(task_id):
	print("HOLA")
	etl_process_students()
	time.sleep(5)

def taskTeachers1(task_id):
	print("HOLA1")
	etl_process_teachers()
	time.sleep(5)

def taskGraduates1(task_id):
	print("HOLA2")
	etl_process_graduates()
	time.sleep(5)

app = Flask(__name__)
api = Api(app, prefix="/api/v1")
# enable CORS
CORS(app)


scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

target_cnx = mysql.connector.connect(**datawarehouse_db_config)
target_cursor = target_cnx.cursor(buffered=True)
target_cursor.execute("USE {}".format(datawarehouse_name))
#cron tab para estudiantes
target_cursor.execute(systemParameter.get_query, [CRON_TAB_STUDENTS])
row = target_cursor.fetchone()
triggerStudents = CronTrigger.from_crontab(row[4])

target_cursor.execute(systemParameter.get_query, [SCHEDULED_TASK_STUDENTS])
row = target_cursor.fetchone()
target_cursor.execute(systemParameter.update_query, ["1", row[0]])
target_cnx.commit()

#cron tab para docentes
target_cursor.execute(systemParameter.get_query, [CRON_TAB_TEACHERS])
row = target_cursor.fetchone()
triggerTeachers = CronTrigger.from_crontab(row[4])

target_cursor.execute(systemParameter.get_query, [SCHEDULED_TASK_TEACHERS])
row = target_cursor.fetchone()
target_cursor.execute(systemParameter.update_query, ["1", row[0]])
target_cnx.commit()

#cron tab para egresados
target_cursor.execute(systemParameter.get_query, [CRON_TAB_GRADUATES])
row = target_cursor.fetchone()
triggerGraduates = CronTrigger.from_crontab(row[4])

target_cursor.execute(systemParameter.get_query, [SCHEDULED_TASK_GRADUATES])
row = target_cursor.fetchone()
target_cursor.execute(systemParameter.update_query, ["1", row[0]])
target_cnx.commit()

app.apscheduler.add_job(func=taskStudents1, trigger=triggerStudents, args=[1], id='j'+str(1))
app.apscheduler.add_job(func=taskTeachers1, trigger=triggerTeachers, args=[1], id='j'+str(2))
app.apscheduler.add_job(func=taskGraduates1, trigger=triggerGraduates, args=[1], id='j'+str(3))

class SystemParameterTaskStudents(BD, Resource):
	representations = {'application/json': make_response}

	def get(self):
		try:
			result = self.queryOne("SELECT definicion FROM parametro_sistema WHERE codigo = %s", [SCHEDULED_TASK_STUDENTS])
			activityMicroservices = self.queryAll("SELECT * FROM log_activity_microservices WHERE status = 0 ORDER BY date DESC")
			for r in activityMicroservices:
				r['date'] = r['date'].strftime('%Y-%m-%d %H:%M:%S')
			result['activityMicroservices'] = activityMicroservices
		except DatabaseError as e:
			self.rollback()
			abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))
		except Exception as e:
			abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))
		return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }
	
	def post(self):
		try:
			active = request.get_json(force=True)
			# print(active)
			message = ''
			result = self.queryOne("SELECT * FROM parametro_sistema WHERE codigo = %s", [SCHEDULED_TASK_STUDENTS])
			# print(result)
			if active['active'] == False:
				result['definicion'] = "0"
				message = "Desactivación de tarea programada para estudiantes"
				app.apscheduler.pause_job(id='j'+str(1))
			else:
				result['definicion'] = "1"
				message = "Activación de tarea programada para estudiantes"
				app.apscheduler.resume_job(id='j'+str(1))
			self.update('parametro_sistema', result, {'ID': result['id']})
			self.commit()
			entity = {
				"activity": str(message),
				"message": '.',
				"endpoint": '.',
				"type": '.' 
			}
			self.insert(log_activity_microservices, entity)
			self.commit()
			username = active['user']
			if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
				ip = request.environ['REMOTE_ADDR']
			else:
				ip = request.environ['HTTP_X_FORWARDED_FOR']
			audit = {
				"username": username,
				"action": message,
				"module": 'Administración',
				"ip": ip,
				"status": True
			}
			self.insert('HISTORY_ACTION', audit)
			self.commit()
			definition = self.queryOne("SELECT definicion FROM parametro_sistema WHERE codigo = %s", [SCHEDULED_TASK_STUDENTS])
			result = {
				"definition": definition
			}
			activityMicriservices = self.queryAll("SELECT * FROM log_activity_microservices WHERE status = 0 ORDER BY date DESC")
			for r in activityMicriservices:
				r['date'] = r['date'].strftime('%Y-%m-%d %H:%M:%S')
			result['activityMicroservices'] = activityMicriservices
		except DatabaseError as e:
			self.rollback()
			abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))
		except Exception as e:
			abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))

		return json.dumps(result), 201, { 'Access-Control-Allow-Origin': '*' }

class SystemParameterTaskTeachers(BD, Resource):
	representations = {'application/json': make_response}

	def get(self):
		try:
			result = self.queryOne("SELECT definicion FROM parametro_sistema WHERE codigo = %s", [SCHEDULED_TASK_TEACHERS])
			activityMicroservices = self.queryAll("SELECT * FROM log_activity_microservices WHERE status = 0 ORDER BY date DESC")
			for r in activityMicroservices:
				r['date'] = r['date'].strftime('%Y-%m-%d %H:%M:%S')
			result['activityMicroservices'] = activityMicroservices
		except DatabaseError as e:
			self.rollback()
			abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))
		except Exception as e:
			abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))
		return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }
	
	def post(self):
		try:
			active = request.get_json(force=True)
			# print(active)
			message = ''
			result = self.queryOne("SELECT * FROM parametro_sistema WHERE codigo = %s", [SCHEDULED_TASK_TEACHERS])
			# print(result)
			if active['active'] == False:
				result['definicion'] = "0"
				message = "Desactivación de tarea programada para docentes"
				app.apscheduler.pause_job(id='j'+str(2))
			else:
				result['definicion'] = "1"
				message = "Activación de tarea programada para docentes"
				app.apscheduler.resume_job(id='j'+str(2))
			self.update('parametro_sistema', result, {'ID': result['id']})
			self.commit()
			entity = {
				"activity": str(message),
				"message": '.',
				"endpoint": '.',
				"type": '.' 
			}
			self.insert(log_activity_microservices, entity)
			self.commit()
			username = active['user']
			if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
				ip = request.environ['REMOTE_ADDR']
			else:
				ip = request.environ['HTTP_X_FORWARDED_FOR']
			audit = {
				"username": username,
				"action": message,
				"module": 'Administración',
				"ip": ip,
				"status": True
			}
			self.insert('HISTORY_ACTION', audit)
			self.commit()
			definition = self.queryOne("SELECT definicion FROM parametro_sistema WHERE codigo = %s", [SCHEDULED_TASK_TEACHERS])
			result = {
				'definition': definition
			}
			activityMicroservices = self.queryAll("SELECT * FROM log_activity_microservices WHERE status = 0 ORDER BY date DESC")
			for r in activityMicroservices:
				r['date'] = r['date'].strftime('%Y-%m-%d %H:%M:%S')
			result['activityMicroservices'] = activityMicroservices
		except DatabaseError as e:
			self.rollback()
			abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))
		except Exception as e:
			abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))

		return json.dumps(result), 201, { 'Access-Control-Allow-Origin': '*' }

class SystemParameterTaskGraduates(BD, Resource):
	representations = {'application/json': make_response}

	def get(self):
		try:
			result = self.queryOne("SELECT definicion FROM parametro_sistema WHERE codigo = %s", [SCHEDULED_TASK_GRADUATES])
			activityMicriservices = self.queryAll("SELECT * FROM log_activity_microservices WHERE status = 0 ORDER BY date DESC")
			for r in activityMicriservices:
				r['date'] = r['date'].strftime('%Y-%m-%d %H:%M:%S')
			result['activityMicroservices'] = activityMicriservices
		except DatabaseError as e:
			self.rollback()
			abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))
		except Exception as e:
			abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))
		return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }
	
	def post(self):
		try:
			active = request.get_json(force=True)
			# print(active)
			message = ''
			result = self.queryOne("SELECT * FROM parametro_sistema WHERE codigo = %s", [SCHEDULED_TASK_GRADUATES])
			# print(result)
			if active['active'] == False:
				result['definicion'] = "0"
				message = "Desactivación de tarea programada para egresados"
				app.apscheduler.pause_job(id='j'+str(3))
			else:
				result['definicion'] = "1"
				message = "Activación de tarea programada para egresados"
				app.apscheduler.resume_job(id='j'+str(3))
			self.update('parametro_sistema', result, {'ID': result['id']})
			self.commit()
			entity = {
				"activity": str(message),
				"message": '.',
				"endpoint": '.',
				"type": '.' 
			}
			self.insert(log_activity_microservices, entity)
			self.commit()
			username = active['user']
			if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
				ip = request.environ['REMOTE_ADDR']
			else:
				ip = request.environ['HTTP_X_FORWARDED_FOR']
			audit = {
				"username": username,
				"action": message,
				"module": 'Administración',
				"ip": ip,
				"status": True
			}
			self.insert('HISTORY_ACTION', audit)
			self.commit()
			definition = self.queryOne("SELECT definicion FROM parametro_sistema WHERE codigo = %s", [SCHEDULED_TASK_GRADUATES])
			result = {
				'definition': definition
			}
			activityMicriservices = self.queryAll("SELECT * FROM log_activity_microservices WHERE status = 0 ORDER BY date DESC")
			for r in activityMicriservices:
				r['date'] = r['date'].strftime('%Y-%m-%d %H:%M:%S')
			result['activityMicroservices'] = activityMicriservices
		except DatabaseError as e:
			self.rollback()
			abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))
		except Exception as e:
			abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))

		return json.dumps(result), 201, { 'Access-Control-Allow-Origin': '*' }
		

class SystemParameterTaskAll(BD, Resource):
	representations = {'application/json': make_response}

	def post(self):
		try:
			active = request.get_json(force=True)
			# print(active)
			messageGraduates = ''
			messageTeachers = ''
			messageStudents = '	' 
			activeTask = ''
			resultGraduates = self.queryOne("SELECT * FROM parametro_sistema WHERE codigo = %s", [SCHEDULED_TASK_GRADUATES])
			resultTeachers = self.queryOne("SELECT * FROM parametro_sistema WHERE codigo = %s", [SCHEDULED_TASK_TEACHERS])
			resultStudents = self.queryOne("SELECT * FROM parametro_sistema WHERE codigo = %s", [SCHEDULED_TASK_STUDENTS])
			# print(result)
			if active['active'] == False:
				activeTask = "0"
				resultGraduates['definicion'] = "0"
				resultTeachers['definicion'] = "0"
				resultStudents['definicion'] = "0"
				messageGraduates = "Desactivación de tarea programada para egresados"
				messageTeachers = "Desactivación de tarea programada para docentes"
				messageStudents = "Desactivación de tarea programada para estudiantes"
				app.apscheduler.pause_job(id='j'+str(1))
				app.apscheduler.pause_job(id='j'+str(2))
				app.apscheduler.pause_job(id='j'+str(3))
			else:
				activeTask = "1"
				resultGraduates['definicion'] = "1"
				resultTeachers['definicion'] = "1"
				resultStudents['definicion'] = "1"
				messageGraduates = "Activación de tarea programada para egresados"
				messageTeachers = "Activación de tarea programada para docentes"
				messageStudents = "Activación de tarea programada para estudiantes"
				app.apscheduler.resume_job(id='j'+str(1))
				app.apscheduler.resume_job(id='j'+str(2))
				app.apscheduler.resume_job(id='j'+str(3))

			self.update('parametro_sistema', resultGraduates, {'ID': resultGraduates['id']})
			self.commit()
			self.update('parametro_sistema', resultTeachers, {'ID': resultTeachers['id']})
			self.commit()
			self.update('parametro_sistema', resultStudents, {'ID': resultStudents['id']})
			self.commit()
			entityGraduates = {
				"activity": str(messageGraduates),
				"message": '.',
				"endpoint": '.',
				"type": '.' 
			}

			entityTeachers = {
				"activity": str(messageTeachers),
				"message": '.',
				"endpoint": '.',
				"type": '.' 
			}
			entityStudents = {
				"activity": str(messageStudents),
				"message": '.',
				"endpoint": '.',
				"type": '.' 
			}
			self.insert(log_activity_microservices, entityGraduates)
			self.commit()
			self.insert(log_activity_microservices, entityTeachers)
			self.commit()
			self.insert(log_activity_microservices, entityStudents)
			self.commit()
			username = active['user']
			if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
				ip = request.environ['REMOTE_ADDR']
			else:
				ip = request.environ['HTTP_X_FORWARDED_FOR']
			audit = {
				"username": username,
				"action": messageStudents,
				"module": 'Administración',
				"ip": ip,
				"status": True
			}
			audit1 = {
				"username": username,
				"action": messageTeachers,
				"module": 'Administración',
				"ip": ip,
				"status": True
			}
			audit2 = {
				"username": username,
				"action": messageGraduates,
				"module": 'Administración',
				"ip": ip,
				"status": True
			}
			self.insert('HISTORY_ACTION', audit)
			self.commit()
			self.insert('HISTORY_ACTION', audit1)
			self.commit()
			self.insert('HISTORY_ACTION', audit2)
			self.commit()
			result = {
				'definicion': activeTask
			}
			activityMicriservices = self.queryAll("SELECT * FROM log_activity_microservices WHERE status = 0 ORDER BY date DESC")
			for r in activityMicriservices:
				r['date'] = r['date'].strftime('%Y-%m-%d %H:%M:%S')
			result['activityMicroservices'] = activityMicriservices

		except DatabaseError as e:
			self.rollback()
			abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))
		except Exception as e:
			abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))

		return json.dumps(result), 201, { 'Access-Control-Allow-Origin': '*' }

@app.route('/')
def extraction():
	
	etl_process()
	return "Hola mundo"

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

#ESTUDIANTES
# cantidad de estudiantes totales
api.add_resource(Student, '/estudiantes-total')
# cantidad de estudiantes por facultad
api.add_resource(StudentFaculty, '/estudiantes-facultad')
# cantidad de estudiantes masculinos por facultad NO
api.add_resource(StudentMaleFaculty, '/estudiantes-masculinos-facultad')
# cantidad de estudiantes femeninos por facultad NO
api.add_resource(StudentFemaleFaculty, '/estudiantes-femeninos-facultad')
# cantidad de estudiantes por sexo y por facultad
api.add_resource(StudentSexFaculty, '/estudiantes-sexo-facultad')
# cantidad de estudiantes internacionales
api.add_resource(StudentInternacional, '/estudiantes-internacionales-proporcion') 
# cantidad de estudiantes internacionales por facultad NO
api.add_resource(StudentInternacionalFaculty, '/estudiantes-internacional-facultad')
# cantidad de estudiantes nacionales por facultad NO
api.add_resource(StudentNacionalFaculty, '/estudiantes-nacional-facultad')
# cantidad de estudiantes por nacionalidad y por facultad
api.add_resource(StudentNationalityFaculty, '/estudiantes-nacionalidad-facultad')
# cantidad de estudiantes por carrera y por facultad NO
api.add_resource(StudentProfessionFaculty, '/estudiantes-carrera-facultad')
# cantidad de estudiantes por carrera, dada la facultad NO
api.add_resource(StudentProfessionConstantsFaculty, '/estudiantes-carrera/<facultad_codigo>')
# cantidad de estudiantes con discapacidad por facultad
api.add_resource(StudentDisabilityFaculty, '/estudiantes-discapacidad-facultad')
# cantidad de estudiantes con etnia por facultad 
api.add_resource(StudentEthnicGroupFaculty, '/estudiantes-etnia-facultad')
# matricula de pregredo por sexo NO
api.add_resource(StudentUndergraduateSex, '/estudiantes-pregrado-sexo')
# matricula de pregrado por nacionalidad
api.add_resource(StudentUndergraduateNacionality, '/estudiantes-pregrado-nacionalidad')
# cantidad de estudiantes por año NO
api.add_resource(StudentPerYear, '/estudiantes-ano')
# cantidad de estudiantes por facultad y por año NO
api.add_resource(StudentYearFaculty, '/estudiantes-ano-facultad')


# DOCENTES
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


#EGRESADO
# cantidad de egresados por facultad
api.add_resource(GraduateFaculty, '/egresado-facultad')
# cantidad de egresados por año
api.add_resource(GraduatePerYear, '/egresado-ano')
# cantidad de egresados por facultad y año
api.add_resource(GraduateFacultyYear, '/egresado-ano-facultad')
# trabajos de los egresados
api.add_resource(GraduateJobs, '/egresado-trabajos')
api.add_resource(GraduateTrust, '/egresado-confianza')


@app.route('/run-tasks')
def run_tasks():
    # for i in range(3):
	# app.apscheduler.add_job(func=scheduled_task, trigger='date', args=[1], id='j'+str(1))
	crojob = '*/1'
	cron = 'cron'
	app.apscheduler.add_job(func=scheduled_task, trigger=cron, minute=crojob, args=[1], id='j'+str(1))
 
	return 'Scheduled several long running tasks.', 200
 
def scheduled_task(task_id):
    # for i in range(3):
	time.sleep(5)
	print('Task {}'.format(task_id))

def scheduled_task2(task_id):
    # for i in range(3):
	time.sleep(5)
	print('Task {}'.format(task_id))


# crojob = '*/1'
# cron = 'cron'
# cron = 'interval'
# cronJob = 5


# app.apscheduler.add_job(func=taskStudents1, trigger=cron, seconds=cronJob, args=[1], id='j'+str(1))
# app.apscheduler.add_job(func=etl_process_teachers, trigger=cron, minute=crojob, args=[1], id='j'+str(2))
# app.apscheduler.add_job(func=etl_process_graduates, trigger=cron, minute=crojob, args=[1], id='j'+str(3))

# @app.route('/stop-tasks')
# def stop_task():
# 	app.apscheduler.pause_job(id='j'+str(1))
# 	return 'stop', 200

# @app.route('/stop-tasks2')
# def stop_task2():l
# 	app.apscheduler.pause_job(id='j'+str(2))
# 	return 'stop', 200
 
# @app.route('/resume-tasks')
# def resume_task():
# 	app.apscheduler.resume_job(id='j'+str(1))
# 	return 'resume', 200

# @app.route('/resume-tasks2')
# def resume_task2():
# 	app.apscheduler.resume_job(id='j'+str(2))
# 	return 'resume', 200



if __name__ == "__main__":
	# sched = BackgroundScheduler(daemon=True)
	# sched.add_job(taskStudents, 'interval', minutes=1)

	# sched1 = BackgroundScheduler(daemon=True)
	# sched1.add_job(taskTeachers, 'interval', minutes=1)

	# sched2 = BackgroundScheduler(daemon=True)
	# sched2.add_job(taskGraduates, 'interval', minutes=1)

	# sched3 = BackgroundScheduler()
	# crojob = '*/1'
	# cron = 'cron'
	# sched3.add_job(sensor1, trigger=cron, minute=crojob, id='my_job_id')

	# sched.start()
	# sched1.start()
	# sched2.start()
	# sched3.start()

	
	app.run(debug=True, use_reloader=False)
	
