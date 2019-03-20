from flask_restful import abort, Resource, reqparse
import simplejson as json
from textwrap import dedent
from cubes import Workspace, Cell, PointCut, Cut
from flask import make_response
from pymysql import DatabaseError
from common.BD import BD
from datetime import datetime
from constants import ROLE_USER_TEACHER
from db_credentials import datawarehouse_db_config

workspace = Workspace()
workspace.register_default_store("sql", url="mysql+mysqlconnector://" + datawarehouse_db_config['user'] + ":" + datawarehouse_db_config['password'] + "@" + datawarehouse_db_config['host'] + "/" + datawarehouse_db_config['database'])
workspace.import_model("resources/cubesmodel/model_teacher_project.json")
browser = workspace.browser("fact_docente_proyecto")

class TeacherProject(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()
    def get(self):
        try:
            r1 = browser.aggregate(drilldown=["dim_docente"])
            teachers = []
            for row1 in r1:
                cut = PointCut("dim_docente", [row1['dim_docente.id']])
                cell = Cell(browser.cube, cuts = [cut])
                r = browser.aggregate(cell, drilldown=["dim_proyecto", "dim_docente"])
                listProject = []
                for row in r:
                    proyect = {
                        "nombre": row['dim_proyecto.titulo']
                    }
                    listProject.append(proyect)
                item = {
                    "cedula": row1['dim_docente.cedula'],
                    "nombre": row1['dim_docente.primer_nombre'],
                    "apellido": row1['dim_docente.primer_apellido'],
                    "premio": listProject
                }
                teachers.append(item)
                teachers = sorted(teachers, key=lambda k: k['cedula']) 
            result = {
                "items": teachers
            }
            # result = {"profesores-premios": r.summary["sumatoria"]}
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