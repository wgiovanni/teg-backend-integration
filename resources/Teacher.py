from flask_restful import abort, Resource, reqparse
import simplejson as json
from textwrap import dedent
from cubes import Workspace, Cell, PointCut, Cut
from flask import make_response
from pymysql import DatabaseError
from common.BD import BD
from datetime import datetime

workspace = Workspace()
workspace.register_default_store("sql", url="mysql+mysqlconnector://root@localhost/prueba")
workspace.import_model("resources/cubesmodel/model_teacher.json")
browser = workspace.browser("fact_docente")

class TeacherWithDoctorate(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()
    def get(self):
        try:
            #r = browser.aggregate(drilldown=["dim_publicacion", "dim_docente"])
            cut = PointCut("dim_facultad", [8])
            cell = Cell(browser.cube, cuts = [cut])
            r = browser.aggregate(cell, drilldown=["dim_facultad", "dim_docente"])
            for row in r:
                print(row)
            print(int(r.summary["sumatoria"]))
            print(int(r.summary["sumatoria_citacion"]))
            
            #result = {"total-estudiantes": int(r.summary["sumatoria"])}
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps([]), 200, { 'Access-Control-Allow-Origin': '*' }