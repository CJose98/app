from flask import Flask
from config import Config
from .routes.actor_bp import actor_bp


def inicializar_app():
        """Crea y configura la aplicación Flask"""
        app = Flask(__name__)
        app.config.from_object(Config)
        app.register_blueprint(actor_bp)

        @app.route('/')
        def init():
                pass#return render_template ('login.html')
        @app.route('/NuevaSala', methods=['post'])
        def sala():
            return crear_sala()
        
#                    insert into user_1.salas (Nombre_sala) values('Literatura Fantastica','Locura Cinematografica','Relatos de Viajes',
# 'Salud y Bienestar','Central de Juegos','Fanaticos del Deporte','Caos Musical'); 

#crear usuario 
# insert into user_1.usuario (Apellido,Nombre,Correo,Contraseña,Nombre_usuario,Fecha_nac)
# values(%s,%s,%s,%s,%s,%s),
# # ('Farfan','Celeste','CElestef@hotamil.com','456','cele21','2-2-2005'),
# ('Colque','Jose','cjose@gmail.com','741258','CJose98','3/3/2002');

# SELECT Nombre_sala FROM user_1.salas where id_Salas=5;
# select Apellido,Nombre,Correo,Nombre_sala from usuario 
# inner join salas
# on usuario.user_id=salas.id_Salas
# where id_user=3;

# delete from user_1.salas where id_Salas=8;
#  UPDATE salas SET Nombre_sala= 'Prueba no boorar' WHERE id_Salas=9;

        return app