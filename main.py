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
from resources.Student import Student, StudentMaleFaculty, StudentFemaleFaculty, StudentSexFaculty, StudentInternacionalFaculty, StudentNacionalFaculty, StudentNationalityFaculty, StudentProfessionFaculty, StudentProfessionConstantsFaculty
from resources.InscribedCourse import InscribedCourseStudent, InscribedCourseStudentFaculty
from resources.TeacherPublication import TeacherPublication, TeacherPublicationFaculty
from resources.Teacher import TeacherWithDoctorateFaculty, TeacherGradeFaculty, TeacherWithDoctorate, TeacherInternacionals, TeacherNational
from resources.GraduatePatents import GraduatePatents
# metodos
from etl import etl_process2

def sensor():
	#print(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) # Se obtiene local para la actualizacion de la data cuando se ejecute el job
	print("Scheduler esta vivo!000000000000000000000")

def sensor1():
	print(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) # Se obtiene local para la actualizacion de la data cuando se ejecute el job
	print("Scheduler esta vivo11111111111111111111111!")
#def extraction():
#	etl_process2()

#sched = BackgroundScheduler(deamon=True)
#sched.add_job(main, 'interval', minutes=1)
#sched.add_job(sensor, trigger='interval', seconds=10)
#sched.add_job(sensor1, 'interval', seconds=20)
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

# route para parametros del sistema
api.add_resource(SystemParameterList, '/parametroSistema')
api.add_resource(SystemParameter, '/parametroSistema/<systemParameter_id>')

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
api.add_resource(StudentProfessionConstantsFaculty, '/estudiantes-carrera/<facultad_codigo>')

# Cube para las materias inscritas
api.add_resource(InscribedCourseStudent, '/asignatura-inscrita-estudiante')
api.add_resource(InscribedCourseStudentFaculty, '/asignatura-inscrita-estudiante/<facultad_codigo>')


# docentes
# pulicaciones por docente
api.add_resource(TeacherPublication, '/profesor-publicacion')
# cantidad de publicaciones por facultad
api.add_resource(TeacherPublicationFaculty, '/profesor-publicacion-facultad')
# cantidad de profesores con doctorado o phd por facultad
api.add_resource(TeacherWithDoctorateFaculty, '/profesor-doctorado-facultad')
# cantidad de profesores por facultad, dado un grado
api.add_resource(TeacherGradeFaculty, '/profesor-grado-facultad/<grado_codigo>')
# proporcion de profesores con doctorado (total doctorado/total profesores)
api.add_resource(TeacherWithDoctorate, '/profesor-doctorado-proporcion')
# cantidad de profesores internacionales 
api.add_resource(TeacherInternacionals, '/profesor-internacional')
# cantidad de profesores nacionales 
api.add_resource(TeacherNational, '/profesor-nacional')




# egresados
api.add_resource(GraduatePatents, '/egresado-patentes')

if __name__ == "__main__":
	#main()
	app.run(debug=True)