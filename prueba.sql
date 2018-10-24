-- phpMyAdmin SQL Dump
-- version 4.8.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 24-10-2018 a las 23:02:48
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
-- Estructura de tabla para la tabla `dim_certificacion`
--

CREATE TABLE `dim_certificacion` (
  `id` int(11) NOT NULL,
  `codigo` varchar(100) NOT NULL,
  `nombre_certificacion` varchar(100) NOT NULL,
  `descripcion` varchar(500) NOT NULL,
  `url_certificacion` varchar(300) NOT NULL,
  `fecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `dim_certificacion`
--

INSERT INTO `dim_certificacion` (`id`, `codigo`, `nombre_certificacion`, `descripcion`, `url_certificacion`, `fecha_creacion`, `fecha_actualizacion`) VALUES
(28, '1', 'Certificacion1', 'descripcion', 'url xxx', '2018-10-24 00:34:10', '2018-10-24 00:34:10'),
(29, '2', 'Certificacion2', 'descripcion', 'url xxx', '2018-10-24 00:34:10', '2018-10-24 00:34:10'),
(30, '3', 'Certificacion3', 'descripcion', 'url certificacion', '2018-10-24 00:34:10', '2018-10-24 00:34:10');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dim_cursos`
--

CREATE TABLE `dim_cursos` (
  `id` int(11) NOT NULL,
  `codigo` varchar(100) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `url` varchar(300) NOT NULL,
  `fecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `dim_cursos`
--

INSERT INTO `dim_cursos` (`id`, `codigo`, `nombre`, `url`, `fecha_creacion`, `fecha_actualizacion`) VALUES
(21, '1', 'Programación basica', 'http://platzi.com/programacionbasica', '2018-10-24 00:26:28', '2018-10-24 00:26:28'),
(22, '2', 'Curso basico PHP', 'http://platzi.com/wgiovanni/phpbasico', '2018-10-24 00:26:28', '2018-10-24 00:26:28'),
(23, '3', 'Curso Java', 'http://platzi.com/java', '2018-10-24 00:26:28', '2018-10-24 00:26:28'),
(24, '4', 'Curso Angular', 'http://platzi.com/angular', '2018-10-24 00:26:28', '2018-10-24 00:26:28'),
(25, '5', 'Curso basico PHP', 'http://platzi.com/lgomez/phpbasico', '2018-10-24 00:26:28', '2018-10-24 00:26:28');

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
(42, '545511', 'Marilyn', 'Guigni', 'investigacion', 'marilyngiugni@gmail.com', '2018-10-20 22:38:59', '2018-10-20 22:38:59'),
(43, '1515515', 'Dessiree', 'Delgado', 'investigacion', 'desidelgado@gmail.com', '2018-10-20 22:38:59', '2018-10-20 22:38:59'),
(44, '11356034', 'Mirella', 'Herrera', 'investigacion', 'mirella.herrera@gmail.com', '2018-10-20 22:38:59', '2018-10-20 22:38:59'),
(45, '1234567', 'prueba_docente', 'prueba_docente', 'prueba_docente@gmail.com', 'cualquier vaina', '2018-10-20 22:57:50', '2018-10-20 22:57:50');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dim_educacion`
--

CREATE TABLE `dim_educacion` (
  `id` int(11) NOT NULL,
  `codigo` varchar(100) NOT NULL,
  `instituto` varchar(100) NOT NULL,
  `campo_estudio` varchar(100) NOT NULL,
  `fecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `titulo_obtenido` varchar(100) NOT NULL,
  `url_certificacion` varchar(300) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `dim_educacion`
--

INSERT INTO `dim_educacion` (`id`, `codigo`, `instituto`, `campo_estudio`, `fecha_creacion`, `fecha_actualizacion`, `titulo_obtenido`, `url_certificacion`) VALUES
(4, '1', 'Instituto1', 'Campo de Estudio1', '2018-10-24 00:26:28', '2018-10-24 00:26:28', 'Titulo1', 'http://urlcertificacion.com'),
(5, '2', 'Instituto2', 'Campo de Estudio2', '2018-10-24 00:26:28', '2018-10-24 00:26:28', 'Titulo2', 'http://urlcertificacion.com'),
(6, '3', 'Instituto3', 'Campo de Estudio3', '2018-10-24 00:26:28', '2018-10-24 00:26:28', 'Titulo3', 'http://urlcertificacion.com');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dim_egresado`
--

CREATE TABLE `dim_egresado` (
  `id` int(11) NOT NULL,
  `nombre_usuario` varchar(100) NOT NULL,
  `primer_nombre` varchar(100) NOT NULL,
  `segundo_nombre` varchar(100) NOT NULL,
  `primer_apellido` varchar(100) NOT NULL,
  `segundo_apellido` varchar(100) NOT NULL,
  `descripcion` varchar(500) NOT NULL,
  `intereses` varchar(500) NOT NULL,
  `correo` varchar(100) NOT NULL,
  `telefono` varchar(100) NOT NULL,
  `identificacion` varchar(100) NOT NULL,
  `fecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `dim_egresado`
--

INSERT INTO `dim_egresado` (`id`, `nombre_usuario`, `primer_nombre`, `segundo_nombre`, `primer_apellido`, `segundo_apellido`, `descripcion`, `intereses`, `correo`, `telefono`, `identificacion`, `fecha_creacion`, `fecha_actualizacion`) VALUES
(25, 'gjimenez', 'Genessis', 'De Jesus', 'Jimenez', 'Zea', 'descripcion', 'futbol', 'gjimenez@gmail,com', '04127658802', '2464987', '2018-10-24 00:26:28', '2018-10-24 00:26:28'),
(26, 'lgomez', 'Luis', 'Augusto', 'Gomez', 'No se', 'descripcion', 'metal', 'luisgomez@gmail,com', '04127658802', '756438457', '2018-10-24 00:26:28', '2018-10-24 00:26:28'),
(27, 'wmorillo', 'Winder', 'Jose', 'Morillo', 'No se', 'descripcion', 'programar', 'wmorillo@gmail,com', '746574323', '146498766', '2018-10-24 00:26:29', '2018-10-24 00:26:29'),
(28, 'wgiovanni', 'Wilkel', 'Alejandro', 'Giovanni', 'Perozo', 'descripcion', 'programar', 'wgiovanni@gmail,com', '746574323', '22422883', '2018-10-24 00:26:29', '2018-10-24 00:26:29');

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
(167, '13381615', 'Luis', 'Servita', '1976-07-07', '02418140120', '04265413615', 'luisservita777@gmail.com', 'Carabobo', '2018-10-20 22:38:58', '2018-10-20 22:38:58'),
(168, '22422883', 'Wilkel', 'Giovanni', '1995-05-24', '02453351406', '04127658802', 'wilkelgiovanni@gmail.com', 'Carabobo', '2018-10-20 22:38:58', '2018-10-20 22:38:58'),
(169, '1234567', 'prueba_estudiante', 'prueba_estudiante', '2018-10-20', '012283733', '02453351406', 'prueba_estudiante@gmail.com', 'Maracay', '2018-10-20 22:57:49', '2018-10-20 22:57:49');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dim_estudiosuc`
--

CREATE TABLE `dim_estudiosuc` (
  `id` int(11) NOT NULL,
  `titulo` varchar(100) NOT NULL,
  `anho_grado` date NOT NULL,
  `url_certificacion` varchar(300) NOT NULL,
  `codigo` varchar(100) NOT NULL,
  `fecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `dim_estudiosuc`
--

INSERT INTO `dim_estudiosuc` (`id`, `titulo`, `anho_grado`, `url_certificacion`, `codigo`, `fecha_creacion`, `fecha_actualizacion`) VALUES
(33, 'Licenciado en Computación', '2018-07-24', 'url...', '1', '2018-10-24 00:26:30', '2018-10-24 00:26:30'),
(34, 'Licenciado en Física', '2018-07-24', 'url...', '2', '2018-10-24 00:26:30', '2018-10-24 00:26:30'),
(35, 'Licenciado en Computación', '2018-07-24', 'url...', '3', '2018-10-24 00:26:30', '2018-10-24 00:26:30'),
(36, 'Licenciado en Química', '2010-07-24', 'url...', '4', '2018-10-24 00:26:30', '2018-10-24 00:26:30');

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
-- Estructura de tabla para la tabla `dim_patentes`
--

CREATE TABLE `dim_patentes` (
  `id` int(11) NOT NULL,
  `codigo` varchar(100) NOT NULL,
  `titulo` varchar(100) NOT NULL,
  `descripcion` varchar(500) NOT NULL,
  `numero` varchar(100) NOT NULL,
  `inventores` varchar(150) NOT NULL,
  `fecha` date NOT NULL,
  `url` varchar(300) NOT NULL,
  `fecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `dim_patentes`
--

INSERT INTO `dim_patentes` (`id`, `codigo`, `titulo`, `descripcion`, `numero`, `inventores`, `fecha`, `url`, `fecha_creacion`, `fecha_actualizacion`) VALUES
(3, '1', 'Patente1', 'Descripcion Patente1', '5151', 'inventor1, inventor2, inventor3', '2018-07-10', 'url', '2018-10-24 00:26:30', '2018-10-24 00:26:30'),
(4, '2', 'Patente2', 'Descripcion Patente1', '987874', 'inventor1, inventor2, inventor3', '2018-07-10', 'url', '2018-10-24 00:26:30', '2018-10-24 00:26:30');

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
(34, 'Tipo1', 'Mirella Herrera', 'Titulo de la publicacion1', '1', '2012-05-30', 'Revista Cientifica', '2018-10-20 22:39:00', '2018-10-20 22:39:00'),
(35, 'Tipo1', 'Desiree Delgado, Mirella Herrera', 'Titulo de la publicacion2', '2', '2013-08-30', 'Revista Cientifica2', '2018-10-20 22:39:00', '2018-10-20 22:39:00'),
(36, 'Tipo2', 'Desiree Delgado', 'Titulo de la publicacion3', '3', '2014-10-10', 'Revista Cientifica', '2018-10-20 22:39:00', '2018-10-20 22:39:00');

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
-- Estructura de tabla para la tabla `dim_trabajos`
--

CREATE TABLE `dim_trabajos` (
  `id` int(11) NOT NULL,
  `codigo` varchar(100) NOT NULL,
  `nombre_empresa` varchar(100) NOT NULL,
  `cargo` varchar(100) NOT NULL,
  `descripcion` varchar(500) NOT NULL,
  `fecha_creacion` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `dim_trabajos`
--

INSERT INTO `dim_trabajos` (`id`, `codigo`, `nombre_empresa`, `cargo`, `descripcion`, `fecha_creacion`, `fecha_actualizacion`) VALUES
(4, '1', 'Intelix', 'Programador web', 'descripcion', '2018-10-24 00:26:30', '2018-10-24 00:26:30'),
(5, '2', 'Promotora Tantalo', 'Programador web', 'descripcion', '2018-10-24 00:26:30', '2018-10-24 00:26:30'),
(6, '3', 'Sofos', 'Programador web', 'descripcion', '2018-10-24 00:26:30', '2018-10-24 00:26:30');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dim_voluntariado`
--

CREATE TABLE `dim_voluntariado` (
  `id` int(11) NOT NULL,
  `codigo` varchar(100) NOT NULL,
  `organizacion` varchar(100) NOT NULL,
  `descripcion` varchar(500) NOT NULL,
  `causa` varchar(300) NOT NULL,
  `fecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `dim_voluntariado`
--

INSERT INTO `dim_voluntariado` (`id`, `codigo`, `organizacion`, `descripcion`, `causa`, `fecha_creacion`, `fecha_actualizacion`) VALUES
(1, '1', 'Organizacion1', 'descripcion', 'una causa ahi', '2018-10-24 00:13:29', '2018-10-24 00:13:29'),
(2, '2', 'Organizacion2', 'descripcion', 'una causa ahi2', '2018-10-24 00:13:29', '2018-10-24 00:13:29'),
(3, '3', 'Organizacion3', 'descripcion', 'una causa ahi2', '2018-10-24 00:13:29', '2018-10-24 00:13:29'),
(4, '4', 'Organizacion4', 'descripcion', 'una causa ahi4', '2018-10-24 13:06:30', '2018-10-24 13:06:30');

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
-- Estructura de tabla para la tabla `fact_docente_facultad`
--

CREATE TABLE `fact_docente_facultad` (
  `id` int(11) NOT NULL,
  `id_docente` int(11) NOT NULL,
  `id_sexo` int(11) NOT NULL,
  `id_grado` int(11) NOT NULL,
  `id_escalafon` int(11) NOT NULL,
  `id_facultad` int(11) DEFAULT NULL,
  `id_nacionalidad` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL DEFAULT '1',
  `fecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `fact_docente_facultad`
--

INSERT INTO `fact_docente_facultad` (`id`, `id_docente`, `id_sexo`, `id_grado`, `id_escalafon`, `id_facultad`, `id_nacionalidad`, `cantidad`, `fecha_creacion`, `fecha_actualizacion`) VALUES
(13, 42, 6, 2, 10, 57, 14, 1, '2018-10-20 22:38:59', '2018-10-22 18:52:37'),
(14, 43, 7, 3, 10, 64, 13, 1, '2018-10-20 22:38:59', '2018-10-22 18:52:37'),
(15, 44, 7, 3, 10, 64, 13, 1, '2018-10-20 22:38:59', '2018-10-22 18:52:37'),
(16, 45, 6, 1, 9, NULL, 13, 1, '2018-10-20 22:46:15', '2018-10-20 22:46:15');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fact_docente_publicacion`
--

CREATE TABLE `fact_docente_publicacion` (
  `id` int(11) NOT NULL,
  `id_docente` int(11) NOT NULL,
  `id_publicacion` int(11) NOT NULL,
  `id_facultad` int(11) NOT NULL,
  `cantidad_citas` int(11) NOT NULL DEFAULT '0',
  `cantidad` int(11) NOT NULL DEFAULT '1',
  `fecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `fact_docente_publicacion`
--

INSERT INTO `fact_docente_publicacion` (`id`, `id_docente`, `id_publicacion`, `id_facultad`, `cantidad_citas`, `cantidad`, `fecha_creacion`, `fecha_actualizacion`) VALUES
(13, 44, 34, 64, 2, 1, '2018-10-20 22:39:00', '2018-10-22 18:52:37'),
(14, 43, 35, 64, 2, 1, '2018-10-20 22:39:00', '2018-10-22 18:52:37'),
(15, 44, 35, 64, 2, 1, '2018-10-20 22:39:01', '2018-10-22 18:52:37'),
(16, 43, 36, 64, 1, 1, '2018-10-20 22:39:01', '2018-10-22 18:52:37');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fact_egresado_certificacion`
--

CREATE TABLE `fact_egresado_certificacion` (
  `id` int(11) NOT NULL,
  `id_egresado` int(11) NOT NULL,
  `id_certificacion` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL DEFAULT '1',
  `fecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `fact_egresado_certificacion`
--

INSERT INTO `fact_egresado_certificacion` (`id`, `id_egresado`, `id_certificacion`, `cantidad`, `fecha_creacion`, `fecha_actualizacion`) VALUES
(19, 27, 28, 1, '2018-10-24 00:42:36', '2018-10-24 00:42:36'),
(20, 28, 29, 1, '2018-10-24 00:42:36', '2018-10-24 00:42:36'),
(21, 28, 30, 1, '2018-10-24 00:42:37', '2018-10-24 00:42:37');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fact_egresado_cursos`
--

CREATE TABLE `fact_egresado_cursos` (
  `id` int(11) NOT NULL,
  `id_egresado` int(11) NOT NULL,
  `id_cursos` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL DEFAULT '1',
  `fecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `fact_egresado_cursos`
--

INSERT INTO `fact_egresado_cursos` (`id`, `id_egresado`, `id_cursos`, `cantidad`, `fecha_creacion`, `fecha_actualizacion`) VALUES
(26, 25, 24, 1, '2018-10-24 00:42:37', '2018-10-24 00:42:37'),
(27, 26, 25, 1, '2018-10-24 00:42:37', '2018-10-24 00:42:37'),
(28, 28, 21, 1, '2018-10-24 00:42:37', '2018-10-24 00:42:37'),
(29, 28, 22, 1, '2018-10-24 00:42:37', '2018-10-24 00:42:37'),
(30, 28, 23, 1, '2018-10-24 00:42:37', '2018-10-24 00:42:37');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fact_egresado_educacion`
--

CREATE TABLE `fact_egresado_educacion` (
  `id` int(11) NOT NULL,
  `id_egresado` int(11) NOT NULL,
  `id_educacion` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL DEFAULT '1',
  `fecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `fact_egresado_educacion`
--

INSERT INTO `fact_egresado_educacion` (`id`, `id_egresado`, `id_educacion`, `cantidad`, `fecha_creacion`, `fecha_actualizacion`) VALUES
(13, 26, 4, 1, '2018-10-24 00:42:37', '2018-10-24 00:42:37'),
(14, 26, 5, 1, '2018-10-24 00:42:37', '2018-10-24 00:42:37'),
(15, 27, 6, 1, '2018-10-24 00:42:37', '2018-10-24 00:42:37');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fact_egresado_estudiosuc`
--

CREATE TABLE `fact_egresado_estudiosuc` (
  `id` int(11) NOT NULL,
  `id_egresado` int(11) DEFAULT NULL,
  `id_estudiosuc` int(11) NOT NULL,
  `id_facultad` int(11) NOT NULL,
  `id_carrera` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL DEFAULT '1',
  `fecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `fact_egresado_estudiosuc`
--

INSERT INTO `fact_egresado_estudiosuc` (`id`, `id_egresado`, `id_estudiosuc`, `id_facultad`, `id_carrera`, `cantidad`, `fecha_creacion`, `fecha_actualizacion`) VALUES
(25, 25, 33, 64, 117, 1, '2018-10-24 00:42:38', '2018-10-24 00:42:38'),
(26, 26, 34, 64, 119, 1, '2018-10-24 00:42:38', '2018-10-24 00:42:38'),
(27, 27, 35, 64, 117, 1, '2018-10-24 00:42:38', '2018-10-24 00:42:38'),
(28, 27, 36, 64, 118, 1, '2018-10-24 00:42:38', '2018-10-24 00:42:38');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fact_egresado_patentes`
--

CREATE TABLE `fact_egresado_patentes` (
  `id` int(11) NOT NULL,
  `id_egresado` int(11) NOT NULL,
  `id_patentes` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL DEFAULT '1',
  `fecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `fact_egresado_patentes`
--

INSERT INTO `fact_egresado_patentes` (`id`, `id_egresado`, `id_patentes`, `cantidad`, `fecha_creacion`, `fecha_actualizacion`) VALUES
(1, 25, 4, 1, '2018-10-24 00:42:39', '2018-10-24 00:42:39'),
(2, 28, 3, 1, '2018-10-24 00:42:39', '2018-10-24 00:42:39');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fact_egresado_trabajos`
--

CREATE TABLE `fact_egresado_trabajos` (
  `id` int(11) NOT NULL,
  `id_egresado` int(11) NOT NULL,
  `id_trabajo` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL DEFAULT '1',
  `fecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `fact_egresado_trabajos`
--

INSERT INTO `fact_egresado_trabajos` (`id`, `id_egresado`, `id_trabajo`, `cantidad`, `fecha_creacion`, `fecha_actualizacion`) VALUES
(1, 26, 6, 0, '2018-10-24 00:42:39', '2018-10-24 00:42:39'),
(2, 28, 4, 0, '2018-10-24 00:42:40', '2018-10-24 00:42:40'),
(3, 28, 5, 0, '2018-10-24 00:42:40', '2018-10-24 00:42:40');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fact_egresado_voluntariado`
--

CREATE TABLE `fact_egresado_voluntariado` (
  `id` int(11) NOT NULL,
  `id_egresado` int(11) NOT NULL,
  `id_voluntariado` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL DEFAULT '1',
  `fecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `fact_egresado_voluntariado`
--

INSERT INTO `fact_egresado_voluntariado` (`id`, `id_egresado`, `id_voluntariado`, `cantidad`, `fecha_creacion`, `fecha_actualizacion`) VALUES
(1, 25, 2, 0, '2018-10-24 00:42:40', '2018-10-24 00:42:40'),
(2, 25, 3, 0, '2018-10-24 00:42:40', '2018-10-24 00:42:40'),
(3, 27, 1, 0, '2018-10-24 00:42:40', '2018-10-24 00:42:40'),
(4, 28, 4, 1, '2018-10-24 13:09:57', '2018-10-24 13:09:57');

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
(21, 167, 64, 119, 7, 13, 1),
(22, 168, 64, 117, 6, 13, 1),
(23, 169, 57, 120, 7, 13, 1);

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
(1, 'CARGA_INICIAL_ACTUALIZACION', 'CARGA_INICIAL_ACTUALIZACION', 'Parametro que toma valores boleanos para la carga inicial (1) y la actualizacion (0, toma la fecha de actualizacion)', '0', '2018-10-18 20:35:32', '2018-10-24 13:09:57'),
(2, 'RUTA_CARGA_ESTUDIANTES', 'RUTA_CARGA_ESTUDIANTES', 'Endpoint o ruta para la carga inicial del modulo de estudiantes', 'http://127.0.0.1:8082/estudiantes', '2018-10-18 20:38:51', '2018-10-20 20:20:36'),
(3, 'RUTA_CARGA_PROFESORES', 'RUTA_CARGA_PROFESORES', 'Endpoint o ruta para la carga inicial del modulo de profesores', 'http://127.0.0.1:8082/profesores', '2018-10-18 20:40:26', '2018-10-20 20:20:54'),
(4, 'RUTA_CARGA_EGRESADOS', 'RUTA_CARGA_EGRESADOS', 'Endpoint o ruta para la carga inicial del modulo de egresados', 'http://127.0.0.1:8082/egresados', '2018-10-18 21:31:21', '2018-10-21 02:05:53');

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
-- Indices de la tabla `dim_certificacion`
--
ALTER TABLE `dim_certificacion`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `codigo` (`codigo`);

--
-- Indices de la tabla `dim_cursos`
--
ALTER TABLE `dim_cursos`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `codigo` (`codigo`);

--
-- Indices de la tabla `dim_docente`
--
ALTER TABLE `dim_docente`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `cedula` (`cedula`);

--
-- Indices de la tabla `dim_educacion`
--
ALTER TABLE `dim_educacion`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `codigo` (`codigo`),
  ADD UNIQUE KEY `codigo_2` (`codigo`);

--
-- Indices de la tabla `dim_egresado`
--
ALTER TABLE `dim_egresado`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre_usuario` (`nombre_usuario`),
  ADD UNIQUE KEY `identificacion` (`identificacion`);

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
-- Indices de la tabla `dim_estudiosuc`
--
ALTER TABLE `dim_estudiosuc`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `codigo` (`codigo`);

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
-- Indices de la tabla `dim_patentes`
--
ALTER TABLE `dim_patentes`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `codigo` (`codigo`);

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
-- Indices de la tabla `dim_trabajos`
--
ALTER TABLE `dim_trabajos`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `codigo` (`codigo`);

--
-- Indices de la tabla `dim_voluntariado`
--
ALTER TABLE `dim_voluntariado`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `codigo` (`codigo`);

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
-- Indices de la tabla `fact_docente_facultad`
--
ALTER TABLE `fact_docente_facultad`
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
-- Indices de la tabla `fact_egresado_certificacion`
--
ALTER TABLE `fact_egresado_certificacion`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_egresado` (`id_egresado`),
  ADD KEY `id_certificacion` (`id_certificacion`);

--
-- Indices de la tabla `fact_egresado_cursos`
--
ALTER TABLE `fact_egresado_cursos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_egresado` (`id_egresado`),
  ADD KEY `id_cursos` (`id_cursos`);

--
-- Indices de la tabla `fact_egresado_educacion`
--
ALTER TABLE `fact_egresado_educacion`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_egresado` (`id_egresado`),
  ADD KEY `id_educacion` (`id_educacion`);

--
-- Indices de la tabla `fact_egresado_estudiosuc`
--
ALTER TABLE `fact_egresado_estudiosuc`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_egresado` (`id_egresado`),
  ADD KEY `id_estudiosuc` (`id_estudiosuc`),
  ADD KEY `id_facultad` (`id_facultad`),
  ADD KEY `id_carrera` (`id_carrera`);

--
-- Indices de la tabla `fact_egresado_patentes`
--
ALTER TABLE `fact_egresado_patentes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_egresado` (`id_egresado`),
  ADD KEY `id_patentes` (`id_patentes`);

--
-- Indices de la tabla `fact_egresado_trabajos`
--
ALTER TABLE `fact_egresado_trabajos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_egresado` (`id_egresado`),
  ADD KEY `id_trabajo` (`id_trabajo`);

--
-- Indices de la tabla `fact_egresado_voluntariado`
--
ALTER TABLE `fact_egresado_voluntariado`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_egresado` (`id_egresado`),
  ADD KEY `id_voluntariado` (`id_voluntariado`);

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
-- AUTO_INCREMENT de la tabla `dim_certificacion`
--
ALTER TABLE `dim_certificacion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT de la tabla `dim_cursos`
--
ALTER TABLE `dim_cursos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT de la tabla `dim_docente`
--
ALTER TABLE `dim_docente`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;

--
-- AUTO_INCREMENT de la tabla `dim_educacion`
--
ALTER TABLE `dim_educacion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `dim_egresado`
--
ALTER TABLE `dim_egresado`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT de la tabla `dim_escalafon`
--
ALTER TABLE `dim_escalafon`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `dim_estudiante`
--
ALTER TABLE `dim_estudiante`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=170;

--
-- AUTO_INCREMENT de la tabla `dim_estudiosuc`
--
ALTER TABLE `dim_estudiosuc`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

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
-- AUTO_INCREMENT de la tabla `dim_patentes`
--
ALTER TABLE `dim_patentes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `dim_publicacion`
--
ALTER TABLE `dim_publicacion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

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
-- AUTO_INCREMENT de la tabla `dim_trabajos`
--
ALTER TABLE `dim_trabajos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `dim_voluntariado`
--
ALTER TABLE `dim_voluntariado`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `fact_asignatura_inscrita`
--
ALTER TABLE `fact_asignatura_inscrita`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `fact_docente_facultad`
--
ALTER TABLE `fact_docente_facultad`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT de la tabla `fact_docente_publicacion`
--
ALTER TABLE `fact_docente_publicacion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT de la tabla `fact_egresado_certificacion`
--
ALTER TABLE `fact_egresado_certificacion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT de la tabla `fact_egresado_cursos`
--
ALTER TABLE `fact_egresado_cursos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT de la tabla `fact_egresado_educacion`
--
ALTER TABLE `fact_egresado_educacion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de la tabla `fact_egresado_estudiosuc`
--
ALTER TABLE `fact_egresado_estudiosuc`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT de la tabla `fact_egresado_patentes`
--
ALTER TABLE `fact_egresado_patentes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `fact_egresado_trabajos`
--
ALTER TABLE `fact_egresado_trabajos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `fact_egresado_voluntariado`
--
ALTER TABLE `fact_egresado_voluntariado`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `fact_estudiante_facultad`
--
ALTER TABLE `fact_estudiante_facultad`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

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
-- Filtros para la tabla `fact_docente_facultad`
--
ALTER TABLE `fact_docente_facultad`
  ADD CONSTRAINT `fact_docente_facultad_ibfk_1` FOREIGN KEY (`id_escalafon`) REFERENCES `dim_escalafon` (`id`),
  ADD CONSTRAINT `fact_docente_facultad_ibfk_2` FOREIGN KEY (`id_facultad`) REFERENCES `dim_facultad` (`id`),
  ADD CONSTRAINT `fact_docente_facultad_ibfk_3` FOREIGN KEY (`id_grado`) REFERENCES `dim_grado` (`id`),
  ADD CONSTRAINT `fact_docente_facultad_ibfk_4` FOREIGN KEY (`id_sexo`) REFERENCES `dim_sexo` (`id`),
  ADD CONSTRAINT `fact_docente_facultad_ibfk_5` FOREIGN KEY (`id_nacionalidad`) REFERENCES `dim_nacionalidad` (`id`),
  ADD CONSTRAINT `fact_docente_facultad_ibfk_6` FOREIGN KEY (`id_docente`) REFERENCES `dim_docente` (`id`);

--
-- Filtros para la tabla `fact_docente_publicacion`
--
ALTER TABLE `fact_docente_publicacion`
  ADD CONSTRAINT `fact_docente_publicacion_ibfk_1` FOREIGN KEY (`id_docente`) REFERENCES `dim_docente` (`id`),
  ADD CONSTRAINT `fact_docente_publicacion_ibfk_2` FOREIGN KEY (`id_facultad`) REFERENCES `dim_facultad` (`id`),
  ADD CONSTRAINT `fact_docente_publicacion_ibfk_3` FOREIGN KEY (`id_publicacion`) REFERENCES `dim_publicacion` (`id`);

--
-- Filtros para la tabla `fact_egresado_certificacion`
--
ALTER TABLE `fact_egresado_certificacion`
  ADD CONSTRAINT `fact_egresado_certificacion_ibfk_1` FOREIGN KEY (`id_egresado`) REFERENCES `dim_egresado` (`id`),
  ADD CONSTRAINT `fact_egresado_certificacion_ibfk_2` FOREIGN KEY (`id_certificacion`) REFERENCES `dim_certificacion` (`id`);

--
-- Filtros para la tabla `fact_egresado_cursos`
--
ALTER TABLE `fact_egresado_cursos`
  ADD CONSTRAINT `fact_egresado_cursos_ibfk_1` FOREIGN KEY (`id_egresado`) REFERENCES `dim_egresado` (`id`),
  ADD CONSTRAINT `fact_egresado_cursos_ibfk_2` FOREIGN KEY (`id_cursos`) REFERENCES `dim_cursos` (`id`);

--
-- Filtros para la tabla `fact_egresado_educacion`
--
ALTER TABLE `fact_egresado_educacion`
  ADD CONSTRAINT `fact_egresado_educacion_ibfk_1` FOREIGN KEY (`id_egresado`) REFERENCES `dim_egresado` (`id`),
  ADD CONSTRAINT `fact_egresado_educacion_ibfk_2` FOREIGN KEY (`id_educacion`) REFERENCES `dim_educacion` (`id`);

--
-- Filtros para la tabla `fact_egresado_estudiosuc`
--
ALTER TABLE `fact_egresado_estudiosuc`
  ADD CONSTRAINT `fact_egresado_estudiosuc_ibfk_1` FOREIGN KEY (`id_facultad`) REFERENCES `dim_facultad` (`id`),
  ADD CONSTRAINT `fact_egresado_estudiosuc_ibfk_2` FOREIGN KEY (`id_estudiosuc`) REFERENCES `dim_estudiosuc` (`id`),
  ADD CONSTRAINT `fact_egresado_estudiosuc_ibfk_3` FOREIGN KEY (`id_carrera`) REFERENCES `dim_carrera` (`id`),
  ADD CONSTRAINT `fact_egresado_estudiosuc_ibfk_4` FOREIGN KEY (`id_egresado`) REFERENCES `dim_egresado` (`id`);

--
-- Filtros para la tabla `fact_egresado_patentes`
--
ALTER TABLE `fact_egresado_patentes`
  ADD CONSTRAINT `fact_egresado_patentes_ibfk_1` FOREIGN KEY (`id_patentes`) REFERENCES `dim_patentes` (`id`),
  ADD CONSTRAINT `fact_egresado_patentes_ibfk_2` FOREIGN KEY (`id_egresado`) REFERENCES `dim_egresado` (`id`);

--
-- Filtros para la tabla `fact_egresado_voluntariado`
--
ALTER TABLE `fact_egresado_voluntariado`
  ADD CONSTRAINT `fact_egresado_voluntariado_ibfk_1` FOREIGN KEY (`id_egresado`) REFERENCES `dim_egresado` (`id`),
  ADD CONSTRAINT `fact_egresado_voluntariado_ibfk_2` FOREIGN KEY (`id_voluntariado`) REFERENCES `dim_voluntariado` (`id`);

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
