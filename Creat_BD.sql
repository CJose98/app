CREATE DATABASE Discor;
USE Discor;

CREATE TABLE IF NOT EXISTS usuarios (
  id_usuario INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(255) NOT NULL,
  apellido VARCHAR(255) NOT NULL,
  correo VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  nombre_user VARCHAR(255) NOT NULL,
  fecha_nac DATE NOT NULL,
  img_perfil VARCHAR(255)
);
CREATE TABLE IF NOT EXISTS servidores (
  id_servidor INT AUTO_INCREMENT PRIMARY KEY,
  nombre_servidor VARCHAR(255) NOT NULL,
  propietario_id INT NOT NULL,
  FOREIGN KEY (propietario_id) REFERENCES usuarios(id_usuario)
);
CREATE TABLE IF NOT EXISTS user_servi (
  id_user_servi INT AUTO_INCREMENT PRIMARY KEY,
  usuario_id INT NOT NULL,
  servidor_id INT NOT NULL,
  FOREIGN KEY (usuario_id) REFERENCES usuarios(id_usuario),
  FOREIGN KEY (servidor_id) REFERENCES servidores(id_servidor)
);
CREATE TABLE IF NOT EXISTS canales (
  id_canal INT AUTO_INCREMENT PRIMARY KEY,
  nombre_canal VARCHAR(50) NOT NULL UNIQUE,
  servidor_id INT NOT NULL,
  creador_id INT NOT NULL,
  FOREIGN KEY (servidor_id) REFERENCES servidores(id_servidor),
  FOREIGN KEY (creador_id) REFERENCES usuarios(id_usuario)
);
CREATE TABLE IF NOT EXISTS mensajes (
  id_mensaje INT AUTO_INCREMENT PRIMARY KEY,
  descripcion_mensaje TEXT,
  fecha_hora DATETIME DEFAULT NOW(),
  canal_id INT NOT NULL,
  FOREIGN KEY (canal_id) REFERENCES canales(id_canal)
);


/* CREAR DATOS PARA EL USUARIO*******************************************************************/
INSERT INTO Discor.usuarios (nombre, apellido, correo, password, nombre_user, fecha_nac, img_perfil) VALUES
('Miguel','Tula','matula77@yahoo.com.ar','123456','Mingo','2000-01-01','https://bit.ly/46hAOe4'),
('Celeste','Farfan','CElestef@hotamil.com','456','cele21','2000-01-01','https://bit.ly/46hAOe4'),
('Jose','Colque','cjose@gmail.com','741258','CJose98','2000-01-01','https://bit.ly/46hAOe4');

/* CREAR DATOS PARA EL SERVIDOR*******************************************************************/
INSERT INTO Discor.servidores (nombre_servidor, propietario_id) VALUES 
('Literatura Fantastica',1),('Locura Cinematografica',1),('Relatos de Viajes',1),('Salud y Bienestar',1),
('Central de Juegos',2),('Fanaticos del Deporte',2),
('Caos Musical',3);

/* CREAR DATOS PARA EL CANAL*********************************************************************/
INSERT INTO Discor.canales (nombre_canal, servidor_id, creador_id) VALUES 
('Club de Lectura',1,1),('Escritores emergentes',2,1),   /*le damos distintos canales y servidores a user_1*/
('Recomendaciones',1,2),('Preguntas Tecnicas',6,2),     /*le damos un servidor de user_1 y un canal propitario a user_2*/
('Proyectos compartidos',1,3),('Recursos utiles',7,3); /*le damos un servidor de user_1 y un canal propitario a user_3*/

/* CREAR DATOS PARA EL MENSAJE*******************************************************************/
INSERT INTO Discor.mensajes (descripcion_mensaje, fecha_hora, canal_id) VALUES 
('Canal donde los amantes de la literatura',NOW(),1),('Este canal está dedicado a los escritores',NOW(),2),('Este canal está pensado para recomendar',NOW(),3),
('Este canal está pensado para plantear',NOW(),4),('En este espacio los desarrolladores',NOW(),5),('En este canal se pueden compartir',NOW(),6);

