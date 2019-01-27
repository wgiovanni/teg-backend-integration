from flask_restful import abort, Resource
import simplejson as json
from textwrap import dedent
from flask import make_response
from pymysql import DatabaseError
from common.BD import BD
from flask import request
import datetime

from constants import DATE_UPDATE, LOAD_INITIAL_UPDATE, DATE_UPDATE_STUDENS, DATE_UPDATE_TEACHERS, DATE_UPDATE_GRADUATE 
from constants import SCHEDULED_TASK_STUDENTS, SCHEDULED_TASK_TEACHERS, SCHEDULED_TASK_GRADUATES, LOG_ACTIVITY_MICROSERVICES

class SystemParameterList(BD, Resource):
	representations = {'application/json': make_response}

	def get(self):
		try:
			result = self.queryAll(dedent("""\
			SELECT id, codigo, nombre, descripcion, definicion
			FROM PARAMETRO_SISTEMA"""))
			#result = self.queryAll("SELECT * FROM PUBLIC.USER")
		except DatabaseError as e:
			self.rollback()
			abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))
		except Exception as e:
			abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

		return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }

	def post(self):
		try:
			systemParameter = request.get_json(force=True)
			print(systemParameter)
			self.insert('PARAMETRO_SISTEMA', systemParameter)
			self.commit()
			result = self.queryOne("SELECT id, codigo, nombre, descripcion, definicion FROM PARAMETRO_SISTEMA ORDER BY ID DESC LIMIT 1")
		except DatabaseError as e:
			self.rollback()
			abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))
		except Exception as e:
			abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))

		return json.dumps(result), 201, { 'Access-Control-Allow-Origin': '*' }

class SystemParameter(BD, Resource):
	representations = {'application/json': make_response}

	def get(self, systemParameter_id):
		try:
			result = self.queryOne("SELECT id, codigo, nombre, descripcion, definicion FROM PARAMETRO_SISTEMA WHERE ID = %s", [systemParameter_id])
			if result is None:
				abort(404, message="Resource {} doesn't exists".format(systemParameter_id))
		except DatabaseError as e:
			self.rollback()
			abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))
		except Exception as e:
			abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))
		return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }

	def put(self, systemParameter_id):
		try:
			jsonData = request.get_json(force=True)
			systemParameter = {
				"codigo": jsonData['codigo'],
				"nombre": jsonData['nombre'],
				"descripcion": jsonData['descripcion'],
				"definicion": jsonData['definicion']
			}
			username = jsonData['user']
			self.update('PARAMETRO_SISTEMA', systemParameter, {'ID': systemParameter_id})
			self.commit()
			result = self.queryOne("SELECT id, codigo, nombre, descripcion, definicion FROM PARAMETRO_SISTEMA WHERE ID = %s", [systemParameter_id])
			if result is None:
				abort(404, message="Resource {} doesn't exist".format(systemParameter_id))
			# datos de auditoria
			ip = ''
			if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
				ip = request.environ['REMOTE_ADDR']
			else:
				ip = request.environ['HTTP_X_FORWARDED_FOR']
			audit = {
				"username": username,
				"action": 'Modificó un parámetro del sistema',
				"module": 'Integración',
				"ip": ip,
				"status": True
			}
			self.insert('HISTORY_ACTION', audit)
			self.commit()
		except DatabaseError as e:
			self.rollback()
			abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))
		except Exception as e:
			abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))

		return json.dumps(result), 201, { 'Access-Control-Allow-Origin': '*' }


	def delete(self, systemParameter_id):
		try:
			print(systemParameter_id)
			result = self.queryOne("SELECT id, codigo, nombre, descripcion, definicion FROM PARAMETRO_SISTEMA WHERE ID = %s", [systemParameter_id])
			print(result)
			if result is None:
				print("Entro")
				abort(404, message="Resource {} doesn't exists".format(systemParameter_id))
			else:
				self.remove("DELETE FROM PARAMETRO_SISTEMA WHERE ID = %s", [systemParameter_id])
				self.commit()
		except DatabaseError as e:
			self.rollback()
			abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))
		except Exception as e:
			abort(404, message="Resource {} doesn't exists".format(systemParameter_id))

		return json.dumps(result), 204, { 'Access-Control-Allow-Origin': '*' }

class SystemParameterUpdateDateStudens(BD, Resource):
	representations = {'application/json': make_response}

	def get(self):
		try:
			date = self.queryOne("SELECT definicion FROM PARAMETRO_SISTEMA WHERE codigo = %s", [DATE_UPDATE_STUDENS])

			if date['definicion'] == '':
				jsonData = {"fecha": '0000-00-00 00:00:00'}
			else:
				jsonData = {"fecha": date['definicion']}
		except DatabaseError as e:
			self.rollback()
			abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))
		except Exception as e:
			abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))
		return json.dumps(jsonData), 200, { 'Access-Control-Allow-Origin': '*' }

class SystemParameterUpdateDateTeachers(BD, Resource):
	representations = {'application/json': make_response}

	def get(self):
		try:
			date = self.queryOne("SELECT definicion FROM PARAMETRO_SISTEMA WHERE codigo = %s", [DATE_UPDATE_TEACHERS])

			if date['definicion'] == '':
				jsonData = {"fecha": '0000-00-00 00:00:00'}
			else:
				jsonData = {"fecha": date['definicion']}
		except DatabaseError as e:
			self.rollback()
			abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))
		except Exception as e:
			abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))
		return json.dumps(jsonData), 200, { 'Access-Control-Allow-Origin': '*' }

class SystemParameterUpdateDateGraduate(BD, Resource):
	representations = {'application/json': make_response}

	def get(self):
		try:
			date = self.queryOne("SELECT definicion FROM PARAMETRO_SISTEMA WHERE codigo = %s", [DATE_UPDATE_GRADUATE])

			if date['definicion'] == '':
				jsonData = {"fecha": '0000-00-00 00:00:00'}
			else:
				jsonData = {"fecha": date['definicion']}
		except DatabaseError as e:
			self.rollback()
			abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))
		except Exception as e:
			abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))
		return json.dumps(jsonData), 200, { 'Access-Control-Allow-Origin': '*' }

