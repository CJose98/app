from flask import Flask, render_template, request
from app.database.database import DatabaseConnection_4
from config import Config
from .routes.actor_bp import actor_bp


def inicializar_app():
        """Crea y configura la aplicación Flask"""
        app = Flask(__name__)
        app.config.from_object(Config)
        app.register_blueprint(actor_bp)

        @app.route('/')
        def init():
                return render_template ('login.html')
        
        @app.route('/NuevaSala', methods=['post'])
        def crear_sala():
               sql="insert into user_1.salas (Nombre_sala) values(%s);"
               params=request.args.get('nombre_sala','')
               DatabaseConnection_4.execute_query(sql,params)
               return {"msg":"Sala creada con exito "},201
       
        @app.route('/Salas',methods=['GET']) 
        def mostrar_salas():
               sql="SELECT * FROM user_1.salas where id_Salas=%s;"
               results = DatabaseConnection_4.fetch_all(sql)
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
              DatabaseConnection_4.execute_query(sql,params)
              return{"msg":"sala actualizad correctamente"},200
        
        @app.route('/EliminarSala/<int:id_sala>',methods=['DELETE'])
        def eliminarSala(id_sala):
                sql="delete from user_1.salas where id_Salas=%s; "
                params=id_sala
                params=DatabaseConnection_4.execute_query(sql,params)
                return {"msg": "Sala eliminada con éxito"}, 204
        
        #----------------------------------#
        #----------------------------------#
        #----------------------------------#
        @app.route('/users',methods=[''])
        def todos_users ():
              sql="SELECT * FROM user_1.usuario;"
              results=DatabaseConnection_4.fetch_all(sql)
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
        @app.route('/CrearUser',methods=['']) 
        def crear_us():
             sql=""
             params=""
             DatabaseConnection_4.execute_query(sql,params)
             return 
        @app.route('/ModificarUsuario/<int:id_user',methods=['PUT']) 
        def mod_user(id_user):
                sql="UPDATE usuario SET password=%s WHERE user_id= %s;"
                params=request.args.get('password',''),id_user
                DatabaseConnection_4.execute_query(sql,params)
                return 

        #        @app.route('/',methods=['']) 




        # id_user int  

        # Apellido varchar(120) 
        # Nombre varchar(120) 
        # Correo varchar(120) 
        # Contraseña varchar(120) 
        # Nombre_usuario varchar(120) 
        # Fecha_nac
        #         return actors,200


                
                



                return {'msg':'Nombre de Sala Modificada corrwectamente'},200


                def crear_usuario ():
                        pass
        # insert into user_1.usuario (Apellido,Nombre,Correo,Contraseña,Nombre_usuario,Fecha_nac)
        # values(%s,%s,%s,%s,%s,%s),
        # # ('Farfan','Celeste','CElestef@hotamil.com','456','cele21','2-2-2005'),
        # ('Colque','Jose','cjose@gmail.com','741258','CJose98','3/3/2002');

        # SELECT Nombre_sala FROM user_1.salas where id_Salas=5;
        # select Apellido,Nombre,Correo,Nombre_sala from usuario 
        # inner join salas
        # on usuario.user_id=salas.id_Salas
        # where id_user=3;

        # 
        #  UPDATE salas SET Nombre_sala= 'Prueba no boorar' WHERE id_Salas=9;
        # @app.route('/actors/<int:actor_id>',methods=['GET'])
        #     def get_actor(actor_id):
        #         sql="SELECT actor_id,first_name,last_name,last_update FROM sakila.actor WHERE actor_id=%s;"
        #         params = actor_id,
        #         result =DatabaseConnection.fetch_one(sql,params)
        #         if result is not None:
        #             return{
        #                 "id":result[0],
        #                 "nombre":result[1],
        #                 "apellido":result[2],
        #                 "ultima_actualizacion":[3]

        #             },200
        #         return {"msg":"No se registra ingreso "},404
        
        #     @app.route('/actors',methods=['GET'])
        #     def get_actors():
        #         sql="SELECT actor_id,first_name,last_name,last_update FROM sakila.actor WHERE actor_id=%s;"
        #         results = DatabaseConnection.fetch_all(sql)
        #         actors=[]
        #         for result in results:
        #             actors.append({"id":result[0],
        #                           "nombre":result[1],
        #                           "apellido":result[2],
        #                           "ultima_actualizacion":[3]})
        #         return actors,200
        
        #     @app.route('/actors',methods=['POST'])
        #     def create_actor():
        #         sql="INSERT INTO sakila.actor (first_name,last_name,last_update)VALUES(%s,%s,%s);"    
        #         params=request.args.get('first_name',''),request.args.get('last_name',''),request.args.get('last_update','')
        #         DatabaseConnection.execute_query(sql,params)
        #         return {"msg":"Actor creado con exito "},201
        
        #     @app.route('/actors/<int:actor_id>',methods=['PUT'])
        #     def update_actor(actor_id):
        #         sql="UPDATE sakila.actor SET last_update=%s WHERE actor.actor_id=%s;"
        #         params=request.args.get('last_update',''),actor_id
        #         DatabaseConnection.execute_query(sql,params)
        #         return{"msg":"Actualizado correctamente"},200

        #     @app.route('/actors/<int:actor_id>', methods = ['DELETE'])
        #     def delete_actor(actor_id):
        #         sql = "DELETE FROM sakila.actor WHERE actor.actor_id = %s;"
        #         params = actor_id,
        #         DatabaseConnection.execute_query(sql, params)
        #     return {"msg": "Actor eliminado con éxito"}, 204
        
        #     @app.route('/actors/', methods = ['DELETE'])
        #     def delete_actores():
        #         sql = "DELETE FROM sakila.actor;"        
        #         DatabaseConnection.execute_query(sql)
        #         return {"msg": "Actores eliminado con éxito"}, 200

        return app