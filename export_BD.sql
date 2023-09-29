-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: discor
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `canales`
--

DROP TABLE IF EXISTS `canales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `canales` (
  `id_canal` int NOT NULL AUTO_INCREMENT,
  `nombre_canal` varchar(50) NOT NULL,
  `servidor_id` int NOT NULL,
  `creador_id` int NOT NULL,
  PRIMARY KEY (`id_canal`),
  UNIQUE KEY `nombre_canal` (`nombre_canal`),
  KEY `servidor_id` (`servidor_id`),
  KEY `creador_id` (`creador_id`),
  CONSTRAINT `canales_ibfk_1` FOREIGN KEY (`servidor_id`) REFERENCES `servidores` (`id_servidor`),
  CONSTRAINT `canales_ibfk_2` FOREIGN KEY (`creador_id`) REFERENCES `usuarios` (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `canales`
--

LOCK TABLES `canales` WRITE;
/*!40000 ALTER TABLE `canales` DISABLE KEYS */;
INSERT INTO `canales` VALUES (1,'Club de Lectura',1,1),(2,'Escritores emergentes',2,1),(3,'Recomendaciones',1,2),(4,'Preguntas Tecnicas',6,2),(5,'Proyectos compartidos',1,3),(6,'Recursos utiles',7,3),(7,'Diccionario',7,3);
/*!40000 ALTER TABLE `canales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mensajes`
--

DROP TABLE IF EXISTS `mensajes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mensajes` (
  `id_mensaje` int NOT NULL AUTO_INCREMENT,
  `descripcion_mensaje` text,
  `fecha_hora` datetime DEFAULT CURRENT_TIMESTAMP,
  `canal_id` int NOT NULL,
  `creador_id` int NOT NULL,
  PRIMARY KEY (`id_mensaje`),
  KEY `canal_id` (`canal_id`),
  KEY `creador_id` (`creador_id`),
  CONSTRAINT `mensajes_ibfk_1` FOREIGN KEY (`canal_id`) REFERENCES `canales` (`id_canal`),
  CONSTRAINT `mensajes_ibfk_2` FOREIGN KEY (`creador_id`) REFERENCES `usuarios` (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mensajes`
--

LOCK TABLES `mensajes` WRITE;
/*!40000 ALTER TABLE `mensajes` DISABLE KEYS */;
INSERT INTO `mensajes` VALUES (1,'Canal donde los amantes de la literatura','2023-09-27 12:21:14',1,1),(2,'Este canal está dedicado a los escritores','2023-09-27 12:21:14',2,1),(3,'Este canal está pensado para recomendar','2023-09-27 12:21:14',3,2),(4,'Este canal está pensado para plantear','2023-09-27 12:21:14',4,2),(5,'En este espacio los desarrolladores','2023-09-27 12:21:14',5,3),(6,'En este canal se pueden compartir','2023-09-27 12:21:14',6,3),(7,'mensaje del usuario unido a este servidor','2023-09-27 12:35:10',1,4),(8,'Hola','2023-09-28 13:04:31',1,1);
/*!40000 ALTER TABLE `mensajes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `servidores`
--

DROP TABLE IF EXISTS `servidores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `servidores` (
  `id_servidor` int NOT NULL AUTO_INCREMENT,
  `nombre_servidor` varchar(255) NOT NULL,
  `propietario_id` int NOT NULL,
  PRIMARY KEY (`id_servidor`),
  KEY `propietario_id` (`propietario_id`),
  CONSTRAINT `servidores_ibfk_1` FOREIGN KEY (`propietario_id`) REFERENCES `usuarios` (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servidores`
--

LOCK TABLES `servidores` WRITE;
/*!40000 ALTER TABLE `servidores` DISABLE KEYS */;
INSERT INTO `servidores` VALUES (1,'Literatura Fantastica',1),(2,'Locura Cinematografica',1),(3,'Relatos de Viajes',1),(4,'Salud y Bienestar',1),(5,'Central de Juegos',2),(6,'Fanaticos del Deporte',2),(7,'Caos Musical',3),(10,'Algoritmica',6);
/*!40000 ALTER TABLE `servidores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_servi`
--

DROP TABLE IF EXISTS `user_servi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_servi` (
  `id_user_servi` int NOT NULL AUTO_INCREMENT,
  `usuario_id` int NOT NULL,
  `servidor_id` int NOT NULL,
  PRIMARY KEY (`id_user_servi`),
  KEY `usuario_id` (`usuario_id`),
  KEY `servidor_id` (`servidor_id`),
  CONSTRAINT `user_servi_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id_usuario`),
  CONSTRAINT `user_servi_ibfk_2` FOREIGN KEY (`servidor_id`) REFERENCES `servidores` (`id_servidor`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_servi`
--

LOCK TABLES `user_servi` WRITE;
/*!40000 ALTER TABLE `user_servi` DISABLE KEYS */;
INSERT INTO `user_servi` VALUES (1,1,1),(2,1,2),(3,1,3),(4,1,4),(5,2,5),(6,2,6),(7,3,7),(8,4,1);
/*!40000 ALTER TABLE `user_servi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `apellido` varchar(255) NOT NULL,
  `correo` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `nombre_user` varchar(255) NOT NULL,
  `fecha_nac` date NOT NULL,
  `img_perfil` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'Miguel','Tula','matula77@yahoo.com.ar','123456','Mingo','2000-01-01','https://bit.ly/46hAOe4'),(2,'Celeste','Farfan','CElestef@hotamil.com','456','cele21','2000-01-01','https://bit.ly/46hAOe4'),(3,'Jose','Colque','cjose@gmail.com','741258','CJose98','2000-01-01','https://bit.ly/46hAOe4'),(4,'iiii','rrree','yyy','321','ewew','2000-04-04','https://bit.ly/46hAOe4'),(5,'Lucas','Max','correo@.gmail','123','ser','2000-04-04','fotoNueva'),(6,'juan','lopez','correolopez@','123','lopez_98','2023-02-02','foto');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-28 21:24:59
