from flask_restful import abort, Resource, reqparse
import simplejson as json
from textwrap import dedent
from cubes import Workspace, Cell, PointCut, Cut
from flask import make_response
from pymysql import DatabaseError
from common.BD import BD
import datetime
from flask import request

class Carga(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()
    def get(self):
        try:
        
            #for i in range(1892, 2050):
            #    item = {
            #        "codigo": i
            #    }
            #    self.insert("dim_ano", item)
            #    self.commit()
            string = "2018-09-10"
            result = string.split("-")
            print(result[0])
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps([]), 200, { 'Access-Control-Allow-Origin': '*' }