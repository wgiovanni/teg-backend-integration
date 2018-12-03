from flask_restful import abort, Resource, reqparse
import simplejson as json
from textwrap import dedent
from cubes import Workspace, Cell, PointCut, Cut
from flask import make_response
from pymysql import DatabaseError
from common.BD import BD
from datetime import datetime
from db_credentials import datawarehouse_db_config

workspace = Workspace()
workspace.register_default_store("sql", url="mysql+mysqlconnector://" + datawarehouse_db_config['user'] + "@" + datawarehouse_db_config['host'] + "/" + datawarehouse_db_config['database'])
workspace.import_model("resources/cubesmodel/model_graduate_jobs.json")
browser = workspace.browser("fact_egresado_trabajos")


class GraduateJobs(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()
    def get(self):
        try:
            r = browser.aggregate(drilldown=["dim_egresado"])
            graduates = []
            for row in r:
                cut = PointCut("dim_egresado", [row['dim_egresado.id']])
                cell = Cell(browser.cube, cuts = [cut])
                r1 = browser.aggregate(cell, drilldown=["dim_trabajos", "dim_egresado"])
                listJobs = []
                for row1 in r1:
                    job = {
                        "nombre": row1['dim_trabajos.nombre_empresa'],
                        "cargo": row1['dim_trabajos.cargo'],
                        "fecha": row1['dim_trabajos.fecha'].strftime('%Y-%m-%d')
                    }
                    listJobs.append(job)
                item = {
                    "cedula": row['dim_egresado.cedula'],
                    "nombre": row['dim_egresado.primer_nombre'],
                    "apellido": row['dim_egresado.primer_apellido'],
                    "trabajos": listJobs
                }
                graduates.append(item)
                graduates = sorted(graduates, key=lambda k: k['cedula']) 
            result = {
                "items": graduates,
                "recuperado": "SIGEUC"
            }
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }