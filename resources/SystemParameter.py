from flask_restful import abort, Resource
import simplejson as json
from textwrap import dedent
from flask import make_response
from pymysql import DatabaseError
from common.BD import BD
from flask import request

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
			audit = {
				"username": username,
				"action": 'Modificó un parámetro del sistema',
				"module": 'Integración'
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