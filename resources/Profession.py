from flask_restful import abort, Resource, reqparse
import simplejson as json
from textwrap import dedent
from cubes import Workspace, Cell, PointCut, Cut
from flask import make_response
from pymysql import DatabaseError
from common.BD import BD
import datetime
from flask import request

class Profession(BD, Resource):
    representations = {'application/json': make_response}
    def get(self):
        try:
            result = self.queryAll(dedent("""\
            SELECT C.id, C.codigo, C.nombre, C.semestre_anho, F.codigo AS facultad, C.id_facultad, C.pregrado_postgrado 
            FROM dim_carrera AS C
            INNER JOIN dim_facultad AS F
            ON (C.id_facultad = F.id)
            ORDER BY C.nombre ASC"""))
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }

    def post(self):
        try:
            profession = request.get_json(force=True)
            print(profession)

            # verificar que se haya guardado en los modulos
            self.insert('dim_carrera', profession)
            self.commit()
            result = self.queryOne("SELECT id, codigo, nombre, semestre_anho, id_facultad, pregrado_postgrado FROM dim_carrera ORDER BY ID DESC LIMIT 1")

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

class ProfessionId(BD, Resource):
    representations = {'application/json': make_response}

    def get(self, profession_id):
        try:
            result = self.queryOne(dedent("""\
            SELECT id, codigo, nombre, semestre_anho, id_facultad, pregrado_postgrado
            FROM dim_carrera
            WHERE id = %s"""), [profession_id])
            if result is None:
                abort(404, message="Resource {} doesn't exists".format(profession_id))
        except DatabaseError as e:
            self.rollback()
            abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))
        except Exception as e:
            abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))
        return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }

    def put(self, profession_id):
        try:
            profession = request.get_json(force=True)
            print(profession)
            self.update('dim_carrera', profession, {'ID': profession_id})
            self.commit()
            result = self.queryOne("SELECT id, codigo, nombre, semestre_anho, id_facultad, pregrado_postgrado FROM dim_carrera WHERE ID = %s", [profession_id])
            if result is None:
                abort(404, message="Resource {} doesn't exist".format(profession_id))
            

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


    def delete(self, profession_id):
        try:
            result = self.queryOne(dedent("""\
            SELECT id, codigo, nombre, semestre_anho, id_facultad, pregrado_postgrado 
            FROM dim_carrera WHERE ID = %s"""), [profession_id])
            if result is None:
                abort(404, message="Resource {} doesn't exists".format(profession_id))
            else:
                
                self.remove("DELETE FROM dim_carrera WHERE ID = %s", [profession_id])
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
            abort(404, message="Resource {} doesn't exists".format(profession_id))

        return json.dumps(result), 204, { 'Access-Control-Allow-Origin': '*' }