INSERT INTO Discor.user_servi (usuario_id, servidor_id) VALUES
(1,1),(1,2),(1,3),(1,4), /* unimos el user --> servidor*/
(2,5),(2,6),
(3,7);


/*++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*/


/*1. Búsqueda de Usuario por Correo Electrónico y Contraseña:
Teniendo el correo electrónico y la contraseña del usuario en sesión y desea obtener su información de usuario:
Esta consulta devuelve filas, significa que el usuario en sesión ha proporcionado credenciales válidas y puede acceder a su información de usuario.*/
SELECT * FROM usuarios
WHERE correo = 'cjose@gmail.com' AND password = '741258';

/*2. Búsqueda de Servidores a los que Pertenece el Usuario:
Para encontrar los servidores a los que pertenece el usuario en sesión, Teniendo el id_usuario del usuario en sesión:
Esta consulta devuelve todos los servidores a los que el usuario en sesión pertenece.*/
SELECT id_usuario
FROM Discor.usuarios
WHERE correo = 'cjose@gmail.com' AND password = '741258'; /*retorna el id user*/

SELECT servidores.*
FROM Discor.servidores
INNER JOIN user_servi ON servidores.id_servidor = user_servi.servidor_id
WHERE user_servi.usuario_id = 1; /*'id_usuario_en_sesion'*/

SELECT servidores.id_servidor, servidores.nombre_servidor
FROM Discor.servidores INNER JOIN Discor.usuarios
ON servidores.propietario_id = usuarios.id_usuario
WHERE usuarios.correo = 'matula77@yahoo.com.ar'; /*'cjose@gmail.com';*/

/*3. Búsqueda de Canales en un Servidor Seleccionado:
Teniendo el id_servidor del servidor seleccionado y deseas encontrar los canales en ese servidor:
Esta consulta devuelve una lista de canales en el servidor seleccionado.*/
SELECT canales.* 
FROM Discor.canales
WHERE canales.servidor_id = 1;  /*'id_servidor_seleccionado'*/

/*4. Cambio de Imagen del usuario*/
UPDATE Discor.usuarios
SET img_perfil = 'https://bit.ly/46hAOe4' /*'nueva_url_o_nombre_de_archivo'*/
WHERE id_usuario = 1;                    /* id_usuario_en_sesion */

/*5. Búsqueda de Mensajes en un Canal Seleccionado:
Para obtener los mensajes en un canal seleccionado, se puede usar el id_canal del canal seleccionado:*/
SELECT mensajes.*
FROM Discor.mensajes
WHERE mensajes.canal_id = 1; /*'id_canal_seleccionado';*/



/* AHORA VEMOS CUANDO UN USUARIO QUIERE UNIRSE A UN SERVIDOR     (practicamos con un usuario nuevo) ****************************************/

/*6. Creacion de un nuevo usuario  (FALTA - REEMPLAZAR )*/
INSERT INTO Discor.usuarios (nombre, apellido, correo, password, nombre_user, fecha_nac, img_perfil) VALUES
('Nuevo','Nuevo','Nuevo@.com','12','Nuev','2000-01-01','https://bit.ly/46hAOe4');


/*7. Actualización de la Base de Datos:		"EN CASO DE QUE EL USUARIO YA ESTE LOGEADO Y QUIERA UNIRSE A MAS SERVIDORES TAMBIEN APLICAMOS ESTE CODIGO"
Cuando un usuario decide unirse a un servidor, 
Realizamos una inserción en la tabla user_servi para registrar su user_servi en ese servidor.*/
INSERT INTO Discor.user_servi (usuario_id, servidor_id) /*nuevo_usuario_id, servidor_existente_id*/
VALUES (4,1);                                     

/*8. Creacion de un canal nuevo    */
INSERT INTO Discor.canales (nombre_canal, servidor_id, creador_id) VALUES 
('Python lectura',1,4);  /*le damos distintos canales y servidores a user_1*/

/*9. Creacion de un mensaje nuevo */
INSERT INTO Discor.mensajes (descripcion_mensaje, fecha_hora, canal_id) VALUES
('Canal de programar python',NOW(),1);



SELECT * FROM usuarios;
SELECT * FROM servidores;
SELECT * FROM user_servi;
SELECT * FROM canales;
SELECT * FROM mensajes;