class SystemParameterTaskStudents(BD, Resource):
	representations = {'application/json': make_response}

	def get(self):
		try:
			result = self.queryOne("SELECT definicion FROM PARAMETRO_SISTEMA WHERE codigo = %s", [SCHEDULED_TASK_STUDENTS])
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
			result = self.queryOne("SELECT * FROM PARAMETRO_SISTEMA WHERE codigo = %s", [SCHEDULED_TASK_STUDENTS])
			# print(result)
			if active['active'] == False:
				result['definicion'] = "0"
				message = "Desactivación de tarea programada para estudiantes"
			else:
				result['definicion'] = "1"
				message = "Activación de tarea programada para estudiantes"
			self.update('PARAMETRO_SISTEMA', result, {'ID': result['id']})
			self.commit()
			entity = {
				"activity": str(message),
				"message": '.',
				"endpoint": '.',
				"type": '.' 
			}
			self.insert(LOG_ACTIVITY_MICROSERVICES, entity)
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
			result = self.queryOne("SELECT definicion FROM PARAMETRO_SISTEMA WHERE codigo = %s", [SCHEDULED_TASK_STUDENTS])
			print(result)
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
			result = self.queryOne("SELECT definicion FROM PARAMETRO_SISTEMA WHERE codigo = %s", [SCHEDULED_TASK_TEACHERS])
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
			result = self.queryOne("SELECT * FROM PARAMETRO_SISTEMA WHERE codigo = %s", [SCHEDULED_TASK_TEACHERS])
			# print(result)
			if active['active'] == False:
				result['definicion'] = "0"
				message = "Desactivación de tarea programada para docentes"
			else:
				result['definicion'] = "1"
				message = "Activación de tarea programada para docentes"
			self.update('PARAMETRO_SISTEMA', result, {'ID': result['id']})
			self.commit()
			entity = {
				"activity": str(message),
				"message": '.',
				"endpoint": '.',
				"type": '.' 
			}
			self.insert(LOG_ACTIVITY_MICROSERVICES, entity)
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
			result = self.queryOne("SELECT definicion FROM PARAMETRO_SISTEMA WHERE codigo = %s", [SCHEDULED_TASK_TEACHERS])
			print(result)
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
			result = self.queryOne("SELECT definicion FROM PARAMETRO_SISTEMA WHERE codigo = %s", [SCHEDULED_TASK_GRADUATES])
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
			result = self.queryOne("SELECT * FROM PARAMETRO_SISTEMA WHERE codigo = %s", [SCHEDULED_TASK_GRADUATES])
			# print(result)
			if active['active'] == False:
				result['definicion'] = "0"
				message = "Desactivación de tarea programada para egresados"
			else:
				result['definicion'] = "1"
				message = "Activación de tarea programada para egresados"
			self.update('PARAMETRO_SISTEMA', result, {'ID': result['id']})
			self.commit()
			entity = {
				"activity": str(message),
				"message": '.',
				"endpoint": '.',
				"type": '.' 
			}
			self.insert(LOG_ACTIVITY_MICROSERVICES, entity)
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
			result = self.queryOne("SELECT definicion FROM PARAMETRO_SISTEMA WHERE codigo = %s", [SCHEDULED_TASK_GRADUATES])
			print(result)
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
			resultGraduates = self.queryOne("SELECT * FROM PARAMETRO_SISTEMA WHERE codigo = %s", [SCHEDULED_TASK_GRADUATES])
			resultTeachers = self.queryOne("SELECT * FROM PARAMETRO_SISTEMA WHERE codigo = %s", [SCHEDULED_TASK_TEACHERS])
			resultStudents = self.queryOne("SELECT * FROM PARAMETRO_SISTEMA WHERE codigo = %s", [SCHEDULED_TASK_STUDENTS])
			# print(result)
			if active['active'] == False:
				activeTask = "0"
				resultGraduates['definicion'] = "0"
				resultTeachers['definicion'] = "0"
				resultStudents['definicion'] = "0"
				messageGraduates = "Desactivación de tarea programada para egresados"
				messageTeachers = "Desactivación de tarea programada para docentes"
				messageStudents = "Desactivación de tarea programada para estudiantes"
			else:
				activeTask = "1"
				resultGraduates['definicion'] = "1"
				resultTeachers['definicion'] = "1"
				resultStudents['definicion'] = "1"
				messageGraduates = "Activación de tarea programada para egresados"
				messageTeachers = "Activación de tarea programada para docentes"
				messageStudents = "Activación de tarea programada para estudiantes"

			self.update('PARAMETRO_SISTEMA', resultGraduates, {'ID': resultGraduates['id']})
			self.commit()
			self.update('PARAMETRO_SISTEMA', resultTeachers, {'ID': resultTeachers['id']})
			self.commit()
			self.update('PARAMETRO_SISTEMA', resultStudents, {'ID': resultStudents['id']})
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
			self.insert(LOG_ACTIVITY_MICROSERVICES, entityGraduates)
			self.commit()
			self.insert(LOG_ACTIVITY_MICROSERVICES, entityTeachers)
			self.commit()
			self.insert(LOG_ACTIVITY_MICROSERVICES, entityStudents)
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
				"definicion": activeTask
			}
		except DatabaseError as e:
			self.rollback()
			abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))
		except Exception as e:
			abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))

		return json.dumps(result), 201, { 'Access-Control-Allow-Origin': '*' }