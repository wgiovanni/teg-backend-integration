from flask_restful import abort, Resource, reqparse
import simplejson as json
from textwrap import dedent
from cubes import Workspace, Cell, PointCut, Cut
from flask import make_response
from pymysql import DatabaseError
from common.BD import BD
import datetime
from flask import request

class FacultyReport(BD, Resource):
    representations = {'application/json': make_response}
    def get(self):
        try:
            result = self.queryAll("SELECT id, codigo, nombre FROM dim_facultad ORDER BY nombre ASC")

        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }

class Faculty(BD, Resource):
    representations = {'application/json': make_response}
    def get(self):
        try:
            result = self.queryAll("SELECT id, codigo, nombre FROM dim_facultad ORDER BY nombre ASC")
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }

    def post(self):
        try:
            faculty = request.get_json(force=True)
            print(faculty)

            # verificar que se haya guardado en los modulos
            self.insert('dim_facultad', faculty)
            self.commit()
            result = self.queryOne("SELECT id, codigo, nombre FROM dim_facultad ORDER BY ID DESC LIMIT 1")

            # ip = ''
            # if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
            #     ip = request.environ['REMOTE_ADDR']
            # else:
            #     ip = request.environ['HTTP_X_FORWARDED_FOR']
            # audit = {
            #     "username": user['user'],
            #     "action": 'Agregó un usuario',
            #     "module": 'Usuarios',
            #     "ip": ip,
            #     "status": True

            # }
            # self.insert('HISTORY_ACTION', audit)
            # self.commit()

        except DatabaseError as e:
            self.rollback()
            abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))
        except Exception as e:
            abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(result), 201, { 'Access-Control-Allow-Origin': '*' }

class FacultyId(BD, Resource):
    representations = {'application/json': make_response}

    def get(self, faculty_id):
        try:
            result = self.queryOne(dedent("""\
            SELECT id, codigo, nombre 
            FROM dim_facultad
            WHERE id = %s"""), [faculty_id])
            if result is None:
                abort(404, message="Resource {} doesn't exists".format(faculty_id))
        except DatabaseError as e:
            self.rollback()
            abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))
        except Exception as e:
            abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))
        return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }

    def put(self, faculty_id):
        try:
            faculty = request.get_json(force=True)
            print(faculty)
            self.update('dim_facultad', faculty, {'ID': faculty_id})
            self.commit()
            result = self.queryOne("SELECT id, codigo, nombre FROM dim_facultad WHERE ID = %s", [faculty_id])
            if result is None:
                abort(404, message="Resource {} doesn't exist".format(faculty_id))
            

            # datos de auditoria
            # ip = ''
            # if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
            #     ip = request.environ['REMOTE_ADDR']
            # else:
            #     ip = request.environ['HTTP_X_FORWARDED_FOR']
            # audit = {
            #     "username": user['user'],
            #     "action": 'Modificó un usuario',
            #     "module": 'Usuarios',
            #     "ip": ip,
            #     "status": True
            # }
            # self.insert('HISTORY_ACTION', audit)
            # self.commit()
        except DatabaseError as e:
            self.rollback()
            abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))
        except Exception as e:
            abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(result), 201, { 'Access-Control-Allow-Origin': '*' }


    def delete(self, faculty_id):
        try:
            # jsonData = request.get_data(cache=False, as_text=False, parse_form_data=False)
            # jsonData = json.loads(jsonData)
            print(faculty_id)
            result = self.queryOne("SELECT id, codigo, nombre FROM dim_facultad WHERE ID = %s", [faculty_id])
            if result is None:
                abort(404, message="Resource {} doesn't exists".format(faculty_id))
            else:
                
                self.remove("DELETE FROM dim_facultad WHERE ID = %s", [faculty_id])
                # datos de auditoria
                # ip = ''
                # if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
                # 	ip = request.environ['REMOTE_ADDR']
                # else:
                # 	ip = request.environ['HTTP_X_FORWARDED_FOR']
                # audit = {
                # 	"username": jsonData['user'],
                # 	"action": 'Eliminó un usuario',
                # 	"module": 'Usuarios',
                # 	"ip": ip,
                # 	"status": True
                # }
                # self.insert('HISTORY_ACTION', audit)
                self.commit()
        except DatabaseError as e:
            print(e)
            self.rollback()
            abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))
        except Exception as e:
            abort(404, message="Resource {} doesn't exists".format(faculty_id))

        return json.dumps(result), 204, { 'Access-Control-Allow-Origin': '*' }