from flask_restful import abort, Resource, reqparse
import simplejson as json
from textwrap import dedent
from cubes import Workspace, Cell, PointCut, Cut
from flask import make_response
from pymysql import DatabaseError
from common.BD import BD
import datetime
from flask import request

class Carga(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()
    def post(self):
        try:
            #parameter = request.get_json(force=True)
            #print(parameter)
            #parameterYear1 = parameter['desde']
            #parameterYear2 = parameter['hasta']
            #result = []
            #if parameterYear1 < parameterYear2:
            #    year = self.queryAll("SELECT * FROM `dim_ano` where ano >= %s and ano <= %s order by ano ASC", [parameterYear1, parameterYear2])
            #    for y in year:
            #        cut = PointCut("dim_ano", [y['id']])
            #        cell = Cell(browser.cube, cuts = [cut])
            #        r = browser.aggregate(cell, drilldown = ["dim_ano", "dim_carga"])
            #        item = {
            #            "Año": y['ano'],
            #            "total": int(r.summary["sumatoria"])
            #        }
            #        result.append(item)
            for i in range(1892, 2050):
                item = {
                    "codigo": i
                }
                self.insert("dim_ano", item)
                self.commit()
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps([]), 200, { 'Access-Control-Allow-Origin': '*' }