from flask_restful import abort, Resource, reqparse
import simplejson as json
from textwrap import dedent
from cubes import Workspace, Cell, PointCut, Cut
from flask import make_response
from pymysql import DatabaseError
from common.BD import BD
import datetime
import requests
from flask import request

class MicroservicesError(BD, Resource):
    representations = {'application/json': make_response}
    def get(self):
        try:
            result = self.queryAll("SELECT * FROM log_errors_microservices WHERE status = 0 ORDER BY date DESC")
            for r in result:
                r['date'] = r['date'].strftime('%Y-%m-%d %H:%M:%S')
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }

    def delete(self):
        try:
            print("Entro")
            #self.remove("DELETE FROM HISTORY_ACTION",[])
            self.remove("UPDATE log_errors_microservices SET status = %s",[True])
            self.commit()
            print("Salio")
        except DatabaseError as e:
            self.rollback()
            abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))
        except Exception as e:
            abort(404, message="Resource {} doesn't exists")

        return json.dumps({"message": "Eliminado todos los registros"}), 204, { 'Access-Control-Allow-Origin': '*' }