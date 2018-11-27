from flask_restful import abort, Resource, reqparse
import simplejson as json
from textwrap import dedent
from cubes import Workspace, Cell, PointCut, Cut
from flask import make_response, request
from pymysql import DatabaseError
from common.BD import BD
import datetime
from constants import ROLE_USER_STUDENT, CONTENT_TYPE

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
            r = browser.aggregate(cell, drilldown=['dim_status', 'dim_estudiante', 'dim_facultad'])
            result = {"total-estudiantes": int(r.summary["sumatoria"])}
            items = []
            for row in r:
                item = {
                    "cedula": row['dim_estudiante.cedula'],
                    "nombre": row['dim_estudiante.nombre'],
                    "apellido": row['dim_estudiante.apellido'],
                    "fecha_nacimiento": row['dim_estudiante.fecha_nacimiento'].strftime('%Y-%m-%d'),
                    "telefono1": row['dim_estudiante.telefono1'],
                    "telefono2": row['dim_estudiante.telefono2'],
                    "email": row['dim_estudiante.email'],
                    "estado_procedencia": row['dim_estudiante.edo_procedencia'],
                    "facultad": row['dim_facultad.nombre']
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
            WHERE r.name = %s"""), [ROLE_USER_STUDENT])
            result['recuperado'] = retreived		
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }

class StudentPerYear(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()
    def post(self):
        try:
            parameter = request.get_json(force=True)
            parameterYear1 = parameter['desde']
            parameterYear2 = parameter['hasta']
            result = []
            if type(parameterYear1) is int and type(parameterYear2) is int:
                year = self.queryAll("SELECT * FROM dim_tiempo where id >= %s and id <= %s order by codigo ASC", [parameterYear1, parameterYear2])
                for y in year:
                    cut = PointCut("dim_tiempo", [y['id']])
                    cell = Cell(browser.cube, cuts = [cut])
                    r = browser.aggregate(cell, drilldown = ["dim_tiempo"])
                    item = {
                        "ano": y['codigo'],
                        "total": int(r.summary["sumatoria"])
                    }
                    result.append(item)
                flag = False
                auxResult = []
                respaldo = {}
                for y in year:
                    for r in result:
                        if y['codigo'] == r['ano']:
                            flag = True
                            respaldo = r
                    if flag == False:
                        #print("entro")
                        item = {
                            "ano": y['codigo'],
                            "total": 0
                        }
                        result.append(item)
                        auxResult.append(item)
                    else:
                        auxResult.append(respaldo)
                    flag = False
                result = auxResult

            if type(parameterYear1) is str and type(parameterYear2) is str:
                year = self.queryAll("SELECT * FROM dim_tiempo ORDER BY codigo ASC")
                for y in year:
                    cut = PointCut("dim_tiempo", [y['id']])
                    cell = Cell(browser.cube, cuts = [cut])
                    r = browser.aggregate(cell, drilldown = ["dim_tiempo"])
                    item = {
                        "ano": y['codigo'],
                        "total": int(r.summary["sumatoria"])
                    }
                    result.append(item)
                flag = False
                auxResult = []
                respaldo = {}
                for y in year:
                    for r in result:
                        if y['codigo'] == r['ano']:
                            flag = True
                            respaldo = r
                    if flag == False:
                        print("entro")
                        item = {
                            "ano": y['codigo'],
                            "total": 0
                        }
                        result.append(item)
                        auxResult.append(item)
                    else:
                        auxResult.append(respaldo)
                    flag = False
                result = auxResult
            
            if type(parameterYear1) is str and type(parameterYear2) is int:
                year = self.queryAll("SELECT * FROM dim_tiempo WHERE id <= %s ORDER BY codigo ASC", [parameterYear2])
                for y in year:
                    cut = PointCut("dim_tiempo", [y['id']])
                    cell = Cell(browser.cube, cuts = [cut])
                    r = browser.aggregate(cell, drilldown = ["dim_tiempo"])
                    item = {
                        "ano": y['codigo'],
                        "total": int(r.summary["sumatoria"])
                    }
                    result.append(item)
                
                flag = False
                auxResult = []
                respaldo = {}
                for y in year:
                    for r in result:
                        if y['codigo'] == r['ano']:
                            flag = True
                            respaldo = r
                    if flag == False:
                        print("entro")
                        item = {
                            "ano": y['codigo'],
                            "total": 0
                        }
                        result.append(item)
                        auxResult.append(item)
                    else:
                        auxResult.append(respaldo)
                    flag = False
                result = auxResult

            if type(parameterYear1) is int and type(parameterYear2) is str:
                year = self.queryAll("SELECT * FROM dim_tiempo WHERE id >= %s ORDER BY codigo ASC", [parameterYear1])
                for y in year:
                    cut = PointCut("dim_tiempo", [y['id']])
                    cell = Cell(browser.cube, cuts = [cut])
                    r = browser.aggregate(cell, drilldown = ["dim_tiempo"])
                    item = {
                        "ano": y['codigo'],
                        "total": int(r.summary["sumatoria"])
                    }
                    result.append(item)

                flag = False
                auxResult = []
                respaldo = {}
                for y in year:
                    for r in result:
                        if y['codigo'] == r['ano']:
                            flag = True
                            respaldo = r

                    if flag == False:
                        item = {
                            "ano": y['codigo'],
                            "total": 0
                        }
                        result.append(item)
                        auxResult.append(item)
                    else:
                        auxResult.append(respaldo)
                    flag = False
                result = auxResult

            result = sorted(result, key=lambda k: k['ano']) 
            response = result

            retreived = []
            retreived = self.queryAll(dedent("""\
            SELECT u.first_name, u.email, u.phone, u.address 
            FROM role as r 
            INNER JOIN user_role as ur 
            ON (r.id = ur.id_role) 
            INNER JOIN user as u 
            ON (ur.id_user = u.id) 
            WHERE r.name = %s"""), [ROLE_USER_STUDENT])

            response = {
                "anos": result,
                "recuperado": retreived
            }
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(response), 200, { 'Access-Control-Allow-Origin': '*' }
        
class StudentYearFaculty(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()
    def post(self):
        try:
            parameter = request.get_json(force=True)
            print(parameter)
            parameterYear1 = parameter['desde']
            parameterYear2 = parameter['hasta']
            parameterFaculty = parameter['facultad'] 
            result = []
            if type(parameterYear1) is int and type(parameterYear2) is int:
                facultad = self.queryOne("SELECT * FROM dim_facultad WHERE id = %s", [parameterFaculty])
                year = self.queryAll("SELECT * FROM dim_tiempo where id >= %s and id <= %s order by codigo ASC", [parameterYear1, parameterYear2])
                cut = PointCut("dim_facultad", [facultad['id']])
                cell = Cell(browser.cube, cuts = [cut])
                r = browser.aggregate(cell, drilldown = ["dim_tiempo", "dim_facultad"])
                for row in r:
                    item = {
                        "ano": row['dim_tiempo.codigo'],
                        "total": int(row["sumatoria"])
                    }
                    result.append(item)
                flag = False
                auxResult = []
                respaldo = {}
                for y in year:
                    for r in result:
                        if y['codigo'] == r['ano']:
                            flag = True
                            respaldo = r
                    if flag == False:
                        item = {
                            "ano": y['codigo'],
                            "total": 0
                        }
                        result.append(item)
                        auxResult.append(item)
                    else:
                        auxResult.append(respaldo)
                    flag = False
                result = auxResult

            if type(parameterYear1) is str and type(parameterYear2) is str:
                facultad = self.queryOne("SELECT * FROM dim_facultad WHERE id = %s", [parameterFaculty])
                year = self.queryAll("SELECT * FROM dim_tiempo ORDER BY codigo ASC")
                cut = PointCut("dim_facultad", [facultad['id']])
                cell = Cell(browser.cube, cuts = [cut])
                r = browser.aggregate(cell, drilldown = ["dim_tiempo", "dim_facultad"])
                for row in r:
                    #print(row)
                    item = {
                        "ano": row['dim_tiempo.codigo'],
                        "total": int(row["sumatoria"])
                    }
                    result.append(item)
                flag = False
                auxResult = []
                respaldo = {}
                for y in year:
                    for r in result:
                        if y['codigo'] == r['ano']:
                            flag = True
                            respaldo = r

                    if flag == False:
                        item = {
                            "ano": y['codigo'],
                            "total": 0
                        }
                        result.append(item)
                        auxResult.append(item)
                    else:
                        auxResult.append(respaldo)

                    flag = False
                result = auxResult
            
            if type(parameterYear1) is str and type(parameterYear2) is int:
                facultad = self.queryOne("SELECT * FROM dim_facultad WHERE id = %s", [parameterFaculty])
                year = self.queryAll("SELECT * FROM dim_tiempo WHERE id <= %s ORDER BY codigo ASC", [parameterYear2])
                cut = PointCut("dim_facultad", [facultad['id']])
                cell = Cell(browser.cube, cuts = [cut])
                r = browser.aggregate(cell, drilldown = ["dim_tiempo", "dim_facultad"])
                for row in r:
                    item = {
                        "ano": row['dim_tiempo.codigo'],
                        "total": int(row["sumatoria"])
                    }
                    result.append(item)
                flag = False
                auxResult = []
                respaldo = {}
                for y in year:
                    for r in result:
                        if y['codigo'] == r['ano']:
                            flag = True
                            respaldo = r
                    if flag == False:
                        #print("entro")
                        item = {
                            "ano": y['codigo'],
                            "total": 0
                        }
                        result.append(item)
                        auxResult.append(item)
                    else:
                        auxResult.append(respaldo)
                    flag = False
                result = auxResult

            if type(parameterYear1) is int and type(parameterYear2) is str:
                facultad = self.queryOne("SELECT * FROM dim_facultad WHERE id = %s", [parameterFaculty])
                year = self.queryAll("SELECT * FROM dim_tiempo WHERE id >= %s ORDER BY codigo ASC", [parameterYear1])
                cut = PointCut("dim_facultad", [facultad['id']])
                cell = Cell(browser.cube, cuts = [cut])
                r = browser.aggregate(cell, drilldown = ["dim_tiempo", "dim_facultad"])
                for row in r:
                    item = {
                        "ano": row['dim_tiempo.codigo'],
                        "total": int(row["sumatoria"])
                    }
                    result.append(item)
                flag = False
                auxResult = []
                respaldo = {}
                for y in year:
                    for r in result:
                        if y['codigo'] == r['ano']:
                            flag = True
                            respaldo = r

                    if flag == False:
                        item = {
                            "ano": y['codigo'],
                            "total": 0
                        }
                        result.append(item)
                        auxResult.append(item)
                    else:
                        auxResult.append(respaldo)
                    flag = False
                result = auxResult

            result = sorted(result, key=lambda k: k['ano']) 
            retreived = []
            retreived = self.queryAll(dedent("""\
            SELECT u.first_name, u.email, u.phone, u.address 
            FROM role as r 
            INNER JOIN user_role as ur 
            ON (r.id = ur.id_role) 
            INNER JOIN user as u 
            ON (ur.id_user = u.id) 
            WHERE r.name = %s"""), [ROLE_USER_STUDENT])
    
            response = {
                "anos": result,
                "recuperado": retreived
            }
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(response), 200, { 'Access-Control-Allow-Origin': '*' }


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
            r = browser.aggregate(drilldown=["dim_estudiante", "dim_nacionalidad", "dim_facultad"])
            items = []
            for row in r:
                item = {
                    "cedula": row['dim_estudiante.cedula'],
                    "nacionalidad": row['dim_nacionalidad.codigo'],
                    "nombre": row['dim_estudiante.nombre'],
                    "apellido": row['dim_estudiante.apellido'],
                    "email": row['dim_estudiante.email'],
                    "facultad": row['dim_facultad.nombre']
                }
                items.append(item)
            result["total-estudiantes"] = r.summary["sumatoria"]
            result['items'] = items

            retreived = []
            retreived = self.queryAll(dedent("""\
            SELECT u.first_name, u.email, u.phone, u.address 
            FROM role as r 
            INNER JOIN user_role as ur 
            ON (r.id = ur.id_role) 
            INNER JOIN user as u 
            ON (ur.id_user = u.id) 
            WHERE r.name = %s"""), [ROLE_USER_STUDENT])
            result['recuperado'] = retreived

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
                print(row)
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
            r = browser.aggregate(drilldown=['dim_estudiante', 'dim_facultad'])
            items = []
            for row in r:
                item = {
                    "cedula": row['dim_estudiante.cedula'],
                    "nombre": row['dim_estudiante.nombre'],
                    "apellido": row['dim_estudiante.apellido'],
                    "fecha_nacimiento": row['dim_estudiante.fecha_nacimiento'].strftime('%Y-%m-%d'),
                    "telefono1": row['dim_estudiante.telefono1'],
                    "email": row['dim_estudiante.email'],
                    "estado_procedencia": row['dim_estudiante.edo_procedencia'],
                    "facultad": row['dim_facultad.nombre']
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
            WHERE r.name = %s"""), [ROLE_USER_STUDENT])
            result['recuperado'] = retreived

        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }

class StudentMaleFaculty(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()
    def get(self):
        try:
            params = "Masculino"
            result = self.queryOne("SELECT * FROM dim_genero WHERE CODIGO = %s", [params])
            if result is None:
                abort(404, message="Resource {} doesn't exists".format(params))
            cut = PointCut("dim_genero", [result['id']])
            cell = Cell(browser.cube, cuts = [cut])
            r = browser.aggregate(cell, drilldown=["dim_genero", "dim_facultad"])
            result = []
            for row in r:
                item = {"sexo": row['dim_genero.codigo'], "facultad": row['dim_facultad.nombre'], "total": row['sumatoria']}
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
            result = self.queryOne("SELECT * FROM dim_genero WHERE CODIGO = %s", [params])
            if result is None:
                abort(404, message="Resource {} doesn't exists".format(params))
            cut = PointCut("dim_genero", [result['id']])
            cell = Cell(browser.cube, cuts = [cut])
            r = browser.aggregate(cell, drilldown=["dim_genero", "dim_facultad"])
            result = []
            for row in r:
                item = {"sexo": row['dim_genero.codigo'], "facultad": row['dim_facultad.nombre'], "total": row['sumatoria']}
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
            facultades = self.queryAll("SELECT codigo FROM DIM_FACULTAD")
            
            r = browser.aggregate(drilldown=["dim_genero", "dim_facultad"])
            for row in r:
                print(row)
            result = []
            item = {}

            for f in facultades:
                item = {"facultad": f['codigo']}
                r = browser.aggregate(drilldown=["dim_genero", "dim_facultad"])
                for row in r:
                    if f['codigo'] == row['dim_facultad.codigo'] and row['dim_genero.codigo'] == "Femenino":
                        item['femenino'] = row['sumatoria']
                    if f['codigo'] == row['dim_facultad.codigo'] and row['dim_genero.codigo'] == "Masculino":
                        item["masculino"] = row['sumatoria']
                if item.get('femenino') is None:
                    item['femenino'] = 0
                if item.get('masculino') is None:
                    item["masculino"] = 0
                result.append(item)

            result = sorted(result, key=lambda k: k['facultad'])

            r2 = browser.aggregate(drilldown=["dim_genero", "dim_estudiante", "dim_facultad"])
            items = []
            for i in r2:
                item = {
                    "cedula": i['dim_estudiante.cedula'],
                    "nombre": i['dim_estudiante.nombre'],
                    "apellido": i['dim_estudiante.apellido'],
                    "fecha_nacimiento": i['dim_estudiante.fecha_nacimiento'].strftime('%Y-%m-%d'),
                    "telefono1": i['dim_estudiante.telefono1'],
                    "email": i['dim_estudiante.email'],
                    "estado_procedencia": i['dim_estudiante.edo_procedencia'],
                    "sexo": i['dim_genero.codigo'],
                    "facultad": i['dim_facultad.nombre']
                }
                items.append(item)
            response = {
                "facultades": result, 
                "items": items
            }
    
            retreived = []
            retreived = self.queryAll(dedent("""\
            SELECT u.first_name, u.email, u.phone, u.address 
            FROM role as r 
            INNER JOIN user_role as ur 
            ON (r.id = ur.id_role) 
            INNER JOIN user as u 
            ON (ur.id_user = u.id) 
            WHERE r.name = %s"""), [ROLE_USER_STUDENT])
        
            response['recuperado'] = retreived     
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(response), 200, { 'Access-Control-Allow-Origin': '*' }

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

            retreived = []
            retreived = self.queryAll(dedent("""\
            SELECT u.first_name, u.email, u.phone, u.address 
            FROM role as r 
            INNER JOIN user_role as ur 
            ON (r.id = ur.id_role) 
            INNER JOIN user as u 
            ON (ur.id_user = u.id) 
            WHERE r.name = %s"""), [ROLE_USER_STUDENT])
            result['recuperado'] = retreived  
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

            retreived = []
            retreived = self.queryAll(dedent("""\
            SELECT u.first_name, u.email, u.phone, u.address 
            FROM role as r 
            INNER JOIN user_role as ur 
            ON (r.id = ur.id_role) 
            INNER JOIN user as u 
            ON (ur.id_user = u.id) 
            WHERE r.name = %s"""), [ROLE_USER_STUDENT])
            result['recuperado'] = retreived  
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
            facultades = self.queryAll("SELECT codigo FROM DIM_FACULTAD")
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
            r = browser.aggregate(drilldown=["dim_estudiante","dim_nacionalidad", "dim_facultad"])
            items = []
            for i in r:
                item = {
                    "cedula": i['dim_estudiante.cedula'],
                    "nombre": i['dim_estudiante.nombre'],
                    "apellido": i['dim_estudiante.apellido'],
                    "email": i['dim_estudiante.email'],
                    "nacionalidad": i['dim_nacionalidad.codigo'],
                    "facultad": i['dim_facultad.nombre']
                }
                items.append(item)
            response = {
                "facultades": result,
                "items": items
            }
            retreived = []
            retreived = self.queryAll(dedent("""\
            SELECT u.first_name, u.email, u.phone, u.address 
            FROM role as r 
            INNER JOIN user_role as ur 
            ON (r.id = ur.id_role) 
            INNER JOIN user as u 
            ON (ur.id_user = u.id) 
            WHERE r.name = %s"""), [ROLE_USER_STUDENT])
            response['recuperado'] = retreived  
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(response), 200, { 'Access-Control-Allow-Origin': '*' }

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

                r = browser.aggregate(drilldown=["dim_estudiante","dim_discapacidad", "dim_facultad"])
                items = []
                for i in r:
                    item = {
                        "cedula": i['dim_estudiante.cedula'],
                        "nombre": i['dim_estudiante.nombre'],
                        "apellido": i['dim_estudiante.apellido'],
                        "email": i['dim_estudiante.email'],
                        "discapacidad": i['dim_discapacidad.codigo'],
                        "facultad": i['dim_facultad.nombre']
                    }
                    items.append(item)
                response = {
                    "facultades": result,
                    "items": items
                }
                retreived = []
                retreived = self.queryAll(dedent("""\
                SELECT u.first_name, u.email, u.phone, u.address 
                FROM role as r 
                INNER JOIN user_role as ur 
                ON (r.id = ur.id_role) 
                INNER JOIN user as u 
                ON (ur.id_user = u.id) 
                WHERE r.name = %s"""), [ROLE_USER_STUDENT])
                response['recuperado'] = retreived   
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(response), 200, { 'Access-Control-Allow-Origin': '*' }

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
                r = browser.aggregate(drilldown=["dim_estudiante","dim_etnia", "dim_facultad"])
                items = []
                for i in r:
                    item = {
                        "cedula": i['dim_estudiante.cedula'],
                        "nombre": i['dim_estudiante.nombre'],
                        "apellido": i['dim_estudiante.apellido'],
                        "email": i['dim_estudiante.email'],
                        "etnia": i['dim_etnia.codigo'],
                        "facultad": i['dim_facultad.nombre']
                    }
                    items.append(item)
                response = {
                    "facultades": result,
                    "items": items
                } 
                retreived = []
                retreived = self.queryAll(dedent("""\
                SELECT u.first_name, u.email, u.phone, u.address 
                FROM role as r 
                INNER JOIN user_role as ur 
                ON (r.id = ur.id_role) 
                INNER JOIN user as u 
                ON (ur.id_user = u.id) 
                WHERE r.name = %s"""), [ROLE_USER_STUDENT])
                response['recuperado'] = retreived   
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(response), 200, { 'Access-Control-Allow-Origin': '*' }

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
            r = browser.aggregate(cell, drilldown=["dim_tipo_estudiante", "dim_genero"])
            result = {}
            for row in r:
                print(row)
                result[row['dim_genero.codigo']] = row['sumatoria'] 

            r = browser.aggregate(drilldown=["dim_estudiante", "dim_tipo_estudiante", "dim_genero"])
            items = []
            for i in r:
                item = {
                    "cedula": i['dim_estudiante.cedula'],
                    "nombre": i['dim_estudiante.nombre'],
                    "apellido": i['dim_estudiante.apellido'],
                    "email": i['dim_estudiante.email'],
                    "tipo": i['dim_tipo_estudiante.codigo'],
                    "sexo": i['dim_genero.codigo']
                }
                items.append(item)
            result["total-estudiantes-pregrado"] = r.summary["sumatoria"]
            result['items'] = items
            retreived = []
            retreived = self.queryAll(dedent("""\
            SELECT u.first_name, u.email, u.phone, u.address 
            FROM role as r 
            INNER JOIN user_role as ur 
            ON (r.id = ur.id_role) 
            INNER JOIN user as u 
            ON (ur.id_user = u.id) 
            WHERE r.name = %s"""), [ROLE_USER_STUDENT])
            result['recuperado'] = retreived  
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
            result["total-estudiantes-pregrado"] = r.summary["sumatoria"]
            for row in r:
                print(row)
                result[row['dim_nacionalidad.codigo']] = row['sumatoria'] 
            r = browser.aggregate(drilldown=["dim_estudiante", "dim_tipo_estudiante", "dim_nacionalidad"])
            items = []
            for i in r:
                item = {
                    "cedula": i['dim_estudiante.cedula'],
                    "nacionalidad": i['dim_nacionalidad.codigo'],
                    "nombre": i['dim_estudiante.nombre'],
                    "apellido": i['dim_estudiante.apellido'],
                    "email": i['dim_estudiante.email'],
                    "tipo": i['dim_tipo_estudiante.codigo']
                }
                items.append(item)
                
            if result.get('Extranjero') is None:
                result['Extranjero'] = 0
            if result.get('Venezolano') is None:
                result['Venezolano'] = 0
             
            result['items'] = items
            retreived = []
            retreived = self.queryAll(dedent("""\
            SELECT u.first_name, u.email, u.phone, u.address 
            FROM role as r 
            INNER JOIN user_role as ur 
            ON (r.id = ur.id_role) 
            INNER JOIN user as u 
            ON (ur.id_user = u.id) 
            WHERE r.name = %s"""), [ROLE_USER_STUDENT])
            result['recuperado'] = retreived  
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
            result = self.queryOne("SELECT * FROM DIM_FACULTAD WHERE CODIGO = %s", [params])
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
        