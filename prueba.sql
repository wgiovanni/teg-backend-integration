-- phpMyAdmin SQL Dump
-- version 4.8.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 30-10-2018 a las 23:42:44
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
(31, '1', 'Certificacion1', 'descripcion', 'url xxx', '2018-10-29 23:42:32', '2018-10-29 23:42:32'),
(32, '2', 'Certificacion2', 'descripcion', 'url xxx', '2018-10-29 23:42:32', '2018-10-29 23:42:32'),
(33, '3', 'Certificacion3', 'descripcion', 'url certificacion', '2018-10-29 23:42:32', '2018-10-29 23:42:32');

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
(26, '1', 'Programación basica', 'http://platzi.com/programacionbasica', '2018-10-29 23:42:32', '2018-10-29 23:42:32'),
(27, '2', 'Curso basico PHP', 'http://platzi.com/wgiovanni/phpbasico', '2018-10-29 23:42:32', '2018-10-29 23:42:32'),
(28, '3', 'Curso Java', 'http://platzi.com/java', '2018-10-29 23:42:32', '2018-10-29 23:42:32'),
(29, '4', 'Curso Angular', 'http://platzi.com/angular', '2018-10-29 23:42:32', '2018-10-29 23:42:32'),
(30, '5', 'Curso basico PHP', 'http://platzi.com/lgomez/phpbasico', '2018-10-29 23:42:32', '2018-10-29 23:42:32');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dim_discapacidad`
--

CREATE TABLE `dim_discapacidad` (
  `id` int(11) NOT NULL,
  `codigo` varchar(100) NOT NULL,
  `fecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `dim_discapacidad`
--

INSERT INTO `dim_discapacidad` (`id`, `codigo`, `fecha_creacion`, `fecha_actualizacion`) VALUES
(1, 'NO POSEO NINGUNA DISCAPACIDAD', '2018-10-28 16:52:43', '2018-10-28 16:52:43'),
(2, 'SI POSEO DISCAPACIDAD', '2018-10-28 16:52:43', '2018-10-28 16:55:25');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dim_docente`
--

CREATE TABLE `dim_docente` (
  `id` int(11) NOT NULL,
  `cedula` varchar(100) NOT NULL,
  `primer_nombre` varchar(100) NOT NULL,
  `segundo_nombre` varchar(100) NOT NULL,
  `primer_apellido` varchar(100) NOT NULL,
  `segundo_apellido` varchar(100) NOT NULL,
  `correo` varchar(100) NOT NULL,
  `area_de_investigacion` varchar(300) NOT NULL,
  `fecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `fecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `dim_docente`
--

INSERT INTO `dim_docente` (`id`, `cedula`, `primer_nombre`, `segundo_nombre`, `primer_apellido`, `segundo_apellido`, `correo`, `area_de_investigacion`, `fecha_creacion`, `fecha_actualizacion`) VALUES
(156, '11356034', 'Mirella', 'SegundoNombre', 'Herrera', 'Segundoapellido', 'mirella.herrera@gmail.com', 'investigacion', '2018-10-30 19:02:08', '2018-10-30 19:02:08'),
(157, '1515515', 'Dessiree', 'SegundoNombre', 'Delgado', 'Segundoapellido', 'desidelgado@gmail.com', 'investigacion', '2018-10-30 19:02:08', '2018-10-30 19:02:08'),
(158, '545511', 'Marilyn', 'SegundoNombre', 'Guigni', 'Segundoapellido', 'marilyngiugni@gmail.com', 'investigacion', '2018-10-30 19:02:08', '2018-10-30 19:02:08'),
(159, '226555', 'Pero', 'SegundoNombre', 'Linares', 'Segundoapellido', 'pedro@gmail.com', 'investigacion', '2018-10-30 19:02:08', '2018-10-30 19:02:08'),
(160, '123456788', 'Alguien ahi', 'SegundoNombre', 'Alguien ahi', 'Segundoapellido', 'alguienahi@gmail.com', 'investigacion', '2018-10-30 19:02:08', '2018-10-30 19:02:08');

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
(7, '1', 'Instituto1', 'Campo de Estudio1', '2018-10-29 23:42:32', '2018-10-29 23:42:32', 'Titulo1', 'http://urlcertificacion.com'),
(8, '2', 'Instituto2', 'Campo de Estudio2', '2018-10-29 23:42:33', '2018-10-29 23:42:33', 'Titulo2', 'http://urlcertificacion.com'),
(9, '3', 'Instituto3', 'Campo de Estudio3', '2018-10-29 23:42:33', '2018-10-29 23:42:33', 'Titulo3', 'http://urlcertificacion.com');

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
(29, 'gjimenez', 'Genessis', 'De Jesus', 'Jimenez', 'Zea', 'descripcion', 'futbol', 'gjimenez@gmail,com', '04127658802', '2464987', '2018-10-29 23:42:33', '2018-10-29 23:42:33'),
(30, 'lgomez', 'Luis', 'Augusto', 'Gomez', 'No se', 'descripcion', 'metal', 'luisgomez@gmail,com', '04127658802', '756438457', '2018-10-29 23:42:33', '2018-10-29 23:42:33'),
(31, 'wmorillo', 'Winder', 'Jose', 'Morillo', 'No se', 'descripcion', 'programar', 'wmorillo@gmail,com', '746574323', '146498766', '2018-10-29 23:42:33', '2018-10-29 23:42:33'),
(32, 'wgiovanni', 'Wilkel', 'Alejandro', 'Giovanni', 'Perozo', 'descripcion', 'programar', 'wgiovanni@gmail,com', '746574323', '22422883', '2018-10-29 23:42:33', '2018-10-29 23:42:33');

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
(7, '22422883', 'Wilkel', 'Apellido', '1995-05-24', '0412-76558802', '0245-3351406', 'wilkelgiovanni@gmail.com', 'Carabobo', '2018-10-29 23:42:31', '2018-10-29 23:42:31'),
(8, '27855129', 'Ana', 'Sanchez', '1999-09-22', '0241-8481233', '0426-3437317', 'anasanchez@gmail.com', 'Carabobo', '2018-10-29 23:42:31', '2018-10-29 23:42:31'),
(9, '26011707', 'Alba', 'Silva', '1997-03-01', '0241-2051334', '0412-1308522', 'andreadellepere_3@hotmail.com', 'Carabobo', '2018-10-29 23:42:31', '2018-10-29 23:42:31'),
(10, '13381615', 'Luis', 'Servita', '1976-07-07', '02418140120', '04265413615', 'luisservita777@gmail.com', 'Carabobo', '2018-10-29 23:42:31', '2018-10-29 23:42:31'),
(11, '22345243', 'Alejandro2', 'Giovanni2', '1995-05-24', '0215545', '155455515', 'alejandro2@gmail.com', 'Carabobo', '2018-10-29 23:42:31', '2018-10-29 23:42:31'),
(12, '22345223', 'Alejandro', 'Giovanni', '1995-05-24', '0215545', '155455515', 'alejandro@gmail.com', 'Carabobo', '2018-10-29 23:42:31', '2018-10-29 23:42:31');

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
(37, 'Licenciado en Computación', '2018-07-24', 'url...', '1', '2018-10-29 23:42:33', '2018-10-29 23:42:33'),
(38, 'Licenciado en Física', '2018-07-24', 'url...', '2', '2018-10-29 23:42:33', '2018-10-29 23:42:33'),
(39, 'Licenciado en Computación', '2018-07-24', 'url...', '3', '2018-10-29 23:42:33', '2018-10-29 23:42:33'),
(40, 'Licenciado en Química', '2010-07-24', 'url...', '4', '2018-10-29 23:42:33', '2018-10-29 23:42:33');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dim_etnia`
--

