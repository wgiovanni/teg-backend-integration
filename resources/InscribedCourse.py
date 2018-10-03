from flask_restful import abort, Resource, reqparse
import simplejson as json
from textwrap import dedent
from cubes import Workspace, Cell, PointCut, Cut
from flask import make_response
from pymysql import DatabaseError
from common.BD import BD

workspace = Workspace()
workspace.register_default_store("sql", url="mysql+mysqlconnector://root@localhost/prueba")
workspace.import_model("resources/cubesmodel/model_inscribed_course.json")
browser = workspace.browser("fact_asignatura_inscrita")

class InscribedCourseStudent(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()
    def get(self):
        try:
            r = browser.aggregate(drilldown=["dim_asignatura_inscrita"])
            result = []
            for row in r:
                item = {"Asignatura": row['dim_asignatura_inscrita.codigo'], "total": row['sumatoria']}
                result.append(item)
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }


class InscribedCourseStudentFaculty(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()
    def get(self, faculty_code):
        try:
            params = faculty_code
            result = self.queryOne("SELECT * FROM DIM_FACULTAD WHERE NOMBRE = %s", [params])
            if result is None:
                abort(404, message="Resource {} doesn't exists".format(params))
            cut = PointCut("dim_facultad", [result['id']])
            cell = Cell(browser.cube, cuts = [cut])
            r = browser.aggregate(cell, drilldown=["dim_facultad","dim_asignatura_inscrita"])
            result = []
            for row in r:
                print(row)
                item = {"asignatura": row['dim_asignatura_inscrita.codigo'], "facultad": row['dim_facultad.nombre'], "total": row['sumatoria']}
                result.append(item)
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }