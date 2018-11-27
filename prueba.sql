-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 27-11-2018 a las 04:55:42
-- Versión del servidor: 10.1.36-MariaDB
-- Versión de PHP: 7.2.11

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
-- Estructura de tabla para la tabla `dim_carrera`
--

CREATE TABLE `dim_carrera` (
  `id` int(11) NOT NULL,
  `codigo` varchar(100) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `dim_carrera`
--

INSERT INTO `dim_carrera` (`id`, `codigo`, `nombre`, `created_date`, `updated_date`) VALUES
(117, 'COMPUTACION', 'COMPUTACION', '2018-10-18 21:28:47', '2018-11-26 23:41:59'),
(118, 'QUIMICA', 'QUIMICA', '2018-10-18 21:28:47', '2018-11-26 23:41:59'),
(119, 'FISICA', 'FISICA', '2018-10-18 21:28:47', '2018-11-26 23:41:59'),
(120, 'MATEMATICA', 'MATEMATICA', '2018-10-18 21:28:47', '2018-11-26 23:41:59'),
(121, 'BIOLOGIA', 'BIOLOGIA', '2018-10-18 21:28:47', '2018-11-26 23:41:59'),
(122, 'MAESTRiA EN MATEMATICAS APLICADAS', 'Maestría en Matemáticas Aplicadas', '2018-11-13 19:42:03', '2018-11-13 19:42:03'),
(123, 'DOCTORADO EN QUIMICA TECNOLOGICA', 'Doctorado en Química Tecnológica', '2018-11-13 19:42:03', '2018-11-13 19:42:03'),
(124, 'ESPECIALIZACION EN DESARROLLO DE SOFTWARE', 'ESPECIALIZACION EN DESARROLLO DE SOFTWARE', '2018-11-13 19:42:44', '2018-11-26 23:41:59'),
(125, 'DERECHO', 'DERECHO', '2018-11-13 19:42:44', '2018-11-26 23:41:59'),
(126, 'CIENCIA FISCALES', 'Ciencia Fiscales', '2018-11-13 19:43:27', '2018-11-13 19:43:27'),
(127, 'ESTUDIOS POLITICOS', 'Estudios Políticos', '2018-11-13 19:43:27', '2018-11-13 19:43:27'),
(128, 'CRIMINOLOGICAS', 'Cronológicas', '2018-11-13 19:44:06', '2018-11-13 19:44:06'),
(129, 'MAESTRIA EN CIENCIAS POLITICAS Y ADMINISTRACION PUBLICA', 'Maestría en Ciencias Políticas y Administración Publica', '2018-11-13 19:46:01', '2018-11-13 19:46:01'),
(130, 'ESPECIALIZACION EN DERECHO PENAL', 'Especialización en Derecho Penal', '2018-11-13 19:46:01', '2018-11-13 19:46:01'),
(131, 'ESPECIALIZACION EN GERENCIA PUBLICA', 'Especialización en Gerencia Pública', '2018-11-13 19:47:30', '2018-11-13 19:47:30'),
(132, 'ESPECIALIZACION EN CRIMINALISTICA', 'Especialización en Criminalistica', '2018-11-13 19:47:30', '2018-11-13 19:47:30'),
(133, 'ESPECIALIZACION EN DERECHO MERCANTIL', 'Especialización en Derecho Mercantil', '2018-11-13 19:48:20', '2018-11-13 19:48:20'),
(134, 'IDIOMAS', 'Idiomas', '2018-11-13 19:48:20', '2018-11-13 19:48:20'),
(135, 'ODONTOLOGIA', 'Odontología', '2018-11-13 19:49:41', '2018-11-13 19:49:41'),
(136, 'ESPECIALISTA EN CIRUGIA BUCAL Y MAXILOFACIAL', 'Especialista en Cirugía Bucal y Maxilofacial', '2018-11-13 19:49:41', '2018-11-13 19:49:41'),
(137, 'ESPECIALISTA EN ODONTOPEDIATRIA', 'Especialista en Odontopediatría', '2018-11-13 19:51:47', '2018-11-13 19:51:47'),
(138, 'ESPECIALISTA EN ENDODONCIA', 'Especialista en Endodoncia', '2018-11-13 19:51:47', '2018-11-13 19:51:47'),
(139, 'ESPECIALISTA EN ORTOPEDIA DENTOFACIAL Y ORTODONCIA', 'Especialista en Ortopedia Dentofacial y Ortodoncia', '2018-11-13 19:53:34', '2018-11-13 19:53:34'),
(140, 'INGENIERIA DE TELECOMUNICACIONES', 'Ingeniería de Telecomunicaciones', '2018-11-13 19:53:34', '2018-11-13 19:53:34'),
(141, 'INGENIERIA CIVIL', 'Ingeniería Civil', '2018-11-13 19:54:23', '2018-11-13 19:54:23'),
(142, 'INGENIERIA ELECTRICA', 'Ingeniería Eléctrica', '2018-11-13 19:54:23', '2018-11-13 19:54:23'),
(143, 'INGENIERIA INDUSTRIAL', 'Ingeniería Industrial', '2018-11-13 19:55:24', '2018-11-13 19:55:24'),
(144, 'INGENIERIA MECANICA', 'Ingeniería Mecánica', '2018-11-13 19:55:24', '2018-11-13 19:55:24'),
(145, 'INGENIERIA QUIMICA', 'Ingeniería Química', '2018-11-13 19:56:31', '2018-11-13 19:56:31'),
(146, 'ESPECIALIZACION EN CALIDAD Y PRODUCTIVIDAD', 'Especialización en Calidad y Productividad', '2018-11-13 19:56:31', '2018-11-13 19:56:31'),
(147, 'ESPECIALIZACION EN GERENCIA DE SERVICIOS AUTOMOTRICES', 'Especialización en General de Servicios Automotrices ', '2018-11-13 19:57:53', '2018-11-13 19:57:53'),
(148, 'ESPECIALIZACION EN MANTENIMIENTO INDUSTRIAL', 'Especialización en Mantenimiento Industrial', '2018-11-13 19:57:53', '2018-11-13 19:57:53'),
(149, 'ESPECIALIZACION EN SISTEMAS TERMICOS', 'Especialización en Sistemas Térmicos', '2018-11-13 19:59:19', '2018-11-13 19:59:19'),
(150, 'MAESTRIA EN INGENIERIA INDUSTRIAL', 'Maestría en Ingeniería Industrial', '2018-11-13 19:59:19', '2018-11-13 19:59:19'),
(151, 'MAESTRIA EN INGENIERIA ELECTRICA', 'Maestría en Ingeniería Eléctrica', '2018-11-13 20:00:27', '2018-11-13 20:00:27'),
(152, 'MAESTRIA EN INGENIERIA MECANICA', 'Maestría en Ingeniería Mecánica', '2018-11-13 20:00:27', '2018-11-13 20:00:27'),
(153, 'MAESTRIA EN INGENIERIA PROCESOS', 'Maestría en Ingeniería Procesos', '2018-11-13 20:01:19', '2018-11-13 20:01:19'),
(154, 'MAESTRIA EN INGENIERIA AMBIENTAL', 'Maestría en Ingeniería Ambiental', '2018-11-13 20:01:19', '2018-11-13 20:01:19'),
(155, 'MAESTRIA EN INGENIERIA EN MATEMATICA Y COMPUTACION', 'Maestría en Ingeniería en Matemática y Computación ', '2018-11-13 20:04:40', '2018-11-13 20:04:40'),
(156, 'MAESTRIA EN INGENIERIA EN GERENCIA DE CONSTRUCCION', 'Maestría en Ingeniería en Gerencia de Construcción ', '2018-11-13 20:04:40', '2018-11-13 20:04:40'),
(157, 'DOCTORADO EN INGENIERIA AREA AMBIENTE', 'Doctorado en Ingeniería Área Ambiente', '2018-11-13 20:04:40', '2018-11-13 20:04:40'),
(158, 'DOCTORADO EN INGENIERIA AREA BIOINGENIERIA', 'Doctorado en Ingeniería Área Bioingeniería ', '2018-11-13 20:04:40', '2018-11-13 20:04:40'),
(159, 'DOCTORADO EN INGENIERIA AREA ELECTRICA', 'Doctorado en Ingeniería Área Eléctrica', '2018-11-13 20:06:32', '2018-11-13 20:06:32'),
(160, 'DOCTORADO EN INGENIERIA AREA QUIMICA', 'Doctorado en Ingeniería Área Química', '2018-11-13 20:06:32', '2018-11-13 20:06:32'),
(161, 'DOCTORADO EN INGENIERIA AREA COMPUTO APLICADO', 'Doctorado en Ingeniería Área Computo Aplicado', '2018-11-13 20:06:32', '2018-11-13 20:06:32'),
(162, 'MEDICINA', 'MEDICINA', '2018-11-13 20:06:32', '2018-11-26 23:41:59'),
(163, 'BIOANALISIS', 'BIOANALISIS', '2018-11-13 20:11:10', '2018-11-26 23:41:59'),
(164, 'ENFERMERIA', 'Enfermería ', '2018-11-13 20:11:10', '2018-11-13 20:11:10'),
(165, 'CIENCIAS BIOMEDICAS Y TECNOLOGICAS', 'Ciencias Biomedicas y Tecnológicas ', '2018-11-13 20:11:10', '2018-11-13 20:11:10'),
(166, 'SALUD PUBLICA Y DESARROLLO SOCIAL', 'Salud Pública y Desarrollo Social', '2018-11-13 20:11:10', '2018-11-13 20:11:10'),
(167, 'ENFERMERIA EN CUIDADO CRITICO DEL ADULTO', 'Enfermería en Cuidado Crítico del Adulto', '2018-11-13 20:11:10', '2018-11-13 20:11:10'),
(168, 'ENFERMERIA EN GERIATRIA Y GERONTOLOGIA', 'ENFERMERIA EN GERIATRIA Y GERONTOLOGIA', '2018-11-13 20:11:10', '2018-11-26 23:41:59'),
(169, 'ENFERMERIA EN SALUD REPRODUCTIVA', 'Enfermería en Salud Reproductiva', '2018-11-13 20:11:10', '2018-11-13 20:11:10'),
(170, 'EDUCACION, MENCION ARTES PLASTICAS', 'EDUCACION, MENCION ARTES PLASTICAS', '2018-11-13 20:24:30', '2018-11-27 02:08:48'),
(171, 'EDUCACION, MENCION BIOLOGIA', 'Educación, Mención Biología', '2018-11-13 20:24:30', '2018-11-13 20:24:30'),
(172, 'EDUCACION, MENCION CIENCIAS SOCIALES', 'Educación, Mención Ciencias Sociales', '2018-11-13 20:24:30', '2018-11-13 20:24:30'),
(173, 'EDUCACION FISICA, DEPORTES Y RECREACION', 'Educación Física, Deportes y Recreación', '2018-11-13 20:24:30', '2018-11-13 20:24:30'),
(174, 'EDUCACION PREESCOLAR', 'Educación Preescolar', '2018-11-13 20:24:30', '2018-11-13 20:24:30'),
(175, 'EDUCACION INTEGRAL', 'EDUCACION INTEGRAL', '2018-11-13 20:24:30', '2018-11-27 02:08:48'),
(176, 'EDUCACION MUSICAL', 'Educación Musical', '2018-11-13 20:31:04', '2018-11-13 20:31:04'),
(177, 'EDUCACION PARA EL TRABAJO', 'Educación para el trabajo', '2018-11-13 20:31:04', '2018-11-13 20:31:04'),
(178, 'EDUCACION, MENCION FISICA', 'Educación, Mención Física', '2018-11-13 20:31:04', '2018-11-13 20:31:04'),
(179, 'EDUCACION, MENCION FRANCES', 'EDUCACION, MENCION FRANCES', '2018-11-13 20:31:04', '2018-11-27 02:08:48'),
(180, 'EDUCACION, MENCION INFORMATICA', 'Educación, Mención Informática', '2018-11-13 20:31:04', '2018-11-13 20:31:04'),
(181, 'EDUCACION, MENCION INGLES', 'Educación, Mención Ingles', '2018-11-13 20:31:04', '2018-11-13 20:31:04'),
(182, 'EDUCACION, MENCION LENGUA Y LITERATURA', 'Educación, Mención Lengua y Literatura', '2018-11-13 20:31:04', '2018-11-13 20:31:04'),
(183, 'EDUCACION, MENCION MATEMATICA', 'Educación, Mención Matemática ', '2018-11-13 20:31:04', '2018-11-13 20:31:04'),
(184, 'EDUCACION, MENCION ORIENTACION', 'Educación, Mención Orientación', '2018-11-13 20:31:04', '2018-11-13 20:31:04'),
(185, 'EDUCACION, MENCION QUIMICA', 'Educación, Mención Química', '2018-11-13 20:31:04', '2018-11-13 20:31:04'),
(186, 'ESPECIALIZACION EN DOCENCIA PARA LA EDUCACION SUPERIOR', 'Especialización en Docencia para la Educación Superior', '2018-11-13 20:31:04', '2018-11-13 20:31:04'),
(187, 'ESPECIALIZACION EN TECNOLOGIA DE LA EDUCACION', 'Especialización en Tecnología de la Educación', '2018-11-13 20:31:04', '2018-11-13 20:31:04'),
(188, 'ESPECIALIZACION EN ENSEÑANZA EN LA GEOGRAFIA NACIONAL', 'Especialización en Enseñanza en la Geografía Nacional', '2018-11-13 20:31:04', '2018-11-13 20:31:04'),
(189, 'ESPECIALIZACION EN DINAMICA DE GRUPO', 'Especialización en Dinámica de Grupo', '2018-11-13 20:31:04', '2018-11-13 20:31:04'),
(190, 'ESPECIALIZACION EN LA ENSEÑANZA DEL INGLES COMO LENGUA EXTRANJERA', 'Especialización en la Enseñanza del Ingles como Lengua Extranjera', '2018-11-13 20:31:04', '2018-11-13 20:31:04'),
(191, 'ECONOMIA', 'Economía', '2018-11-13 20:35:40', '2018-11-13 20:35:40'),
(192, 'ADMINISTRACION COMERCIAL', 'Administración Comercial', '2018-11-13 20:35:40', '2018-11-13 20:35:40'),
(193, 'CONTADURIA PUBLICA', 'Contaduría Publica', '2018-11-13 20:35:40', '2018-11-13 20:35:40'),
(194, 'RELACIONES INDUSTRIALES', 'Relaciones Industriales', '2018-11-13 20:35:40', '2018-11-13 20:35:40'),
(195, 'ESPECIALIZACION EN GERENCIA TRIBUTARIA', 'Especialización en Gerencia Tributaria', '2018-11-13 20:35:40', '2018-11-13 20:35:40'),
(196, 'ESPECIALIZACION EN MERCADEO', 'Especialización en Mercadeo', '2018-11-13 20:35:40', '2018-11-13 20:35:40'),
(197, 'ESPECIALIZACION EN PROTECCION INDUSTRIAL', 'Especialización en Protección Industrial', '2018-11-13 20:35:40', '2018-11-13 20:35:40'),
(198, 'ESPECIALIZACION EN GERENCIA DE CALIDAD Y PRODUCTIVIDAD', 'Especialización en Gerencia de Calidad y Productividad', '2018-11-13 20:35:40', '2018-11-13 20:35:40'),
(199, 'ESPECIALIZACION EN GERENCIA DE RECURSOS HUMANOS', 'Especialización en Gerencia de Recursos', '2018-11-13 20:35:40', '2018-11-13 20:35:40');

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
(3, 'SI POSEO DISCAPACIDAD', '2018-11-27 00:09:16', '2018-11-27 00:09:16'),
(4, 'NO POSEO NINGUNA DISCAPACIDAD', '2018-11-27 00:09:16', '2018-11-27 00:09:16');

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
(285, '11356034', 'Mirella', 'Segundo', 'Herrera', 'Segundo', 'mirella.herrera@gmail.com', 'investigacion', '2018-11-27 03:14:37', '2018-11-27 03:14:37'),
(286, '1515515', 'Dessiree', 'SegundoNombre', 'Delgado', 'Segundoapellido', 'desidelgado@gmail.com', 'investigacion', '2018-11-27 03:14:37', '2018-11-27 03:14:37'),
(287, '545511', 'Marilyn', 'SegundoNombre', 'Guigni', 'Segundoapellido', 'marilyngiugni@gmail.com', 'investigacion', '2018-11-27 03:14:37', '2018-11-27 03:14:37'),
(288, '226555', 'Pedro', 'SegundoNombre', 'Linares', 'Segundoapellido', 'pedro@gmail.com', 'investigacion', '2018-11-27 03:14:37', '2018-11-27 03:14:37'),
(289, '123456788', 'Alguien ahi', 'SegundoNombre', 'Alguien ahi', 'Segundoapellido', 'alguienahi@gmail.com', 'investigacion', '2018-11-27 03:14:37', '2018-11-27 03:14:37'),
(290, '65', 'Afddgd', 'SegundoNombre', 'Adfgdi', 'Segundoapellido', 'alguienahi@gmail.com', 'derecho penal', '2018-11-27 03:14:37', '2018-11-27 03:14:37');

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
(19, '22422883', 'Wilkel', 'Apellido', '1995-05-24', '0412-76558802', '0245-3351406', 'wilkelgiovanni@gmail.com', 'Carabobo', '2018-11-27 00:54:04', '2018-11-27 00:54:04'),
(20, '27855129', 'Ana', 'Sanchez', '1999-09-22', '0241-8481233', '0426-3437317', 'anasanchez@gmail.com', 'Carabobo', '2018-11-27 00:54:04', '2018-11-27 00:54:04'),
(21, '26011707', 'Alba', 'Silva', '1997-03-01', '0241-2051334', '0412-1308522', 'andreadellepere_3@hotmail.com', 'Carabobo', '2018-11-27 00:54:04', '2018-11-27 00:54:04'),
(22, '13381615', 'Luis', 'Servita', '1976-07-07', '02418140120', '04265413615', 'luisservita777@gmail.com', 'Carabobo', '2018-11-27 00:54:04', '2018-11-27 00:54:04'),
(23, '22345243', 'Alejandro2', 'Giovanni2', '1995-05-24', '0215545', '155455515', 'alejandro2@gmail.com', 'Carabobo', '2018-11-27 00:54:04', '2018-11-27 00:54:04'),
(24, '22345223', 'Alejandro', 'Giovanni', '1995-05-24', '0215545', '155455515', 'alejandro@gmail.com', 'Carabobo', '2018-11-27 00:54:04', '2018-11-27 00:54:04'),
(25, '123456789', 'Alejandro', 'Giovanni', '1995-05-24', '0215545', '155455515', 'alejandro@gmail.com', 'Carabobo', '2018-11-27 00:54:04', '2018-11-27 00:54:04'),
(26, '0983653', 'Alejandro', 'Giovanni', '1995-05-24', '0215545', '155455515', 'alejandro@gmail.com', 'Carabobo', '2018-11-27 00:54:04', '2018-11-27 00:54:04'),
(27, '32424', 'Alejandro', 'Giovanni', '1995-05-24', '0215545', '155455515', 'alejandro@gmail.com', 'Carabobo', '2018-11-27 00:54:04', '2018-11-27 00:54:04'),
(28, '3245959524', 'Alejandro', 'Giovanni', '1995-05-24', '0215545', '155455515', 'alejandro@gmail.com', 'Carabobo', '2018-11-27 00:54:04', '2018-11-27 00:54:04'),
(29, '12', 'jose', 'dsd', '1995-05-24', '0215545', '322', 'alejandro@gmail.com', 'Carabobo', '2018-11-27 00:54:04', '2018-11-27 00:54:04'),
(30, '22', 'jose', 'dsd', '1995-05-24', '0215545', '322', 'alejandro@gmail.com', 'Carabobo', '2018-11-27 01:58:51', '2018-11-27 01:58:51'),
(31, '24', 'jose', 'dsd', '1995-05-24', '0215545', '322', 'alejandro@gmail.com', 'Carabobo', '2018-11-27 02:08:49', '2018-11-27 02:08:49'),
(32, '25', 'jose', 'dsd', '1995-05-24', '0215545', '322', 'alejandro@gmail.com', 'Carabobo', '2018-11-27 02:08:49', '2018-11-27 02:08:49'),
(33, '26', 'juan', 'dsd', '1995-05-24', '0215545', '322', 'alejandro@gmail.com', 'Carabobo', '2018-11-27 02:08:49', '2018-11-27 02:08:49');

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
  `codigo` varchar(100) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `dim_facultad`
--

INSERT INTO `dim_facultad` (`id`, `codigo`, `nombre`, `created_date`, `updated_date`) VALUES
(57, 'INGENIERIA', 'Ingeniería', '2018-10-18 19:46:57', '2018-11-10 01:44:39'),
(58, 'FCJP', 'Ciencias Jurídicas y Políticas', '2018-10-18 19:46:57', '2018-11-10 01:44:30'),
(59, 'FCS', 'Ciencias de la Salud', '2018-10-18 19:46:57', '2018-11-10 01:44:50'),
(60, 'FACES', 'Ciencias Económicas y Sociales', '2018-10-18 19:46:57', '2018-11-10 01:45:11'),
(61, 'FACE', 'Ciencias de la Educación', '2018-10-18 19:46:57', '2018-11-10 01:45:03'),
(62, 'ODONTOLOGIA', 'Odontología', '2018-10-18 19:46:57', '2018-11-10 01:44:17'),
(64, 'FACYT', 'Ciencias y Tecnología', '2018-10-18 19:46:57', '2018-11-10 01:43:57');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dim_genero`
--

CREATE TABLE `dim_genero` (
  `id` int(11) NOT NULL,
  `codigo` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `dim_genero`
--

INSERT INTO `dim_genero` (`id`, `codigo`) VALUES
(7, 'Femenino'),
(6, 'Masculino');

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
  `fecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

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
(40, '4', 'Titulo de la publicacion2', 'http://dhcvhzvgvgvgvz.com', 'http://aquiseencuentra.com', '2018-11-27 03:20:21', '2018-11-27 03:20:21'),
(41, '6', 'Titulo de la publicacion2', 'http://dhcvhzvgvgvgvz.com', 'http://aquiseencuentra.com', '2018-11-27 03:20:21', '2018-11-27 03:20:21'),
(42, '7', 'Titulo de la publicacion3', 'http://dhcvhzvgvgvgvz.com', 'http://aquiseencuentra.com', '2018-11-27 03:20:21', '2018-11-27 03:20:21'),
(43, '8', 'Titulo de la publicacion4', 'http://dhcvhzvgvgvgvz.com', 'http://aquiseencuentra.com', '2018-11-27 03:20:21', '2018-11-27 03:20:21'),
(44, '9', 'Titulo de la publicacion5', 'http://dhcvhzvgvgvgvz.com', 'http://aquiseencuentra.com', '2018-11-27 03:20:21', '2018-11-27 03:20:21'),
(45, '10', 'Titulo de la publicacion6', 'http://dhcvhzvgvgvgvz.com', 'http://aquiseencuentra.com', '2018-11-27 03:20:21', '2018-11-27 03:20:21');

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
(2, 'Inactivo'),
(3, 'Active'),
(4, 'Inactivo'),
(5, 'Active'),
(6, 'Inactivo'),
(7, 'Active'),
(8, 'Inactivo'),
(9, 'Active'),
(10, 'Inactivo'),
(11, 'Active'),
(12, 'Inactivo'),
(13, 'Active'),
(14, 'Inactivo'),
(15, 'Active'),
(16, 'Inactivo'),
(17, 'Active'),
(18, 'Inactivo'),
(19, 'Active'),
(20, 'Inactivo'),
(21, 'Active'),
(22, 'Inactivo'),
(23, 'Active'),
(24, 'Inactivo'),
(25, 'Active'),
(26, 'Inactivo'),
(27, 'Active'),
(28, 'Inactivo'),
(29, 'Active'),
(30, 'Inactivo'),
(31, 'Active'),
(32, 'Inactivo'),
(33, 'Active'),
(34, 'Inactivo'),
(35, 'Active'),
(36, 'Inactivo'),
(37, 'Active'),
(38, 'Inactivo'),
(39, 'Active'),
(40, 'Inactivo'),
(41, 'Active'),
(42, 'Inactivo'),
(43, 'Active'),
(44, 'Inactivo'),
(45, 'Active'),
(46, 'Inactivo'),
(47, 'Active'),
(48, 'Inactivo'),
(49, 'Active'),
(50, 'Inactivo'),
(51, 'Active'),
(52, 'Inactivo'),
(53, 'Active'),
(54, 'Inactivo'),
(55, 'Active'),
(56, 'Inactivo'),
(57, 'Active'),
(58, 'Inactivo'),
(59, 'Active'),
(60, 'Inactivo'),
(61, 'Active'),
(62, 'Inactivo'),
(63, 'Active'),
(64, 'Inactivo'),
(65, 'Active'),
(66, 'Inactivo'),
(67, 'Active'),
(68, 'Inactivo'),
(69, 'Active'),
(70, 'Inactivo'),
(71, 'Active'),
(72, 'Inactivo'),
(73, 'Active'),
(74, 'Inactivo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dim_tiempo`
--

CREATE TABLE `dim_tiempo` (
  `id` int(11) NOT NULL,
  `codigo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `dim_tiempo`
--

INSERT INTO `dim_tiempo` (`id`, `codigo`) VALUES
(324, 1892),
(325, 1893),
(326, 1894),
(327, 1895),
(328, 1896),
(329, 1897),
(330, 1898),
(331, 1899),
(332, 1900),
(333, 1901),
(334, 1902),
(335, 1903),
(336, 1904),
(337, 1905),
(338, 1906),
(339, 1907),
(340, 1908),
(341, 1909),
(342, 1910),
(343, 1911),
(344, 1912),
(345, 1913),
(346, 1914),
(347, 1915),
(348, 1916),
(349, 1917),
(350, 1918),
(351, 1919),
(352, 1920),
(353, 1921),
(354, 1922),
(355, 1923),
(356, 1924),
(357, 1925),
(358, 1926),
(359, 1927),
(360, 1928),
(361, 1929),
(362, 1930),
(363, 1931),
(364, 1932),
(365, 1933),
(366, 1934),
(367, 1935),
(368, 1936),
(369, 1937),
(370, 1938),
(371, 1939),
(372, 1940),
(373, 1941),
(374, 1942),
(375, 1943),
(376, 1944),
(377, 1945),
(378, 1946),
(379, 1947),
(380, 1948),
(381, 1949),
(382, 1950),
(383, 1951),
(384, 1952),
(385, 1953),
(386, 1954),
(387, 1955),
(388, 1956),
(389, 1957),
(390, 1958),
(391, 1959),
(392, 1960),
(393, 1961),
(394, 1962),
(395, 1963),
(396, 1964),
(397, 1965),
(398, 1966),
(399, 1967),
(400, 1968),
(401, 1969),
(402, 1970),
(403, 1971),
(404, 1972),
(405, 1973),
(406, 1974),
(407, 1975),
(408, 1976),
(409, 1977),
(410, 1978),
(411, 1979),
(412, 1980),
(413, 1981),
(414, 1982),
(415, 1983),
(416, 1984),
(417, 1985),
(418, 1986),
(419, 1987),
(420, 1988),
(421, 1989),
(422, 1990),
(423, 1991),
(424, 1992),
(425, 1993),
(426, 1994),
(427, 1995),
(428, 1996),
(429, 1997),
(430, 1998),
(431, 1999),
(432, 2000),
(433, 2001),
(434, 2002),
(435, 2003),
(436, 2004),
(437, 2005),
(438, 2006),
(439, 2007),
(440, 2008),
(441, 2009),
(442, 2010),
(443, 2011),
(444, 2012),
(445, 2013),
(446, 2014),
(447, 2015),
(448, 2016),
(449, 2017),
(450, 2018),
(451, 2019),
(452, 2020),
(453, 2021),
(454, 2022),
(455, 2023),
(456, 2024),
(457, 2025),
(458, 2026),
(459, 2027),
(460, 2028),
(461, 2029),
(462, 2030),
(463, 2031),
(464, 2032),
(465, 2033),
(466, 2034),
(467, 2035),
(468, 2036),
(469, 2037),
(470, 2038),
(471, 2039),
(472, 2040),
(473, 2041),
(474, 2042),
(475, 2043),
(476, 2044),
(477, 2045),
(478, 2046),
(479, 2047),
(480, 2048),
(481, 2049);

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
(4, 'Investigador', '2018-10-30 02:29:16', '2018-11-10 02:21:41'),
(5, 'Contratado', '2018-10-30 02:29:16', '2018-11-10 02:21:50'),
(6, 'Normal', '2018-11-09 19:02:43', '2018-11-09 19:02:43');

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
(27, '3', 'Licenciado en Computacion', '2018-11-27 03:46:28', '2018-11-27 03:46:28'),
(28, '4', 'Ingeniera', '2018-11-27 03:46:28', '2018-11-27 03:46:28'),
(29, '5', 'Licenciado en Computacion', '2018-11-27 03:46:28', '2018-11-27 03:46:28'),
(30, '6', 'Ingeniera', '2018-11-27 03:46:28', '2018-11-27 03:46:28');

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
-- Estructura de tabla para la tabla `fact_docente_facultad`
--

CREATE TABLE `fact_docente_facultad` (
  `id` int(11) NOT NULL,
  `id_docente` int(11) NOT NULL,
  `id_genero` int(11) NOT NULL,
  `id_tipo_docente` int(11) NOT NULL,
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

INSERT INTO `fact_docente_facultad` (`id`, `id_docente`, `id_genero`, `id_tipo_docente`, `id_escalafon`, `id_facultad`, `id_nacionalidad`, `cantidad`, `fecha_creacion`, `fecha_actualizacion`) VALUES
(223, 285, 7, 4, 10, 64, 13, 1, '2018-11-27 03:14:37', '2018-11-27 03:14:37'),
(224, 286, 7, 4, 10, 64, 13, 1, '2018-11-27 03:14:37', '2018-11-27 03:14:37'),
(225, 287, 7, 4, 9, 64, 13, 1, '2018-11-27 03:14:37', '2018-11-27 03:14:37'),
(226, 288, 6, 5, 9, 57, 14, 1, '2018-11-27 03:14:37', '2018-11-27 03:14:37'),
(227, 289, 7, 6, 7, 62, 14, 1, '2018-11-27 03:14:37', '2018-11-27 03:14:37'),
(228, 290, 7, 6, 10, 58, 14, 1, '2018-11-27 03:14:37', '2018-11-27 03:14:37');

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
(103, 285, 40, 64, 50, 1, '2018-11-27 03:55:28', '2018-11-27 03:55:28'),
(104, 286, 40, 64, 50, 1, '2018-11-27 03:55:28', '2018-11-27 03:55:28'),
(105, 287, 41, 64, 75, 1, '2018-11-27 03:55:28', '2018-11-27 03:55:28'),
(106, 288, 42, 57, 500, 1, '2018-11-27 03:55:28', '2018-11-27 03:55:28'),
(107, 289, 43, 62, 22, 1, '2018-11-27 03:55:28', '2018-11-27 03:55:28'),
(108, 287, 43, 64, 22, 1, '2018-11-27 03:55:28', '2018-11-27 03:55:28'),
(109, 290, 44, 58, 43, 1, '2018-11-27 03:55:28', '2018-11-27 03:55:28'),
(110, 290, 45, 58, 873, 1, '2018-11-27 03:55:28', '2018-11-27 03:55:28');

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
(94, 285, 27, 4, 1, '2018-11-27 03:55:28', '2018-11-27 03:55:28'),
(95, 286, 27, 4, 1, '2018-11-27 03:55:28', '2018-11-27 03:55:28'),
(96, 287, 28, 3, 1, '2018-11-27 03:55:28', '2018-11-27 03:55:28'),
(97, 288, 29, 1, 1, '2018-11-27 03:55:28', '2018-11-27 03:55:28'),
(98, 289, 30, 3, 1, '2018-11-27 03:55:28', '2018-11-27 03:55:28'),
(99, 287, 30, 3, 1, '2018-11-27 03:55:28', '2018-11-27 03:55:28'),
(100, 290, 30, 3, 1, '2018-11-27 03:55:28', '2018-11-27 03:55:28');

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
  `id_ano` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL DEFAULT '1',
  `fecha_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_actualizacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `fact_egresado_estudiosuc`
--

INSERT INTO `fact_egresado_estudiosuc` (`id`, `id_egresado`, `id_estudiosuc`, `id_facultad`, `id_carrera`, `id_ano`, `cantidad`, `fecha_creacion`, `fecha_actualizacion`) VALUES
(1, 29, 37, 64, 117, 442, 1, '2018-10-29 23:42:34', '2018-11-16 13:19:13'),
(2, 30, 38, 64, 119, 443, 1, '2018-10-29 23:42:34', '2018-11-16 13:19:17'),
(3, 31, 39, 64, 117, 443, 1, '2018-10-29 23:42:34', '2018-11-16 13:19:29'),
(4, 31, 40, 61, 118, 446, 1, '2018-10-29 23:42:34', '2018-11-16 15:01:33');

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
  `id_genero` int(11) DEFAULT NULL,
  `id_nacionalidad` int(11) DEFAULT NULL,
  `id_status` int(11) NOT NULL,
  `id_discapacidad` int(11) NOT NULL,
  `id_etnia` int(11) NOT NULL,
  `id_tipo_estudiante` int(11) NOT NULL,
  `id_tiempo` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `fact_estudiante_facultad`
--

INSERT INTO `fact_estudiante_facultad` (`id`, `id_estudiante`, `id_facultad`, `id_carrera`, `id_genero`, `id_nacionalidad`, `id_status`, `id_discapacidad`, `id_etnia`, `id_tipo_estudiante`, `id_tiempo`, `cantidad`) VALUES
(24, 19, 64, 117, 7, 13, 3, 4, 1, 2, 446, 1),
(25, 20, 64, 118, 7, 14, 3, 4, 1, 1, 444, 1),
(26, 21, 64, 117, 7, 14, 2, 3, 2, 2, 447, 1),
(27, 22, 64, 119, 7, 13, 3, 4, 1, 2, 445, 1),
(28, 23, 64, 120, 6, 13, 2, 4, 2, 1, 442, 1),
(29, 24, 64, 120, 6, 13, 2, 3, 1, 2, 443, 1),
(30, 25, 59, 162, 6, 13, 2, 3, 1, 1, 442, 1),
(31, 26, 59, 163, 6, 13, 3, 3, 1, 1, 446, 1),
(32, 27, 59, 168, 6, 13, 3, 4, 2, 2, 444, 1),
(33, 28, 64, 124, 6, 13, 3, 3, 2, 2, 445, 1),
(34, 29, 58, 125, 6, 13, 3, 3, 2, 1, 445, 1),
(35, 30, 58, 125, 6, 13, 3, 3, 2, 1, 445, 1),
(36, 31, 61, 179, 6, 14, 3, 4, 2, 1, 448, 1),
(37, 32, 61, 170, 7, 14, 3, 4, 1, 1, 448, 1),
(38, 33, 61, 175, 6, 14, 2, 4, 1, 1, 448, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `history_action`
--

CREATE TABLE `history_action` (
  `id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `action` varchar(100) NOT NULL,
  `module` varchar(100) NOT NULL,
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `history_action`
--

INSERT INTO `history_action` (`id`, `username`, `action`, `module`, `date`) VALUES
(20, 'wgiovanni', 'Ingreso al sistema', 'Usuarios', '2018-11-07 19:40:40'),
(21, 'wgiovanni', 'Agregó un usuario', 'Usuarios', '2018-11-07 20:09:19'),
(22, 'wgiovanni', 'Agregó un usuario', 'Usuarios', '2018-11-07 20:13:22'),
(23, 'wgiovanni', 'Agregó un usuario', 'Usuarios', '2018-11-07 20:21:55'),
(24, 'wgiovanni', 'Agregó un usuario', 'Usuarios', '2018-11-07 20:26:32'),
(25, 'wgiovanni', 'Eliminó un usuario', 'Usuarios', '2018-11-07 20:26:46'),
(26, 'wgiovanni', 'Agregó un usuario', 'Usuarios', '2018-11-07 20:27:50'),
(27, 'wgiovanni', 'Eliminó un usuario', 'Usuarios', '2018-11-07 20:32:21'),
(28, 'wgiovanni', 'Modificó un parámetro del sistema', 'Integración', '2018-11-07 20:56:42'),
(29, 'wgiovanni', 'Modificó un parámetro del sistema', 'Integración', '2018-11-07 20:56:59'),
(30, 'wgiovanni', 'Ingreso al sistema', 'Usuarios', '2018-11-07 21:12:38'),
(31, 'prueba', 'Ingreso al sistema', 'Usuarios', '2018-11-08 13:12:03'),
(32, 'wgiovanni', 'Ingreso al sistema', 'Usuarios', '2018-11-08 13:13:02'),
(33, 'wgiovanni', 'Ingreso al sistema', 'Usuarios', '2018-11-08 13:15:40'),
(34, 'prueba', 'Ingreso al sistema', 'Usuarios', '2018-11-08 14:27:02'),
(35, 'wgiovanni', 'Ingreso al sistema', 'Usuarios', '2018-11-08 14:27:13'),
(36, 'wgiovanni', 'Agregó un usuario', 'Usuarios', '2018-11-08 14:27:30'),
(37, 'wgiovanni', 'Agregó un usuario', 'Usuarios', '2018-11-08 14:43:25'),
(38, 'wgiovanni', 'Agregó un usuario', 'Usuarios', '2018-11-08 14:44:15'),
(39, 'wgiovanni', 'Agregó un usuario', 'Usuarios', '2018-11-10 15:36:13'),
(40, 'Facyt', 'Ingreso al sistema', 'Usuarios', '2018-11-10 15:36:31'),
(41, 'Facyt', 'Ingreso al sistema', 'Usuarios', '2018-11-10 16:27:46'),
(42, 'Facyt', 'Carga de archivo', 'Docentes', '2018-11-10 16:48:38'),
(43, 'Facyt', 'Carga de archivo', 'Docentes', '2018-11-10 16:52:44'),
(44, 'Facyt', 'Carga de archivo', 'Docentes', '2018-11-10 17:29:17'),
(45, 'Facyt', 'Carga de archivo', 'Docentes', '2018-11-10 17:56:56'),
(46, 'Facyt', 'Carga de archivo', 'Docentes', '2018-11-10 18:12:56'),
(47, 'Facyt', 'Carga de archivo', 'Docentes', '2018-11-10 18:28:08'),
(48, 'Facyt', 'Carga de archivo', 'Docentes', '2018-11-10 18:47:38'),
(49, 'Facyt', 'Carga de archivo', 'Docentes', '2018-11-10 18:51:34'),
(50, 'Facyt', 'Carga de archivo', 'Docentes', '2018-11-10 18:57:05'),
(51, 'Facyt', 'Carga de archivo', 'Docentes', '2018-11-10 19:04:29'),
(52, 'Facyt', 'Carga de archivo', 'Docentes', '2018-11-10 19:07:56'),
(53, 'Facyt', 'Carga de archivo', 'Docentes', '2018-11-10 19:11:00'),
(54, 'Facyt', 'Carga de archivo', 'Docentes', '2018-11-10 19:13:26'),
(55, 'Facyt', 'Carga de archivo', 'Docentes', '2018-11-10 19:13:58'),
(56, 'Facyt', 'Carga de archivo', 'Docentes', '2018-11-10 19:15:04'),
(57, 'Facyt', 'Carga de archivo', 'Docentes', '2018-11-10 19:15:48'),
(58, 'Facyt', 'Carga de archivo', 'Docentes', '2018-11-10 19:19:13'),
(59, 'Facyt', 'Carga de archivo', 'Docentes', '2018-11-10 19:21:01'),
(60, 'Facyt', 'Carga de archivo', 'Docentes', '2018-11-10 19:25:34'),
(61, 'Facyt', 'Carga de archivo', 'Docentes', '2018-11-10 19:43:31'),
(62, 'Facyt', 'Carga de archivo', 'Docentes', '2018-11-10 19:44:10'),
(63, 'Facyt', 'Carga de archivo', 'Docentes', '2018-11-10 19:44:30'),
(64, 'prueba', 'Ingreso al sistema', 'Usuarios', '2018-11-10 20:38:46'),
(65, 'Facyt', 'Ingreso al sistema', 'Usuarios', '2018-11-10 20:51:05'),
(66, 'Facyt', 'Carga de archivo', 'Docentes', '2018-11-10 20:51:18'),
(67, 'prueba', 'Ingreso al sistema', 'Usuarios', '2018-11-10 20:55:12'),
(68, 'Facyt', 'Ingreso al sistema', 'Usuarios', '2018-11-10 20:55:34'),
(69, 'Facyt', 'Carga de archivo', 'Docentes', '2018-11-10 20:55:45'),
(70, 'prueba', 'Ingreso al sistema', 'Usuarios', '2018-11-10 20:56:10'),
(71, 'wgiovanni', 'Ingreso al sistema', 'Usuarios', '2018-11-11 13:15:53'),
(72, 'Faces', 'Ingreso al sistema', 'Usuarios', '2018-11-11 13:17:20'),
(73, 'wgiovanni', 'Ingreso al sistema', 'Usuarios', '2018-11-11 13:29:48'),
(74, 'Facyt', 'Ingreso al sistema', 'Usuarios', '2018-11-11 14:19:51'),
(75, 'wgiovanni', 'Ingreso al sistema', 'Usuarios', '2018-11-11 14:29:25'),
(76, 'wgiovanni', 'Modificó un usuario', 'Usuarios', '2018-11-11 14:30:05'),
(77, 'wgiovanni', 'Modificó un usuario', 'Usuarios', '2018-11-11 14:30:58'),
(78, 'wgiovanni', 'Modificó un usuario', 'Usuarios', '2018-11-11 14:34:33'),
(79, 'wgiovanni', 'Modificó un usuario', 'Usuarios', '2018-11-11 14:34:47'),
(80, 'wgiovanni', 'Modificó un usuario', 'Usuarios', '2018-11-11 14:34:57'),
(81, 'wgiovanni', 'Modificó un usuario', 'Usuarios', '2018-11-11 14:35:08'),
(82, 'wgiovanni', 'Agregó un usuario', 'Usuarios', '2018-11-11 14:36:16'),
(83, 'wgiovanni', 'Agregó un usuario', 'Usuarios', '2018-11-11 14:37:21'),
(84, 'wgiovanni', 'Agregó un usuario', 'Usuarios', '2018-11-11 14:38:26'),
(85, 'wgiovanni', 'Modificó un usuario', 'Usuarios', '2018-11-11 14:38:49'),
(86, 'wgiovanni', 'Modificó un usuario', 'Usuarios', '2018-11-11 14:39:19'),
(87, 'wgiovanni', 'Modificó un usuario', 'Usuarios', '2018-11-11 14:39:40'),
(88, 'wgiovanni', 'Modificó un usuario', 'Usuarios', '2018-11-11 14:40:13'),
(89, 'wgiovanni', 'Modificó un usuario', 'Usuarios', '2018-11-11 14:41:07'),
(90, 'wgiovanni', 'Agregó un usuario', 'Usuarios', '2018-11-11 14:44:11'),
(91, 'wgiovanni', 'Agregó un usuario', 'Usuarios', '2018-11-11 14:46:15'),
(92, 'wgiovanni', 'Agregó un usuario', 'Usuarios', '2018-11-11 14:47:02'),
(93, 'wgiovanni', 'Agregó un usuario', 'Usuarios', '2018-11-11 14:48:00'),
(94, 'wgiovanni', 'Agregó un usuario', 'Usuarios', '2018-11-11 14:48:48'),
(95, 'wgiovanni', 'Agregó un usuario', 'Usuarios', '2018-11-11 14:49:31'),
(96, 'wgiovanni', 'Agregó un usuario', 'Usuarios', '2018-11-11 14:50:59'),
(97, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-11 14:54:54'),
(98, 'Facyt_estudiante', 'Ingreso al sistema', 'Usuarios', '2018-11-11 15:07:28'),
(99, 'facyt_docente', 'Ingreso al sistema', 'Usuarios', '2018-11-11 15:08:34'),
(100, 'Facyt_docente', 'Carga de archivo', 'Docentes', '2018-11-11 15:09:28'),
(101, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-11 15:35:52'),
(102, 'Admin', 'Modificó un usuario', 'Usuarios', '2018-11-11 15:36:46'),
(103, 'Admin', 'Modificó un usuario', 'Usuarios', '2018-11-11 15:37:03'),
(104, 'Admin', 'Modificó un usuario', 'Usuarios', '2018-11-11 15:37:16'),
(105, 'Admin', 'Modificó un usuario', 'Usuarios', '2018-11-11 15:37:28'),
(106, 'Admin', 'Modificó un usuario', 'Usuarios', '2018-11-11 15:37:41'),
(107, 'Admin', 'Modificó un usuario', 'Usuarios', '2018-11-11 15:37:54'),
(108, 'Admin', 'Modificó un usuario', 'Usuarios', '2018-11-11 15:38:08'),
(109, 'Admin', 'Modificó un usuario', 'Usuarios', '2018-11-11 15:39:56'),
(110, 'Admin', 'Modificó un usuario', 'Usuarios', '2018-11-11 15:40:07'),
(111, 'Admin', 'Modificó un usuario', 'Usuarios', '2018-11-11 15:40:16'),
(112, 'Admin', 'Modificó un usuario', 'Usuarios', '2018-11-11 15:40:25'),
(113, 'Admin', 'Modificó un usuario', 'Usuarios', '2018-11-11 15:40:34'),
(114, 'Admin', 'Modificó un usuario', 'Usuarios', '2018-11-11 15:40:57'),
(115, 'Admin', 'Modificó un usuario', 'Usuarios', '2018-11-11 15:41:10'),
(116, 'FACYT', 'Ingreso al sistema', 'Usuarios', '2018-11-11 15:41:57'),
(117, 'FACYT', 'Carga de archivo', 'Estudiantes', '2018-11-11 15:59:17'),
(118, 'vicerrector', 'Ingreso al sistema', 'Usuarios', '2018-11-11 16:01:43'),
(119, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-12 15:58:39'),
(120, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-12 17:01:44'),
(121, 'FACE', 'Ingreso al sistema', 'Usuarios', '2018-11-12 17:10:35'),
(122, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-12 17:12:44'),
(123, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-12 17:16:59'),
(124, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-12 17:17:57'),
(125, 'FACE', 'Ingreso al sistema', 'Usuarios', '2018-11-12 17:35:55'),
(126, 'FACE', 'Ingreso al sistema', 'Usuarios', '2018-11-12 17:37:16'),
(127, 'FACE', 'Ingreso al sistema', 'Usuarios', '2018-11-12 17:46:25'),
(128, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-12 17:46:49'),
(129, 'Faces_docente', 'Ingreso al sistema', 'Usuarios', '2018-11-12 17:52:20'),
(130, 'Faces_docente', 'Ingreso al sistema', 'Usuarios', '2018-11-12 17:55:43'),
(131, 'FACE', 'Ingreso al sistema', 'Usuarios', '2018-11-12 17:57:00'),
(132, 'FACE', 'Ingreso al sistema', 'Usuarios', '2018-11-12 17:57:19'),
(133, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-12 17:59:36'),
(134, 'FACE', 'Ingreso al sistema', 'Usuarios', '2018-11-12 18:01:44'),
(135, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-12 18:05:33'),
(136, 'vicerrector', 'Ingreso al sistema', 'Usuarios', '2018-11-12 18:06:26'),
(137, 'vicerrector', 'Ingreso al sistema', 'Usuarios', '2018-11-12 18:08:04'),
(138, 'vicerrector', 'Ingreso al sistema', 'Usuarios', '2018-11-13 01:17:51'),
(139, 'vicerrector', 'Ingreso al sistema', 'Usuarios', '2018-11-13 01:29:43'),
(140, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-13 12:34:41'),
(141, 'vicerrector', 'Ingreso al sistema', 'Usuarios', '2018-11-13 12:36:02'),
(142, 'vicerrector', 'Ingreso al sistema', 'Usuarios', '2018-11-13 12:44:25'),
(143, 'vicerrector', 'Ingreso al sistema', 'Usuarios', '2018-11-14 13:05:34'),
(144, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-14 20:27:37'),
(145, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-14 21:09:45'),
(146, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-15 13:00:21'),
(147, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-15 13:06:03'),
(148, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-15 21:41:46'),
(149, 'Admin', 'Agregó un usuario', 'Usuarios', '2018-11-15 21:48:20'),
(150, 'Admin', 'Eliminó un usuario', 'Usuarios', '2018-11-15 21:48:25'),
(151, 'Admin', 'Agregó un usuario', 'Usuarios', '2018-11-15 21:48:47'),
(152, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-15 21:52:00'),
(153, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-15 21:54:46'),
(154, 'Admin', 'Modificó un parámetro del sistema', 'Integración', '2018-11-15 22:00:35'),
(155, 'Admin', 'Modificó un parámetro del sistema', 'Integración', '2018-11-15 22:00:42'),
(156, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-15 22:07:58'),
(157, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-15 22:20:55'),
(158, 'Admin', 'Modificó un usuario', 'Usuarios', '2018-11-15 22:22:27'),
(159, 'Admin', 'Eliminó un usuario', 'Usuarios', '2018-11-15 22:23:59'),
(160, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-15 23:06:44'),
(161, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-16 12:07:12'),
(162, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-16 12:12:49'),
(163, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-16 12:14:16'),
(164, 'vicerrector', 'Ingreso al sistema', 'Usuarios', '2018-11-16 12:14:48'),
(165, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-16 13:07:57'),
(166, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-16 15:26:39'),
(167, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-16 17:48:20'),
(168, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-18 22:14:54'),
(169, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-19 12:46:23'),
(170, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-19 13:32:50'),
(171, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-19 14:14:46'),
(172, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-20 13:39:05'),
(173, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-20 13:47:20'),
(174, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-22 12:55:55'),
(175, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-22 15:02:26'),
(176, 'FACE', 'Ingreso al sistema', 'Usuarios', '2018-11-22 20:00:48'),
(177, 'vicerrector', 'Ingreso al sistema', 'Usuarios', '2018-11-22 20:02:33'),
(178, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-23 00:58:01'),
(179, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-23 16:07:11'),
(180, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-23 16:50:53'),
(181, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-23 17:48:52'),
(182, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-23 19:42:57'),
(183, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-23 20:04:27'),
(184, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-23 20:13:02'),
(185, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-23 20:34:54'),
(186, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-23 20:43:49'),
(187, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-23 20:44:00'),
(188, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-23 20:45:46'),
(189, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-23 23:19:25'),
(190, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-25 16:17:47'),
(191, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-25 20:32:30'),
(192, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-25 21:18:21'),
(193, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-25 21:58:30'),
(194, 'Admin', 'Modificó un parámetro del sistema', 'Integración', '2018-11-25 22:07:02'),
(195, 'Admin', 'Modificó un parámetro del sistema', 'Integración', '2018-11-25 22:07:17'),
(196, 'Admin', 'Modificó un parámetro del sistema', 'Integración', '2018-11-25 22:07:31'),
(197, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-25 23:04:49'),
(198, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-25 23:17:18'),
(199, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-25 23:17:44'),
(200, 'Admin', 'Ingreso al sistema', 'Usuarios', '2018-11-26 05:37:57');

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
(1, 'CARGA_INICIAL_ACTUALIZACION', 'CARGA_INICIAL_ACTUALIZACION', 'Parametro que toma valores boleanos para la carga inicial (1) y la actualizacion (0)', '0', '2018-10-18 20:35:32', '2018-11-27 03:55:28'),
(2, 'RUTA_CARGA_ESTUDIANTES', 'RUTA_CARGA_ESTUDIANTES', 'Endpoint o ruta para la carga inicial o actualización del modulo de estudiantes', 'http://127.0.0.1:8082/api/v1/estudiantes', '2018-10-18 20:38:51', '2018-11-25 22:07:17'),
(3, 'RUTA_CARGA_DOCENTES', 'RUTA_CARGA_DOCENTES', 'Endpoint o ruta para la carga inicial o actualización del modulo de docentes', 'http://127.0.0.1:8082/api/v1/docentes', '2018-10-18 20:40:26', '2018-11-27 03:05:56'),
(4, 'RUTA_CARGA_EGRESADOS', 'RUTA_CARGA_EGRESADOS', 'Endpoint o ruta para la carga inicial o actualización del modulo de egresados', 'http://127.0.0.1:8082/api/v1/egresados', '2018-10-18 21:31:21', '2018-11-25 22:07:31'),
(5, 'FECHA_ACTUALIZACION', 'FECHA_ACTUALIZACION', 'Parámetro de fecha que se utilizara para poder llevar el control de la fecha de actualización en cada ejecución del proceso ETL  ', '2018-11-26 23:55:28', '2018-10-28 17:44:52', '2018-11-27 03:55:28');

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
(5, 'administrador'),
(9, 'facultad_docente'),
(7, 'facultad_estudiante'),
(8, 'verificador'),
(6, 'vicerrector');

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
  `phone` varchar(50) NOT NULL,
  `address` varchar(300) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `user`
--

INSERT INTO `user` (`id`, `first_name`, `last_name`, `username`, `email`, `phone`, `address`, `password`) VALUES
(42, 'Admin', 'Admin', 'Admin', 'Admin@gmail.com', '04122345768', 'direccion administrador', '123456'),
(44, 'vicerrector', 'vicerrector', 'vicerrector', 'vicerrector@gmail.com', '04122345768', 'direccion', '123456'),
(54, 'Ingeneria', 'Ingeneria', 'INGENIERIA', 'Ingeneria@gmail.com', '04122345768', 'direccion', '123456'),
(55, 'aja', 'aja', 'aja', 'aja@gmail.com', '04122345768', 'direccion', '123456'),
(56, 'Face', 'face', 'FACE', 'Face_estudiante@gmail.com', '04122345768', 'direccion', '123456'),
(57, 'Facyt', 'Facyt', 'FACYT', 'Facyt_estudiante@gmail.com', '04122345768', 'direccion', '123'),
(58, 'Faces', 'Faces', 'FACES', 'Faces@gmail.com', '04122345768', 'direccion', '123456'),
(59, 'Fcs', 'Fcs', 'FCS', 'Fcs@gmail.com', '04122345768', 'direccion', '123456'),
(60, 'odontologia', 'odontologia', 'ODONTOLOGIA', 'odontologia_estudiante@gmail.com', '04122345768', 'direccion', '123456'),
(61, 'derecho_estudiante', 'derecho_estudiante', 'FCJP', 'Fcjp_estudiante@gmail.com', '04122345768', 'direccion', '12345'),
(62, 'Facyt', 'Facyt', 'Facyt_docente', 'Facyt@gmail.com', '04122345768', 'direccion', '123'),
(63, 'Face', 'Face', 'Face_docente', 'Face_docente@hotmail.com', '04122345768', 'direccion', '123'),
(64, 'Fcjp', 'Fcjp', 'Fcjp_docente', 'Fcjp_docente@gmail.com', '04122345768', 'direccion', '123'),
(65, 'Odontologia', 'Odontologia', 'Odontologia_docente', 'Odontologia_docente@gmail.com', '04122345768', 'direccion', '123'),
(66, 'Fcs', 'Fcs', 'Fcs_docente', 'Fcs_docente@gmail.com', '04122345768', 'direccion', '123'),
(67, 'Faces', 'Faces', 'Faces_docente', 'Faces_docente@gmail.com', '04122345768', 'direccion', '123'),
(68, 'Ingeneria', 'Ingeneria', 'Ingeneria_docente', 'Ingeneria_docente@gmail.com', '04122345768', 'direccion', '123');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user_role`
--

CREATE TABLE `user_role` (
  `id` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `id_role` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `user_role`
--

INSERT INTO `user_role` (`id`, `id_user`, `id_role`) VALUES
(47, 42, 5),
(48, 44, 6),
(49, 44, 8),
(50, 62, 9),
(51, 63, 9),
(52, 64, 9),
(53, 65, 9),
(54, 66, 9),
(55, 67, 9),
(56, 68, 9),
(64, 54, 7),
(65, 56, 7),
(66, 57, 7),
(67, 58, 7),
(68, 59, 7),
(69, 60, 7),
(70, 61, 7);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `dim_carrera`
--
ALTER TABLE `dim_carrera`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`codigo`);

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
  ADD UNIQUE KEY `codigo` (`codigo`);

--
-- Indices de la tabla `dim_genero`
--
ALTER TABLE `dim_genero`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `codigo` (`codigo`);

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
-- Indices de la tabla `dim_status`
--
ALTER TABLE `dim_status`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `dim_tiempo`
--
ALTER TABLE `dim_tiempo`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `codigo` (`codigo`);

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
-- Indices de la tabla `fact_docente_facultad`
--
ALTER TABLE `fact_docente_facultad`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_docente` (`id_docente`),
  ADD KEY `id_sexo` (`id_genero`),
  ADD KEY `id_grado` (`id_tipo_docente`),
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
  ADD KEY `id_carrera` (`id_carrera`),
  ADD KEY `id_ano` (`id_ano`);

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
  ADD KEY `id_sexo` (`id_genero`),
  ADD KEY `id_nacionalidad` (`id_nacionalidad`),
  ADD KEY `id_status` (`id_status`),
  ADD KEY `id_discapacidad` (`id_discapacidad`),
  ADD KEY `id_etnia` (`id_etnia`),
  ADD KEY `id_tipo` (`id_tipo_estudiante`),
  ADD KEY `id_ano` (`id_tiempo`);

--
-- Indices de la tabla `history_action`
--
ALTER TABLE `history_action`
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
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `user_role`
--
ALTER TABLE `user_role`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_user` (`id_user`),
  ADD KEY `id_role` (`id_role`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `dim_carrera`
--
ALTER TABLE `dim_carrera`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=200;

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `dim_docente`
--
ALTER TABLE `dim_docente`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=291;

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

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
-- AUTO_INCREMENT de la tabla `dim_genero`
--
ALTER TABLE `dim_genero`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

--
-- AUTO_INCREMENT de la tabla `dim_patentes`
--
ALTER TABLE `dim_patentes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `dim_premio`
--
ALTER TABLE `dim_premio`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT de la tabla `dim_proyecto`
--
ALTER TABLE `dim_proyecto`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;

--
-- AUTO_INCREMENT de la tabla `dim_publicacion`
--
ALTER TABLE `dim_publicacion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;

--
-- AUTO_INCREMENT de la tabla `dim_status`
--
ALTER TABLE `dim_status`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=75;

--
-- AUTO_INCREMENT de la tabla `dim_tiempo`
--
ALTER TABLE `dim_tiempo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=482;

--
-- AUTO_INCREMENT de la tabla `dim_tipo_docente`
--
ALTER TABLE `dim_tipo_docente`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `dim_tipo_estudiante`
--
ALTER TABLE `dim_tipo_estudiante`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `dim_titulo`
--
ALTER TABLE `dim_titulo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

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
-- AUTO_INCREMENT de la tabla `fact_docente_facultad`
--
ALTER TABLE `fact_docente_facultad`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=229;

--
-- AUTO_INCREMENT de la tabla `fact_docente_otroestudio`
--
ALTER TABLE `fact_docente_otroestudio`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=71;

--
-- AUTO_INCREMENT de la tabla `fact_docente_premio`
--
ALTER TABLE `fact_docente_premio`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=58;

--
-- AUTO_INCREMENT de la tabla `fact_docente_proyecto`
--
ALTER TABLE `fact_docente_proyecto`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=74;

--
-- AUTO_INCREMENT de la tabla `fact_docente_publicacion`
--
ALTER TABLE `fact_docente_publicacion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=111;

--
-- AUTO_INCREMENT de la tabla `fact_docente_titulo`
--
ALTER TABLE `fact_docente_titulo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=101;

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- AUTO_INCREMENT de la tabla `history_action`
--
ALTER TABLE `history_action`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=201;

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=69;

--
-- AUTO_INCREMENT de la tabla `user_role`
--
ALTER TABLE `user_role`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=71;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `fact_docente_facultad`
--
ALTER TABLE `fact_docente_facultad`
  ADD CONSTRAINT `fact_docente_facultad_ibfk_1` FOREIGN KEY (`id_escalafon`) REFERENCES `dim_escalafon` (`id`),
  ADD CONSTRAINT `fact_docente_facultad_ibfk_2` FOREIGN KEY (`id_facultad`) REFERENCES `dim_facultad` (`id`),
  ADD CONSTRAINT `fact_docente_facultad_ibfk_3` FOREIGN KEY (`id_tipo_docente`) REFERENCES `dim_tipo_docente` (`id`),
  ADD CONSTRAINT `fact_docente_facultad_ibfk_4` FOREIGN KEY (`id_genero`) REFERENCES `dim_genero` (`id`),
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
  ADD CONSTRAINT `fact_egresado_estudiosuc_ibfk_4` FOREIGN KEY (`id_egresado`) REFERENCES `dim_egresado` (`id`),
  ADD CONSTRAINT `fact_egresado_estudiosuc_ibfk_5` FOREIGN KEY (`id_ano`) REFERENCES `dim_tiempo` (`id`);

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
  ADD CONSTRAINT `fact_estudiante_facultad_ibfk_10` FOREIGN KEY (`id_tiempo`) REFERENCES `dim_tiempo` (`id`),
  ADD CONSTRAINT `fact_estudiante_facultad_ibfk_2` FOREIGN KEY (`id_facultad`) REFERENCES `dim_facultad` (`id`),
  ADD CONSTRAINT `fact_estudiante_facultad_ibfk_3` FOREIGN KEY (`id_carrera`) REFERENCES `dim_carrera` (`id`),
  ADD CONSTRAINT `fact_estudiante_facultad_ibfk_4` FOREIGN KEY (`id_nacionalidad`) REFERENCES `dim_nacionalidad` (`id`),
  ADD CONSTRAINT `fact_estudiante_facultad_ibfk_5` FOREIGN KEY (`id_genero`) REFERENCES `dim_genero` (`id`),
  ADD CONSTRAINT `fact_estudiante_facultad_ibfk_6` FOREIGN KEY (`id_status`) REFERENCES `dim_status` (`id`),
  ADD CONSTRAINT `fact_estudiante_facultad_ibfk_7` FOREIGN KEY (`id_etnia`) REFERENCES `dim_etnia` (`id`),
  ADD CONSTRAINT `fact_estudiante_facultad_ibfk_8` FOREIGN KEY (`id_discapacidad`) REFERENCES `dim_discapacidad` (`id`),
  ADD CONSTRAINT `fact_estudiante_facultad_ibfk_9` FOREIGN KEY (`id_tipo_estudiante`) REFERENCES `dim_tipo_estudiante` (`id`);

--
-- Filtros para la tabla `user_role`
--
ALTER TABLE `user_role`
  ADD CONSTRAINT `user_role_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `user_role_ibfk_2` FOREIGN KEY (`id_role`) REFERENCES `role` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
