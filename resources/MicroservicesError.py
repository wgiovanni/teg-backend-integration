from flask_restful import abort, Resource, reqparse
import simplejson as json
from textwrap import dedent
from cubes import Workspace, Cell, PointCut, Cut
from flask import make_response
from pymysql import DatabaseError
from common.BD import BD
import datetime
import requests
from flask import request
from constants import LOG_ACTIVITY_MICROSERVICES, SCHEDULED_TASK_STUDENTS, SCHEDULED_TASK_GRADUATES, SCHEDULED_TASK_TEACHERS

class MicroservicesError(BD, Resource):
    representations = {'application/json': make_response}
    def get(self):
        try:
            # sistemParamaterStudentsScheduler = self.queryOne("SELECT definicion FROM PARAMETRO_SISTEMA WHERE codigo = %s", [SCHEDULED_TASK_STUDENTS])
            # sistemParamaterTeachersScheduler = self.queryOne("SELECT definicion FROM PARAMETRO_SISTEMA WHERE codigo = %s", [SCHEDULED_TASK_TEACHERS])
            # sistemParamaterGraduatesScheduler = self.queryOne("SELECT definicion FROM PARAMETRO_SISTEMA WHERE codigo = %s", [SCHEDULED_TASK_GRADUATES])
            activityMicroservices = self.queryAll("SELECT * FROM {} WHERE status = 0 ORDER BY date DESC".format(LOG_ACTIVITY_MICROSERVICES))
            for r in activityMicroservices:
                r['date'] = r['date'].strftime('%Y-%m-%d %H:%M:%S')
            result = activityMicroservices
            # result = {
            #     'dates': [
            #         { 'dateStudents': sistemParamaterStudentsScheduler['definicion']}, 
            #         {'dateTeachers': sistemParamaterTeachersScheduler['definicion']}, 
            #         {'dateGraduate': sistemParamaterGraduatesScheduler['definicion']}
            #     ], 
            #     'activity': activityMicroservices
            # }
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(result), 200, { 'Access-Control-Allow-Origin': '*' }

    def delete(self):
        try:
            print("Entro")
            #self.remove("DELETE FROM HISTORY_ACTION",[])
            self.remove("UPDATE {} SET status = %s".format(LOG_ACTIVITY_MICROSERVICES),[True])
            self.commit()
            print("Salio")
        except DatabaseError as e:
            self.rollback()
            abort(500, message="{0}: {1}".format(e.__class__.__name__, e.__str__()))
        except Exception as e:
            abort(404, message="Resource {} doesn't exists")

        return json.dumps({"message": "Eliminado todos los registros"}), 204, { 'Access-Control-Allow-Origin': '*' }