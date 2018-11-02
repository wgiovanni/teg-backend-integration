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
workspace.import_model("resources/cubesmodel/model_teacher_faculty.json")
browser = workspace.browser("fact_docente_facultad")

class TeacherStudent(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()
    def get(self):
        try:
            r = browser.aggregate()
            result = {"total-empleado": r.summary["sumatoria"]}

            workspace.import_model("resources/cubesmodel/model_student_faculty.json")
            browser1 = workspace.browser("fact_estudiante_facultad")
            r1 = browser1.aggregate()
            
            result['total-estudiantes'] = r1.summary["sumatoria"]
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }