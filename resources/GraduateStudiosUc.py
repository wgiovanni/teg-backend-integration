from flask_restful import abort, Resource, reqparse
import simplejson as json
from textwrap import dedent
from cubes import Workspace, Cell, PointCut, Cut
from flask import make_response, request
from pymysql import DatabaseError
from common.BD import BD
from datetime import datetime
from db_credentials import datawarehouse_db_config

workspace = Workspace()
workspace.register_default_store("sql", url="mysql+mysqlconnector://" + datawarehouse_db_config['user'] + "@" + datawarehouse_db_config['host'] + "/" + datawarehouse_db_config['database'])
workspace.import_model("resources/cubesmodel/model_graduate_studiosuc.json")
browser = workspace.browser("fact_egresado_estudiosuc")


class GraduateFaculty(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()
    def get(self):
        try:
            items = []
            r = browser.aggregate(drilldown=["dim_facultad"])
            for row in r:
                item = {
                    "nombre": row['dim_facultad.nombre'],
                    "total": row['sumatoria']
                }
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
            result = {} 
            result['facultad'] = items

            r = browser.aggregate(drilldown=['dim_egresado', 'dim_facultad'])
            items = []
            for row in r:
                item = {
                    "cedula": row['dim_egresado.cedula'],
                    "nombre": row['dim_egresado.nombre'],
                    "apellido": row['dim_egresado.apellido'],
                    "email": row['dim_egresado.correo'],
                    "facultad": row['dim_facultad.nombre']
                }
                items.append(item)
            result['items'] = items

        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }


class GraduatePerYear(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()
    def post(self):
        try:
            parameter = request.get_json(force=True)
            parameterYear1 = parameter['desde']
            parameterYear2 = parameter['hasta']
            result = []
            items = []
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
            r = browser.aggregate(drilldown=['dim_egresado', 'dim_tiempo'])
            items = []
            for row in r:
                item = {
                    "cedula": row['dim_egresado.cedula'],
                    "nombre": row['dim_egresado.nombre'],
                    "apellido": row['dim_egresado.apellido'],
                    "email": row['dim_egresado.correo'],
                    "ano": row['dim_tiempo.codigo']
                }
                items.append(item)
            response = {
                "anos": result,
                "items": items
            } 
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(response), 200, { 'Access-Control-Allow-Origin': '*' }


class GraduateFacultyYear(BD, Resource):
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
                    print(row)
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
                    print(row)
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
            r = browser.aggregate(drilldown=['dim_egresado', 'dim_tiempo', 'dim_facultad'])
            items = []
            for row in r:
                item = {
                    "cedula": row['dim_egresado.cedula'],
                    "nombre": row['dim_egresado.nombre'],
                    "apellido": row['dim_egresado.apellido'],
                    "email": row['dim_egresado.correo'],
                    "ano": row['dim_tiempo.codigo'],
                    "facultad": row['dim_facultad.nombre']
                }
                items.append(item)
            response = {
                "anos": result,
                "items": items
            } 
            
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(response), 200, { 'Access-Control-Allow-Origin': '*' }

# class GraduateFacultyYear(BD, Resource):
#     representations = {'application/json': make_response}
#     parser = reqparse.RequestParser()
#     def post(self):
#         try:
#             parameter = request.get_json(force=True)
#             print(parameter)
#             parameterYear1 = parameter['desde']
#             parameterYear2 = parameter['hasta']
#             parameterFaculty = parameter['facultad'] 
#             result = []
#             SELECT e.*, f.nombre as facultad FROM `fact_egresado_estudiosuc` as fact INNER JOIN dim_egresado as e on(fact.id_egresado = e.id) INNER JOIN dim_facultad as f on(fact.id_facultad = f.id) WHERE e.confianza>= 20 and e.confianza<= 60
            
            
#         except Exception as e:
#             abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

#         return json.dumps(response), 200, { 'Access-Control-Allow-Origin': '*' }