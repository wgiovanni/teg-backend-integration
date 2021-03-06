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
workspace.import_model("resources/cubesmodel/model_teacher_title.json")
browser = workspace.browser("fact_docente_titulo")

class TeacherTitle(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()
    def get(self):
        try:
            browser = workspace.browser("fact_docente_titulo")

            params = "Doctorado"
            result = self.queryOne("SELECT * FROM dim_nivel WHERE codigo = %s", [params])
            if result is None:
                abort(404, message="Resource {} doesn't exists".format(params))
            cut = PointCut("dim_nivel", [result['id']])
            cell = Cell(browser.cube, cuts = [cut])
            r = browser.aggregate(cell, drilldown=["dim_nivel"])
            result = {"profesores-doctorado": r.summary["sumatoria"]}

            r = browser.aggregate(drilldown=["dim_nivel", "dim_docente"])
            items = []
            for row in r:
                item = {
                    "cedula": row['dim_docente.cedula'],
                    "nombre": row['dim_docente.primer_nombre'],
                    "apellido": row['dim_docente.primer_apellido'],
                    "correo": row['dim_docente.correo'],
                    "area_de_investigacion": row['dim_docente.area_de_investigacion'],
                    "nivel": row['dim_nivel.codigo']
                }
                items.append(item)

            workspace.import_model("resources/cubesmodel/model_teacher_faculty.json")
            browser1 = workspace.browser("fact_docente_facultad")
            r1 = browser1.aggregate(drilldown=["dim_docente"])
                        
            result['total-profesores'] = r1.summary["sumatoria"]
            result['items'] = items
            retreived =[]
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

class TeacherTitleFaculty(BD, Resource):
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
            r = browser.aggregate(cell, drilldown=["dim_nivel", "dim_docente"])
           
            result = []
            for row in r:
                workspace.import_model("resources/cubesmodel/model_teacher_faculty.json")
                browser1 = workspace.browser("fact_docente_facultad")
                cut = PointCut("dim_docente", [row['dim_docente.id']])
                cell = Cell(browser1.cube, cuts = [cut])
                r1 = browser1.aggregate(cell, drilldown=["dim_docente", "dim_facultad"])
                for row1 in r1:
                    item = {
                        "cedula": row['dim_docente.cedula'],
                        "primer_nombre": row['dim_docente.primer_nombre'],
                        "segundo_nombre": row['dim_docente.segundo_nombre'],
                        "primer_apellido": row['dim_docente.primer_apellido'],
                        "segundo_apellido": row['dim_docente.segundo_apellido'],
                        "correo": row["dim_docente.correo"],
                        "area_de_investigacion": row["dim_docente.area_de_investigacion"]
                    }
                    item['facultad'] = row1['dim_facultad.nombre']
                    result.append(item)

            facultades = self.queryAll("SELECT nombre FROM dim_facultad")
            count = 0
            response = []
            flag = False
            for f in facultades:
                for r in result:
                    if r['facultad'] == f['nombre']:
                        flag = True
                        count = count + 1
                if flag == False:
                    item = {"facultad": f['nombre'], "cantidad": 0}
                    response.append(item)
                else:
                    item = {"facultad": f['nombre'], "cantidad": count}
                    response.append(item)
                flag = False
                count = 0
            response = sorted(response, key=lambda k: k['facultad'])
            retreived =[]
            retreived = self.queryAll(dedent("""\
            SELECT u.first_name, u.email, u.phone, u.address 
            FROM role as r 
            INNER JOIN user_role as ur 
            ON (r.id = ur.id_role) 
            INNER JOIN user as u 
            ON (ur.id_user = u.id) 
            WHERE r.name = %s"""), [ROLE_USER_TEACHER])

            response = {
                "facultades": response,
                "items": result,
                "recuperado": retreived
            }
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(response), 200, { 'Access-Control-Allow-Origin': '*' }