from flask_restful import abort, Resource, reqparse
import simplejson as json
from textwrap import dedent
from cubes import Workspace, Cell, PointCut, Cut
from flask import make_response
from pymysql import DatabaseError
from common.BD import BD

workspace = Workspace()
workspace.register_default_store("sql", url="mysql+mysqlconnector://root@localhost/prueba")
workspace.import_model("resources/cubesmodel/model_student_faculty.json")
browser = workspace.browser("fact_estudiante_facultad")

class Student(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()
    def get(self):
        try:
            params = "Activo"
            result = self.queryOne("SELECT * FROM DIM_STATUS WHERE CODIGO = %s", [params])
            cut = PointCut("dim_status", [result['id']])
            cell = Cell(browser.cube, cuts = [cut])
            r = browser.aggregate(cell, drilldown=['dim_status'])
            result = {"total-estudiantes": int(r.summary["sumatoria"])}
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }


class StudentInternacional(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()
    def get(self):
        try:
            params = "Extranjero"
            result = self.queryOne("SELECT * FROM DIM_NACIONALIDAD WHERE CODIGO = %s", [params])
            cut = PointCut("dim_nacionalidad", [result['id']])
            cell = Cell(browser.cube, cuts = [cut])
            r = browser.aggregate(cell, drilldown=['dim_nacionalidad'])
            result = {"estudiantes-internacionales": int(r.summary["sumatoria"])}
            r = browser.aggregate()
            result["total-estudiantes"] = r.summary["sumatoria"]

        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }

class StudentFaculty(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()
    def get(self):
        try:
            r = browser.aggregate(drilldown=['dim_facultad'])
            result = {"total-estudiantes": int(r.summary["sumatoria"])}
            items = []
            for row in r:
                item = {"nombre": row['dim_facultad.nombre'], "total": row['sumatoria']}
                items.append(item)

            facultades = self.queryAll("SELECT nombre FROM DIM_FACULTAD")
            flag = False
            for f in facultades:
                for r in items:
                    if r['nombre'] == f['nombre']:
                        flag = True
                if flag == False:
                    item = {"nombre": f['nombre'], "total": 0}
                    items.append(item)
                flag = False
            items = sorted(items, key=lambda k: k['nombre']) 
            result['facultad'] = items


        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }

class StudentMaleFaculty(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()
    def get(self):
        try:
            params = "Masculino"
            result = self.queryOne("SELECT * FROM DIM_SEXO WHERE CODIGO = %s", [params])
            if result is None:
                abort(404, message="Resource {} doesn't exists".format(params))
            cut = PointCut("dim_sexo", [result['id']])
            cell = Cell(browser.cube, cuts = [cut])
            r = browser.aggregate(cell, drilldown=["dim_sexo", "dim_facultad"])
            result = []
            for row in r:
                item = {"sexo": row['dim_sexo.codigo'], "facultad": row['dim_facultad.nombre'], "total": row['sumatoria']}
                result.append(item)
        except DatabaseError as e:
            self.rollback()
            abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }

class StudentFemaleFaculty(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()
    def get(self):
        try:
            params = "Femenino"
            result = self.queryOne("SELECT * FROM DIM_SEXO WHERE CODIGO = %s", [params])
            if result is None:
                abort(404, message="Resource {} doesn't exists".format(params))
            cut = PointCut("dim_sexo", [result['id']])
            cell = Cell(browser.cube, cuts = [cut])
            r = browser.aggregate(cell, drilldown=["dim_sexo", "dim_facultad"])
            result = []
            for row in r:
                item = {"sexo": row['dim_sexo.codigo'], "facultad": row['dim_facultad.nombre'], "total": row['sumatoria']}
                result.append(item)
        except DatabaseError as e:
            self.rollback()
            abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }

class StudentSexFaculty(BD, Resource):
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
                result = sorted(result, key=lambda k: k['facultad']) 
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }

class StudentInternacionalFaculty(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()
    def get(self):
        try:
            params = "Extranjero"
            result = self.queryOne("SELECT * FROM DIM_NACIONALIDAD WHERE CODIGO = %s", [params])
            if result is None:
                abort(404, message="Resource {} doesn't exists".format(params))
            cut = PointCut("dim_nacionalidad", [result['id']])
            cell = Cell(browser.cube, cuts = [cut])
            r = browser.aggregate(cell, drilldown=["dim_nacionalidad", "dim_facultad"])
            result = []
            for row in r:
                item = {"nacionalidad": row['dim_nacionalidad.codigo'], "facultad": row['dim_facultad.nombre'], "total": row['sumatoria']}
                result.append(item)
        except DatabaseError as e:
            self.rollback()
            abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }

class StudentNacionalFaculty(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()
    def get(self):
        try:
            params = "Venezolano"
            result = self.queryOne("SELECT * FROM DIM_NACIONALIDAD WHERE CODIGO = %s", [params])
            if result is None:
                abort(404, message="Resource {} doesn't exists".format(params))
            cut = PointCut("dim_nacionalidad", [result['id']])
            cell = Cell(browser.cube, cuts = [cut])
            r = browser.aggregate(cell, drilldown=["dim_nacionalidad", "dim_facultad"])
            result = []
            for row in r:
                item = {"sexo": row['dim_nacionalidad.codigo'], "facultad": row['dim_facultad.nombre'], "total": row['sumatoria']}
                result.append(item)
        except DatabaseError as e:
            self.rollback()
            abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }

class StudentNationalityFaculty(BD, Resource):
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
                result = sorted(result, key=lambda k: k['facultad']) 
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }

class StudentDisabilityFaculty(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()

    def get(self):
        try:
            params = "SI POSEO DISCAPACIDAD"
            result = self.queryOne("SELECT * FROM DIM_DISCAPACIDAD WHERE CODIGO = %s", [params])
            facultades = self.queryAll("SELECT nombre FROM DIM_FACULTAD")

            if result is None:
                abort(404, message="Resource {} doesn't exists".format(params))
            
            cut = PointCut("dim_discapacidad", [result['id']])
            cell = Cell(browser.cube, cuts = [cut])
            r = browser.aggregate(cell, drilldown=["dim_discapacidad", "dim_facultad"])
            result = []
            item = {}
            if r is not None:
                for row in r:
                    item = {"facultad": row['dim_facultad.nombre'], "total-estudiantes-discapacidad": row['sumatoria']}
                    result.append(item)
                flag = False
                for f in facultades:
                    for r in result:
                        if r['facultad'] == f['nombre']:
                            flag = True
                    if flag == False:
                        item = {"facultad": f['nombre'], "total-estudiantes-discapacidad": 0}
                        result.append(item)
                    flag = False
                result = sorted(result, key=lambda k: k['facultad']) 
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }

class StudentEthnicGroupFaculty(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()

    def get(self):
        try:
            params = "SI PERTENEZCO A UN PUEBLO INDÍGENA"
            result = self.queryOne("SELECT * FROM DIM_ETNIA WHERE CODIGO = %s", [params])
            facultades = self.queryAll("SELECT nombre FROM DIM_FACULTAD")
            
            if result is None:
                abort(404, message="Resource {} doesn't exists".format(params))
            
            cut = PointCut("dim_etnia", [result['id']])
            cell = Cell(browser.cube, cuts = [cut])
            r = browser.aggregate(cell, drilldown=["dim_etnia", "dim_facultad"])
            result = []
            item = {}
            if r is not None:
                for row in r:
                    item = {"facultad": row['dim_facultad.nombre'], "total-estudiantes-etnia": row['sumatoria']}
                    result.append(item)
                flag = False
                for f in facultades:
                    for r in result:
                        if r['facultad'] == f['nombre']:
                            flag = True
                    if flag == False:
                        item = {"facultad": f['nombre'], "total-estudiantes-etnia": 0}
                        result.append(item)
                    flag = False
                result = sorted(result, key=lambda k: k['facultad']) 
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }

class StudentUndergraduateSex(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()

    def get(self):
        try:
            params = "Pregrado"
            result = self.queryOne("SELECT * FROM DIM_TIPO_ESTUDIANTE WHERE CODIGO = %s", [params])            
            if result is None:
                abort(404, message="Resource {} doesn't exists".format(params))
            
            cut = PointCut("dim_tipo_estudiante", [result['id']])
            cell = Cell(browser.cube, cuts = [cut])
            r = browser.aggregate(cell, drilldown=["dim_tipo_estudiante", "dim_sexo"])
            result = {}
            for row in r:
                print(row)
                result[row['dim_sexo.codigo']] = row['sumatoria'] 
            r = browser.aggregate()
            result["total-estudiantes-pregrado"] = r.summary["sumatoria"]
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }

class StudentUndergraduateNacionality(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()

    def get(self):
        try:
            params = "Pregrado"
            result = self.queryOne("SELECT * FROM DIM_TIPO_ESTUDIANTE WHERE CODIGO = %s", [params])            
            if result is None:
                abort(404, message="Resource {} doesn't exists".format(params))
            
            cut = PointCut("dim_tipo_estudiante", [result['id']])
            cell = Cell(browser.cube, cuts = [cut])
            r = browser.aggregate(cell, drilldown=["dim_tipo_estudiante", "dim_nacionalidad"])
            result = {}
            for row in r:
                print(row)
                result[row['dim_nacionalidad.codigo']] = row['sumatoria'] 
            r = browser.aggregate()
            if result.get('Extrajero') is None:
                result['Extranjero'] = 0
            if result.get('Venezolano') is None:
                result['Venezolano'] = 0
            result["total-estudiantes-pregrado"] = r.summary["sumatoria"]
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }

class StudentProfessionFaculty(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()
    def get(self):
        try:
            r = browser.aggregate(drilldown=["dim_carrera", "dim_facultad"])
            result = []
            for row in r:
                item = {"carrera": row['dim_carrera.nombre'], "facultad": row['dim_facultad.nombre'], "total": row['sumatoria']}
                result.append(item)
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }


class StudentProfessionConstantsFaculty(BD, Resource):
    representations = {'application/json': make_response}
    def get(self, facultad_codigo):
        try:
            params = facultad_codigo
            result = self.queryOne("SELECT * FROM DIM_FACULTAD WHERE NOMBRE = %s", [params])
            if result is None:
                abort(404, message="Resource {} doesn't exists".format(params))
            cut = PointCut("dim_facultad", [result['id']])
            cell = Cell(browser.cube, cuts = [cut])
            r = browser.aggregate(cell, drilldown=["dim_facultad", "dim_carrera"])
            result = []
            for row in r:
                item = {"carrera": row['dim_carrera.nombre'], "total": row['sumatoria']}
                result.append(item)
            response = {
                "facultad": facultad_codigo,
                "carrera": result
            }
        except DatabaseError as e:
            self.rollback()
            abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(response), 200, { 'Access-Control-Allow-Origin': '*' }
        