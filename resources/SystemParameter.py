from flask_restful import abort
import simplejson as json
from textwrap import dedent
from resources.BaseRes import BaseRes
from pymysql import DatabaseError

class SystemParameterList(BaseRes):
	database = "PRUEBA"
	table = "PARAMETRO_SISTEMA"

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
			systemParameter = self.parser.parse_args()
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

class SystemParameter(BaseRes):
	database = "PRUEBA"
	table = "PARAMETRO_SISTEMA"

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
			systemParameter = self.parser.parse_args()
			del systemParameter['id']
			self.update('PARAMETRO_SISTEMA', systemParameter, {'ID': systemParameter_id})
			self.commit()
			result = self.queryOne("SELECT id, codigo, nombre, descripcion, definicion FROM PARAMETRO_SISTEMA WHERE ID = %s", [systemParameter_id])
			if result is None:
				abort(404, message="Resource {} doesn't exist".format(systemParameter_id))
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