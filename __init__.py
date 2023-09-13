from flask import Flask, render_template, request,Blueprint
from app.database.database import DataBaseConnection_4
from config import Config
from .routes.sala_bp import sala_bp
from .routes.user_pb import user_bp


def inicializar_app():
        """Crea y configura la aplicación Flask"""
        app = Flask(__name__)
        app.config.from_object(Config)
        #app.register_blueprint(actor_bp)
        sala_bp = Blueprint('sala_bp',__name__)
        user_bp=Blueprint('Users')


        @app.route('/')
        def init():
                return render_template ('login.html')
        
        @app.route('/NuevaSala', methods=['post'])
        def crear_sala():
               sql="insert into user_1.salas (Nombre_sala) values(%s);"
               params=request.args.get('nombre_sala','')
               DataBaseConnection_4.execute_query(sql,params)
               return {"msg":"Sala creada con exito "},201
       
        @app.route('/Salas',methods=['GET']) 
        def mostrar_salas():
               sql="SELECT * FROM user_1.salas where id_Salas=%s;"
               results = DataBaseConnection_4.fetch_all(sql)
               salas=[]
               for result in results:
                salas.append({"Id_Sala":result[0],
                              "Nombre Sala":result[1]
                              })
                return salas,200
        
        @app.route('/ModificarSalas/<int:sala_id>',methods=['PUT'])
        def mod_sala(id_sala):
              sql=" UPDATE salas SET Nombre_sala= %s WHERE id_Salas=%s;"
              params=request.args.get('Nombre_sala',''),id_sala
              DataBaseConnection_4.execute_query(sql,params)
              return{"msg":"sala actualizad correctamente"},200
        
        @app.route('/EliminarSala/<int:id_sala>',methods=['DELETE'])
        def eliminarSala(id_sala):
                sql="delete from user_1.salas where id_Salas=%s; "
                params=id_sala
                params=DataBaseConnection_4.execute_query(sql,params)
                return {"msg": "Sala eliminada con éxito"}, 204
        
        #----------------------------------#
        #----app para usuario------------------------------#
        #----------------------------------#
        @app.route('/users',methods=['GET'])
        def todos_users ():
              sql="SELECT * FROM user_1.usuario;"
              results=DataBaseConnection_4.fetch_all(sql)
              Usuarios=[]
              for result in results:
                   Usuarios.append({"Id_Usuario":result[0],
                          "Apellido ":result[1],
                          "Nombre":result[2],
                          "Correo":[3],
                          "Pass":[4],
                          "Nombre Usuario":[5],
                          "fecha Nacimiento":[6],
                          })
              return Usuarios,200  
        @app.route('/CrearUser',methods=['POST']) 
        def crear_us():
             sql="insert into user_1.usuario (Apellido,Nombre,Correo,Contraseña,Nombre_usuario,Fecha_nac)values(%s,%s,%s,%s,%s,%s);"
             params=request.args.get('Apellido',''),request.args.get('Nombre',''),request.args.get('Correo',''),
             request.args.get('Contraseña',''),request.args.get('Nombre_usuario',''),request.args.get('Fecha_nac','')
             DataBaseConnection_4.execute_query(sql,params)
             return {'msg':'Usuario Creado con exito'},201
        @app.route('/ModificarUsuario/<int:id_user',methods=['PUT']) 
        def mod_user(id_user):
                sql="UPDATE usuario SET password=%s WHERE user_id= %s;"
                params=request.args.get('password',''),id_user
                DataBaseConnection_4.execute_query(sql,params)
                return {'msg':'Usuario Modificado  con exito'},201
        @app.route('/EliminarUser/<int:id_us>',methods=['DELETE'])
        def eliminarUs(id_user):
                sql="delete from usuario where id_user=%s;"
                params=request.args.get(id_user)
                DataBaseConnection_4.execute_query(sql,params)
                return {"msg": "Actores eliminado con éxito"}, 200

         # id_user int  

        
        return app