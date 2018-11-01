# modulos python
from flask_restful import abort
import psycopg2
import mysql.connector
from datetime import datetime
from textwrap import dedent
import simplejson as json
import requests
from common.BD import BD
from db_credentials import datawarehouse_db_config
from sql_queries import systemParameter, nationalityQuery, sexQuery, statusQuery, disabilityQuery, ethnicGroupQuery, studentQuery, typeStudentQuery, teacherQuery, professionQuery, facultyQuery 
from sql_queries import publicationQuery, scaleQuery, studentRelationship, gradeQuery, teacherFacultyRelationship, teacherPublicationRelationship
from sql_queries import graduateQuery, studiosUcQuery, certificationQuery, coursesQuery, educationQuery, educationQuery, patentsQuery
from sql_queries import jobsQuery, volunteeringQuery, graduateJobsRelationship, graduatePatentsRelationship, graduateCertificationRelationship 
from sql_queries import graduateCoursesRelationship, graduateEducationRelationship, graduateVolunteeringRelationship, typeTeacherQuery
from constants import LOAD_INITIAL_UPDATE, ENDPOINT_LOAD_STUDENTS, ENDPOINT_LOAD_TEACHERS, ENDPOINT_LOAD_GRADUATES, DATE_UPDATE, CONTENT_TYPE
from constants import DIMENSION, FACT, ITEMS
from constants import STUDENT, PROFESSION, FACULTY, STUDENT_PROFESSION_FACULTY, TEACHER, SCALE, GRADE, PUBLICATION, TEACHER_PUBLICATION, TEACHER_FACULTY, GRADUATE, STUDIOS_UC
from constants import NACIONALITY_ATTRIBUTE, SEX_ATTRIBUTE, IDENTIFICATION_CARD, FIRST_NAME_ATRIBUTE, LAST_NAME_ATRIBUTE, BIRTH_DATE_ATTRIBUTE, PHONE_ONE_ATTRIBUTE, PHONE_TWO_ATTRIBUTE, EMAIL_ATTRIBUTE, STATE_PROVENANCE_ATTRIBUTE, WORK_AREA_ATTRIBUTE, CITE_ATTRIBUTE, USER_NAME_ATTRIBUTE
from constants import MALE, FEMALE, NATIONAL, INTERNACIONAL
# variables
from variables import datawarehouse_name

def etl_process2():
	print("ETL \n")
	target_cnx = mysql.connector.connect(**datawarehouse_db_config)
	target_cursor = target_cnx.cursor()
	target_cursor.execute("USE {}".format(datawarehouse_name))
	target_cursor.execute(systemParameter.get_query, [LOAD_INITIAL_UPDATE])
	row = target_cursor.fetchone()
	target_cursor.execute(systemParameter.get_query, [DATE_UPDATE])
	systemParameterDate = target_cursor.fetchone()
	dateUpdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	print(row)
	dimension = DIMENSION
	hechos = FACT
	table = ''
	if row is not None:
		if row[4] == "0":
			#actualizacion
			print("Actualizacion")
			print(systemParameterDate[4])
			dataList = requestUpdate(target_cnx, systemParameterDate[4])
			
			for data in dataList:
				print(data)
				keyList= data.keys()
				#keyList = sorted(keyList)
				for key in keyList:
					print("KEY:{}".format(key))
					if dimension in key:
						print("Dimension")
						#picar string
						table = key[len(dimension):]
					elif hechos in key:
						print("Hechos")
						#picar string
						table = key[len(hechos):]
					content = data[key]
					print("\n\n")
					print(table)
					print(content)
					distributionUpdate(target_cnx, table, content)
		else:
			print("Carga Inicial")
			# insercion de tablas estaticas
			insertTableStatic(target_cnx)
			dataList = requestCargaInitial(target_cnx)
			print(dataList)
			print("\n\n")
			for data in dataList:
				print(data)
				print("\n")
				# ordenamiento: ESTO ES RELEVANTE
				keyList= data.keys()
				keyList = sorted(keyList)
				#insercion
				for key in keyList:
					print("KEY:{}".format(key))
					if dimension in key:
						print("Dimension")
						#picar string
						table = key[len(dimension):]
					elif hechos in key:
						print("Hechos")
						#picar string
						table = key[len(hechos):]
					content = data[key]
					print("\n\n")
					print(table)
					print(content)
					distributionCargaInitial(target_cnx, table, content)

		
		target_cursor.execute(systemParameter.update_query, [dateUpdate, systemParameterDate[0]])
		target_cursor.execute(systemParameter.update_query, ["0", row[0]])
		target_cnx.commit()
		print("Se actualizo la fecha")
	else:
		print("Debe llenar un registro en la Tabla 'last_update'")
	
	target_cursor.close()

def requestCargaInitial(target_cnx):
	
	headers = CONTENT_TYPE
	pathList = []
	target_cursor = target_cnx.cursor()
	target_cursor.execute(systemParameter.get_query, [ENDPOINT_LOAD_STUDENTS])
	endPointStudent = target_cursor.fetchone()
	target_cursor.execute(systemParameter.get_query, [ENDPOINT_LOAD_TEACHERS])
	endPointTeacher = target_cursor.fetchone()
	target_cursor.execute(systemParameter.get_query, [ENDPOINT_LOAD_GRADUATES])
	endPointGraduated = target_cursor.fetchone()
	#pathList.append(endPointStudent[4])
	pathList.append(endPointTeacher[4])
	#print(pathList)
	#pathList.append(endPointGraduated[4])
	result = []
	for path in pathList:
		try:
			r = requests.get(path, headers=headers)
			if r.status_code == requests.codes.ok:
				result.append(json.loads(r.text))
		except Exception as e:
			abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))
		except r.raise_for_status() as e:
			abort(404, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))
		continue		

	return result
	

def requestUpdate(target_cnx, lastUpdate):
	headers = CONTENT_TYPE
	pathList = []
	target_cursor = target_cnx.cursor()
	target_cursor.execute(systemParameter.get_query, [ENDPOINT_LOAD_STUDENTS])
	endPointStudent = target_cursor.fetchone()
	target_cursor.execute(systemParameter.get_query, [ENDPOINT_LOAD_TEACHERS])
	endPointTeacher = target_cursor.fetchone()
	target_cursor.execute(systemParameter.get_query, [ENDPOINT_LOAD_GRADUATES])
	endPointGraduated = target_cursor.fetchone()
	#pathList.append(endPointStudent[4]+"/{}".format(lastUpdate))
	pathList.append(endPointTeacher[4]+"/{}".format(lastUpdate))
	#pathList.append(endPointGraduated[4]) 
	#print(pathList)
	result = []
	for path in pathList:
		try:
			r = requests.get(path, headers=headers)
			if r.status_code == requests.codes.ok:
				result.append(json.loads(r.text))
		except Exception as e:
			abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))		
		except r.raise_for_status() as e:
			abort(404, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))
		continue

	return result


def distributionCargaInitial(target_cnx, table: str, content: dict):
	target_cursor = target_cnx.cursor()

	if table == STUDENT:
		items = content[ITEMS]
		print(items)
		print("\n")
		for item in items:
			# aqui deberian ir las verificaciones de cada item
			print(item)
			nationalityCode = item[NACIONALITY_ATTRIBUTE]
			if nationalityCode == "V" or nationalityCode == "v":
				nationalityCode = NATIONAL
			elif nationalityCode == "E" or nationalityCode == "e":
				nationalityCode = INTERNACIONAL
			target_cursor.execute(nationalityQuery.get_query_code, [nationalityCode])
			idNationality = target_cursor.fetchone()
			print(idNationality)
			#if idNationality[0] is not None:
			print("nacionalidad: {}".format(idNationality))
			sexCode = item[SEX_ATTRIBUTE]
			if sexCode == "f" or sexCode == "F":
				sexCode = FEMALE
			elif sexCode == "m" or sexCode == "M":
				sexCode = MALE
			target_cursor.execute(sexQuery.get_query_code, [sexCode])
			idSex = target_cursor.fetchone()
			print("sexo: {}".format(idSex))

			statusCode = item['status']
			if statusCode == 1:
				statusCode = "Activo"
			elif statusCode == 2:
				statusCode = "Inactivo"
			target_cursor.execute(statusQuery.get_query_code, [statusCode])
			idStatus = target_cursor.fetchone()
			print("status: {}".format(idStatus))

			disabilityCode = item['discapacidad']
			if disabilityCode != "NO POSEO NINGUNA DISCAPACIDAD":
				disabilityCode = "SI POSEO DISCAPACIDAD"
			target_cursor.execute(disabilityQuery.get_query_code, [disabilityCode])
			idDisability = target_cursor.fetchone()
			print("discapacidad: {}".format(idDisability))

			ethnicGroupCode = item['etnia']
			if ethnicGroupCode == "NO PERTENEZCO A UN PUEBLO INDÍGENA" or ethnicGroupCode == "NO PERTENEZCO A UN PUEBLO INDIGENA":
				ethnicGroupCode = "NO PERTENEZCO A UN PUEBLO INDÍGENA"
			elif ethnicGroupCode == "SI PERTENEZCO A UN PUEBLO INDÍGENA" or ethnicGroupCode == "NO PERTENEZCO A UN PUEBLO INDIGENA":
				ethnicGroupCode = "SI PERTENEZCO A UN PUEBLO INDÍGENA"
			else:
				ethnicGroupCode = "SI PERTENEZCO A UN PUEBLO INDÍGENA"
			target_cursor.execute(ethnicGroupQuery.get_query_code, [ethnicGroupCode])
			idEthnicGroup = target_cursor.fetchone()
			print("etnia: {}".format(idEthnicGroup))

			typeStudentCode = item['tipo']
			if typeStudentCode == "1":
				typeStudentCode = "Pregrado"
			elif typeStudentCode == "2":
				typeStudentCode = "Postgrado"
			target_cursor.execute(typeStudentQuery.get_query_code, [typeStudentCode])
			idTypeStudent = target_cursor.fetchone()
			print("etnia: {}".format(idTypeStudent))


			# aqui iran todas las dimensiones que saldran de estudiantes
			student = [
				item[IDENTIFICATION_CARD],  
				item[FIRST_NAME_ATRIBUTE], 
				item[LAST_NAME_ATRIBUTE], 
				item[BIRTH_DATE_ATTRIBUTE],
				item[PHONE_ONE_ATTRIBUTE], 
				item[PHONE_TWO_ATTRIBUTE],
				item[EMAIL_ATTRIBUTE],
				item[STATE_PROVENANCE_ATTRIBUTE]
			]
			target_cursor.execute(studentQuery.load_query, student)
			target_cnx.commit()

			target_cursor.execute(studentQuery.get_query_code, [item[IDENTIFICATION_CARD]])
			idStudent = target_cursor.fetchone()
			print(idStudent)

			# insertar estudiante con sexo y nacionalidad...

			target_cursor.execute(dedent("""\
			INSERT INTO FACT_ESTUDIANTE_FACULTAD 
				(id_estudiante, id_sexo, id_nacionalidad, id_status, id_discapacidad, id_etnia, id_tipo)
			VALUES (%s, %s, %s, %s, %s, %s, %s)"""), [idStudent[0], idSex[0], idNationality[0], idStatus[0], idDisability[0], idEthnicGroup[0], idTypeStudent[0]])
			target_cnx.commit()
	elif table == PROFESSION:
		print("DEMAS TABLAS")
		items = content[ITEMS]
		for item in items:
			target_cursor.execute(professionQuery.get_query_code, [item[FIRST_NAME_ATRIBUTE]])
			profession = target_cursor.fetchone()
			if profession is None:
				insert(target_cursor, table, item)
				target_cnx.commit()
			else: 
				print("Ya existe {}".format(item[FIRST_NAME_ATRIBUTE]))
		print("Insercion finalizada")

	elif table == FACULTY:
		print("DEMAS TABLAS")
		items = content[ITEMS]
		for item in items:
			target_cursor.execute(facultyQuery.get_query_code, [item[FIRST_NAME_ATRIBUTE]])
			faculty = target_cursor.fetchone()
			if faculty is None:
				insert(target_cursor, table, item)
				target_cnx.commit()
			else: 
				print("Ya existe {}".format(item[FIRST_NAME_ATRIBUTE]))
		print("Insercion finalizada")
	elif table == STUDENT_PROFESSION_FACULTY:
		items = content[ITEMS]
		for item in items:
			professionCode = item[PROFESSION]
			target_cursor.execute(professionQuery.get_query_code, [professionCode])
			idProfession = target_cursor.fetchone()

			facultyCode = item[FACULTY]
			target_cursor.execute(facultyQuery.get_query_code, [facultyCode])
			idFaculty = target_cursor.fetchone()

			studentCode = item[STUDENT]
			target_cursor.execute(studentRelationship.get_query_code, [studentCode])
			idFact = target_cursor.fetchone()
			

			target_cursor.execute(dedent("""\
			UPDATE fact_estudiante_facultad
			SET id_facultad=%s, id_carrera=%s
			WHERE id=%s;"""), [idFaculty[0], idProfession[0], idFact[0]])
			#insert(target_cursor, table, item)
			target_cnx.commit()
		print("Insercion finalizada")
	elif table == TEACHER:
		print("DOCENTE:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
		items = content[ITEMS]
		print(items)
		print("\n")
		for item in items:
			nationalityCode = item[NACIONALITY_ATTRIBUTE]
			if nationalityCode == "V" or nationalityCode == "v":
				nationalityCode = NATIONAL
			elif nationalityCode == "E" or nationalityCode == "e":
				nationalityCode = INTERNACIONAL
			target_cursor.execute(nationalityQuery.get_query_code, [nationalityCode])
			idNationality = target_cursor.fetchone()
			print(idNationality)
			#if idNationality[0] is not None:
			print("nacionalidad: {}".format(idNationality))
			sexCode = item[SEX_ATTRIBUTE]
			if sexCode == "f" or sexCode == "F":
				sexCode = FEMALE
			elif sexCode == "m" or sexCode == "M":
				sexCode = MALE
			target_cursor.execute(sexQuery.get_query_code, [sexCode])
			idSex = target_cursor.fetchone()
			print("sexo: {}".format(idSex))

			# facultad
			facultyCode = item[FACULTY]
			target_cursor.execute(facultyQuery.get_query_code, [facultyCode])
			idFaculty = target_cursor.fetchone()

			# escalafon
			scaleCode = item[SCALE]
			target_cursor.execute(scaleQuery.get_query_code, [scaleCode])
			idScale = target_cursor.fetchone()
			print("escalafon: {}".format(idScale))

			typeTeacherCode = item['tipo']
			target_cursor.execute(typeTeacherQuery.get_query_code, [typeTeacherCode])
			idTypeTeacher = target_cursor.fetchone()

			#gradeCode = item[GRADE]
			#target_cursor.execute(gradeQuery.get_query_code, [gradeCode])
			#idGrade = target_cursor.fetchone()
			#print("grado: {}".format(idGrade))

			teacher = [
				item[IDENTIFICATION_CARD],  
				item['primernombre'],
				item['segundonombre'], 
				item['primerapellido'],
				item['segundoapellido'], 
				item[EMAIL_ATTRIBUTE],
				item[WORK_AREA_ATTRIBUTE]
			]
			target_cursor.execute(teacherQuery.load_query, teacher)
			target_cnx.commit()

			target_cursor.execute(teacherQuery.get_query_code, [item[IDENTIFICATION_CARD]])
			idTeacher = target_cursor.fetchone()
			print(idTeacher)

			# insertar estudiante con sexo y nacionalidad...

			target_cursor.execute(dedent("""\
			INSERT INTO FACT_DOCENTE_FACULTAD 
				(id_docente, id_sexo, id_nacionalidad, id_escalafon, id_tipo, id_facultad)
			VALUES (%s, %s, %s, %s, %s, %s)"""), [idTeacher[0], idSex[0], idNationality[0], idScale[0], idTypeTeacher[0], idFaculty[0]])
			target_cnx.commit()
		print("INSERCION DOCENTE FINALIZADA")

	elif table == SCALE:
		print("DEMAS TABLAS")
		items = content[ITEMS]
		for item in items:
			target_cursor.execute(scaleQuery.get_query_code, [item[FIRST_NAME_ATRIBUTE]])
			scale = target_cursor.fetchone()
			if scale is None:
				insert(target_cursor, table, item)
				target_cnx.commit()
			else: 
				print("Ya existe {}".format(item[FIRST_NAME_ATRIBUTE]))
		print("Insercion finalizada")
	elif table == TEACHER_PUBLICATION:
		items = content[ITEMS]
		for item in items:
			teacherCode = item['cedulaautor']
			numberCites = item['numerocitaciones']
			target_cursor.execute(dedent("""\
			SELECT d.id as idTeacher, f.id as idFaculty 
			FROM fact_docente_facultad AS fact 
			INNER JOIN dim_docente AS d 
			ON (fact.id_docente = d.id)
			INNER JOIN dim_facultad AS f 
			ON (fact.id_facultad = f.id) 
			WHERE d.cedula = %s"""), [teacherCode])
			ids = target_cursor.fetchone()

			item = {
				"codigo": item['codigo'],
				"titulo_publicacion": item['titulopublicacion'],
				"url_citacion": item['urlcitacion'],
				"url_publicacion": item['urlpublicacion'],
			}
			insert(target_cursor, "publicacion", item)
			target_cnx.commit()

			target_cursor.execute(dedent("""\
			SELECT id FROM dim_publicacion
			WHERE codigo = %s"""), [item['codigo']])
			idPublication = target_cursor.fetchone()

			if len(ids) == 2:
				if ids[0] is not None and ids[1] is not None or idPublication[0] is not None:
					target_cursor.execute(dedent("""\
					INSERT INTO fact_docente_publicacion 
						(id_docente, id_facultad, id_publicacion, cantidad_citas)
					VALUES (%s, %s, %s, %s)"""), [ids[0], ids[1], idPublication[0], numberCites])
					target_cnx.commit()
				else:
					print("Error")
			else: 
				print("No encontrado")

			print("Insercion finalizada")
	#elif table == TEACHER_PUBLICATION:
	#	items = content[ITEMS]
	#	for item in items:
	#		target_cursor.execute(teacherQuery.get_query_code, [item[TEACHER]])
	#		idTeacher = target_cursor.fetchone()

	#		target_cursor.execute(facultyQuery.get_query_code, [item[FACULTY]])
	#		idFaculty = target_cursor.fetchone()

	#		target_cursor.execute(publicationQuery.get_query_code, [item[PUBLICATION]])
	#		idPublication = target_cursor.fetchone()

	#		if idTeacher is not None and idFaculty is not None and idPublication is not None: 
	#			target_cursor.execute(dedent("""\
	#				INSERT INTO FACT_DOCENTE_PUBLICACION 
	#					(id_docente, id_publicacion, id_facultad, cantidad_citas)
	#				VALUES (%s, %s, %s, %s)"""), [idTeacher[0], idPublication[0], idFaculty[0], item[CITE_ATTRIBUTE]])
	#			target_cnx.commit()
	#			print("INSERTO DOCENTE, PUBLICACION Y FACULTAD")
	#elif table == TEACHER_FACULTY:
	#	items = content[ITEMS]
	#	for item in items:
	#		target_cursor.execute(teacherFacultyRelationship.get_query_code, [item[TEACHER]])
	#		idFact = target_cursor.fetchone()

	#		target_cursor.execute(facultyQuery.get_query_code, [item[FACULTY]])
	#		idFaculty = target_cursor.fetchone()

	#		if idFact is not None and idFaculty is not None: 
	#			target_cursor.execute(dedent("""\
	#				UPDATE fact_docente_facultad
	#				SET id_facultad=%s
	#				WHERE id=%s;"""), [idFaculty[0], idFact[0]])
	#			target_cnx.commit()
	#			print("INSERTO DOCENTE, PUBLICACION Y FACULTAD")
	elif table == "docente-proyecto":
		items = content[ITEMS]
		for item in items:
			teacherCode = item['cedulaautor']
			target_cursor.execute(dedent("""\
			SELECT id 
			FROM dim_docente
			WHERE cedula = %s"""), [teacherCode])
			idTeacher = target_cursor.fetchone()

			item = {
				"codigo": item['codigo'],
				"titulo": item['titulo']
			}
			insert(target_cursor, "proyecto", item)
			target_cnx.commit()

			target_cursor.execute(dedent("""\
			SELECT id FROM dim_proyecto
			WHERE codigo = %s"""), [item['codigo']])
			idProyect = target_cursor.fetchone()

			if idTeacher[0] is not None and idProyect[0] is not None:
				target_cursor.execute(dedent("""\
				INSERT INTO fact_docente_proyecto 
					(id_docente, id_proyecto)
				VALUES (%s, %s)"""), [idTeacher[0], idProyect[0]])
				target_cnx.commit()
			else:
				print("Error")

			print("Insercion finalizada")

	elif table == "docente-otro-estudio":
		items = content[ITEMS]
		for item in items:
			teacherCode = item['cedulaautor']
			target_cursor.execute(dedent("""\
			SELECT id 
			FROM dim_docente
			WHERE cedula = %s"""), [teacherCode])
			idTeacher = target_cursor.fetchone()

			item = {
				"codigo": item['codigo'],
				"nombre_titulo": item['nomtitulo']
			}
			insert(target_cursor, "otroestudio", item)
			target_cnx.commit()

			target_cursor.execute(dedent("""\
			SELECT id FROM dim_otroestudio
			WHERE codigo = %s"""), [item['codigo']])
			idOtherStudio = target_cursor.fetchone()

			if idTeacher[0] is not None and idOtherStudio[0] is not None:
				target_cursor.execute(dedent("""\
				INSERT INTO fact_docente_otroestudio 
					(id_docente, id_otroestudio)
				VALUES (%s, %s)"""), [idTeacher[0], idOtherStudio[0]])
				target_cnx.commit()
			else:
				print("Error")
			print("Insercion finalizada")

	elif table == "docente-titulo":
		items = content[ITEMS]
		for item in items:
			teacherCode = item['cedulaautor']
			levelCode = item['nivel']
			print("codigo nivel {}".format(levelCode))
			target_cursor.execute(dedent("""\
			SELECT id 
			FROM dim_docente
			WHERE cedula = %s"""), [teacherCode])
			idTeacher = target_cursor.fetchone()

			target_cursor.execute(dedent("""\
			SELECT id 
			FROM dim_nivel
			WHERE codigo = %s"""), [levelCode])
			idLevel = target_cursor.fetchone()

			item = {
				"codigo": item['codigo'],
				"nombre": item['nomtitulo']
			}
			insert(target_cursor, "titulo", item)
			target_cnx.commit()

			target_cursor.execute(dedent("""\
			SELECT id FROM dim_titulo
			WHERE codigo = %s"""), [item['codigo']])
			idTitle = target_cursor.fetchone()
			print("LEVEL {}".format(idLevel[0]))
			if idTeacher[0] is not None and idTitle[0] is not None and idLevel[0] is not None:
				target_cursor.execute(dedent("""\
				INSERT INTO fact_docente_titulo
					(id_docente, id_titulo, id_nivel)
				VALUES (%s, %s, %s)"""), [idTeacher[0], idTitle[0], idLevel[0]])
				target_cnx.commit()
			else:
				print("Error")
			print("Insercion finalizada")

	elif table == "docente-premio":
		items = content[ITEMS]
		for item in items:
			teacherCode = item['cedulaautor']
			target_cursor.execute(dedent("""\
			SELECT id 
			FROM dim_docente
			WHERE cedula = %s"""), [teacherCode])
			idTeacher = target_cursor.fetchone()

			item = {
				"codigo": item['codigo'],
				"nombre": item['nombre']
			}
			insert(target_cursor, "premio", item)
			target_cnx.commit()

			target_cursor.execute(dedent("""\
			SELECT id FROM dim_premio
			WHERE codigo = %s"""), [item['codigo']])
			idPrize = target_cursor.fetchone()

			if idTeacher[0] is not None and idPrize[0] is not None:
				target_cursor.execute(dedent("""\
				INSERT INTO fact_docente_premio 
					(id_docente, id_premio)
				VALUES (%s, %s)"""), [idTeacher[0], idPrize[0]])
				target_cnx.commit()
			else:
				print("Error")
			print("Insercion finalizada")

	elif table == GRADUATE:
		items = content[ITEMS]
		for item in items:
			graduateCode = item['nombreusuario']
			target_cursor.execute(graduateQuery.get_query_code, [graduateCode])
			idGraduate = target_cursor.fetchone()
			#print(idGraduate)
			if idGraduate is None:
				graduate = [
					item['nombreusuario'],  
					item['primernombre'], 
					item['segundonombre'], 
					item['primerapellido'],
					item['segundoapellido'], 
					item['descripcion'],
					item['intereses'],
					item['email'],
					item['telefono'],
					item['identificacion']
				]
				target_cursor.execute(graduateQuery.load_query, graduate)
				target_cnx.commit()
			else: 
				print("Ya existe el EGRESADO")
		print("INSERCION EGRESADOS")

	elif table == STUDIOS_UC:
		items = content[ITEMS]
		for item in items:
			print(item)

			target_cursor.execute(facultyQuery.get_query_code, [item[FACULTY]])
			idFaculty = target_cursor.fetchone()

			target_cursor.execute(professionQuery.get_query_code, [item[PROFESSION]])
			idProfession = target_cursor.fetchone()

			item = {
				"titulo": item['titulo'],
				"anho_grado": item['anhogrado'],
				"url_certificacion": item['urlcertificacion'],
				"codigo": item['codigo']
			}
			target_cursor.execute(studiosUcQuery.get_query_code, [item['codigo']])
			studiosUc = target_cursor.fetchone()
			if studiosUc is None:
				insert(target_cursor, table, item)
				target_cnx.commit()
			else: 
				print("Ya existe {}".format(item['codigo']))

			#target_cursor.execute(studiosUcQuery.get_query_code, [item['codigo']])
			#idStudiosUc = target_cursor.fetchone()
			#print(idStudiosUc)
			
		print("INSERCION ESTUDIOS UC")
	elif table == 'egresado-estudiosuc':
		items = content[ITEMS]
		for item in items:
			#print(item)
			target_cursor.execute(graduateQuery.get_query_code, [item['egresado']])
			idGraduate = target_cursor.fetchone()
			studiosUcList = item["estudiosuc"]
			if studiosUcList is not None:
				for i in studiosUcList:
					studiosUcCode = i['codigo']
					facultyCode = i['facultad']
					professionCode = i['carrera']

					target_cursor.execute(studiosUcQuery.get_query_code, [studiosUcCode])
					idStudiosUc = target_cursor.fetchone()

					target_cursor.execute(facultyQuery.get_query_code, [facultyCode])
					idFaculty = target_cursor.fetchone()

					target_cursor.execute(professionQuery.get_query_code, [professionCode])
					idProfession = target_cursor.fetchone()

					if idStudiosUc is not None and idFaculty is not None and idProfession is not None and idGraduate is not None:
						target_cursor.execute(dedent("""\
						INSERT INTO FACT_EGRESADO_ESTUDIOSUC 
							(id_egresado, id_estudiosuc, id_facultad, id_carrera)
						VALUES (%s, %s, %s, %s)"""), [idGraduate[0], idStudiosUc[0], idFaculty[0], idProfession[0]])
						target_cnx.commit()
					else: 
						print("Error")

	elif table == "certificacion":
		items = content[ITEMS]
		for item in items:
			item = {
				"codigo": item['codigo'],
				"nombre_certificacion": item['nombrecertificacion'],
				"descripcion": item['descripcion'],
				"url_certificacion": item['urlcertificacion']
			}
			target_cursor.execute(certificationQuery.get_query_code, [item['codigo']])
			certification = target_cursor.fetchone()
			if certification is None:
				insert(target_cursor, table, item)
				target_cnx.commit()
			else: 
				print("Ya existe {}".format(item['codigo']))
		
	elif table == "egresado-certificacion":
		items = content[ITEMS]
		for item in items:
			target_cursor.execute(graduateQuery.get_query_code, [item['egresado']])
			idGraduate = target_cursor.fetchone()
			certificationList = item["certificacion"]
			if certificationList is not None:
				for i in certificationList:
					certificationCode = i['codigo']

					target_cursor.execute(certificationQuery.get_query_code, [certificationCode])
					idCertification = target_cursor.fetchone()

					if idCertification is not None and idGraduate is not None:
						target_cursor.execute(dedent("""\
						INSERT INTO FACT_EGRESADO_CERTIFICACION
							(id_egresado, id_certificacion)
						VALUES (%s, %s)"""), [idGraduate[0], idCertification[0]])
						target_cnx.commit()
					else: 
						print("Error")

	elif table == "cursos":
		items = content[ITEMS]
		for item in items:
			target_cursor.execute(coursesQuery.get_query_code, [item['codigo']])
			courses = target_cursor.fetchone()
			if courses is None:
				insert(target_cursor, table, item)
				target_cnx.commit()
			else: 
				print("Ya existe {}".format(item['codigo']))
	elif table == "egresado-cursos":
		items = content[ITEMS]
		for item in items:
			target_cursor.execute(graduateQuery.get_query_code, [item['egresado']])
			idGraduate = target_cursor.fetchone()
			coursesList = item["cursos"]
			if coursesList is not None:
				for i in coursesList:
					coursesCode = i['codigo']

					target_cursor.execute(coursesQuery.get_query_code, [coursesCode])
					idCourses = target_cursor.fetchone()

					if idCourses is not None and idGraduate is not None:
						target_cursor.execute(dedent("""\
						INSERT INTO FACT_EGRESADO_CURSOS
							(id_egresado, id_cursos)
						VALUES (%s, %s)"""), [idGraduate[0], idCourses[0]])
						target_cnx.commit()
					else: 
						print("Error")

	elif table == "educacion":
		items = content[ITEMS]
		for item in items:
			item = {
				"codigo": item['codigo'],
				"instituto": item['instituto'],
				"campo_estudio": item['campoestudio'],
				"titulo_obtenido": item['tituloobtenido'],
				"url_certificacion": item['urlcertificacion']
			}
			target_cursor.execute(educationQuery.get_query_code, [item['codigo']])
			education = target_cursor.fetchone()
			if education is None:
				insert(target_cursor, table, item)
				target_cnx.commit()
			else: 
				print("Ya existe {}".format(item['codigo']))
	elif table == "egresado-educacion":
		items = content[ITEMS]
		for item in items:
			target_cursor.execute(graduateQuery.get_query_code, [item['egresado']])
			idGraduate = target_cursor.fetchone()
			educationList = item["educacion"]
			if educationList is not None:
				for i in educationList:
					educationCode = i['codigo']

					target_cursor.execute(educationQuery.get_query_code, [educationCode])
					idEducation = target_cursor.fetchone()

					if idEducation is not None and idGraduate is not None:
						target_cursor.execute(dedent("""\
						INSERT INTO FACT_EGRESADO_EDUCACION
							(id_egresado, id_educacion)
						VALUES (%s, %s)"""), [idGraduate[0], idEducation[0]])
						target_cnx.commit()
					else: 
						print("Error")

	elif table == "patentes":
		items = content[ITEMS]
		for item in items:
			item = {
				"codigo": item['codigo'],
				"titulo": item['titulo'],
				"descripcion": item['descripcion'],
				"numero": item['numero'],
				"inventores": item['inventores'],
				"fecha": item['fecha'],
				"url": item['url']
			}
			target_cursor.execute(patentsQuery.get_query_code, [item['codigo']])
			patents = target_cursor.fetchone()
			if patents is None:
				insert(target_cursor, table, item)
				target_cnx.commit()
			else: 
				print("Ya existe {}".format(item['codigo']))

	elif table == "trabajos":
		items = content[ITEMS]
		for item in items:
			item = {
				"codigo": item['codigo'],
				"nombre_empresa": item['nombreempresa'],
				"cargo": item['cargo'],
				"descripcion": item['descripcion']
			}
			target_cursor.execute(jobsQuery.get_query_code, [item['codigo']])
			jobs = target_cursor.fetchone()
			if jobs is None:
				insert(target_cursor, table, item)
				target_cnx.commit()
			else: 
				print("Ya existe {}".format(item['codigo']))
				
	elif table == "voluntariado":
		items = content[ITEMS]
		for item in items:
			item = {
				"codigo": item['codigo'],
				"organizacion": item['organizacion'],
				"descripcion": item['descripcion'],
				"causa": item['causa']
			}
			target_cursor.execute(volunteeringQuery.get_query_code, [item['codigo']])
			volunteering = target_cursor.fetchone()
			if volunteering is None:
				insert(target_cursor, table, item)
				target_cnx.commit()
			else: 
				print("Ya existe {}".format(item['codigo']))

	elif table == "egresado-voluntariado":
		items = content[ITEMS]
		for item in items:
			print(item)
			target_cursor.execute(graduateQuery.get_query_code, [item['egresado']])
			idGraduate = target_cursor.fetchone()
			volunteerinList = item["voluntariado"]

			if volunteerinList is not None:
				for i in volunteerinList:
					volunteerinCode = i['codigo']

					target_cursor.execute(volunteeringQuery.get_query_code, [volunteerinCode])
					idVolunteering = target_cursor.fetchone()

					if idVolunteering is not None and idGraduate is not None:
						target_cursor.execute(dedent("""\
						INSERT INTO FACT_EGRESADO_VOLUNTARIADO
							(id_egresado, id_voluntariado)
						VALUES (%s, %s)"""), [idGraduate[0], idVolunteering[0]])
						target_cnx.commit()
					else: 
						print("Error")

	elif table == "egresado-patentes":
		items = content[ITEMS]
		for item in items:
			print(item)
			target_cursor.execute(graduateQuery.get_query_code, [item['egresado']])
			idGraduate = target_cursor.fetchone()
			patentsList = item["patentes"]

			if patentsList is not None:
				for i in patentsList:
					patentsCode = i['codigo']

					target_cursor.execute(patentsQuery.get_query_code, [patentsCode])
					idpatents = target_cursor.fetchone()

					if idpatents is not None and idGraduate is not None:
						target_cursor.execute(dedent("""\
						INSERT INTO FACT_EGRESADO_PATENTES
							(id_egresado, id_patentes)
						VALUES (%s, %s)"""), [idGraduate[0], idpatents[0]])
						target_cnx.commit()
					else: 
						print("Error")

	elif table == "egresado-trabajos":
		items = content[ITEMS]
		for item in items:
			print(item)
			target_cursor.execute(graduateQuery.get_query_code, [item['egresado']])
			idGraduate = target_cursor.fetchone()
			jobsList = item["trabajos"]

			if jobsList is not None:
				for i in jobsList:
					jobsCode = i['codigo']

					target_cursor.execute(jobsQuery.get_query_code, [jobsCode])
					idjobs = target_cursor.fetchone()

					if idjobs is not None and idGraduate is not None:
						target_cursor.execute(dedent("""\
						INSERT INTO FACT_EGRESADO_TRABAJOS
							(id_egresado, id_trabajo)
						VALUES (%s, %s)"""), [idGraduate[0], idjobs[0]])
						target_cnx.commit()
					else: 
						print("Error")

	target_cursor.close()


def distributionUpdate(target_cnx, table: str, content: dict):
	target_cursor = target_cnx.cursor()

	if table == STUDENT:
		items = content[ITEMS]
		print(items)
		print("Cargando estudiantes...")
		for item in items:
			# aqui deberian ir las verificaciones de cada item
			nationalityCode = item[NACIONALITY_ATTRIBUTE]
			if nationalityCode == "V" or nationalityCode == "v":
				nationalityCode = NATIONAL
			elif nationalityCode == "E" or nationalityCode == "e":
				nationalityCode = INTERNACIONAL
			target_cursor.execute(nationalityQuery.get_query_code, [nationalityCode])
			idNationality = target_cursor.fetchone()
			print("nacionalidad: {}".format(idNationality))
			sexCode = item[SEX_ATTRIBUTE]
			if sexCode == "f" or sexCode == "F":
				sexCode = FEMALE
			elif sexCode == "m" or sexCode == "M":
				sexCode = MALE
			target_cursor.execute(sexQuery.get_query_code, [sexCode])
			idSex = target_cursor.fetchone()
			print("sexo: {}".format(idSex))
			# aqui iran todas las dimensiones que saldran de estudiantes

			statusCode = item['status']
			if statusCode == 1:
				statusCode = "Activo"
			elif statusCode == 2:
				statusCode = "Inactivo"
			target_cursor.execute(statusQuery.get_query_code, [statusCode])
			idStatus = target_cursor.fetchone()
			print("status: {}".format(idStatus))

			disabilityCode = item['discapacidad']
			if disabilityCode != "NO POSEO NINGUNA DISCAPACIDAD":
				disabilityCode = "SI POSEO DISCAPACIDAD"
			target_cursor.execute(disabilityQuery.get_query_code, [disabilityCode])
			idDisability = target_cursor.fetchone()
			print("discapacidad: {}".format(idDisability))

			ethnicGroupCode = item['etnia']
			if ethnicGroupCode == "NO PERTENEZCO A UN PUEBLO INDÍGENA" or ethnicGroupCode == "NO PERTENEZCO A UN PUEBLO INDIGENA":
				ethnicGroupCode = "NO PERTENEZCO A UN PUEBLO INDÍGENA"
			elif ethnicGroupCode == "SI PERTENEZCO A UN PUEBLO INDÍGENA" or ethnicGroupCode == "NO PERTENEZCO A UN PUEBLO INDIGENA":
				ethnicGroupCode = "SI PERTENEZCO A UN PUEBLO INDÍGENA"
			else:
				ethnicGroupCode = "SI PERTENEZCO A UN PUEBLO INDÍGENA"
			target_cursor.execute(ethnicGroupQuery.get_query_code, [ethnicGroupCode])
			idEthnicGroup = target_cursor.fetchone()
			print("etnia: {}".format(idEthnicGroup))

			typeStudentCode = item['tipo']
			if typeStudentCode == "1":
				typeStudentCode = "Pregrado"
			elif typeStudentCode == "2":
				typeStudentCode = "Postgrado"
			target_cursor.execute(typeStudentQuery.get_query_code, [typeStudentCode])
			idTypeStudent = target_cursor.fetchone()
			print("tipo: {}".format(idTypeStudent))

			student = [
				item[IDENTIFICATION_CARD],  
				item[FIRST_NAME_ATRIBUTE], 
				item[LAST_NAME_ATRIBUTE], 
				item[BIRTH_DATE_ATTRIBUTE],
				item[PHONE_ONE_ATTRIBUTE], 
				item[PHONE_TWO_ATTRIBUTE],
				item[EMAIL_ATTRIBUTE],
				item[STATE_PROVENANCE_ATTRIBUTE]
			]
			target_cursor.execute(studentQuery.get_query_code, [item[IDENTIFICATION_CARD]])
			idStudentExist = target_cursor.fetchone()
			if idStudentExist is not None:
				student.append(idStudentExist[0])
				print(student)
				target_cursor.execute(studentQuery.update_query, student)
				target_cnx.commit()
				target_cursor.execute(studentRelationship.get_query_code,[item[IDENTIFICATION_CARD]])
				idFact = target_cursor.fetchone()
				if idFact is not None:
					target_cursor.execute(dedent("""\
					UPDATE fact_estudiante_facultad
					SET id_estudiante=%s, id_sexo=%s, id_nacionalidad=%s, id_status=%s, id_discapacidad=%s, id_etnia=%s, id_tipo=%s
					WHERE id = %s"""), [idStudentExist[0], idSex[0], idNationality[0], idStatus[0], idDisability[0], idEthnicGroup[0], idTypeStudent[0], idFact[0]])
					target_cnx.commit()
				else: 
					print("No existe el registro")
				
			else:			
				target_cursor.execute(studentQuery.load_query, student)
				target_cnx.commit()
				target_cursor.execute(studentQuery.get_query_code, [item[IDENTIFICATION_CARD]])
				idStudent = target_cursor.fetchone()
				target_cursor.execute(dedent("""\
				INSERT INTO FACT_ESTUDIANTE_FACULTAD 
					(id_estudiante, id_sexo, id_nacionalidad, id_status, id_discapacidad, id_etnia, id_tipo)
				VALUES (%s, %s, %s, %s, %s, %s, %s)"""), [idStudent[0], idSex[0], idNationality[0], idStatus[0], idDisability[0], idEthnicGroup[0], idTypeStudent[0]])
			
	elif table == FACULTY:
		print("DEMAS TABLAS")
		print("Cargando facultad...")
		items = content[ITEMS]
		for item in items:
			target_cursor.execute(facultyQuery.get_query_code, [item[FIRST_NAME_ATRIBUTE]])
			row = target_cursor.fetchone()
			if row is not None:
				#params = list(item)
				#params.append(row[0])
				#target_cursor.execute(f"UPDATE DIM_{table} SET nombre = %s WHERE id = %s", params)
				update(target_cursor, table, item, {"id": row[0]})
			else: 
				insert(target_cursor, table, item)
			
			target_cnx.commit()
		print("Insercion finalizada")
	
	elif table == PROFESSION:
		print("DEMAS TABLAS")
		print("Cargando carrera...")
		items = content[ITEMS]
		for item in items:
			target_cursor.execute(professionQuery.get_query_code, [item[FIRST_NAME_ATRIBUTE]])
			row = target_cursor.fetchone()
			if row is not None:
				update(target_cursor, table, item, {"id": row[0]})
			else: 
				insert(target_cursor, table, item)
			
			target_cnx.commit()
		print("Insercion finalizada")

	elif table == STUDENT_PROFESSION_FACULTY:
		print("Cargando relacion...")
		items = content[ITEMS]
		for item in items:
			professionCode = item[PROFESSION]
			target_cursor.execute(professionQuery.get_query_code, [professionCode])
			idProfession = target_cursor.fetchone()

			facultyCode = item[FACULTY]
			target_cursor.execute(facultyQuery.get_query_code, [facultyCode])
			idFaculty = target_cursor.fetchone()
			
			studentCode = item[STUDENT]

			target_cursor.execute(studentQuery.get_query_code, [studentCode])
			idStudent = target_cursor.fetchone()

			target_cursor.execute(studentRelationship.get_query_code, [studentCode])
			idFact = target_cursor.fetchone()

			if idFact is not None:
				target_cursor.execute(dedent("""\
				UPDATE fact_estudiante_facultad
				SET id_estudiante=%s, id_facultad=%s, id_carrera=%s
				WHERE id=%s;"""), [idStudent[0], idFaculty[0], idProfession[0], idFact[0]])
				target_cnx.commit()
				print("Registro actualizado")
			else:
				print("Registro no existe")
		print("Insercion finalizada")

	elif table == TEACHER:
		print("DOCENTE:::::::::::::::::::ACTUALIZACION:::::::::::::::::::::::::::::::::")
		items = content[ITEMS]
		print(items)
		print("\n")
		for item in items:
			nationalityCode = item[NACIONALITY_ATTRIBUTE]
			if nationalityCode == "V" or nationalityCode == "v":
				nationalityCode = NATIONAL
			elif nationalityCode == "E" or nationalityCode == "e":
				nationalityCode = INTERNACIONAL
			target_cursor.execute(nationalityQuery.get_query_code, [nationalityCode])
			idNationality = target_cursor.fetchone()
			print(idNationality)
			#if idNationality[0] is not None:
			print("nacionalidad: {}".format(idNationality))
			sexCode = item[SEX_ATTRIBUTE]
			if sexCode == "f" or sexCode == "F":
				sexCode = FEMALE
			elif sexCode == "m" or sexCode == "M":
				sexCode = MALE
			target_cursor.execute(sexQuery.get_query_code, [sexCode])
			idSex = target_cursor.fetchone()
			print("sexo: {}".format(idSex))

			scaleCode = item[SCALE]
			target_cursor.execute(scaleQuery.get_query_code, [scaleCode])
			idScale = target_cursor.fetchone()
			print("escalafon: {}".format(idScale))

			typeTeacherCode = item['tipo']
			target_cursor.execute(typeTeacherQuery.get_query_code, [typeTeacherCode])
			idTypeTeacher = target_cursor.fetchone()

			facultyCode = item[FACULTY]
			target_cursor.execute(facultyQuery.get_query_code, [facultyCode])
			idFaculty = target_cursor.fetchone()


			teacher = [
				item[IDENTIFICATION_CARD],  
				item['primernombre'],
				item['segundonombre'], 
				item['primerapellido'],
				item['segundoapellido'], 
				item[EMAIL_ATTRIBUTE],
				item[WORK_AREA_ATTRIBUTE]
			]

			target_cursor.execute(teacherQuery.get_query_code, [item[IDENTIFICATION_CARD]])
			idTeacherExits = target_cursor.fetchone()
			if idTeacherExits is not None:
				teacher.append(idTeacherExits[0])
				target_cursor.execute(teacherQuery.update_query, teacher)
				target_cnx.commit()
				target_cursor.execute(teacherFacultyRelationship.get_query_code, [item[IDENTIFICATION_CARD]])
				idFact = target_cursor.fetchone()
				if idFact is not None:
					target_cursor.execute(dedent("""\
						UPDATE fact_docente_facultad
						SET id_docente=%s, id_sexo=%s, id_nacionalidad=%s, id_escalafon=%s, id_tipo=%s, id_facultad=%s
						WHERE id=%s"""), [idTeacherExits[0], idSex[0], idNationality[0], idScale[0], idTypeTeacher[0], idFaculty[0], idFact[0]])
					target_cnx.commit()
				else:
					print("No existe el registro")
			else:
				target_cursor.execute(teacherQuery.load_query, teacher)
				target_cnx.commit()

				target_cursor.execute(teacherQuery.get_query_code, [item[IDENTIFICATION_CARD]])
				idTeacher = target_cursor.fetchone()
				target_cursor.execute(dedent("""\
				INSERT INTO FACT_DOCENTE_FACULTAD 
					(id_docente, id_sexo, id_nacionalidad, id_escalafon, id_tipo, id_facultad)
				VALUES (%s, %s, %s, %s, %s, %s)"""), [idTeacher[0], idSex[0], idNationality[0], idScale[0], idTypeTeacher[0], idFaculty[0]])
				target_cnx.commit()

		print("ACTUALIZACION DOCENTE FINALIZADA")

	elif table == TEACHER_PUBLICATION:
		items = content[ITEMS]
		for item in items:
			teacherCode = item['cedulaautor']
			numberCites = item['numerocitaciones']
			target_cursor.execute(dedent("""\
			SELECT d.id as idTeacher, f.id as idFaculty 
			FROM fact_docente_facultad AS fact 
			INNER JOIN dim_docente AS d 
			ON (fact.id_docente = d.id)
			INNER JOIN dim_facultad AS f 
			ON (fact.id_facultad = f.id) 
			WHERE d.cedula = %s"""), [teacherCode])
			ids = target_cursor.fetchone()

			item = {
				"codigo": item['codigo'],
				"titulo_publicacion": item['titulopublicacion'],
				"url_citacion": item['urlcitacion'],
				"url_publicacion": item['urlpublicacion'],
			}

			target_cursor.execute(dedent("""\
			SELECT id FROM dim_publicacion
			WHERE codigo = %s"""), [item['codigo']])
			idPublication = target_cursor.fetchone()

			if idPublication is None:
				insert(target_cursor, "publicacion", item)
				target_cnx.commit()
				target_cursor.execute(dedent("""\
				SELECT id FROM dim_publicacion
				WHERE codigo = %s"""), [item['codigo']])
				idPublication = target_cursor.fetchone()

			target_cursor.execute(dedent("""\
			SELECT fact.id 
			FROM fact_docente_publicacion AS fact
			INNER JOIN dim_publicacion AS p
			ON (fact.id_publicacion = p.id)
			WHERE p.codigo = %s"""), [item['codigo']])
			idFact = target_cursor.fetchone()

			if ids[0] is not None and idPublication[0] is not None and ids[1] is not None:
				if idFact is not None:
					target_cursor.execute(dedent("""\
					UPDATE fact_docente_publicacion
					SET id_docente=%s, id_publicacion=%s, id_facultad=%s, cantidad_citas=%s
					WHERE id=%s"""), [ids[0], idPublication[0], ids[1], numberCites, idFact[0]])
					target_cnx.commit()
				else:
					target_cursor.execute(dedent("""\
					INSERT INTO fact_docente_publicacion
					(id_docente, id_facultad, id_publicacion, cantidad_citas)
					VALUES (%s, %s, %s, %s)"""), [ids[0], ids[1], idPublication[0], numberCites])
			else: 
				print("Error")
			print("Insercion finalizada")

	elif table == "docente-proyecto":
		items = content[ITEMS]
		for item in items:
			teacherCode = item['cedulaautor']
			target_cursor.execute(dedent("""\
			SELECT id 
			FROM dim_docente
			WHERE cedula = %s"""), [teacherCode])
			idTeacher = target_cursor.fetchone()

			item = {
				"codigo": item['codigo'],
				"titulo": item['titulo']
			}

			target_cursor.execute(dedent("""\
			SELECT id FROM dim_proyecto
			WHERE codigo = %s"""), [item['codigo']])
			idProyect = target_cursor.fetchone()

			if idProyect is None:
				insert(target_cursor, "proyecto", item)
				target_cnx.commit()
				target_cursor.execute(dedent("""\
				SELECT id FROM dim_proyecto
				WHERE codigo = %s"""), [item['codigo']])
				idProyect = target_cursor.fetchone()

			target_cursor.execute(dedent("""\
			SELECT fact.id 
			FROM fact_docente_proyecto AS fact
			INNER JOIN dim_proyecto AS p
			ON (fact.id_proyecto = p.id)
			WHERE p.codigo = %s"""), [item['codigo']])
			idFact = target_cursor.fetchone()

			if idTeacher[0] is not None and idProyect[0] is not None:
				if idFact is not None:
					target_cursor.execute(dedent("""\
					UPDATE fact_docente_proyecto
					SET id_docente=%s, id_proyecto=%s
					WHERE id=%s"""), [idTeacher[0], idProyect[0], idFact[0]])
					target_cnx.commit()
				else:
					target_cursor.execute(dedent("""\
					INSERT INTO fact_docente_proyecto
					(id_docente, id_proyecto)
					VALUES (%s, %s)"""), [idTeacher[0], idProyect[0]])
			else: 
				print("Error")
			print("Insercion finalizada")

	elif table == "docente-otro-estudio":
		items = content[ITEMS]
		for item in items:
			teacherCode = item['cedulaautor']
			target_cursor.execute(dedent("""\
			SELECT id 
			FROM dim_docente
			WHERE cedula = %s"""), [teacherCode])
			idTeacher = target_cursor.fetchone()

			item = {
				"codigo": item['codigo'],
				"nombre_titulo": item['nomtitulo']
			}
			
			target_cursor.execute(dedent("""\
			SELECT id FROM dim_otroestudio
			WHERE codigo = %s"""), [item['codigo']])
			idOtherStudio = target_cursor.fetchone()

			if idOtherStudio is None:
				insert(target_cursor, "otroestudio", item)
				target_cnx.commit()
				target_cursor.execute(dedent("""\
				SELECT id FROM dim_otroestudio
				WHERE codigo = %s"""), [item['codigo']])
				idOtherStudio = target_cursor.fetchone()

			target_cursor.execute(dedent("""\
			SELECT fact.id 
			FROM fact_docente_otroestudio AS fact
			INNER JOIN dim_otroestudio AS o
			ON (fact.id_otroestudio = o.id)
			WHERE o.codigo = %s"""), [item['codigo']])
			idFact = target_cursor.fetchone()

			if idTeacher[0] is not None and idOtherStudio[0] is not None:
				if idFact is not None:
					target_cursor.execute(dedent("""\
					UPDATE fact_docente_otroestudio
					SET id_docente=%s, id_otroestudio=%s
					WHERE id=%s"""), [idTeacher[0], idOtherStudio[0], idFact[0]])
					target_cnx.commit()
				else:
					target_cursor.execute(dedent("""\
					INSERT INTO fact_docente_otroestudio
					(id_docente, id_otroestudio)
					VALUES (%s, %s)"""), [idTeacher[0], idOtherStudio[0]])
			else:
				print("Error")
			print("Insercion finalizada")


	elif table == "docente-titulo":
		items = content[ITEMS]
		for item in items:
			teacherCode = item['cedulaautor']
			levelCode = item['nivel']
			print("codigo nivel {}".format(levelCode))
			target_cursor.execute(dedent("""\
			SELECT id 
			FROM dim_docente
			WHERE cedula = %s"""), [teacherCode])
			idTeacher = target_cursor.fetchone()

			target_cursor.execute(dedent("""\
			SELECT id 
			FROM dim_nivel
			WHERE codigo = %s"""), [levelCode])
			idLevel = target_cursor.fetchone()

			item = {
				"codigo": item['codigo'],
				"nombre": item['nomtitulo']
			}

			target_cursor.execute(dedent("""\
			SELECT id FROM dim_titulo
			WHERE codigo = %s"""), [item['codigo']])
			idTitle = target_cursor.fetchone()

			if idTitle is None:
				insert(target_cursor, "titulo", item)
				target_cnx.commit()
				target_cursor.execute(dedent("""\
				SELECT id FROM dim_titulo
				WHERE codigo = %s"""), [item['codigo']])
				idTitle = target_cursor.fetchone()

			print("LEVEL {}".format(idLevel[0]))

			target_cursor.execute(dedent("""\
			SELECT fact.id 
			FROM fact_docente_titulo AS fact
			INNER JOIN dim_titulo AS t
			ON (fact.id_titulo = t.id)
			WHERE t.codigo = %s"""), [item['codigo']])
			idFact = target_cursor.fetchone()

			if idTeacher[0] is not None and idLevel[0] is not None and idTitle[0] is not None:
				if idFact is not None:
					target_cursor.execute(dedent("""\
					UPDATE fact_docente_titulo
					SET id_docente=%s, id_titulo=%s, id_nivel=%s
					WHERE id=%s"""), [idTeacher[0], idTitle[0], idLevel[0], idFact[0]])
					target_cnx.commit()
				else:
					target_cursor.execute(dedent("""\
					INSERT INTO fact_docente_titulo
					(id_docente, id_titulo, id_nivel)
					VALUES (%s, %s, %s)"""), [idTeacher[0], idTitle[0], idLevel[0]])
			else:
				print("Error")
			print("Insercion finalizada")

	elif table == "docente-premio":
		items = content[ITEMS]
		for item in items:
			teacherCode = item['cedulaautor']
			target_cursor.execute(dedent("""\
			SELECT id 
			FROM dim_docente
			WHERE cedula = %s"""), [teacherCode])
			idTeacher = target_cursor.fetchone()

			item = {
				"codigo": item['codigo'],
				"nombre": item['nombre']
			}

			target_cursor.execute(dedent("""\
			SELECT id FROM dim_premio
			WHERE codigo = %s"""), [item['codigo']])
			idPrize = target_cursor.fetchone()

			if idPrize is None:
				insert(target_cursor, "premio", item)
				target_cnx.commit()
				target_cursor.execute(dedent("""\
				SELECT id FROM dim_premio
				WHERE codigo = %s"""), [item['codigo']])
				idPrize = target_cursor.fetchone()

			target_cursor.execute(dedent("""\
			SELECT fact.id 
			FROM fact_docente_premio AS fact
			INNER JOIN dim_premio AS p
			ON (fact.id_premio = p.id)
			WHERE p.codigo = %s"""), [item['codigo']])
			idFact = target_cursor.fetchone()

			if idTeacher[0] is not None and idPrize[0] is not None:
				if idFact is not None:
					target_cursor.execute(dedent("""\
					UPDATE fact_docente_premio
					SET id_docente=%s, id_premio=%s
					WHERE id=%s"""), [idTeacher[0], idPrize[0], idFact[0]])
					target_cnx.commit()
				else:
					target_cursor.execute(dedent("""\
					INSERT INTO fact_docente_premio
					(id_docente, id_premio)
					VALUES (%s, %s)"""), [idTeacher[0], idPrize[0]])
			else:
				print("Error")
			print("Insercion finalizada")

	elif table == SCALE:
		print("{}".format(table))
		items = content[ITEMS]
		for item in items:
			target_cursor.execute(scaleQuery.get_query_code, [item[FIRST_NAME_ATRIBUTE]])
			scale = target_cursor.fetchone()
			if scale is not None:
				update(target_cursor, table, item, {"id": scale[0]})
			else: 
				insert(target_cursor, table, item)
			target_cnx.commit()	
		print("Insercion finalizada")

	#elif table == PUBLICATION:
	#	print("{}".format(table))
	#	items = content[ITEMS]
	#	for item in items:
	#		target_cursor.execute(publicationQuery.get_query_code, [item[FIRST_NAME_ATRIBUTE]])
	#		publicacion = target_cursor.fetchone()
	#		if publication is not None:
	#			update(target_cursor, table, item, {"id": publication[0]})
	#		else: 
	#			insert(target_cursor, table, item)
	#		target_cnx.commit()
	#	print("Insercion finalizada")
	#elif table == TEACHER_PUBLICATION:
	#	print("{}".format(table))
	#	items = content[ITEMS]
	#	for item in items:
	#		publicationCode = item[PUBLICATION]
	#		target_cursor.execute(publicationQuery.get_query_code, [publicationCode])
	#		idPublication = target_cursor.fetchone()

	#		facultyCode = item[FACULTY]
	#		target_cursor.execute(facultyQuery.get_query_code, [facultyCode])
	#		idFaculty = target_cursor.fetchone()
			
	#		teacherCode = item[TEACHER]
	#		target_cursor.execute(teacherQuery.get_query_code, [teacherCode])
	#		idTeacher = target_cursor.fetchone()

			# pasar dos parametros
	#		target_cursor.execute(teacherPublicationRelationship.get_query_code, [teacherCode, publicationCode])
	#		idFact = target_cursor.fetchone()

	#		if idFact is not None:
	#			target_cursor.execute(dedent("""\
	#			UPDATE fact_docente_publicacion
	#			SET id_docente=%s, id_facultad=%s, id_publicacion=%s, cantidad_citas=%s
	#			WHERE id=%s;"""), [idTeacher[0], idFaculty[0], idPublication[0], item[CITE_ATTRIBUTE], idFact[0]])
	#			target_cnx.commit()
	#			print("Registro actualizado")
	#		else:
	#			print("Registro no existe")
	#	print("ACTUALIZACION finalizada")
	#elif table == TEACHER_FACULTY:
	#	items = content[ITEMS]
	#	for item in items:
	#		facultyCode = item[FACULTY]
	#		target_cursor.execute(facultyQuery.get_query_code, [facultyCode])
	#		idFaculty = target_cursor.fetchone()
			
	#		teacherCode = item[TEACHER]
	#		target_cursor.execute(teacherFacultyRelationship.get_query_code, [teacherCode])
	#		idFact = target_cursor.fetchone()

	#		if idFact is not None:
	#			target_cursor.execute(dedent("""\
	#			UPDATE fact_docente_facultad
	#			SET id_facultad=%s
	#			WHERE id=%s;"""), [idFaculty[0], idFact[0]])
	#			target_cnx.commit()
	#			print("Registro actualizado")
	#		else:
	#			print("Registro no existe")
	#	print("Actualizacion finalizada")

	elif table == GRADUATE:
		items = content[ITEMS]
		for item in items:
			graduateCode = item['nombreusuario']
			target_cursor.execute(graduateQuery.get_query_code, [graduateCode])
			idGraduate = target_cursor.fetchone()

			item = {
				"nombre_usuario": item['nombreusuario'],  
				"primer_nombre": item['primernombre'], 
				"segundo_nombre": item['segundonombre'], 
				"primer_apellido": item['primerapellido'],
				"segundo_apellido": item['segundoapellido'], 
				"descripcion": item['descripcion'],
				"intereses": item['intereses'],
				"correo": item['email'],
				"telefono": item['telefono'],
				"identificacion": item['identificacion']
			}
			if idGraduate is None:
				insert(target_cursor, table, item)
			else: 
				update(target_cursor, table, item, {"id": idGraduate[0]})
			target_cnx.commit()

	elif table == STUDIOS_UC:
		items = content[ITEMS]
		for item in items:
			print(item)

			item = {
				"titulo": item['titulo'],
				"anho_grado": item['anhogrado'],
				"url_certificacion": item['urlcertificacion'],
				"codigo": item['codigo']
			}
			target_cursor.execute(studiosUcQuery.get_query_code, [item['codigo']])
			studiosUc = target_cursor.fetchone()
			if studiosUc is None:
				insert(target_cursor, table, item)
			else: 
				update(target_cursor, table, item, {"id": studiosUc[0]})
			target_cnx.commit()

	elif table == "certificacion":
		items = content[ITEMS]
		for item in items:
			item = {
				"codigo": item['codigo'],
				"nombre_certificacion": item['nombrecertificacion'],
				"descripcion": item['descripcion'],
				"url_certificacion": item['urlcertificacion']
			}
			target_cursor.execute(certificationQuery.get_query_code, [item['codigo']])
			certification = target_cursor.fetchone()
			if certification is None:
				insert(target_cursor, table, item)
			else: 
				update(target_cursor, table, item, {"id": certification[0]})

			target_cnx.commit()

	elif table == "cursos":
		items = content[ITEMS]
		for item in items:
			target_cursor.execute(coursesQuery.get_query_code, [item['codigo']])
			courses = target_cursor.fetchone()
			if courses is None:
				insert(target_cursor, table, item)
			else: 
				update(target_cursor, table, item, {"id": courses[0]})

			target_cnx.commit()

	elif table == "educacion":
		items = content[ITEMS]
		for item in items:
			item = {
				"codigo": item['codigo'],
				"instituto": item['instituto'],
				"campo_estudio": item['campoestudio'],
				"titulo_obtenido": item['tituloobtenido'],
				"url_certificacion": item['urlcertificacion']
			}
			target_cursor.execute(educationQuery.get_query_code, [item['codigo']])
			education = target_cursor.fetchone()
			if education is None:
				insert(target_cursor, table, item)
			else: 
				update(target_cursor, table, item, {"id": education[0]})
			target_cnx.commit()

	elif table == "patentes":
		items = content[ITEMS]
		for item in items:
			item = {
				"codigo": item['codigo'],
				"titulo": item['titulo'],
				"descripcion": item['descripcion'],
				"numero": item['numero'],
				"inventores": item['inventores'],
				"fecha": item['fecha'],
				"url": item['url']
			}
			target_cursor.execute(patentsQuery.get_query_code, [item['codigo']])
			patents = target_cursor.fetchone()
			if patents is None:
				insert(target_cursor, table, item)
			else: 
				update(target_cursor, table, item, {"id": patents[0]})
			target_cnx.commit()

	elif table == "trabajos":
		items = content[ITEMS]
		for item in items:
			item = {
				"codigo": item['codigo'],
				"nombre_empresa": item['nombreempresa'],
				"cargo": item['cargo'],
				"descripcion": item['descripcion']
			}
			target_cursor.execute(jobsQuery.get_query_code, [item['codigo']])
			jobs = target_cursor.fetchone()
			if jobs is None:
				insert(target_cursor, table, item)
			else: 
				update(target_cursor, table, item, {"id": jobs[0]})
			target_cnx.commit()
				
	elif table == "voluntariado":
		items = content[ITEMS]
		for item in items:
			item = {
				"codigo": item['codigo'],
				"organizacion": item['organizacion'],
				"descripcion": item['descripcion'],
				"causa": item['causa']
			}
			target_cursor.execute(volunteeringQuery.get_query_code, [item['codigo']])
			volunteering = target_cursor.fetchone()
			if volunteering is None:
				insert(target_cursor, table, item)
			else: 
				update(target_cursor, table, item, {"id": volunteering[0]})
			target_cnx.commit()

	elif table == "egresado-patentes":
		items = content[ITEMS]
		for item in items:
			target_cursor.execute(graduateQuery.get_query_code, [item['egresado']])
			idGraduate = target_cursor.fetchone()
			patentsList = item["patentes"]
			if patentsList is not None:
				for i in patentsList:
					patentsCode = i['codigo']

					target_cursor.execute(patentsQuery.get_query_code, [patentsCode])
					idPatents = target_cursor.fetchone()

					target_cursor.execute(graduatePatentsRelationship.get_query_code, [patentsCode])
					idFact = target_cursor.fetchone()

					if idFact is not None:
						target_cursor.execute(dedent("""\
						UPDATE fact_egresado_patentes
						SET id_egresado=%s, id_patentes=%s
						WHERE id=%s;"""), [idGraduate[0], idPatents[0], idFact[0]])
						print("Registro actualizado")
					else:
						target_cursor.execute(dedent("""\
						INSERT INTO fact_egresado_patentes 
							(id_egresado, id_patentes)
						VALUES (%s, %s)"""), [idGraduate[0], idPatents[0]])
						print("Registro insertado")

					target_cnx.commit()
		print("Actualizacion finalizada")

	elif table == "egresado-trabajos":
		items = content[ITEMS]
		for item in items:
			target_cursor.execute(graduateQuery.get_query_code, [item['egresado']])
			idGraduate = target_cursor.fetchone()

			jobsList = item["trabajos"]

			if jobsList is not None:
				for i in jobsList:
					jobsCode = i['codigo']

					target_cursor.execute(jobsQuery.get_query_code, [jobsCode])
					idJobs = target_cursor.fetchone()

					target_cursor.execute(graduateJobsRelationship.get_query_code, [jobsCode])
					idFact = target_cursor.fetchone()

					if idFact is not None:
						target_cursor.execute(dedent("""\
						UPDATE fact_egresado_trabajos
						SET id_egresado=%s, id_trabajo=%s
						WHERE id=%s;"""), [idGraduate[0], idJobs[0], idFact[0]])
						print("Registro actualizado")
					else:
						target_cursor.execute(dedent("""\
						INSERT INTO fact_egresado_trabajos 
							(id_egresado, id_patentes)
						VALUES (%s, %s)"""), [idGraduate[0], idJobs[0]])
						print("Registro insertado")
						
					target_cnx.commit()
		print("Actualizacion finalizada")

	elif table == "egresado-certificacion":
		items = content[ITEMS]
		for item in items:
			target_cursor.execute(graduateQuery.get_query_code, [item['egresado']])
			idGraduate = target_cursor.fetchone()

			certificationList = item["certificacion"]

			if certificationList is not None:
				for i in certificationList:
					certificationCode = i['codigo']

					target_cursor.execute(certificationQuery.get_query_code, [certificationCode])
					idCertification = target_cursor.fetchone()

					target_cursor.execute(graduateCertificationRelationship.get_query_code, [certificationCode])
					idFact = target_cursor.fetchone()

					if idFact is not None:
						target_cursor.execute(dedent("""\
						UPDATE fact_egresado_certificacion
						SET id_egresado=%s, id_certificacion=%s
						WHERE id=%s;"""), [idGraduate[0], idCertification[0], idFact[0]])
						print("Registro actualizado")
					else:
						target_cursor.execute(dedent("""\
						INSERT INTO fact_egresado_certificacion 
							(id_egresado, id_certificacion)
						VALUES (%s, %s)"""), [idGraduate[0], idCertification[0]])
						print("Registro insertado")
						
					target_cnx.commit()
		print("Actualizacion finalizada")

	elif table == "egresado-cursos":
		items = content[ITEMS]
		for item in items:
			target_cursor.execute(graduateQuery.get_query_code, [item['egresado']])
			idGraduate = target_cursor.fetchone()

			coursesList = item["cursos"]

			if coursesList is not None:
				for i in coursesList:
					coursesCode = i['codigo']

					target_cursor.execute(coursesQuery.get_query_code, [coursesCode])
					idCourses = target_cursor.fetchone()

					target_cursor.execute(graduateCoursesRelationship.get_query_code, [coursesCode])
					idFact = target_cursor.fetchone()

					if idFact is not None:
						target_cursor.execute(dedent("""\
						UPDATE fact_egresado_cursos
						SET id_egresado=%s, id_cursos=%s
						WHERE id=%s;"""), [idGraduate[0], idCourses[0], idFact[0]])
						print("Registro actualizado")
					else:
						target_cursor.execute(dedent("""\
						INSERT INTO fact_egresado_cursos 
							(id_egresado, id_cursos)
						VALUES (%s, %s)"""), [idGraduate[0], idCourses[0]])
						print("Registro insertado")
						
					target_cnx.commit()
		print("Actualizacion finalizada")

	elif table == "egresado-educacion":
		items = content[ITEMS]
		for item in items:
			target_cursor.execute(graduateQuery.get_query_code, [item['egresado']])
			idGraduate = target_cursor.fetchone()

			educationList = item["educacion"]

			if educationList is not None:
				for i in educationList:
					educationCode = i['codigo']

					target_cursor.execute(educationQuery.get_query_code, [educationCode])
					idEducation = target_cursor.fetchone()

					target_cursor.execute(graduateEducationRelationship.get_query_code, [educationCode])
					idFact = target_cursor.fetchone()

					if idFact is not None:
						target_cursor.execute(dedent("""\
						UPDATE fact_egresado_educacion
						SET id_egresado=%s, id_educacion=%s
						WHERE id=%s;"""), [idGraduate[0], idEducation[0], idFact[0]])
						print("Registro actualizado")
					else:
						target_cursor.execute(dedent("""\
						INSERT INTO fact_egresado_cursos 
							(id_egresado, id_educacion)
						VALUES (%s, %s)"""), [idGraduate[0], idEducation[0]])
						print("Registro insertado")
						
					target_cnx.commit()
		print("Actualizacion finalizada")

	elif table == "egresado-voluntariado":
		items = content[ITEMS]
		for item in items:
			target_cursor.execute(graduateQuery.get_query_code, [item['egresado']])
			idGraduate = target_cursor.fetchone()

			volunteeringList = item["voluntariado"]

			if volunteeringList is not None:
				for i in volunteeringList:
					volunteeringCode = i['codigo']

					target_cursor.execute(volunteeringQuery.get_query_code, [volunteeringCode])
					idVolunteering = target_cursor.fetchone()

					target_cursor.execute(graduateVolunteeringRelationship.get_query_code, [volunteeringCode])
					idFact = target_cursor.fetchone()

					if idFact is not None:
						target_cursor.execute(dedent("""\
						UPDATE fact_egresado_voluntariado
						SET id_egresado=%s, id_voluntariado=%s
						WHERE id=%s;"""), [idGraduate[0], idVolunteering[0], idFact[0]])
						print("Registro actualizado")
					else:
						target_cursor.execute(dedent("""\
						INSERT INTO fact_egresado_voluntariado 
						(id_egresado, id_voluntariado)
						VALUES (%s, %s)"""), [idGraduate[0], idVolunteering[0]])
						print("Registro insertado")
						
					target_cnx.commit()
		print("Actualizacion finalizada")


	target_cursor.close()


def insertTableStatic(target_cnx):
	target_cursor = target_cnx.cursor()
	male = MALE
	female = FEMALE
	sexParams = [(male,), (female,)]
	target_cursor.execute(sexQuery.get_verify, [male, female])
	sexList = target_cursor.fetchall()
	print(sexList)
	if len(sexList) != 2:
		target_cursor.executemany(sexQuery.load_query, sexParams)
		target_cnx.commit()
	
	national = NATIONAL
	international = INTERNACIONAL
	nationalityParams = [(national,), (international,)]
	target_cursor.execute(nationalityQuery.get_verify, [national, international])
	nationalityList = target_cursor.fetchall()
	print(nationalityList)
	if len(nationalityList) != 2:
		target_cursor.executemany(nationalityQuery.load_query, nationalityParams)
		target_cnx.commit()

	active = "Activo"
	inactive = "Inactivo"
	statusParams = [(active,), (inactive,)]
	target_cursor.execute(statusQuery.get_verify, [active, inactive])
	statusList = target_cursor.fetchall()
	if len(statusList) != 2:
		target_cursor.executemany(statusQuery.load_query, statusParams)
		target_cnx.commit()
	
	etniaFalse = "NO PERTENEZCO A UN PUEBLO INDÍGENA"
	etniaTrue = "SI PERTENEZCO A UN PUEBLO INDÍGENA"
	etniaGroupParams = [(etniaTrue,), (etniaFalse,)]
	target_cursor.execute(ethnicGroupQuery.get_verify, [etniaTrue, etniaFalse])
	etniaGroupList = target_cursor.fetchall()
	if len(etniaGroupList) != 2:
		target_cursor.executemany(ethnicGroupQuery.load_query, etniaGroupParams)
		target_cnx.commit()


	disabilityFalse = "NO POSEO NINGUNA DISCAPACIDAD"
	disabilityTrue = "SI POSEO DISCAPACIDAD"
	disabilityParams = [(disabilityTrue,), (disabilityFalse,)]
	target_cursor.execute(disabilityQuery.get_verify, [disabilityTrue, disabilityFalse])
	disabilityList = target_cursor.fetchall()
	if len(disabilityList) != 2:
		target_cursor.executemany(disabilityQuery.load_query, disabilityParams)
		target_cnx.commit()

	undergraduate = "Pregrado"
	postgraduate = "Postgrado"
	typeStudentParams = [(undergraduate,), (postgraduate,)]
	target_cursor.execute(typeStudentQuery.get_verify,[undergraduate, postgraduate])
	typeList = target_cursor.fetchall()
	if len(typeList) != 2:
		target_cursor.execute(typeStudentQuery.load_query,typeStudentParams)
		target_cnx.commit()


def insert(cursor, table: str, datos: dict=None, columns=None, values: list=None):
	if datos is not None:
		columns = []
		values = []
		for col, val in datos.items():
			columns.append(col)
			values.append(val)

	if isinstance(columns, str):
		columns = "("+columns+")"
	elif isinstance(columns, list):
		columns = "("+", ".join(columns)+")"


	if isinstance(values[0], (list, tuple)):
		marks = "(%s" + (",%s" * (len(values[0]) - 1)) + ")"
		sql = f"insert into dim_{table} {columns} values {marks}", values
		cursor.execute(sql, values)
	else:
		marks = "(%s" + (",%s" * (len(values) - 1)) + ")"
		sql = f"insert into dim_{table} {columns} values {marks}"
		cursor.execute(sql, values)	

def update(cursor, table: str, datos: dict, where: dict):

	sql = f"update dim_{table} set "
	values = []
	for col, val in datos.items():
		if val is not None:
			sql += f"{col} = %s, "
			values.append(val)

	sql = sql.rstrip(', ')
	sql += " where "
	for col, val in where.items():
		sql += f"{col} = %s and "
		values.append(val)

	sql = sql.rstrip(' and ')
	cursor.execute(sql, values)