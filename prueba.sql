-- phpMyAdmin SQL Dump
-- version 4.8.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 18-10-2018 a las 23:33:05
-- Versión del servidor: 10.1.34-MariaDB
-- Versión de PHP: 7.2.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `prueba`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dim_asignatura_inscrita`
--

CREATE TABLE `dim_asignatura_inscrita` (
  `id` int(11) NOT NULL,
  `codigo` varchar(100) NOT NULL,
  `nombre` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `dim_asignatura_inscrita`
--

INSERT INTO `dim_asignatura_inscrita` (`id`, `codigo`, `nombre`) VALUES
(1, 'DW', 'Desarrollo Web'),
(2, 'Electiva3', 'Electiva III'),
(3, 'Matemetica1', 'Matemetica 1');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dim_asigtura_aprobada`
--

CREATE TABLE `dim_asigtura_aprobada` (
  `id` int(11) NOT NULL,
  `codigo` varchar(100) NOT NULL,
  `nombre` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `dim_asigtura_aprobada`
--

INSERT INTO `dim_asigtura_aprobada` (`id`, `codigo`, `nombre`) VALUES
(1, 'CAO102', 'REDES 2'),
(2, 'CAO103', 'Sistemas de Informacion');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dim_carrera`
--

CREATE TABLE `dim_carrera` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `tipo` varchar(50) NOT NULL,
  `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `dim_carrera`
--

INSERT INTO `dim_carrera` (`id`, `nombre`, `tipo`, `created_date`, `updated_date`) VALUES
(117, 'Computación', 'Semestre', '2018-10-18 21:28:47', '2018-10-18 21:28:47'),
(118, 'Química', 'Semestre', '2018-10-18 21:28:47', '2018-10-18 21:28:47'),
(119, 'Física', 'Semestre', '2018-10-18 21:28:47', '2018-10-18 21:28:47'),
(120, 'Matemática', 'Semestre', '2018-10-18 21:28:47', '2018-10-18 21:28:47'),
(121, 'Biología', 'Semestre', '2018-10-18 21:28:47', '2018-10-18 21:28:47');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dim_docente`
--

CREATE TABLE `dim_docente` (
  `id` int(11) NOT NULL,
  `cedula` varchar(100) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `correo` varchar(100) NOT NULL,
  `area_trabajo` varchar(300) NOT NULL,
  `fecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `fecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `dim_docente`
--

INSERT INTO `dim_docente` (`id`, `cedula`, `nombre`, `apellido`, `correo`, `area_trabajo`, `fecha_creacion`, `fecha_actualizacion`) VALUES
(19, '545511', 'Marilyn', 'Guigni', 'investigacion', 'marilyngiugni@gmail.com', '2018-10-18 21:28:48', '2018-10-18 21:28:48'),
(20, '1515515', 'Dessiree', 'Delgado', 'investigacion', 'desidelgado@gmail.com', '2018-10-18 21:28:48', '2018-10-18 21:28:48'),
(21, '11356034', 'Mirella', 'Herrera', 'investigacion', 'mirella.herrera@gmail.com', '2018-10-18 21:28:48', '2018-10-18 21:28:48');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dim_escalafon`
--

CREATE TABLE `dim_escalafon` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `fecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `dim_escalafon`
--

INSERT INTO `dim_escalafon` (`id`, `nombre`, `fecha_creacion`, `fecha_actualizacion`) VALUES
(6, 'Instructor', '2018-10-18 19:08:43', '2018-10-18 19:08:43'),
(7, 'Asistente', '2018-10-18 19:08:43', '2018-10-18 19:08:43'),
(8, 'Agregado', '2018-10-18 19:08:43', '2018-10-18 19:08:43'),
(9, 'Asociado', '2018-10-18 19:08:43', '2018-10-18 19:08:43'),
(10, 'Titular', '2018-10-18 19:08:43', '2018-10-18 19:08:43');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dim_estudiante`
--

CREATE TABLE `dim_estudiante` (
  `id` int(11) NOT NULL,
  `cedula` varchar(100) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `telefono1` varchar(100) NOT NULL,
  `telefono2` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `edo_procedencia` varchar(100) NOT NULL,
  `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `dim_estudiante`
--

INSERT INTO `dim_estudiante` (`id`, `cedula`, `nombre`, `apellido`, `fecha_nacimiento`, `telefono1`, `telefono2`, `email`, `edo_procedencia`, `created_date`, `updated_date`) VALUES
(112, '22422883', 'Wilkel', 'Apellido', '1995-05-24', '0412-76558802', '0245-3351406', 'wilkelgiovanni@gmail.com', 'Carabobo', '2018-10-18 21:28:47', '2018-10-18 21:28:47'),
(113, '26011707', 'Alba', 'Silva', '1997-03-01', '0241-2051334', '0412-1308522', 'andreadellepere_3@hotmail.com', 'Carabobo', '2018-10-18 21:28:47', '2018-10-18 21:28:47'),
(114, '27855129', 'Ana', 'Sanchez', '1999-09-22', '0241-8481233', '0426-3437317', 'anasanchez@gmail.com', 'Carabobo', '2018-10-18 21:28:47', '2018-10-18 21:28:47'),
(115, '13381615', 'Luis', 'Servita', '1976-07-07', '02418140120', '04265413615', 'luisservita777@gmail.com', 'Carabobo', '2018-10-18 21:28:47', '2018-10-18 21:28:47'),
(116, '22345223', 'Alejandro', 'Giovanni', '1995-05-24', '0215545', '155455515', 'alejandro@gmail.com', 'Carabobo', '2018-10-18 21:28:47', '2018-10-18 21:28:47'),
(117, '22345243', 'Alejandro2', 'Giovanni2', '1995-05-24', '0215545', '155455515', 'alejandro2@gmail.com', 'Carabobo', '2018-10-18 21:28:47', '2018-10-18 21:28:47');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dim_facultad`
--

CREATE TABLE `dim_facultad` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `dim_facultad`
--

INSERT INTO `dim_facultad` (`id`, `nombre`, `created_date`, `updated_date`) VALUES
(57, 'Ingeniería', '2018-10-18 19:46:57', '2018-10-18 19:46:57'),
(58, 'Ciencias Jurídicas y Políticas', '2018-10-18 19:46:57', '2018-10-18 19:46:57'),
(59, 'Ciencias de la Salud', '2018-10-18 19:46:57', '2018-10-18 19:46:57'),
(60, 'Ciencias Económicas y Sociales', '2018-10-18 19:46:57', '2018-10-18 19:46:57'),
(61, 'Ciencias de la Educación', '2018-10-18 19:46:57', '2018-10-18 19:46:57'),
(62, 'Odontología', '2018-10-18 19:46:57', '2018-10-18 19:46:57'),
(63, 'Dirección General de Postgrado', '2018-10-18 19:46:57', '2018-10-18 19:46:57'),
(64, 'Ciencias y Tecnología', '2018-10-18 19:46:57', '2018-10-18 19:46:57');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dim_grado`
--

CREATE TABLE `dim_grado` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `fecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `dim_grado`
--

INSERT INTO `dim_grado` (`id`, `nombre`, `fecha_creacion`, `fecha_actualizacion`) VALUES
(1, 'Especializacion', '2018-10-11 19:45:36', '2018-10-11 19:45:36'),
(2, 'Maestria', '2018-10-11 19:45:36', '2018-10-11 19:45:36'),
(3, 'Doctorado', '2018-10-11 19:45:36', '2018-10-11 19:45:36');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dim_nacionalidad`
--

CREATE TABLE `dim_nacionalidad` (
  `id` int(11) NOT NULL,
  `codigo` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `dim_nacionalidad`
--

INSERT INTO `dim_nacionalidad` (`id`, `codigo`) VALUES
(13, 'Venezolano'),
(14, 'Extranjero');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dim_publicacion`
--

CREATE TABLE `dim_publicacion` (
  `id` int(11) NOT NULL,
  `tipo` varchar(50) NOT NULL,
  `autor` varchar(100) NOT NULL,
  `titulo` varchar(100) NOT NULL,
  `codigo` varchar(100) NOT NULL,
  `fecha` date NOT NULL,
  `revista` varchar(100) NOT NULL,
  `fecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `dim_publicacion`
--

INSERT INTO `dim_publicacion` (`id`, `tipo`, `autor`, `titulo`, `codigo`, `fecha`, `revista`, `fecha_creacion`, `fecha_actualizacion`) VALUES
(16, 'Tipo1', 'Mirella Herrera', 'Titulo de la publicacion1', '1', '2012-05-30', 'Revista Cientifica', '2018-10-18 21:28:48', '2018-10-18 21:28:48'),
(17, 'Tipo1', 'Desiree Delgado, Mirella Herrera', 'Titulo de la publicacion2', '2', '2013-08-30', 'Revista Cientifica2', '2018-10-18 21:28:48', '2018-10-18 21:28:48'),
(18, 'Tipo2', 'Desiree Delgado', 'Titulo de la publicacion3', '3', '2014-10-10', 'Revista Cientifica', '2018-10-18 21:28:48', '2018-10-18 21:28:48');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dim_sexo`
--

CREATE TABLE `dim_sexo` (
  `id` int(11) NOT NULL,
  `codigo` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `dim_sexo`
--

INSERT INTO `dim_sexo` (`id`, `codigo`) VALUES
(7, 'Femenino'),
(6, 'Masculino');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dim_status`
--

CREATE TABLE `dim_status` (
  `id` int(11) NOT NULL,
  `codigo` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `dim_status`
--

INSERT INTO `dim_status` (`id`, `codigo`) VALUES
(1, 'activo'),
(2, 'inactivo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dim_titulo`
--

CREATE TABLE `dim_titulo` (
  `id` int(11) NOT NULL,
  `codigo` varchar(100) NOT NULL,
  `tipo` varchar(100) NOT NULL,
  `descripcion` varchar(100) NOT NULL,
  `nivel` varchar(100) NOT NULL,
  `universidad` varchar(100) NOT NULL,
  `fecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `fecha_actualizacion` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fact_asignatura_inscrita`
--

CREATE TABLE `fact_asignatura_inscrita` (
  `id` int(11) NOT NULL,
  `id_estudiante` int(11) NOT NULL,
  `id_facultad` int(11) NOT NULL,
  `id_carrera` int(11) NOT NULL,
  `id_status` int(11) NOT NULL,
  `id_asignatura_inscrita` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fact_docente`
--

CREATE TABLE `fact_docente` (
  `id` int(11) NOT NULL,
  `id_docente` int(11) NOT NULL,
  `id_sexo` int(11) NOT NULL,
  `id_grado` int(11) NOT NULL,
  `id_escalafon` int(11) NOT NULL,
  `id_facultad` int(11) NOT NULL,
  `id_nacionalidad` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL DEFAULT '1',
  `fecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fact_docente_publicacion`
--

CREATE TABLE `fact_docente_publicacion` (
  `id` int(11) NOT NULL,
  `id_docente` int(11) DEFAULT NULL,
  `id_publicacion` int(11) DEFAULT NULL,
  `id_facultad` int(11) DEFAULT NULL,
  `cantidad_citas` int(11) DEFAULT '0',
  `cantidad` int(11) NOT NULL DEFAULT '1',
  `fecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `fact_docente_publicacion`
--

INSERT INTO `fact_docente_publicacion` (`id`, `id_docente`, `id_publicacion`, `id_facultad`, `cantidad_citas`, `cantidad`, `fecha_creacion`, `fecha_actualizacion`) VALUES
(12, 21, 17, 64, 2, 1, '2018-10-18 21:28:48', '2018-10-18 21:28:48'),
(13, 20, 17, 64, 2, 1, '2018-10-18 21:28:48', '2018-10-18 21:28:48'),
(14, 21, 16, 64, 2, 1, '2018-10-18 21:28:48', '2018-10-18 21:28:48'),
(15, 20, 18, 64, 1, 1, '2018-10-18 21:28:48', '2018-10-18 21:28:48');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fact_estudiante_facultad`
--

CREATE TABLE `fact_estudiante_facultad` (
  `id` int(11) NOT NULL,
  `id_estudiante` int(11) DEFAULT NULL,
  `id_facultad` int(11) DEFAULT NULL,
  `id_carrera` int(11) DEFAULT NULL,
  `id_sexo` int(11) DEFAULT NULL,
  `id_nacionalidad` int(11) DEFAULT NULL,
  `cantidad` int(11) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `fact_estudiante_facultad`
--

INSERT INTO `fact_estudiante_facultad` (`id`, `id_estudiante`, `id_facultad`, `id_carrera`, `id_sexo`, `id_nacionalidad`, `cantidad`) VALUES
(37, 112, 64, 117, 6, 13, 1),
(38, 113, 64, 117, 7, 13, 1),
(39, 114, 64, 118, 7, 13, 1),
(40, 115, 64, 119, 7, 13, 1),
(41, 116, 64, 120, 6, 13, 1),
(42, 117, 64, 120, 6, 13, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `last_update`
--

CREATE TABLE `last_update` (
  `id` int(11) NOT NULL,
  `is_load_initial` tinyint(1) NOT NULL,
  `last_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `last_update`
--

INSERT INTO `last_update` (`id`, `is_load_initial`, `last_update`) VALUES
(7, 0, '2018-10-18 20:25:38');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `parametro_sistema`
--

CREATE TABLE `parametro_sistema` (
  `id` int(11) NOT NULL,
  `codigo` varchar(100) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `descripcion` varchar(300) NOT NULL,
  `definicion` varchar(3000) NOT NULL,
  `fecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `parametro_sistema`
--

INSERT INTO `parametro_sistema` (`id`, `codigo`, `nombre`, `descripcion`, `definicion`, `fecha_creacion`, `fecha_actualizacion`) VALUES
(1, 'CARGA_INICIAL_ACTUALIZACION', 'CARGA_INICIAL_ACTUALIZACION', 'Parametro que toma valores boleanos para la carga inicial (1) y la actualizacion (0, toma la fecha de actualizacion)', '0', '2018-10-18 20:35:32', '2018-10-18 21:28:48'),
(2, 'RUTA_CARGA_INICIAL_ESTUDIANTES', 'RUTA_CARGA_INICIAL_ESTUDIANTES', 'Endpoint o ruta para la carga inicial del modulo de estudiantes', 'http://127.0.0.1:8082/estudiantes', '2018-10-18 20:38:51', '2018-10-18 20:38:51'),
(3, 'RUTA_CARGA_INICIAL_PROFESORES', 'RUTA_CARGA_INICIAL_PROFESORES', 'Endpoint o ruta para la carga inicial del modulo de profesores', 'http://127.0.0.1:8082/profesores', '2018-10-18 20:40:26', '2018-10-18 20:40:26'),
(4, 'RUTA_CARGA_INICIAL_EGRESADOS', 'RUTA_CARGA_INICIAL_EGRESADOS', 'Endpoint o ruta para la carga inicial del modulo de egresados', 'http://127.0.0.1:8082/egresados', '2018-10-18 21:31:21', '2018-10-18 21:31:21');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `prueba`
--

CREATE TABLE `prueba` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `created_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `prueba`
--

INSERT INTO `prueba` (`id`, `name`, `email`, `created_date`, `updated_date`) VALUES
(100, 'Wilkel', 'wilkel@gmail.com', '2018-09-27 18:43:21', '2018-09-27 18:43:21'),
(101, 'Wilkel otro mas', 'wilkelotromas@gmail.com', '2018-09-27 18:43:21', '2018-09-27 18:43:21'),
(102, 'Otro', 'otro1@gmail.com', '2018-09-27 18:43:21', '2018-09-27 18:43:21');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `role`
--

CREATE TABLE `role` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `role`
--

INSERT INTO `role` (`id`, `name`) VALUES
(1, 'administrador'),
(2, 'vicerrector');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `id_role` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `user`
--

INSERT INTO `user` (`id`, `first_name`, `last_name`, `username`, `email`, `password`, `id_role`) VALUES
(19, 'Wilkel2', 'Giovanni', 'wgiovanni', 'wilkelgiovanni@gmail.com', '123456789', 1),
(20, 'prueba', 'prueba', 'prueba', 'prueba@gmail.com', '123456', 1),
(22, 'aja', 'aja', 'aja', 'aja@gmail.com', '123456', 2),
(23, 'dfgdf', 'fdgdgd', 'ghcgh', 'aja2@gmail.com', '123456', 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `dim_asignatura_inscrita`
--
ALTER TABLE `dim_asignatura_inscrita`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `dim_asigtura_aprobada`
--
ALTER TABLE `dim_asigtura_aprobada`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `dim_carrera`
--
ALTER TABLE `dim_carrera`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indices de la tabla `dim_docente`
--
ALTER TABLE `dim_docente`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `cedula` (`cedula`);

--
-- Indices de la tabla `dim_escalafon`
--
ALTER TABLE `dim_escalafon`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indices de la tabla `dim_estudiante`
--
ALTER TABLE `dim_estudiante`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `cedula` (`cedula`);

--
-- Indices de la tabla `dim_facultad`
--
ALTER TABLE `dim_facultad`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indices de la tabla `dim_grado`
--
ALTER TABLE `dim_grado`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indices de la tabla `dim_nacionalidad`
--
ALTER TABLE `dim_nacionalidad`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `dim_publicacion`
--
ALTER TABLE `dim_publicacion`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `codigo` (`codigo`);

--
-- Indices de la tabla `dim_sexo`
--
ALTER TABLE `dim_sexo`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `codigo` (`codigo`);

--
-- Indices de la tabla `dim_status`
--
ALTER TABLE `dim_status`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `dim_titulo`
--
ALTER TABLE `dim_titulo`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `fact_asignatura_inscrita`
--
ALTER TABLE `fact_asignatura_inscrita`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_estudiante` (`id_estudiante`),
  ADD KEY `id_asignatura_inscrita` (`id_asignatura_inscrita`),
  ADD KEY `id_status` (`id_status`),
  ADD KEY `id_carrera` (`id_carrera`),
  ADD KEY `id_facultad` (`id_facultad`);

--
-- Indices de la tabla `fact_docente`
--
ALTER TABLE `fact_docente`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_docente` (`id_docente`),
  ADD KEY `id_sexo` (`id_sexo`),
  ADD KEY `id_grado` (`id_grado`),
  ADD KEY `id_escalafon` (`id_escalafon`),
  ADD KEY `id_facultad` (`id_facultad`),
  ADD KEY `id_nacionalidad` (`id_nacionalidad`);

--
-- Indices de la tabla `fact_docente_publicacion`
--
ALTER TABLE `fact_docente_publicacion`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_docente` (`id_docente`),
  ADD KEY `id_publicacion` (`id_publicacion`),
  ADD KEY `id_facultad` (`id_facultad`);

--
-- Indices de la tabla `fact_estudiante_facultad`
--
ALTER TABLE `fact_estudiante_facultad`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_estudiante` (`id_estudiante`),
  ADD KEY `id_facultad` (`id_facultad`),
  ADD KEY `id_carrera` (`id_carrera`),
  ADD KEY `id_sexo` (`id_sexo`),
  ADD KEY `id_nacionalidad` (`id_nacionalidad`);

--
-- Indices de la tabla `last_update`
--
ALTER TABLE `last_update`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `parametro_sistema`
--
ALTER TABLE `parametro_sistema`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `codigo` (`codigo`);

--
-- Indices de la tabla `prueba`
--
ALTER TABLE `prueba`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `role`
--
ALTER TABLE `role`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `username` (`username`),
  ADD KEY `id_role` (`id_role`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `dim_asignatura_inscrita`
--
ALTER TABLE `dim_asignatura_inscrita`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `dim_asigtura_aprobada`
--
ALTER TABLE `dim_asigtura_aprobada`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `dim_carrera`
--
ALTER TABLE `dim_carrera`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=122;

--
-- AUTO_INCREMENT de la tabla `dim_docente`
--
ALTER TABLE `dim_docente`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT de la tabla `dim_escalafon`
--
ALTER TABLE `dim_escalafon`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `dim_estudiante`
--
ALTER TABLE `dim_estudiante`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=118;

--
-- AUTO_INCREMENT de la tabla `dim_facultad`
--
ALTER TABLE `dim_facultad`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=65;

--
-- AUTO_INCREMENT de la tabla `dim_grado`
--
ALTER TABLE `dim_grado`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `dim_nacionalidad`
--
ALTER TABLE `dim_nacionalidad`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de la tabla `dim_publicacion`
--
ALTER TABLE `dim_publicacion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT de la tabla `dim_sexo`
--
ALTER TABLE `dim_sexo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `dim_status`
--
ALTER TABLE `dim_status`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `dim_titulo`
--
ALTER TABLE `dim_titulo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `fact_asignatura_inscrita`
--
ALTER TABLE `fact_asignatura_inscrita`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `fact_docente`
--
ALTER TABLE `fact_docente`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `fact_docente_publicacion`
--
ALTER TABLE `fact_docente_publicacion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de la tabla `fact_estudiante_facultad`
--
ALTER TABLE `fact_estudiante_facultad`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- AUTO_INCREMENT de la tabla `last_update`
--
ALTER TABLE `last_update`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `parametro_sistema`
--
ALTER TABLE `parametro_sistema`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `prueba`
--
ALTER TABLE `prueba`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=103;

--
-- AUTO_INCREMENT de la tabla `role`
--
ALTER TABLE `role`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `fact_asignatura_inscrita`
--
ALTER TABLE `fact_asignatura_inscrita`
  ADD CONSTRAINT `fact_asignatura_inscrita_ibfk_1` FOREIGN KEY (`id_estudiante`) REFERENCES `dim_estudiante` (`id`),
  ADD CONSTRAINT `fact_asignatura_inscrita_ibfk_2` FOREIGN KEY (`id_facultad`) REFERENCES `dim_facultad` (`id`),
  ADD CONSTRAINT `fact_asignatura_inscrita_ibfk_3` FOREIGN KEY (`id_asignatura_inscrita`) REFERENCES `dim_asignatura_inscrita` (`id`),
  ADD CONSTRAINT `fact_asignatura_inscrita_ibfk_4` FOREIGN KEY (`id_carrera`) REFERENCES `dim_carrera` (`id`),
  ADD CONSTRAINT `fact_asignatura_inscrita_ibfk_5` FOREIGN KEY (`id_status`) REFERENCES `dim_status` (`id`);

--
-- Filtros para la tabla `fact_docente`
--
ALTER TABLE `fact_docente`
  ADD CONSTRAINT `fact_docente_ibfk_1` FOREIGN KEY (`id_escalafon`) REFERENCES `dim_escalafon` (`id`),
  ADD CONSTRAINT `fact_docente_ibfk_2` FOREIGN KEY (`id_facultad`) REFERENCES `dim_facultad` (`id`),
  ADD CONSTRAINT `fact_docente_ibfk_3` FOREIGN KEY (`id_grado`) REFERENCES `dim_grado` (`id`),
  ADD CONSTRAINT `fact_docente_ibfk_4` FOREIGN KEY (`id_sexo`) REFERENCES `dim_sexo` (`id`),
  ADD CONSTRAINT `fact_docente_ibfk_5` FOREIGN KEY (`id_nacionalidad`) REFERENCES `dim_nacionalidad` (`id`),
  ADD CONSTRAINT `fact_docente_ibfk_6` FOREIGN KEY (`id_docente`) REFERENCES `dim_docente` (`id`);

--
-- Filtros para la tabla `fact_docente_publicacion`
--
ALTER TABLE `fact_docente_publicacion`
  ADD CONSTRAINT `fact_docente_publicacion_ibfk_1` FOREIGN KEY (`id_docente`) REFERENCES `dim_docente` (`id`),
  ADD CONSTRAINT `fact_docente_publicacion_ibfk_4` FOREIGN KEY (`id_publicacion`) REFERENCES `dim_publicacion` (`id`),
  ADD CONSTRAINT `fact_docente_publicacion_ibfk_5` FOREIGN KEY (`id_facultad`) REFERENCES `dim_facultad` (`id`);

--
-- Filtros para la tabla `fact_estudiante_facultad`
--
ALTER TABLE `fact_estudiante_facultad`
  ADD CONSTRAINT `fact_estudiante_facultad_ibfk_1` FOREIGN KEY (`id_estudiante`) REFERENCES `dim_estudiante` (`id`),
  ADD CONSTRAINT `fact_estudiante_facultad_ibfk_2` FOREIGN KEY (`id_facultad`) REFERENCES `dim_facultad` (`id`),
  ADD CONSTRAINT `fact_estudiante_facultad_ibfk_3` FOREIGN KEY (`id_carrera`) REFERENCES `dim_carrera` (`id`),
  ADD CONSTRAINT `fact_estudiante_facultad_ibfk_4` FOREIGN KEY (`id_nacionalidad`) REFERENCES `dim_nacionalidad` (`id`),
  ADD CONSTRAINT `fact_estudiante_facultad_ibfk_5` FOREIGN KEY (`id_sexo`) REFERENCES `dim_sexo` (`id`);

--
-- Filtros para la tabla `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `user_ibfk_1` FOREIGN KEY (`id_role`) REFERENCES `role` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
