from flask_restful import abort, Resource, reqparse
import simplejson as json
from textwrap import dedent
from cubes import Workspace, Cell, PointCut, Cut
from flask import make_response
from pymysql import DatabaseError
from common.BD import BD
from datetime import datetime
from constants import ROLE_USER_TEACHER

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
            result = self.queryOne("SELECT * FROM dim_nivel WHERE codigo = %s", [params])
            
            if result is None:
                abort(404, message="Resource {} doesn't exists".format(params))
            cut = PointCut("dim_nivel", [result['id']])
            cell = Cell(browser.cube, cuts = [cut])
            r = browser.aggregate(cell, drilldown=["dim_facultad"])

            facultades = self.queryAll("SELECT nombre FROM dim_facultad")

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
            result = sorted(result, key=lambda k: k['facultad']) 
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

            facultades = self.queryAll("SELECT nombre FROM dim_facultad")

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
            r = browser.aggregate(drilldown=["dim_docente", "dim_facultad", "dim_nacionalidad"])
            items = []
            for row in r:
                item = {
                    "cedula": row['dim_docente.cedula'],
                    "nombre": row['dim_docente.primer_nombre'],
                    "apellido": row['dim_docente.primer_apellido'],
                    "correo": row['dim_docente.correo'],
                    "nacionalidad": row['dim_nacionalidad.codigo'],
                    "facultad": row['dim_facultad.nombre']
                }
                items.append(item)
            result['total-profesores'] = r.summary['sumatoria']
            result['items'] = items
            retreived = []
            retreived = self.queryAll(dedent("""\
            SELECT u.first_name, u.email, u.phone, u.address 
            FROM role as r 
            INNER JOIN user_role as ur 
            ON (r.id = ur.id_role) 
            INNER JOIN user as u 
            ON (ur.id_user = u.id) 
            WHERE r.name = %s"""), [ROLE_USER_TEACHER])
            result['recuperado'] = retreived
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }


class TeacherSexFaculty(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()
    def get(self):
        try:
            facultades = self.queryAll("SELECT codigo FROM dim_facultad")
            r = browser.aggregate(drilldown=["dim_genero", "dim_facultad"])
            result = []
            item = {}

            for f in facultades:
                item = {"facultad": f['codigo']}
                r = browser.aggregate(drilldown=["dim_genero", "dim_facultad"])
                for row in r:
                    if f['codigo'] == row['dim_facultad.codigo'] and row['dim_genero.codigo'] == "Femenino":
                        item['femenino'] = row['sumatoria']
                        print(item)
                    if f['codigo'] == row['dim_facultad.codigo'] and row['dim_genero.codigo'] == "Masculino":
                        item["masculino"] = row['sumatoria']
                        print(item)
                if item.get('femenino') is None:
                    item['femenino'] = 0
                if item.get('masculino') is None:
                    item["masculino"] = 0
                result.append(item)
          
            result = sorted(result, key=lambda k: k['facultad'])
            r = browser.aggregate(drilldown=["dim_docente", "dim_facultad", "dim_genero"])
            items = []
            for row in r:
                item = {
                    "cedula": row['dim_docente.cedula'],
                    "nombre": row['dim_docente.primer_nombre'],
                    "apellido": row['dim_docente.primer_apellido'],
                    "correo": row['dim_docente.correo'],
                    "sexo": row['dim_genero.codigo'],
                    "facultad": row['dim_facultad.nombre']
                }
                items.append(item)
            retreived = []
            retreived = self.queryAll(dedent("""\
            SELECT u.first_name, u.email, u.phone, u.address 
            FROM role as r 
            INNER JOIN user_role as ur 
            ON (r.id = ur.id_role) 
            INNER JOIN user as u 
            ON (ur.id_user = u.id) 
            WHERE r.name = %s"""), [ROLE_USER_TEACHER])
            response = {
                "facultades": result,
                "items": items,
                "recuperado": retreived
            } 
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(response), 200, { 'Access-Control-Allow-Origin': '*' }

class TeacherNacionalityFaculty(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()

    def get(self):
        try:
            facultades = self.queryAll("SELECT codigo FROM dim_facultad")
            
            r = browser.aggregate(drilldown=["dim_nacionalidad", "dim_facultad"])
            result = []
            item = {}

            for f in facultades:
                item = {"facultad": f['codigo']}
                r = browser.aggregate(drilldown=["dim_nacionalidad", "dim_facultad"])
                for row in r:
                    if f['codigo'] == row['dim_facultad.codigo'] and row['dim_nacionalidad.codigo'] == "Extranjero":
                        item['extranjero'] = row['sumatoria']
                        print(item)
                    if f['codigo'] == row['dim_facultad.codigo'] and row['dim_nacionalidad.codigo'] == "Venezolano":
                        item["venezolano"] = row['sumatoria']
                        print(item)
                if item.get('extranjero') is None:
                    item['extranjero'] = 0
                if item.get('venezolano') is None:
                    item["venezolano"] = 0
                result.append(item)
            result = sorted(result, key=lambda k: k['facultad'])
            r = browser.aggregate(drilldown=["dim_docente", "dim_facultad", "dim_nacionalidad"])
            items = []
            for row in r:
                item = {
                    "cedula": row['dim_docente.cedula'],
                    "nombre": row['dim_docente.primer_nombre'],
                    "apellido": row['dim_docente.primer_apellido'],
                    "correo": row['dim_docente.correo'],
                    "nacionalidad": row['dim_nacionalidad.codigo'],
                    "facultad": row['dim_facultad.nombre']
                }
                items.append(item)

            retreived = []
            retreived = self.queryAll(dedent("""\
            SELECT u.first_name, u.email, u.phone, u.address 
            FROM role as r 
            INNER JOIN user_role as ur 
            ON (r.id = ur.id_role) 
            INNER JOIN user as u 
            ON (ur.id_user = u.id) 
            WHERE r.name = %s"""), [ROLE_USER_TEACHER])
            response = {
                "facultades": result,
                "items": items,
                "recuperado": retreived
            } 
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(response), 200, { 'Access-Control-Allow-Origin': '*' }

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
            r = browser.aggregate(drilldown=["dim_escalafon", "dim_docente", "dim_nacionalidad"])
            items = []
            for row in r:
                item = {
                    "cedula": row['dim_docente.cedula'],
                    "nombre": row['dim_docente.primer_nombre'],
                    "apellido": row['dim_docente.primer_apellido'],
                    "correo": row['dim_docente.correo'],
                    "nacionalidad": row['dim_nacionalidad.codigo'],
                    "escalafon": row['dim_escalafon.nombre']
                }
                items.append(item)
            
            result['items'] = items
            retreived = []
            retreived = self.queryAll(dedent("""\
            SELECT u.first_name, u.email, u.phone, u.address 
            FROM role as r 
            INNER JOIN user_role as ur 
            ON (r.id = ur.id_role) 
            INNER JOIN user as u 
            ON (ur.id_user = u.id) 
            WHERE r.name = %s"""), [ROLE_USER_TEACHER])
            result['recuperado'] = retreived
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