CREATE TABLE `dim_etnia` (
  `id` int(11) NOT NULL,
  `codigo` varchar(100) NOT NULL,
  `fecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `dim_etnia`
--

INSERT INTO `dim_etnia` (`id`, `codigo`, `fecha_creacion`, `fecha_actualizacion`) VALUES
(1, 'NO PERTENEZCO A UN PUEBLO INDÍGENA', '2018-10-28 16:52:04', '2018-10-28 16:52:04'),
(2, 'SI PERTENEZCO A UN PUEBLO INDÍGENA', '2018-10-28 16:52:04', '2018-10-28 16:52:04');

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
-- Estructura de tabla para la tabla `dim_nivel`
--

CREATE TABLE `dim_nivel` (
  `id` int(11) NOT NULL,
  `codigo` varchar(100) NOT NULL,
  `fecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `dim_nivel`
--

INSERT INTO `dim_nivel` (`id`, `codigo`, `fecha_creacion`, `fecha_actualizacion`) VALUES
(1, 'Pregrado', '2018-10-30 18:40:38', '2018-10-30 18:40:38'),
(2, 'Postgrado', '2018-10-30 18:40:38', '2018-10-30 18:40:38'),
(3, 'Maestria', '2018-10-30 18:40:52', '2018-10-30 18:40:52'),
(4, 'Doctorado', '2018-10-30 18:40:52', '2018-10-30 18:40:52'),
(5, 'Especializacion', '2018-10-30 18:42:05', '2018-10-30 18:42:05');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dim_otroestudio`
--

CREATE TABLE `dim_otroestudio` (
  `id` int(11) NOT NULL,
  `codigo` varchar(100) NOT NULL,
  `nombre_titulo` varchar(100) NOT NULL,
  `fecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fec` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `dim_otroestudio`
--

INSERT INTO `dim_otroestudio` (`id`, `codigo`, `nombre_titulo`, `fecha_creacion`, `fec`) VALUES
(36, '5', 'Estudio1', '2018-10-30 19:02:08', '2018-10-30 19:02:08'),
(37, '6', 'Estudio2', '2018-10-30 19:02:08', '2018-10-30 19:02:08'),
(38, '7', 'Estudio3', '2018-10-30 19:02:08', '2018-10-30 19:02:08'),
(39, '8', 'Estudio4', '2018-10-30 19:02:08', '2018-10-30 19:02:08'),
(40, '9', 'Estudio5', '2018-10-30 19:02:08', '2018-10-30 19:02:08');

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
(5, '1', 'Patente1', 'Descripcion Patente1', '5151', 'inventor1, inventor2, inventor3', '2018-07-10', 'url', '2018-10-29 23:42:33', '2018-10-29 23:42:33'),
(6, '2', 'Patente2', 'Descripcion Patente1', '987874', 'inventor1, inventor2, inventor3', '2018-07-10', 'url', '2018-10-29 23:42:33', '2018-10-29 23:42:33');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dim_premio`
--

CREATE TABLE `dim_premio` (
  `id` int(11) NOT NULL,
  `codigo` varchar(100) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `fecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `dim_premio`
--

INSERT INTO `dim_premio` (`id`, `codigo`, `nombre`, `fecha_creacion`, `fecha_actualizacion`) VALUES
(26, '7', 'Mejor profesor', '2018-10-30 19:02:08', '2018-10-30 19:02:08'),
(27, '8', 'Mejor Investigador 2016', '2018-10-30 19:02:08', '2018-10-30 19:02:08'),
(28, '9', 'Mejor publicacion 2018', '2018-10-30 19:02:09', '2018-10-30 19:02:09'),
(29, '10', 'Mejor publicacion 2019', '2018-10-30 19:02:09', '2018-10-30 19:02:09');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dim_proyecto`
--

CREATE TABLE `dim_proyecto` (
  `id` int(11) NOT NULL,
  `codigo` varchar(100) NOT NULL,
  `titulo` varchar(100) NOT NULL,
  `fecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `dim_proyecto`
--

INSERT INTO `dim_proyecto` (`id`, `codigo`, `titulo`, `fecha_creacion`, `fecha_actualizacion`) VALUES
(21, '5', 'Proyecto1', '2018-10-30 19:02:09', '2018-10-30 19:02:09'),
(22, '6', 'Proyecto2', '2018-10-30 19:02:09', '2018-10-30 19:02:09'),
(23, '7', 'Proyecto3', '2018-10-30 19:02:09', '2018-10-30 19:02:09'),
(24, '8', 'Proyecto4', '2018-10-30 19:02:09', '2018-10-30 19:02:09');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dim_publicacion`
--

CREATE TABLE `dim_publicacion` (
  `id` int(11) NOT NULL,
  `codigo` varchar(100) NOT NULL,
  `titulo_publicacion` varchar(100) NOT NULL,
  `url_citacion` varchar(300) NOT NULL,
  `url_publicacion` varchar(300) NOT NULL,
  `fecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `dim_publicacion`
--

INSERT INTO `dim_publicacion` (`id`, `codigo`, `titulo_publicacion`, `url_citacion`, `url_publicacion`, `fecha_creacion`, `fecha_actualizacion`) VALUES
(17, '4', 'Titulo de la publicacion2', 'http://dhcvhzvgvgvgvz.com', 'http://aquiseencuentra.com', '2018-10-30 19:02:09', '2018-10-30 19:02:09'),
(18, '5', 'Titulo de la publicacion1', 'http://dhcvhzvgvgvgvz.com', 'http://aquiseencuentra.com', '2018-10-30 19:02:09', '2018-10-30 19:02:09'),
(19, '6', 'Titulo de la publicacion2', 'http://dhcvhzvgvgvgvz.com', 'http://aquiseencuentra.com', '2018-10-30 19:02:09', '2018-10-30 19:02:09'),
(20, '7', 'Titulo de la publicacion3', 'http://dhcvhzvgvgvgvz.com', 'http://aquiseencuentra.com', '2018-10-30 19:02:09', '2018-10-30 19:02:09');

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
(1, 'Activo'),
(2, 'Inactivo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dim_tipo_docente`
--

CREATE TABLE `dim_tipo_docente` (
  `id` int(11) NOT NULL,
  `codigo` varchar(100) NOT NULL,
  `fecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `dim_tipo_docente`
--

INSERT INTO `dim_tipo_docente` (`id`, `codigo`, `fecha_creacion`, `fecha_actualizacion`) VALUES
(4, 'Investigacion', '2018-10-30 02:29:16', '2018-10-30 02:29:16'),
(5, 'Docente', '2018-10-30 02:29:16', '2018-10-30 02:29:16');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dim_tipo_estudiante`
--

CREATE TABLE `dim_tipo_estudiante` (
  `id` int(11) NOT NULL,
  `codigo` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `dim_tipo_estudiante`
--

INSERT INTO `dim_tipo_estudiante` (`id`, `codigo`) VALUES
(2, 'Postgrado'),
(1, 'Pregrado');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dim_titulo`
--

CREATE TABLE `dim_titulo` (
  `id` int(11) NOT NULL,
  `codigo` varchar(100) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `fecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `dim_titulo`
--

INSERT INTO `dim_titulo` (`id`, `codigo`, `nombre`, `fecha_creacion`, `fecha_actualizacion`) VALUES
(13, '3', 'Licenciado en Computacion', '2018-10-30 19:02:09', '2018-10-30 19:02:09'),
(14, '4', 'Ingeniera', '2018-10-30 19:02:09', '2018-10-30 19:02:09'),
(15, '5', 'Licenciado en Computacion', '2018-10-30 19:02:09', '2018-10-30 19:02:09'),
(16, '6', 'Ingeniera', '2018-10-30 19:02:09', '2018-10-30 19:02:09');

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
(7, '1', 'Intelix', 'Programador web', 'descripcion', '2018-10-29 23:42:33', '2018-10-29 23:42:33'),
(8, '2', 'Promotora Tantalo', 'Programador web', 'descripcion', '2018-10-29 23:42:33', '2018-10-29 23:42:33'),
(9, '3', 'Sofos', 'Programador web', 'descripcion', '2018-10-29 23:42:33', '2018-10-29 23:42:33');

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
(5, '1', 'Organizacion1', 'descripcion', 'una causa ahi', '2018-10-29 23:42:33', '2018-10-29 23:42:33'),
(6, '2', 'Organizacion2', 'descripcion', 'una causa ahi2', '2018-10-29 23:42:33', '2018-10-29 23:42:33'),
(7, '3', 'Organizacion3', 'descripcion', 'una causa ahi2', '2018-10-29 23:42:33', '2018-10-29 23:42:33'),
(8, '4', 'Organizacion4', 'descripcion', 'una causa ahi4', '2018-10-29 23:42:33', '2018-10-29 23:42:33');

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
  `id_tipo` int(11) NOT NULL,
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

INSERT INTO `fact_docente_facultad` (`id`, `id_docente`, `id_sexo`, `id_tipo`, `id_escalafon`, `id_facultad`, `id_nacionalidad`, `cantidad`, `fecha_creacion`, `fecha_actualizacion`) VALUES
(106, 156, 7, 4, 10, 64, 13, 1, '2018-10-30 19:02:08', '2018-10-30 19:02:08'),
(107, 157, 7, 4, 10, 64, 13, 1, '2018-10-30 19:02:08', '2018-10-30 19:02:08'),
(108, 158, 7, 4, 9, 64, 13, 1, '2018-10-30 19:02:08', '2018-10-30 19:02:08'),
(109, 159, 6, 4, 9, 57, 14, 1, '2018-10-30 19:02:08', '2018-10-30 19:02:08'),
(110, 160, 7, 4, 7, 62, 14, 1, '2018-10-30 19:02:08', '2018-10-30 19:02:08');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fact_docente_otroestudio`
--

CREATE TABLE `fact_docente_otroestudio` (
  `id` int(11) NOT NULL,
  `id_docente` int(11) NOT NULL,
  `id_otroestudio` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL DEFAULT '1',
  `fecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `fact_docente_otroestudio`
--

INSERT INTO `fact_docente_otroestudio` (`id`, `id_docente`, `id_otroestudio`, `cantidad`, `fecha_creacion`, `fecha_actualizacion`) VALUES
(36, 156, 36, 1, '2018-10-30 19:02:08', '2018-10-30 19:02:08'),
(37, 156, 37, 1, '2018-10-30 19:02:08', '2018-10-30 19:02:08'),
(38, 156, 38, 1, '2018-10-30 19:02:08', '2018-10-30 19:02:08'),
(39, 157, 39, 1, '2018-10-30 19:02:08', '2018-10-30 19:02:08'),
(40, 157, 40, 1, '2018-10-30 19:02:08', '2018-10-30 19:02:08');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fact_docente_premio`
--

CREATE TABLE `fact_docente_premio` (
  `id` int(11) NOT NULL,
  `id_docente` int(11) NOT NULL,
  `id_premio` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL DEFAULT '1',
  `fecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `fact_docente_premio`
--

INSERT INTO `fact_docente_premio` (`id`, `id_docente`, `id_premio`, `cantidad`, `fecha_creacion`, `fecha_actualizacion`) VALUES
(26, 159, 26, 1, '2018-10-30 19:02:08', '2018-10-30 19:02:08'),
(27, 156, 27, 1, '2018-10-30 19:02:08', '2018-10-30 19:02:08'),
(28, 156, 28, 1, '2018-10-30 19:02:09', '2018-10-30 19:02:09'),
(29, 157, 29, 1, '2018-10-30 19:02:09', '2018-10-30 19:02:09');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fact_docente_proyecto`
--

CREATE TABLE `fact_docente_proyecto` (
  `id` int(11) NOT NULL,
  `id_docente` int(11) NOT NULL,
  `id_proyecto` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL DEFAULT '1',
  `fecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `fact_docente_proyecto`
--

INSERT INTO `fact_docente_proyecto` (`id`, `id_docente`, `id_proyecto`, `cantidad`, `fecha_creacion`, `fecha_actualizacion`) VALUES
(21, 158, 21, 1, '2018-10-30 19:02:09', '2018-10-30 19:02:09'),
(22, 158, 22, 1, '2018-10-30 19:02:09', '2018-10-30 19:02:09'),
(23, 156, 23, 1, '2018-10-30 19:02:09', '2018-10-30 19:02:09'),
(24, 159, 24, 1, '2018-10-30 19:02:09', '2018-10-30 19:02:09');

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
(9, 156, 17, 64, 50, 1, '2018-10-30 19:02:09', '2018-10-30 19:02:09'),
(10, 156, 18, 64, 100, 1, '2018-10-30 19:02:09', '2018-10-30 19:02:09'),
(11, 157, 19, 64, 75, 1, '2018-10-30 19:02:09', '2018-10-30 19:02:09'),
(12, 157, 20, 64, 500, 1, '2018-10-30 19:02:09', '2018-10-30 19:02:09');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fact_docente_titulo`
--

CREATE TABLE `fact_docente_titulo` (
  `id` int(11) NOT NULL,
  `id_docente` int(11) NOT NULL,
  `id_titulo` int(11) NOT NULL,
  `id_nivel` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL DEFAULT '1',
  `fecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `fact_docente_titulo`
--

INSERT INTO `fact_docente_titulo` (`id`, `id_docente`, `id_titulo`, `id_nivel`, `cantidad`, `fecha_creacion`, `fecha_actualizacion`) VALUES
(11, 156, 13, 3, 1, '2018-10-30 19:02:09', '2018-10-30 19:02:09'),
(12, 156, 14, 4, 1, '2018-10-30 19:02:09', '2018-10-30 19:02:09'),
(13, 157, 15, 4, 1, '2018-10-30 19:02:09', '2018-10-30 19:02:09'),
(14, 159, 16, 1, 1, '2018-10-30 19:02:09', '2018-10-30 19:02:09');

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
(1, 31, 31, 1, '2018-10-29 23:42:33', '2018-10-29 23:42:33'),
(2, 32, 32, 1, '2018-10-29 23:42:33', '2018-10-29 23:42:33'),
(3, 32, 33, 1, '2018-10-29 23:42:33', '2018-10-29 23:42:33');

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
(1, 29, 29, 1, '2018-10-29 23:42:33', '2018-10-29 23:42:33'),
(2, 30, 30, 1, '2018-10-29 23:42:33', '2018-10-29 23:42:33'),
(3, 32, 26, 1, '2018-10-29 23:42:33', '2018-10-29 23:42:33'),
(4, 32, 27, 1, '2018-10-29 23:42:33', '2018-10-29 23:42:33'),
(5, 32, 28, 1, '2018-10-29 23:42:33', '2018-10-29 23:42:33');

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
(1, 30, 7, 1, '2018-10-29 23:42:33', '2018-10-29 23:42:33'),
(2, 30, 8, 1, '2018-10-29 23:42:33', '2018-10-29 23:42:33'),
(3, 31, 9, 1, '2018-10-29 23:42:33', '2018-10-29 23:42:33');

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
(1, 29, 37, 64, 117, 1, '2018-10-29 23:42:34', '2018-10-29 23:42:34'),
(2, 30, 38, 64, 119, 1, '2018-10-29 23:42:34', '2018-10-29 23:42:34'),
(3, 31, 39, 64, 117, 1, '2018-10-29 23:42:34', '2018-10-29 23:42:34'),
(4, 31, 40, 64, 118, 1, '2018-10-29 23:42:34', '2018-10-29 23:42:34');

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
(1, 29, 6, 1, '2018-10-29 23:42:34', '2018-10-29 23:42:34'),
(2, 32, 5, 1, '2018-10-29 23:42:34', '2018-10-29 23:42:34');

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
(1, 30, 9, 1, '2018-10-29 23:42:34', '2018-10-29 23:42:34'),
(2, 32, 7, 1, '2018-10-29 23:42:35', '2018-10-29 23:42:35'),
(3, 32, 8, 1, '2018-10-29 23:42:35', '2018-10-29 23:42:35');

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
(1, 29, 6, 1, '2018-10-29 23:42:35', '2018-10-29 23:42:35'),
(2, 29, 7, 1, '2018-10-29 23:42:35', '2018-10-29 23:42:35'),
(3, 31, 5, 1, '2018-10-29 23:42:35', '2018-10-29 23:42:35'),
(4, 32, 8, 1, '2018-10-29 23:42:35', '2018-10-29 23:42:35');

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
  `id_status` int(11) NOT NULL,
  `id_discapacidad` int(11) NOT NULL,
  `id_etnia` int(11) NOT NULL,
  `id_tipo` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `fact_estudiante_facultad`
--

INSERT INTO `fact_estudiante_facultad` (`id`, `id_estudiante`, `id_facultad`, `id_carrera`, `id_sexo`, `id_nacionalidad`, `id_status`, `id_discapacidad`, `id_etnia`, `id_tipo`, `cantidad`) VALUES
(7, 7, 64, 117, 6, 13, 1, 1, 1, 1, 1),
(8, 8, 64, 118, 7, 13, 1, 1, 1, 1, 1),
(9, 9, 64, 117, 7, 13, 1, 2, 2, 1, 1),
(10, 10, 64, 119, 7, 13, 2, 1, 1, 2, 1),
(11, 11, 64, 120, 6, 13, 1, 1, 2, 2, 1),
(12, 12, 64, 120, 6, 13, 2, 2, 1, 1, 1);

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
(1, 'CARGA_INICIAL_ACTUALIZACION', 'CARGA_INICIAL_ACTUALIZACION', 'Parametro que toma valores boleanos para la carga inicial (1) y la actualizacion (0, toma la fecha de actualizacion)', '0', '2018-10-18 20:35:32', '2018-10-30 19:02:09'),
(2, 'RUTA_CARGA_ESTUDIANTES', 'RUTA_CARGA_ESTUDIANTES', 'Endpoint o ruta para la carga inicial del modulo de estudiantes', 'http://127.0.0.1:8082/api/v1/estudiantes', '2018-10-18 20:38:51', '2018-10-29 19:06:57'),
(3, 'RUTA_CARGA_PROFESORES', 'RUTA_CARGA_PROFESORES', 'Endpoint o ruta para la carga inicial del modulo de profesores', 'http://127.0.0.1:8082/api/v1/profesores', '2018-10-18 20:40:26', '2018-10-29 00:04:01'),
(4, 'RUTA_CARGA_EGRESADOS', 'RUTA_CARGA_EGRESADOS', 'Endpoint o ruta para la carga inicial del modulo de egresados', 'http://127.0.0.1:8082/api/v1/egresados', '2018-10-18 21:31:21', '2018-10-29 00:04:17'),
(5, 'FECHA_ACTUALIZACION', 'FECHA_ACTUALIZACION', 'Parámetro de fecha que se utilizara para poder llevar el control de la fecha de actualización en cada ejecución del proceso ETL  ', '2018-10-30 15:02:08', '2018-10-28 17:44:52', '2018-10-30 19:02:09');

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
(25, 'prueba', 'prueba', 'prueba', 'prueba@gmail.com', '$pbkdf2-sha256$29000$q7U2JgTgXGstxRhj7H2PEQ$z9T/d86slJ35mzHUfEsvLlm4paJmoihDeizGbyagQx4', 1),
(26, 'Wilkel', 'Giovanni', 'wgiovanni', 'wilkelgiovanni@gmail.com', '$pbkdf2-sha256$29000$ktJ6j9Eaw3hvrVVqLUXo3Q$HuJzneKriNMP/niQb74OJkqSqZ0WUG0VtS9GYUxb8rU', 2);

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
-- Indices de la tabla `dim_discapacidad`
--
ALTER TABLE `dim_discapacidad`
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
-- Indices de la tabla `dim_etnia`
--
ALTER TABLE `dim_etnia`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `codigo` (`codigo`);

--
-- Indices de la tabla `dim_facultad`
--
ALTER TABLE `dim_facultad`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indices de la tabla `dim_nacionalidad`
--
ALTER TABLE `dim_nacionalidad`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `dim_nivel`
--
ALTER TABLE `dim_nivel`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `codigo` (`codigo`);

--
-- Indices de la tabla `dim_otroestudio`
--
ALTER TABLE `dim_otroestudio`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `codigo` (`codigo`);

--
-- Indices de la tabla `dim_patentes`
--
ALTER TABLE `dim_patentes`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `codigo` (`codigo`);

--
-- Indices de la tabla `dim_premio`
--
ALTER TABLE `dim_premio`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `codigo` (`codigo`);

--
-- Indices de la tabla `dim_proyecto`
--
ALTER TABLE `dim_proyecto`
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
-- Indices de la tabla `dim_tipo_docente`
--
ALTER TABLE `dim_tipo_docente`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`codigo`);

--
-- Indices de la tabla `dim_tipo_estudiante`
--
ALTER TABLE `dim_tipo_estudiante`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `codigo` (`codigo`);

--
-- Indices de la tabla `dim_titulo`
--
ALTER TABLE `dim_titulo`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `codigo` (`codigo`);

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
  ADD KEY `id_grado` (`id_tipo`),
  ADD KEY `id_escalafon` (`id_escalafon`),
  ADD KEY `id_facultad` (`id_facultad`),
  ADD KEY `id_nacionalidad` (`id_nacionalidad`);

--
-- Indices de la tabla `fact_docente_otroestudio`
--
ALTER TABLE `fact_docente_otroestudio`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_docente` (`id_docente`),
  ADD KEY `id_otroestudio` (`id_otroestudio`);

--
-- Indices de la tabla `fact_docente_premio`
--
ALTER TABLE `fact_docente_premio`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_docente` (`id_docente`),
  ADD KEY `id_premio` (`id_premio`);

--
-- Indices de la tabla `fact_docente_proyecto`
--
ALTER TABLE `fact_docente_proyecto`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_docente` (`id_docente`),
  ADD KEY `id_proyecto` (`id_proyecto`);

--
-- Indices de la tabla `fact_docente_publicacion`
--
ALTER TABLE `fact_docente_publicacion`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_docente` (`id_docente`),
  ADD KEY `id_publicacion` (`id_publicacion`),
  ADD KEY `id_facultad` (`id_facultad`);

--
-- Indices de la tabla `fact_docente_titulo`
--
ALTER TABLE `fact_docente_titulo`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_docente` (`id_docente`),
  ADD KEY `id_titulo` (`id_titulo`),
  ADD KEY `id_nivel` (`id_nivel`);

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
  ADD KEY `id_nacionalidad` (`id_nacionalidad`),
  ADD KEY `id_status` (`id_status`),
  ADD KEY `id_discapacidad` (`id_discapacidad`),
  ADD KEY `id_etnia` (`id_etnia`),
  ADD KEY `id_tipo` (`id_tipo`);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT de la tabla `dim_cursos`
--
ALTER TABLE `dim_cursos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT de la tabla `dim_discapacidad`
--
ALTER TABLE `dim_discapacidad`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `dim_docente`
--
ALTER TABLE `dim_docente`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=161;

--
-- AUTO_INCREMENT de la tabla `dim_educacion`
--
ALTER TABLE `dim_educacion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `dim_egresado`
--
ALTER TABLE `dim_egresado`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT de la tabla `dim_escalafon`
--
ALTER TABLE `dim_escalafon`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `dim_estudiante`
--
ALTER TABLE `dim_estudiante`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `dim_estudiosuc`
--
ALTER TABLE `dim_estudiosuc`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT de la tabla `dim_etnia`
--
ALTER TABLE `dim_etnia`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `dim_facultad`
--
ALTER TABLE `dim_facultad`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=65;

--
-- AUTO_INCREMENT de la tabla `dim_nacionalidad`
--
ALTER TABLE `dim_nacionalidad`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de la tabla `dim_nivel`
--
ALTER TABLE `dim_nivel`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `dim_otroestudio`
--
ALTER TABLE `dim_otroestudio`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT de la tabla `dim_patentes`
--
ALTER TABLE `dim_patentes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `dim_premio`
--
ALTER TABLE `dim_premio`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT de la tabla `dim_proyecto`
--
ALTER TABLE `dim_proyecto`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT de la tabla `dim_publicacion`
--
ALTER TABLE `dim_publicacion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

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
-- AUTO_INCREMENT de la tabla `dim_tipo_docente`
--
ALTER TABLE `dim_tipo_docente`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `dim_tipo_estudiante`
--
ALTER TABLE `dim_tipo_estudiante`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `dim_titulo`
--
ALTER TABLE `dim_titulo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT de la tabla `dim_trabajos`
--
ALTER TABLE `dim_trabajos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `dim_voluntariado`
--
ALTER TABLE `dim_voluntariado`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `fact_asignatura_inscrita`
--
ALTER TABLE `fact_asignatura_inscrita`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `fact_docente_facultad`
--
ALTER TABLE `fact_docente_facultad`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=111;

--
-- AUTO_INCREMENT de la tabla `fact_docente_otroestudio`
--
ALTER TABLE `fact_docente_otroestudio`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT de la tabla `fact_docente_premio`
--
ALTER TABLE `fact_docente_premio`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT de la tabla `fact_docente_proyecto`
--
ALTER TABLE `fact_docente_proyecto`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT de la tabla `fact_docente_publicacion`
--
ALTER TABLE `fact_docente_publicacion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `fact_docente_titulo`
--
ALTER TABLE `fact_docente_titulo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de la tabla `fact_egresado_certificacion`
--
ALTER TABLE `fact_egresado_certificacion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `fact_egresado_cursos`
--
ALTER TABLE `fact_egresado_cursos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `fact_egresado_educacion`
--
ALTER TABLE `fact_egresado_educacion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `fact_egresado_estudiosuc`
--
ALTER TABLE `fact_egresado_estudiosuc`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `parametro_sistema`
--
ALTER TABLE `parametro_sistema`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

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
  ADD CONSTRAINT `fact_docente_facultad_ibfk_3` FOREIGN KEY (`id_tipo`) REFERENCES `dim_tipo_docente` (`id`),
  ADD CONSTRAINT `fact_docente_facultad_ibfk_4` FOREIGN KEY (`id_sexo`) REFERENCES `dim_sexo` (`id`),
  ADD CONSTRAINT `fact_docente_facultad_ibfk_5` FOREIGN KEY (`id_nacionalidad`) REFERENCES `dim_nacionalidad` (`id`),
  ADD CONSTRAINT `fact_docente_facultad_ibfk_6` FOREIGN KEY (`id_docente`) REFERENCES `dim_docente` (`id`);

--
-- Filtros para la tabla `fact_docente_otroestudio`
--
ALTER TABLE `fact_docente_otroestudio`
  ADD CONSTRAINT `fact_docente_otroestudio_ibfk_1` FOREIGN KEY (`id_docente`) REFERENCES `dim_docente` (`id`),
  ADD CONSTRAINT `fact_docente_otroestudio_ibfk_2` FOREIGN KEY (`id_otroestudio`) REFERENCES `dim_otroestudio` (`id`);

--
-- Filtros para la tabla `fact_docente_premio`
--
ALTER TABLE `fact_docente_premio`
  ADD CONSTRAINT `fact_docente_premio_ibfk_1` FOREIGN KEY (`id_docente`) REFERENCES `dim_docente` (`id`),
  ADD CONSTRAINT `fact_docente_premio_ibfk_2` FOREIGN KEY (`id_premio`) REFERENCES `dim_premio` (`id`);

--
-- Filtros para la tabla `fact_docente_proyecto`
--
ALTER TABLE `fact_docente_proyecto`
  ADD CONSTRAINT `fact_docente_proyecto_ibfk_1` FOREIGN KEY (`id_proyecto`) REFERENCES `dim_proyecto` (`id`),
  ADD CONSTRAINT `fact_docente_proyecto_ibfk_2` FOREIGN KEY (`id_docente`) REFERENCES `dim_docente` (`id`);

--
-- Filtros para la tabla `fact_docente_publicacion`
--
ALTER TABLE `fact_docente_publicacion`
  ADD CONSTRAINT `fact_docente_publicacion_ibfk_1` FOREIGN KEY (`id_docente`) REFERENCES `dim_docente` (`id`),
  ADD CONSTRAINT `fact_docente_publicacion_ibfk_2` FOREIGN KEY (`id_facultad`) REFERENCES `dim_facultad` (`id`),
  ADD CONSTRAINT `fact_docente_publicacion_ibfk_3` FOREIGN KEY (`id_publicacion`) REFERENCES `dim_publicacion` (`id`);

--
-- Filtros para la tabla `fact_docente_titulo`
--
ALTER TABLE `fact_docente_titulo`
  ADD CONSTRAINT `fact_docente_titulo_ibfk_1` FOREIGN KEY (`id_titulo`) REFERENCES `dim_titulo` (`id`),
  ADD CONSTRAINT `fact_docente_titulo_ibfk_2` FOREIGN KEY (`id_docente`) REFERENCES `dim_docente` (`id`),
  ADD CONSTRAINT `fact_docente_titulo_ibfk_3` FOREIGN KEY (`id_nivel`) REFERENCES `dim_nivel` (`id`);

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
  ADD CONSTRAINT `fact_estudiante_facultad_ibfk_5` FOREIGN KEY (`id_sexo`) REFERENCES `dim_sexo` (`id`),
  ADD CONSTRAINT `fact_estudiante_facultad_ibfk_6` FOREIGN KEY (`id_status`) REFERENCES `dim_status` (`id`),
  ADD CONSTRAINT `fact_estudiante_facultad_ibfk_7` FOREIGN KEY (`id_etnia`) REFERENCES `dim_etnia` (`id`),
  ADD CONSTRAINT `fact_estudiante_facultad_ibfk_8` FOREIGN KEY (`id_discapacidad`) REFERENCES `dim_discapacidad` (`id`),
  ADD CONSTRAINT `fact_estudiante_facultad_ibfk_9` FOREIGN KEY (`id_tipo`) REFERENCES `dim_tipo_estudiante` (`id`);

--
-- Filtros para la tabla `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `user_ibfk_1` FOREIGN KEY (`id_role`) REFERENCES `role` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
