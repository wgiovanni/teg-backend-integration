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
workspace.import_model("resources/cubesmodel/model_teacher_title.json")
browser = workspace.browser("fact_docente_titulo")

class TeacherTitle(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()
    def get(self):
        try:
            browser = workspace.browser("fact_docente_titulo")

            params = "Doctorado"
            result = self.queryOne("SELECT * FROM dim_nivel WHERE codigo = %s", [params])
            if result is None:
                abort(404, message="Resource {} doesn't exists".format(params))
            cut = PointCut("dim_nivel", [result['id']])
            cell = Cell(browser.cube, cuts = [cut])
            r = browser.aggregate(cell, drilldown=["dim_nivel"])
            result = {"profesores-doctorado": r.summary["sumatoria"]}

            workspace.import_model("resources/cubesmodel/model_teacher_faculty.json")
            browser1 = workspace.browser("fact_docente_facultad")
            r1 = browser1.aggregate()
            
            result['total-profesores'] = r1.summary["sumatoria"]
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }

class TeacherTitleFaculty(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()
    def get(self):
        try:
            browser = workspace.browser("fact_docente_titulo")

            params = "Doctorado"
            result = self.queryOne("SELECT * FROM dim_nivel WHERE codigo = %s", [params])
            if result is None:
                abort(404, message="Resource {} doesn't exists".format(params))
            cut = PointCut("dim_nivel", [result['id']])
            cell = Cell(browser.cube, cuts = [cut])
            r = browser.aggregate(cell, drilldown=["dim_nivel"])
            result = {"profesores-doctorado": r.summary["sumatoria"]}

            workspace.import_model("resources/cubesmodel/model_teacher_faculty.json")
            browser1 = workspace.browser("fact_docente_facultad")
            r1 = browser1.aggregate()
            
            result['total-profesores'] = r1.summary["sumatoria"]
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }