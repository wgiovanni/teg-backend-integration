from textwrap import dedent

class SqlQuery:
	def __init__(self, extract_initial_query, extract_update_query, load_query, update_query, get_query, type_table):
		self.extract_initial_query = extract_initial_query
		self.extract_update_query = extract_update_query
		self.load_query = load_query
		self.update_query = update_query
		self.get_query = get_query
		self.type_table = type_table

# exportando consultas para tablas de hechos
class SqlQueryFact:
	def __init__(self, extract_initial_query, load_query, get_query, verificate_query, type_table, tables):
		self.extract_initial_query = extract_initial_query
		self.load_query = load_query
		self.get_query = get_query
		self.verificate_query = verificate_query
		self.type_table = type_table
		self.tables = tables

class SqlSystemParameter:
	def __init__(self, get_query, update_query):
		self.get_query = get_query
		self.update_query = update_query

class SqlTableStatic:
	def __init__(self, get_query_code, load_query, get_verify):
		self.get_query_code = get_query_code
		self.load_query = load_query
		self.get_verify = get_verify

class SqlFact:
	def __init__(self, get_query_code, load_query, update_query):
		self.get_query_code = get_query_code
		self.load_query = load_query
		self.update_query = update_query

class SqlTableSameParse:
	def __init__(self, get_query_code):
		self.get_query_code = get_query_code

class SqlFactRelationship:
	def __init__(self, get_query_code):
		self.get_query_code = get_query_code


# Querys para tablas donde se almacena la informacion de los estudiantes 
# consultas para la actualizacion
get_system_parameter = dedent("""\
	SELECT * FROM parametro_sistema WHERE codigo = %s""")

update_system_parameter = dedent("""\
	UPDATE parametro_sistema SET definicion=%s, fecha_actualizacion=NOW() WHERE id = %s""")

# consultas para tablas estaticas
get_nationality_code = dedent("""\
	SELECT id FROM dim_nacionalidad WHERE codigo = %s""") 

insert_nationality = dedent("""\
	INSERT INTO dim_nacionalidad (codigo) VALUES (%s)""")

get_nationality_code_verify = dedent("""\
	SELECT id FROM dim_nacionalidad WHERE codigo = %s OR codigo = %s""")	

get_sex_code = dedent("""\
	SELECT id FROM dim_genero WHERE codigo = %s""") 

insert_sex = dedent("""\
	INSERT INTO dim_genero (codigo) VALUES (%s)""")

get_sex_code_verify = dedent("""\
	SELECT id FROM dim_genero WHERE codigo = %s OR codigo = %s""")

# status
get_status_code = dedent("""\
	SELECT id FROM dim_status WHERE codigo = %s""") 

insert_status = dedent("""\
	INSERT INTO dim_status (codigo) VALUES (%s)""")

get_status_code_verify = dedent("""\
	SELECT id FROM dim_status WHERE codigo = %s OR codigo = %s""")

# DISCAPACIDAD
get_disability_code = dedent("""\
	SELECT id FROM dim_discapacidad WHERE codigo = %s""") 

insert_disability = dedent("""\
	INSERT INTO dim_discapacidad (codigo) VALUES (%s)""")

get_disability_code_verify = dedent("""\
	SELECT id FROM dim_discapacidad WHERE codigo = %s OR codigo = %s""")

# ETNIA
get_ethnic_group_code = dedent("""\
	SELECT id FROM dim_etnia WHERE codigo = %s""") 

insert_ethnic_group = dedent("""\
	INSERT INTO dim_etnia (codigo) VALUES (%s)""")

get_ethnic_group_code_verify = dedent("""\
	SELECT id FROM dim_etnia WHERE codigo = %s OR codigo = %s""")

# ETNIA
get_type_student_code = dedent("""\
	SELECT id FROM dim_tipo_estudiante WHERE codigo = %s""") 

insert_type_student = dedent("""\
	INSERT INTO dim_tipo_estudiante (codigo) VALUES (%s)""")

get_type_student_code_verify = dedent("""\
	SELECT id FROM dim_tipo_estudiante WHERE codigo = %s OR codigo = %s""")

# Año
get_year_code = dedent("""\
	SELECT id FROM dim_tiempo WHERE codigo = %s""") 

insert_year = dedent("""\
	INSERT INTO dim_tiempo (codigo) VALUES (%s)""")

get_year_code_verify = dedent("""\
	SELECT id FROM dim_tiempo WHERE codigo = %s OR codigo = %s""")

# consultas para estudiante
get_student_code = dedent("""\
	SELECT id FROM dim_estudiante WHERE cedula = %s""")

insert_student = dedent("""\
	INSERT INTO dim_estudiante
		(cedula, nombre, apellido, fecha_nacimiento, telefono1, telefono2, email, edo_procedencia)
	VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""")

update_student = dedent("""\
	UPDATE dim_estudiante
	SET cedula = %s, nombre=%s, apellido=%s, fecha_nacimiento=%s, telefono1=%s, telefono2=%s, email=%s, edo_procedencia=%s
	WHERE id=%s""")

# consultas para carrera
get_profession_code = dedent("""\
	SELECT id FROM dim_carrera WHERE nombre = %s""")

# consultas para facultad
get_faculty_code = dedent("""\
	SELECT id FROM dim_facultad WHERE codigo = %s""")

# consulta para verificar
get_relationship_student = dedent("""\
	SELECT fact.id 
	FROM fact_estudiante_facultad AS fact 
	INNER JOIN dim_estudiante AS e 
	ON (fact.id_estudiante = e.id) WHERE cedula = %s""")

# consulta para verificar docente_facultad
get_relationship_docente_facultad = dedent("""\
	SELECT fact.id 
	FROM fact_docente_facultad AS fact 
	INNER JOIN dim_docente AS d 
	ON (fact.id_docente = d.id) WHERE cedula = %s""")

get_relationship_docente_publication = dedent("""\
	SELECT fact.id 
	FROM fact_docente_publicacion AS fact 
	INNER JOIN dim_docente AS d 
	ON (fact.id_docente = d.id) 
	INNER JOIN dim_publicacion AS p
	ON (fact.id_publicacion = p.id) 
	WHERE d.cedula = %s AND p.codigo = %s""")

get_relationship_graduate_jobs = dedent("""\
	SELECT fact.id
	FROM fact_egresado_trabajos AS fact
	INNER JOIN dim_trabajos AS t
	ON (fact.id_trabajo = t.id) 
	WHERE t.codigo = %s""")

get_relationship_graduate_patents = dedent("""\
	SELECT fact.id
	FROM fact_egresado_patentes AS fact
	INNER JOIN dim_patentes AS p
	ON (fact.id_patentes = p.id) 
	WHERE p.codigo = %s""")

get_relationship_graduate_certification = dedent("""\
	SELECT fact.id
	FROM fact_egresado_certificacion AS fact
	INNER JOIN dim_certificacion AS c
	ON (fact.id_certificacion = c.id) 
	WHERE c.codigo = %s""")

get_relationship_graduate_courses = dedent("""\
	SELECT fact.id
	FROM fact_egresado_cursos AS fact
	INNER JOIN dim_cursos AS c
	ON (fact.id_cursos = c.id) 
	WHERE c.codigo = %s""")

get_relationship_graduate_education = dedent("""\
	SELECT fact.id
	FROM fact_egresado_educacion AS fact
	INNER JOIN dim_educacion AS e
	ON (fact.id_educacion = e.id) 
	WHERE e.codigo = %s""")

get_relationship_graduate_volunteering = dedent("""\
	SELECT fact.id
	FROM fact_egresado_voluntariado AS fact
	INNER JOIN dim_voluntariado AS v
	ON (fact.id_voluntariado = v.id) 
	WHERE v.codigo = %s""")

get_relationship_graduate_studiosuc = dedent("""\
	SELECT fact.id
	FROM fact_egresado_estudiosuc AS fact
	INNER JOIN dim_estudiosuc AS v
	ON (fact.id_estudiosuc = v.id) 
	WHERE v.codigo = %s""")

# consulta para escalafon
get_scale_code = dedent("""\
	SELECT id FROM dim_escalafon WHERE nombre = %s""")

# consulta para grado
get_grade_code = dedent("""\
	SELECT id FROM dim_grado WHERE nombre = %s""")

# consultas para docente
get_teacher_code = dedent("""\
	SELECT id FROM dim_docente WHERE cedula = %s""")

insert_teacher = dedent("""\
	INSERT INTO dim_docente
		(cedula, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, correo, area_de_investigacion)
	VALUES (%s, %s, %s, %s, %s, %s, %s)""")

update_teacher = dedent("""\
	UPDATE dim_docente
	SET cedula = %s, primer_nombre=%s, segundo_nombre=%s, primer_apellido=%s,segundo_apellido=%s, correo=%s, area_de_investigacion=%s
	WHERE id=%s""")

# consulta para publicacion
get_publication_code = dedent("""\
	SELECT id FROM dim_publicacion WHERE codigo = %s""")

# consulta para proyecto
get_project_code = dedent("""\
	SELECT id FROM dim_proyecto WHERE codigo = %s""")

# consulta para otroestudio
get_other_studio_code = dedent("""\
	SELECT id FROM dim_otroestudio WHERE codigo = %s""")

get_title_code = dedent("""\
	SELECT id FROM dim_titulo WHERE codigo = %s""")

get_prize_code = dedent("""\
	SELECT id FROM dim_premio WHERE codigo = %s""")

# consultas para egresados
get_graduate_code = dedent("""\
	SELECT id FROM dim_egresado WHERE nombre_usuario = %s""")

insert_graduate = dedent("""\
	INSERT INTO dim_egresado
		(nombre_usuario, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, descripcion, intereses, correo, telefono, identificacion)
	VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""")

update_graduate = dedent("""\
	UPDATE dim_docente
	SET nombre_usuario=%s, primer_nombre=%s, segundo_nombre=%s, primer_apellido=%s, segundo_apellido=%s, descripcion=%s, intereses=%s, correo=%s, telefono=%s, identificacion=%s
	WHERE id=%s""")
	
# consultas para estudios uc
get_estudiosUc_code = dedent("""\
	SELECT id, anho_grado FROM dim_estudiosuc WHERE codigo = %s""")

insert_estudiosUc = dedent("""\
	INSERT INTO dim_estudiosuc
		(titulo, ano_grado, url_certificacion, codigo)
	VALUES (%s, %s, %s, %s)""")

update_estudiosUc = dedent("""\
	UPDATE dim_estudiosuc
	SET titulo=%s, ano_grado=%s, url_certificacion=%s, codigo=%s
	WHERE id=%s""")

# consulta para certificacion
get_certification_code = dedent("""\
	SELECT id FROM dim_certificacion WHERE codigo = %s""")

# consulta para cursos
get_courses_code = dedent("""\
	SELECT id FROM dim_cursos WHERE codigo = %s""")

# consulta para educacion
get_education_code = dedent("""\
	SELECT id FROM dim_educacion WHERE codigo = %s""")

# consulta para patentes
get_patents_code = dedent("""\
	SELECT id FROM dim_patentes WHERE codigo = %s""")

# consulta para trabajos
get_jobs_code = dedent("""\
	SELECT id FROM dim_trabajos WHERE codigo = %s""")

# consulta para voluntariado
get_volunteering_code = dedent("""\
	SELECT id FROM dim_voluntariado WHERE codigo = %s""")


get_type_teacher_code = dedent("""\
	SELECT id FROM dim_tipo_docente WHERE codigo = %s""")

insert_type_teacher = dedent("""\
	INSERT INTO dim_tipo_docente (codigo) VALUES (%s)""")

get_type_teacher_code_verify = dedent("""\
	SELECT id FROM dim_tipo_docente WHERE codigo = %s OR codigo = %s""")

systemParameter = SqlSystemParameter(get_system_parameter, update_system_parameter)
nationalityQuery = SqlTableStatic(get_nationality_code, insert_nationality, get_nationality_code_verify)
sexQuery = SqlTableStatic(get_sex_code, insert_sex, get_sex_code_verify)
statusQuery = SqlTableStatic(get_status_code, insert_status, get_status_code_verify)
typeTeacherQuery = SqlTableStatic(get_type_teacher_code, insert_type_teacher, get_type_teacher_code_verify)
disabilityQuery = SqlTableStatic(get_disability_code, insert_disability, get_disability_code_verify)
ethnicGroupQuery = SqlTableStatic(get_ethnic_group_code, insert_ethnic_group, get_ethnic_group_code_verify)
typeStudentQuery = SqlTableStatic(get_type_student_code, insert_type_student, get_type_student_code_verify)
yearQuery = SqlTableStatic(get_year_code, insert_year, get_year_code_verify)
studentQuery = SqlFact(get_student_code, insert_student, update_student)
teacherQuery = SqlFact(get_teacher_code, insert_teacher, update_teacher)
graduateQuery = SqlFact(get_graduate_code, insert_graduate, update_graduate)
studiosUcQuery = SqlFact(get_estudiosUc_code, insert_estudiosUc, update_estudiosUc)
professionQuery = SqlTableSameParse(get_profession_code)
facultyQuery = SqlTableSameParse(get_faculty_code)
scaleQuery = SqlTableSameParse(get_scale_code)
gradeQuery = SqlTableSameParse(get_grade_code)
publicationQuery = SqlTableSameParse(get_publication_code)
projectQuery = SqlTableSameParse(get_project_code)
otherStudioQuery = SqlTableSameParse(get_other_studio_code)
titleQuery = SqlTableSameParse(get_title_code)
prizeQuery = SqlTableSameParse(get_prize_code)
studentRelationship = SqlFactRelationship(get_relationship_student)
teacherFacultyRelationship = SqlFactRelationship(get_relationship_docente_facultad)
teacherPublicationRelationship = SqlFactRelationship(get_relationship_docente_publication)
graduateJobsRelationship = SqlFactRelationship(get_relationship_graduate_jobs)
graduatePatentsRelationship = SqlFactRelationship(get_relationship_graduate_patents)
graduateCertificationRelationship = SqlFactRelationship(get_relationship_graduate_certification)
graduateCoursesRelationship = SqlFactRelationship(get_relationship_graduate_courses)
graduateEducationRelationship = SqlFactRelationship(get_relationship_graduate_education)
graduateVolunteeringRelationship = SqlFactRelationship(get_relationship_graduate_volunteering)
graduateStudiosUcRelationship = SqlFactRelationship(get_relationship_graduate_studiosuc)
certificationQuery = SqlTableSameParse(get_certification_code)
coursesQuery = SqlTableSameParse(get_courses_code)
educationQuery = SqlTableSameParse(get_education_code)
patentsQuery = SqlTableSameParse(get_patents_code)
jobsQuery = SqlTableSameParse(get_jobs_code)
volunteeringQuery = SqlTableSameParse(get_volunteering_code)




