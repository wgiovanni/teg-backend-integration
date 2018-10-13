# variables
from db_credentials import datawarehouse_db_config, postgresql_db_config
from sql_queries import postgresql_queries
from variables import *
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
import mysql.connector

# Resources
from resources.Student import Student, StudentMaleFaculty, StudentFemaleFaculty, StudentSexFaculty, StudentInternacionalFaculty, StudentNacionalFaculty, StudentNationalityFaculty, StudentProfessionFaculty, StudentProfessionConstantsFaculty
from resources.InscribedCourse import InscribedCourseStudent, InscribedCourseStudentFaculty
from resources.Teacher import TeacherPublication, TeacherPublicationFaculty, TeacherWithDoctorate
# metodos
from etl import etl_process, etl_process2

def main():
	print('Empezando ETL')

	# establecer la conexion para la base de datos de destino
	target_cnx = mysql.connector.connect(**datawarehouse_db_config)

	# ciclo para las credenciales

	# postgresql
	for config in postgresql_db_config:
		try:
			print("Cargando db: " + config['database'])
			etl_process(postgresql_queries, target_cnx, config, 'postgresql')
		except Exception as error:
			print("etl para {} tiene error".format(config['database']))
			print('mensaje de error: {}'.format(error))

			continue

	target_cnx.close()

def sensor():
	print(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) # Se obtiene local para la actualizacion de la data cuando se ejecute el job
	print("Scheduler esta vivo!")
#def extraction():
#	etl_process2()

#sched = BackgroundScheduler(deamon=True)
#sched.add_job(main, 'interval', minutes=1)
#sched.add_job(extraction, 'interval', minutes=1)
#sched.start()

app = Flask(__name__)
api = Api(app)
# enable CORS
CORS(app)

@app.route('/')
def extraction():
	#target_cnx = mysql.connector.connect(**datawarehouse_db_config)
	etl_process2()
	
	return "Hola mundo"


# cantidad de estudiantes totales
api.add_resource(Student, '/estudiantes')
# cantidad de estudiantes masculinos por facultad
api.add_resource(StudentMaleFaculty, '/estudiantes-masculinos-facultad')
# cantidad de estudiantes femeninos por facultad
api.add_resource(StudentFemaleFaculty, '/estudiantes-femeninos-facultad')
# cantidad de estudiantes por sexo y por facultad
api.add_resource(StudentSexFaculty, '/estudiantes-sexo-facultad')
# cantidad de estudiantes internacionales por facultad
api.add_resource(StudentInternacionalFaculty, '/estudiantes-internacional-facultad')
# cantidad de estudiantes nacionales por facultad
api.add_resource(StudentNacionalFaculty, '/estudiantes-nacional-facultad')
# cantidad de estudiantes por nacionalidad y por facultad
api.add_resource(StudentNationalityFaculty, '/estudiantes-nacionalidad-facultad')
# cantidad de estudiantes por carrera y por facultad
api.add_resource(StudentProfessionFaculty, '/estudiantes-carrera-facultad')
# cantidad de estudiantes por carrera, dada la facultad
api.add_resource(StudentProfessionConstantsFaculty, '/estudiantes-carrera/<faculty_code>')

# Cube para las materias inscritas
api.add_resource(InscribedCourseStudent, '/asignatura-inscrita-estudiante')
api.add_resource(InscribedCourseStudentFaculty, '/asignatura-inscrita-estudiante/<faculty_code>')


# docentes
# pulicaciones por docente
api.add_resource(TeacherPublication, '/profesor-publicacion')
api.add_resource(TeacherWithDoctorate, '/profesor-doctorado')
if __name__ == "__main__":
	#main()
	app.run(debug=True)