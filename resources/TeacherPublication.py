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
workspace.import_model("resources/cubesmodel/model_teacher_publication.json")
browser = workspace.browser("fact_docente_publicacion")

class TeacherPublication(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()
    def get(self):
        try:
            idsTeachers = self.queryAll("SELECT id_docente FROM fact_docente_publicacion")
            listIds = []
            for ids in idsTeachers:
                listIds.append(ids['id_docente'])
            listIds = set(listIds)
            listIds = list(listIds)
            result = []
            for ids in listIds:
                #print(ids)
                teacher = self.queryOne("SELECT cedula, nombre, apellido FROM DIM_DOCENTE WHERE ID = %s", [ids])
                #print(teacher)
                cut = PointCut("dim_docente", [ids])
                cell = Cell(browser.cube, cuts = [cut])
                r = browser.aggregate(cell, drilldown=["dim_publicacion", "dim_docente"])
                publications = []
                for row in r:
                    print(row)
                    item = {"autor": row["dim_publicacion.autor"], 
                        "titulo": row["dim_publicacion.titulo"], 
                        "revista": row["dim_publicacion.revista"], 
                        "fecha_publicacion": row["dim_publicacion.fecha"].strftime('%Y-%m-%d'),
                        "citas": row["sumatoria_citacion"]}
                    publications.append(item)
                
                teacher["publicaciones"] = publications
                result.append(teacher)

                    
            #print(int(r.summary["sumatoria"]))
            #print(int(r.summary["sumatoria_citacion"]))
            
            #result = {"total-estudiantes": int(r.summary["sumatoria"])}
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }

class TeacherPublicationFaculty(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()
    def get(self):
        try:
            facultyList = self.queryAll("SELECT * FROM dim_facultad")
            result = []
            for faculty in facultyList:
                print(faculty)
                cut = PointCut("dim_facultad", [faculty['id']])
                cell = Cell(browser.cube, cuts = [cut])
                r = browser.aggregate(cell, drilldown=["dim_publicacion", "dim_facultad"])
                item = {"facultad": faculty['nombre'], "cantidad_publicaciones": r.summary['sumatoria']}
                result.append(item)
                
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }
