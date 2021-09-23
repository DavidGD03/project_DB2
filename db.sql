-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 26-08-2019 a las 20:07:25
-- Versión del servidor: 10.1.38-MariaDB
-- Versión de PHP: 7.3.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `db`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `califica`
--

CREATE TABLE `califica` (
  `valoracion` varchar(10) NOT NULL,
  `descripcion` varchar(300) NOT NULL,
  `fecha` date NOT NULL,
  `fk_id_usuario` int(11) NOT NULL,
  `fk_correo` varchar(30) NOT NULL,
  `fk_id_objeto` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cargo`
--

CREATE TABLE `cargo` (
  `id` int(11) NOT NULL,
  `nombre` varchar(60) NOT NULL,
  `descripcion` varchar(200) NOT NULL,
  `fk_id_contrato` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carrito`
--

CREATE TABLE `carrito` (
  `idusuario` int(11) NOT NULL,
  `correousuario` varchar(30) NOT NULL,
  `idobjeto` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `carrito`
--

INSERT INTO `carrito` (`idusuario`, `correousuario`, `idobjeto`) VALUES
(2, 'david3@gmail.com', 7);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categoria`
--

CREATE TABLE `categoria` (
  `id` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `descripcion` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `categoria`
--

INSERT INTO `categoria` (`id`, `nombre`, `descripcion`) VALUES
(1, 'Tecnologia', 'Aquí encontrarás lo mejor en tecnología.'),
(2, 'Electrodomésticos y Hogar', 'Encuentra lo mejor para tu hogar.'),
(3, 'Moda', 'Encuentra las mejores prendas a los mejores precios.'),
(4, 'Libros', 'Encuentra los best-sellers del momento a tan solo un click.');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `contrato`
--

CREATE TABLE `contrato` (
  `id` int(11) NOT NULL,
  `salario` bigint(20) NOT NULL,
  `fchvencimiento` date NOT NULL,
  `fchrealizado` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `desea`
--

CREATE TABLE `desea` (
  `nombre` varchar(30) NOT NULL,
  `fecha` date NOT NULL,
  `fk_id_usuario` int(11) NOT NULL,
  `fk_correo` varchar(30) DEFAULT NULL,
  `fk_id_objeto` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleado`
--

CREATE TABLE `empleado` (
  `id` int(11) NOT NULL,
  `nombrec` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `telefono` varchar(25) NOT NULL,
  `password` varchar(100) NOT NULL,
  `telefono2` bigint(20) DEFAULT NULL,
  `genero` varchar(20) NOT NULL,
  `fchnacimiento` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `empleado`
--

INSERT INTO `empleado` (`id`, `nombrec`, `email`, `telefono`, `password`, `telefono2`, `genero`, `fchnacimiento`) VALUES
(5, 'david', 'phashior@gmail.com', '31432208845', '$5$rounds=535000$bQ.PyYExbD/SF00c$F4AXDCgFW2C3D5i7Jx9ceLIXpnaRgQHMUzW8qvPJiq.', NULL, '', '0000-00-00'),
(10454, 'David', 'david2@gmail.com', '45484848', '$5$rounds=535000$1gHvyXwTcAB6WnS9$mWd5fyIV789zVHgsw6cQfhcNBzgWXE5WF8yHY3vDBN8', 4444545, 'Macho', '2000-03-03');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empresa`
--

CREATE TABLE `empresa` (
  `id` int(11) NOT NULL,
  `nombre` varchar(60) NOT NULL,
  `cuentabancaria` bigint(20) NOT NULL,
  `correo` varchar(30) NOT NULL,
  `ubicacion` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `empresa`
--

INSERT INTO `empresa` (`id`, `nombre`, `cuentabancaria`, `correo`, `ubicacion`) VALUES
(1, 'Motorola', 15515155151, 'motorola@gmail.com', 'Bogotá'),
(2, 'Xiaomi', 5458454848, 'xiaomi@gmail.com', 'Medellín'),
(3, 'Louis Vuitton', 84788488459, 'louis@gmail.com', 'Bucaramanga'),
(4, 'Planeta', 478884844848, 'editorialplaneta@gmail.com', 'Bogotá'),
(5, 'Samsung', 4744748481, 'samsung@gmail.com', 'Bogotá'),
(6, 'Rimax', 48488484848, 'rimax@gmail.com', 'Bucaramanga'),
(7, 'Norma', 44848844848, 'norma@gmail.com', 'Bogotá'),
(8, 'Gef', 7478484848, 'gef@gmail.com', 'Bucaramanga');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empresae`
--

CREATE TABLE `empresae` (
  `id` int(11) NOT NULL,
  `nombre` varchar(60) NOT NULL,
  `descripcion` varchar(300) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `invita`
--

CREATE TABLE `invita` (
  `id_referente` int(11) NOT NULL,
  `correo_referente` varchar(30) NOT NULL,
  `id_invitado` int(11) NOT NULL,
  `correo_invitado` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `nivel`
--

CREATE TABLE `nivel` (
  `id` int(11) NOT NULL,
  `numnivel` int(11) NOT NULL,
  `nbnivel` varchar(60) NOT NULL,
  `recompensa` varchar(200) NOT NULL,
  `puntosnecesarios` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `nivel`
--

INSERT INTO `nivel` (`id`, `numnivel`, `nbnivel`, `recompensa`, `puntosnecesarios`) VALUES
(1, 1, 'Principiante', 'Alcanza el nivel 2 para mejores recompensas.', 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `noticia`
--

CREATE TABLE `noticia` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `fecha` date NOT NULL,
  `titulo` varchar(60) NOT NULL,
  `descripcion` varchar(300) NOT NULL,
  `fk_id_empleado` int(11) NOT NULL,
  `imagen` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `noticia`
--

INSERT INTO `noticia` (`id`, `fecha`, `titulo`, `descripcion`, `fk_id_empleado`, `imagen`) VALUES
(1, '0000-00-00', 'pop', 'pop', 5, 'Universidad_Industrial_de_Santander_Logo.jpg'),
(3, '0000-00-00', 'pop3', 'pop3', 5, 'Misión-e1487266341501.jpg');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `objeto`
--

CREATE TABLE `objeto` (
  `id` int(11) NOT NULL,
  `precio` bigint(20) NOT NULL,
  `descripcion` varchar(100) NOT NULL,
  `garantia` varchar(30) NOT NULL,
  `nombre` varchar(60) NOT NULL,
  `cantidad` bigint(20) NOT NULL,
  `fk_id_empresa` int(11) NOT NULL,
  `fk_id_categoria` int(11) NOT NULL,
  `imagen` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `objeto`
--

INSERT INTO `objeto` (`id`, `precio`, `descripcion`, `garantia`, `nombre`, `cantidad`, `fk_id_empresa`, `fk_id_categoria`, `imagen`) VALUES
(1, 800000, 'terst', '6 meses', 'pocophone', 10, 4, 2, '61ltnpIsyXL._SY879_.jpg'),
(6, 80000, 'test', '2 meses', 'moto', 5, 1, 1, 'Universidad_Industrial_de_Santander_Logo'),
(7, 100000, 'xd123', '4 meses', 'tiopops', 5, 1, 1, 'descarga.jpg');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `oferta`
--

CREATE TABLE `oferta` (
  `fechai` date NOT NULL,
  `fechav` date NOT NULL,
  `titulo` varchar(60) NOT NULL,
  `descripcion` varchar(300) NOT NULL,
  `porcentajedescuento` int(11) NOT NULL,
  `fk_id_empleado` int(11) NOT NULL,
  `fk_id_objeto` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `orden`
--

CREATE TABLE `orden` (
  `id` int(11) NOT NULL,
  `totaldes` bigint(20) DEFAULT NULL,
  `iva` bigint(20) NOT NULL,
  `precioenvio` bigint(20) NOT NULL,
  `total` bigint(20) NOT NULL,
  `fecha` date NOT NULL,
  `fk_id_usuario` int(11) NOT NULL,
  `fk_correo` varchar(30) DEFAULT NULL,
  `fk_id_pago` int(11) NOT NULL,
  `fechaenvio` date NOT NULL,
  `fechaentrega` date DEFAULT NULL,
  `numguia` bigint(20) NOT NULL,
  `estadoentrega` varchar(10) NOT NULL,
  `fk_id_empresae` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pago`
--

CREATE TABLE `pago` (
  `id` int(11) NOT NULL,
  `metodopago` varchar(60) NOT NULL,
  `numerocuotas` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pertenece`
--

CREATE TABLE `pertenece` (
  `id_categoria` int(11) NOT NULL,
  `id_objeto` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `pertenece`
--

INSERT INTO `pertenece` (`id_categoria`, `id_objeto`) VALUES
(1, 7);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reclama`
--

CREATE TABLE `reclama` (
  `descripcion` varchar(200) NOT NULL,
  `estado` varchar(10) NOT NULL DEFAULT 'Pendiente',
  `titulo` varchar(60) NOT NULL,
  `fk_id_objeto` int(11) NOT NULL,
  `fk_id_usuario` int(11) NOT NULL,
  `fk_correo` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `reclama`
--

INSERT INTO `reclama` (`descripcion`, `estado`, `titulo`, `fk_id_objeto`, `fk_id_usuario`, `fk_correo`) VALUES
('no sirve', 'Pendiente', 'no sirve', 1, 2, 'david3@gmail.com');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registra`
--

CREATE TABLE `registra` (
  `id_orden` int(11) NOT NULL,
  `id_objeto` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `cantidad` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tiene`
--

CREATE TABLE `tiene` (
  `id_orden` int(11) NOT NULL,
  `id_pago` int(11) NOT NULL,
  `estadopago` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `correo` varchar(30) NOT NULL,
  `contrasena` varchar(200) NOT NULL,
  `telefono` bigint(20) NOT NULL,
  `dinero` bigint(20) NOT NULL DEFAULT '0',
  `nickname` varchar(30) NOT NULL,
  `genero` varchar(10) NOT NULL,
  `ciudad` varchar(20) NOT NULL,
  `direccion` varchar(30) NOT NULL,
  `codpostal` bigint(20) NOT NULL,
  `departamento` varchar(20) NOT NULL,
  `fchnacimiento` date NOT NULL,
  `puntos` bigint(20) NOT NULL DEFAULT '0',
  `idref` int(11) DEFAULT NULL,
  `correoref` varchar(30) DEFAULT NULL,
  `fk_id_nivel` int(11) NOT NULL DEFAULT '1',
  `fk_numnivel_nivel` int(11) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id`, `nombre`, `correo`, `contrasena`, `telefono`, `dinero`, `nickname`, `genero`, `ciudad`, `direccion`, `codpostal`, `departamento`, `fchnacimiento`, `puntos`, `idref`, `correoref`, `fk_id_nivel`, `fk_numnivel_nivel`) VALUES
(1, 'David rojas', 'dakkas@gmail.com', '$5$rounds=53500', 2342343454, 0, 'david', 'macho', 'bucaramanga', 'calle xd', 2343, 'santander', '0000-00-00', 0, NULL, NULL, 1, 1),
(2, 'David Rojas', 'david3@gmail.com', '$5$rounds=535000$jExBqNrtTsfOUwjw$kLdgX.XSJkpeNI/rFdeAlT0l3tdAvGtD0GXkHKULcUD', 3182993816, 0, 'Davidgd', 'Hombre', 'Bucaramanga', 'Calle 20 # 24-32', 545, 'Santander', '2000-03-03', 0, NULL, NULL, 1, 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `califica`
--
ALTER TABLE `califica`
  ADD PRIMARY KEY (`fk_id_objeto`,`fk_id_usuario`),
  ADD KEY `fk_id_usuarioc` (`fk_id_usuario`,`fk_correo`);

--
-- Indices de la tabla `cargo`
--
ALTER TABLE `cargo`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_id_contrato` (`fk_id_contrato`);

--
-- Indices de la tabla `carrito`
--
ALTER TABLE `carrito`
  ADD PRIMARY KEY (`idusuario`,`correousuario`,`idobjeto`),
  ADD KEY `fk_objeto` (`idobjeto`);

--
-- Indices de la tabla `categoria`
--
ALTER TABLE `categoria`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `contrato`
--
ALTER TABLE `contrato`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `desea`
--
ALTER TABLE `desea`
  ADD PRIMARY KEY (`fk_id_usuario`,`fk_id_objeto`),
  ADD KEY `fk_id_usuariod` (`fk_id_usuario`,`fk_correo`),
  ADD KEY `fk_id_objetod` (`fk_id_objeto`);

--
-- Indices de la tabla `empleado`
--
ALTER TABLE `empleado`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `empresa`
--
ALTER TABLE `empresa`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `empresae`
--
ALTER TABLE `empresae`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `invita`
--
ALTER TABLE `invita`
  ADD PRIMARY KEY (`id_referente`,`id_invitado`),
  ADD KEY `id_referente` (`id_referente`,`correo_referente`),
  ADD KEY `id_invitado` (`id_invitado`,`correo_invitado`);

--
-- Indices de la tabla `nivel`
--
ALTER TABLE `nivel`
  ADD PRIMARY KEY (`id`,`numnivel`);

--
-- Indices de la tabla `noticia`
--
ALTER TABLE `noticia`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `fk_id_empleado` (`fk_id_empleado`);

--
-- Indices de la tabla `objeto`
--
ALTER TABLE `objeto`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_id_empresa` (`fk_id_empresa`),
  ADD KEY `fk_id_categoria` (`fk_id_categoria`);

--
-- Indices de la tabla `oferta`
--
ALTER TABLE `oferta`
  ADD PRIMARY KEY (`fk_id_empleado`,`fk_id_objeto`),
  ADD KEY `fk_id_objetoo` (`fk_id_objeto`);

--
-- Indices de la tabla `orden`
--
ALTER TABLE `orden`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_id_usuarior` (`fk_id_usuario`,`fk_correo`),
  ADD KEY `fk_id_empresae` (`fk_id_empresae`),
  ADD KEY `fk_id_pago` (`fk_id_pago`);

--
-- Indices de la tabla `pago`
--
ALTER TABLE `pago`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `pertenece`
--
ALTER TABLE `pertenece`
  ADD PRIMARY KEY (`id_objeto`,`id_categoria`),
  ADD KEY `id_categoria` (`id_categoria`);

--
-- Indices de la tabla `reclama`
--
ALTER TABLE `reclama`
  ADD PRIMARY KEY (`fk_id_objeto`,`fk_id_usuario`),
  ADD KEY `fk_id_usuariore` (`fk_id_usuario`,`fk_correo`);

--
-- Indices de la tabla `registra`
--
ALTER TABLE `registra`
  ADD PRIMARY KEY (`id_objeto`,`id_orden`),
  ADD KEY `id_orden` (`id_orden`);

--
-- Indices de la tabla `tiene`
--
ALTER TABLE `tiene`
  ADD PRIMARY KEY (`id_orden`,`id_pago`),
  ADD KEY `id_pagot` (`id_pago`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`,`correo`),
  ADD KEY `referido` (`idref`,`correoref`),
  ADD KEY `fk_id_nivel` (`fk_id_nivel`,`fk_numnivel_nivel`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `cargo`
--
ALTER TABLE `cargo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `categoria`
--
ALTER TABLE `categoria`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `contrato`
--
ALTER TABLE `contrato`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `empleado`
--
ALTER TABLE `empleado`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10455;

--
-- AUTO_INCREMENT de la tabla `empresa`
--
ALTER TABLE `empresa`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `empresae`
--
ALTER TABLE `empresae`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `nivel`
--
ALTER TABLE `nivel`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `noticia`
--
ALTER TABLE `noticia`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `objeto`
--
ALTER TABLE `objeto`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `orden`
--
ALTER TABLE `orden`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `pago`
--
ALTER TABLE `pago`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `califica`
--
ALTER TABLE `califica`
  ADD CONSTRAINT `fk_id_objetoc` FOREIGN KEY (`fk_id_objeto`) REFERENCES `objeto` (`id`),
  ADD CONSTRAINT `fk_id_usuarioc` FOREIGN KEY (`fk_id_usuario`,`fk_correo`) REFERENCES `usuario` (`id`, `correo`);

--
-- Filtros para la tabla `cargo`
--
ALTER TABLE `cargo`
  ADD CONSTRAINT `fk_id_contrato` FOREIGN KEY (`fk_id_contrato`) REFERENCES `contrato` (`id`);

--
-- Filtros para la tabla `carrito`
--
ALTER TABLE `carrito`
  ADD CONSTRAINT `fk_objeto` FOREIGN KEY (`idobjeto`) REFERENCES `objeto` (`id`),
  ADD CONSTRAINT `fk_usuario` FOREIGN KEY (`idusuario`,`correousuario`) REFERENCES `usuario` (`id`, `correo`);

--
-- Filtros para la tabla `desea`
--
ALTER TABLE `desea`
  ADD CONSTRAINT `fk_id_objetod` FOREIGN KEY (`fk_id_objeto`) REFERENCES `objeto` (`id`),
  ADD CONSTRAINT `fk_id_usuariod` FOREIGN KEY (`fk_id_usuario`,`fk_correo`) REFERENCES `usuario` (`id`, `correo`);

--
-- Filtros para la tabla `invita`
--
ALTER TABLE `invita`
  ADD CONSTRAINT `id_invitado` FOREIGN KEY (`id_invitado`,`correo_invitado`) REFERENCES `usuario` (`id`, `correo`),
  ADD CONSTRAINT `id_referente` FOREIGN KEY (`id_referente`,`correo_referente`) REFERENCES `usuario` (`id`, `correo`);

--
-- Filtros para la tabla `noticia`
--
ALTER TABLE `noticia`
  ADD CONSTRAINT `fk_id_empleado` FOREIGN KEY (`fk_id_empleado`) REFERENCES `empleado` (`id`);

--
-- Filtros para la tabla `objeto`
--
ALTER TABLE `objeto`
  ADD CONSTRAINT `fk_id_categoria` FOREIGN KEY (`fk_id_categoria`) REFERENCES `categoria` (`id`),
  ADD CONSTRAINT `fk_id_empresa` FOREIGN KEY (`fk_id_empresa`) REFERENCES `empresa` (`id`);

--
-- Filtros para la tabla `oferta`
--
ALTER TABLE `oferta`
  ADD CONSTRAINT `fk_id_empleado2` FOREIGN KEY (`fk_id_empleado`) REFERENCES `empleado` (`id`),
  ADD CONSTRAINT `fk_id_objetoo` FOREIGN KEY (`fk_id_objeto`) REFERENCES `objeto` (`id`);

--
-- Filtros para la tabla `orden`
--
ALTER TABLE `orden`
  ADD CONSTRAINT `fk_id_empresae` FOREIGN KEY (`fk_id_empresae`) REFERENCES `empresae` (`id`),
  ADD CONSTRAINT `fk_id_pago` FOREIGN KEY (`fk_id_pago`) REFERENCES `pago` (`id`),
  ADD CONSTRAINT `fk_id_usuarior` FOREIGN KEY (`fk_id_usuario`,`fk_correo`) REFERENCES `usuario` (`id`, `correo`);

--
-- Filtros para la tabla `pertenece`
--
ALTER TABLE `pertenece`
  ADD CONSTRAINT `id_categoria` FOREIGN KEY (`id_categoria`) REFERENCES `categoria` (`id`),
  ADD CONSTRAINT `id_objetop` FOREIGN KEY (`id_objeto`) REFERENCES `objeto` (`id`);

--
-- Filtros para la tabla `reclama`
--
ALTER TABLE `reclama`
  ADD CONSTRAINT `fk_id_objetore` FOREIGN KEY (`fk_id_objeto`) REFERENCES `objeto` (`id`),
  ADD CONSTRAINT `fk_id_usuariore` FOREIGN KEY (`fk_id_usuario`,`fk_correo`) REFERENCES `usuario` (`id`, `correo`);

--
-- Filtros para la tabla `registra`
--
ALTER TABLE `registra`
  ADD CONSTRAINT `id_objeto` FOREIGN KEY (`id_objeto`) REFERENCES `objeto` (`id`),
  ADD CONSTRAINT `id_orden` FOREIGN KEY (`id_orden`) REFERENCES `orden` (`id`);

--
-- Filtros para la tabla `tiene`
--
ALTER TABLE `tiene`
  ADD CONSTRAINT `id_ordent` FOREIGN KEY (`id_orden`) REFERENCES `orden` (`id`),
  ADD CONSTRAINT `id_pagot` FOREIGN KEY (`id_pago`) REFERENCES `pago` (`id`);

--
-- Filtros para la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD CONSTRAINT `fk_id_nivel` FOREIGN KEY (`fk_id_nivel`,`fk_numnivel_nivel`) REFERENCES `nivel` (`id`, `numnivel`),
  ADD CONSTRAINT `referido` FOREIGN KEY (`idref`,`correoref`) REFERENCES `usuario` (`id`, `correo`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
