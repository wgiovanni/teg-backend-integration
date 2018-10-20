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
browser = workspace.browser("fact_docente_facultad")

class TeacherWithDoctorateFaculty(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()
    def get(self):
        try:
            params = "Doctorado"
            result = self.queryOne("SELECT * FROM dim_grado WHERE nombre = %s", [params])
            if result is None:
                abort(404, message="Resource {} doesn't exists".format(params))
            cut = PointCut("dim_grado", [result['id']])
            cell = Cell(browser.cube, cuts = [cut])
            r = browser.aggregate(cell, drilldown=["dim_facultad", "dim_grado"])

            facultades = self.queryAll("SELECT nombre FROM DIM_FACULTAD")

            result = []
            for row in r:
                print(row)
                item = {"facultad": row['dim_facultad.nombre'], "cantidad": row['sumatoria']}
                result.append(item)
            flag = False
            for f in facultades:
                for r in result:
                    if r['facultad'] == f['nombre']:
                        flag = True
                if flag == False:
                    item = {"facultad": f['nombre'], "cantidad": 0}
                    result.append(item)
                flag = False
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }


class TeacherGradeFaculty(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()
    def get(self, grado_codigo):
        try:
            params = grado_codigo
            result = self.queryOne("SELECT * FROM dim_grado WHERE nombre = %s", [params])
            if result is None:
                abort(404, message="Resource {} doesn't exists".format(params))
            cut = PointCut("dim_grado", [result['id']])
            cell = Cell(browser.cube, cuts = [cut])
            r = browser.aggregate(cell, drilldown=["dim_facultad", "dim_grado"])

            facultades = self.queryAll("SELECT nombre FROM DIM_FACULTAD")

            result = []
            for row in r:
                item = {"facultad": row['dim_facultad.nombre'], "cantidad": row['sumatoria']}
                result.append(item)
            flag = False
            for f in facultades:
                for r in result:
                    if r['facultad'] == f['nombre']:
                        flag = True
                if flag == False:
                    item = {"facultad": f['nombre'], "cantidad": 0}
                    result.append(item)
                flag = False
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }

class TeacherWithDoctorate(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()
    def get(self):
        try:
            params = "Maestria"
            result = self.queryOne("SELECT * FROM dim_grado WHERE nombre = %s", [params])
            if result is None:
                abort(404, message="Resource {} doesn't exists".format(params))

            cut = PointCut("dim_grado", [result['id']])
            cell = Cell(browser.cube, cuts = [cut])
            r = browser.aggregate(cell, drilldown=["dim_grado"])

            result = {}
            if r is not None:
                result = {"profesores-doctorado": r.summary['sumatoria']}
            
            r = browser.aggregate(drilldown=["dim_docente"])
            if r is not None:
                result['total-profesores'] = r.summary['sumatoria']
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }


class TeacherInternacionals(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()
    def get(self):
        try:
            params = "Extranjero"
            result = self.queryOne("SELECT * FROM dim_nacionalidad WHERE codigo = %s", [params])
            if result is None:
                abort(404, message="Resource {} doesn't exists".format(params))

            cut = PointCut("dim_nacionalidad", [result['id']])
            cell = Cell(browser.cube, cuts = [cut])
            r = browser.aggregate(cell, drilldown=["dim_nacionalidad"])

            result = {}
            if r is not None:
                result = {"profesores-internacionales": r.summary['sumatoria']}
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }

class TeacherNational(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()
    def get(self):
        try:
            params = "Venezolano"
            result = self.queryOne("SELECT * FROM dim_nacionalidad WHERE codigo = %s", [params])
            if result is None:
                abort(404, message="Resource {} doesn't exists".format(params))

            cut = PointCut("dim_nacionalidad", [result['id']])
            cell = Cell(browser.cube, cuts = [cut])
            r = browser.aggregate(cell, drilldown=["dim_nacionalidad"])

            result = {}
            if r is not None:
                result = {"profesores-nacionales": r.summary['sumatoria']}
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }