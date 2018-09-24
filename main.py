# variables
from db_credentials import datawarehouse_db_config, postgresql_db_config
from sql_queries import postgresql_queries
from variables import *
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
import mysql.connector

# metodos
from etl import etl_process

def main():
	print('Empezando ETL')

	# establecer la conexion para la base de datos de destino
	target_cnx = mysql.connector.connect(**datawarehouse_db_config)

	# ciclo para las credenciales

	# postgresql
	for config in postgresql_db_config:
		try:
			print("Cargando db: " + config['database'])
			etl_process(postgresql_queries, target_cnx, config, 'postgresql')
		except Exception as error:
			print("etl para {} tiene error".format(config['database']))
			print('mensaje de error: {}'.format(error))

			continue

	target_cnx.close()

def sensor():
	print("Scheduler esta vivo!")

sched = BackgroundScheduler(deamon=True)
sched.add_job(sensor, 'interval', minutes=1)
sched.start()

app = Flask(__name__)

@app.route("/home")
def home():
	""" Funcion para fines de prueba. """
	return "Bienvenidos :) !"


if __name__ == "__main__":
	#main()
	app.run()