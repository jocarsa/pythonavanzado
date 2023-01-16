-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 16-01-2023 a las 18:04:26
-- Versión del servidor: 10.4.27-MariaDB
-- Versión de PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `curso`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `Identificador` int(255) NOT NULL,
  `nombre` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `apellidos` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `email` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `telefono` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`Identificador`, `nombre`, `apellidos`, `email`, `telefono`) VALUES
(1, 'Jose Vicente', 'Carratala Sanchis', 'info@josevicentecarratala.com', '1234'),
(2, 'Jose Vicente', 'Carratala Sanchis', 'info@josevicentecarratala.com', '1234'),
(3, 'Jose Vicente', 'Carratala Sanchis', 'info@josevicentecarratala.com', '1234'),
(4, 'Jose Vicente', 'Carratala Sanchis', 'info@josevicentecarratala.com', '1234'),
(5, 'Jose Vicente', 'Carratala Sanchis', 'info@josevicentecarratala.com', '12345678'),
(6, 'Jose Vicente', 'Carratala Sanchis', 'info@josevicentecarratala.com', '1234'),
(7, 'Jose Vicente', 'Carratala Sanchis', 'info@josevicentecarratala.com', '1234'),
(8, 'Jose Vicente', 'Carratala Sanchis', 'info@josevicentecarratala.com', '1234'),
(9, 'Jose Vicente', 'Carratala Sanchis', 'info@josevicentecarratala.com', '1234'),
(10, 'Jose Vicente', 'Carratala Sanchis', 'info@josevicentecarratala.com', '1234'),
(11, 'Jose Vicente', 'Carratala Sanchis', 'info@josevicentecarratala.com', '1234'),
(12, 'Jose Vicente', 'Carratala Sanchis', 'info@josevicentecarratala.com', '1234'),
(13, 'Jose Vicente', 'Carratala Sanchis', 'info@josevicentecarratala.com', '1234'),
(14, 'Jose Vicente', 'Carratala Sanchis', 'info@josevicentecarratala.com', '1234'),
(15, 'Jose Vicente', 'Carratala Sanchis', 'info@josevicentecarratala.com', '1234'),
(16, 'Jose Vicente', 'Carratala Sanchis', 'info@josevicentecarratala.com', '1234'),
(17, 'Jose Vicente', 'Carratala Sanchis', 'info@josevicentecarratala.com', '1234'),
(18, 'Jose Vicente', 'Carratala Sanchis', 'info@josevicentecarratala.com', '1234'),
(19, 'Jose Vicente', 'Carratala Sanchis', 'info@josevicentecarratala.com', '1234');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `Identificador` int(255) NOT NULL,
  `titulo` varchar(100) NOT NULL,
  `descripcion` varchar(255) NOT NULL,
  `precio` decimal(5,2) NOT NULL,
  `imagen` varchar(100) NOT NULL,
  `stock` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`Identificador`, `titulo`, `descripcion`, `precio`, `imagen`, `stock`) VALUES
(1, 'camisa1', 'esta es una buena camisa', '15.34', 'camisa1.jpg', 5);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`Identificador`);

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`Identificador`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `clientes`
--
ALTER TABLE `clientes`
  MODIFY `Identificador` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `Identificador` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
