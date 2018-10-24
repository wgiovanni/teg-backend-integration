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
workspace.import_model("resources/cubesmodel/model_graduate_patents.json")
browser = workspace.browser("fact_egresado_patentes")


class GraduatePatents(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()
    def get(self):
        try:
           
            #cut = PointCut("dim_egresado", [ids])
            #cell = Cell(browser.cube, cuts = [cut])
            r = browser.aggregate(drilldown=["dim_egresado", "dim_patentes"])
            for row in r:
                print(row)
                print("\n")
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps([]), 200, { 'Access-Control-Allow-Origin': '*' }