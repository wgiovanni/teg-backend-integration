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


class Teacher(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()
    def get(self):
        try:
            r = browser.aggregate()
            result = {"total-empleado": r.summary["sumatoria"]}
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }


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
            r = browser.aggregate()
            result['total-profesores'] = r.summary['sumatoria']
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }


class TeacherSexFaculty(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()
    def get(self):
        try:
            params = "Femenino"
            result = self.queryOne("SELECT * FROM DIM_SEXO WHERE CODIGO = %s", [params])
            params1 = "Masculino"
            result1 = self.queryOne("SELECT * FROM DIM_SEXO WHERE CODIGO = %s", [params1])
            facultades = self.queryAll("SELECT nombre FROM DIM_FACULTAD")
            if result is None:
                abort(404, message="Resource {} doesn't exists".format(params))
            if result1 is None:
                abort(404, message="Resource {} doesn't exists".format(params1))
            
            cut = PointCut("dim_sexo", [result['id']])
            cell = Cell(browser.cube, cuts = [cut])
            r = browser.aggregate(cell, drilldown=["dim_sexo", "dim_facultad"])
            cut = PointCut("dim_sexo", [result1['id']])
            cell = Cell(browser.cube, cuts = [cut])
            r1 = browser.aggregate(cell, drilldown=["dim_sexo", "dim_facultad"])
            result = []
            item = {}
            if r is not None and r1 is not None:
                for row in r:
                    item = {"facultad": row['dim_facultad.nombre']}
                    for row1 in r1:
                        if row['dim_facultad.nombre'] == row1['dim_facultad.nombre']:
                            item["masculino"] = row1['sumatoria']
                    item["femenino"] = row['sumatoria']
                    if len(item) == 2:
                        item["masculino"] = 0
                    result.append(item)
                flag = False
                for f in facultades:
                    for r in result:
                        if r['facultad'] == f['nombre']:
                            flag = True
                    if flag == False:
                        item = {"facultad": f['nombre'], "masculino": 0, "femenino": 0}
                        result.append(item)
                    flag = False
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }

class TeacherNacionalityFaculty(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()

    def get(self):
        try:
            params = "Venezolano"
            result = self.queryOne("SELECT * FROM DIM_NACIONALIDAD WHERE CODIGO = %s", [params])
            params1 = "Extranjero"
            result1 = self.queryOne("SELECT * FROM DIM_NACIONALIDAD WHERE CODIGO = %s", [params1])
            facultades = self.queryAll("SELECT nombre FROM DIM_FACULTAD")
            if result is None:
                abort(404, message="Resource {} doesn't exists".format(params))
            if result1 is None:
                abort(404, message="Resource {} doesn't exists".format(params1))
            
            cut = PointCut("dim_nacionalidad", [result['id']])
            cell = Cell(browser.cube, cuts = [cut])
            r = browser.aggregate(cell, drilldown=["dim_nacionalidad", "dim_facultad"])
            cut = PointCut("dim_nacionalidad", [result1['id']])
            cell = Cell(browser.cube, cuts = [cut])
            r1 = browser.aggregate(cell, drilldown=["dim_nacionalidad", "dim_facultad"])
            result = []
            item = {}
            if r is not None and r1 is not None:
                for row in r:
                    item = {"facultad": row['dim_facultad.nombre']}
                    for row1 in r1:
                        if row['dim_facultad.nombre'] == row1['dim_facultad.nombre']:
                            item["extranjero"] = row1['sumatoria']
                    item["venezolano"] = row['sumatoria']
                    if len(item) == 2:
                        item["extranjero"] = 0
                    result.append(item)
                flag = False
                for f in facultades:
                    for r in result:
                        if r['facultad'] == f['nombre']:
                            flag = True
                    if flag == False:
                        item = {"facultad": f['nombre'], "venezolano": 0, "extranjero": 0}
                        result.append(item)
                    flag = False
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }

class TeacherScale(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()

    def get(self):
        try:
            scale = self.queryAll("SELECT nombre FROM dim_escalafon")
            r = browser.aggregate()
            result = {}
            if r is not None:
                result = {"total-profesores": r.summary['sumatoria']}
            r = browser.aggregate(drilldown=["dim_escalafon"])
            items = []
            for row in r:
                item = {"nombre": row['dim_escalafon.nombre'], "total": row['sumatoria']}
                items.append(item)

            flag = False
            for s in scale:
                for i in items:
                    if i['nombre'] == s['nombre']:
                        flag = True
                if flag == False:
                    item = {"nombre": s['nombre'], "total": 0}
                    items.append(item)
                flag = False

            result['escalafon'] = items
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