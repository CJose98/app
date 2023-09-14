#from ..models.actor_model import Actor
#from ..routes.actor_bp import Actor
from flask import request, render_template

from app.database.database import DatabaseConnection, DatabaseConnection_2

from ..database import DataBaseConnection_4

from flask import jsonify

print("Hola mundo! 2")


class App_Discor:
    def __init__(self,id_user=None,apellido=None,nombre=None,correo=None,password=None,nombre_usuario=None,fecha_nac=None):
            #Contructor
            self.id_user=id_user
            self.nombre=nombre
            self.apellido=apellido
            self.correo=correo
            self.password=password
            self.nombre_usuario=nombre_usuario
            self.fecha_nac=fecha_nac
    
    @classmethod
    def todos_users ():
              sql="SELECT * FROM user_1.usuario;"
              results=DataBaseConnection_4.fetch_all(sql)
              Usuarios=[]
              for result in results:
                   Usuarios.append({"Id_Usuario":result[0],
                          "Nombre":result[1],
                          "Apellido ":result[2],
                          "Correo":[3],
                          "Pass":[4],
                          "Nombre Usuario":[5],
                          "fecha Nacimiento":[6],
                          })
              return Usuarios,200  
    @classmethod
    def crear_us():
             sql="insert into user_1.usuario (apellido,nombre,correo,password,nombre_usuario,fecha_nac)values(%s,%s,%s,%s,%s,%s);"
             params=request.args.get('apellido',''),request.args.get('nombre',''),request.args.get('correo',''),
             request.args.get('password',''),request.args.get('nombre_usuario',''),request.args.get('fecha_nac','')
             DataBaseConnection_4.execute_query(sql,params)
             return {'msg':'Usuario Creado con exito'},201
    @classmethod
    def mod_user(id_user):
                sql="UPDATE usuario SET password=%s WHERE user_id= %s;"
                params=request.args.get('password',''),id_user
                DataBaseConnection_4.execute_query(sql,params)
                return {'msg':'Usuario Modificado  con exito'},201
    @classmethod
    def eliminarUs(id_user):
                sql="delete from usuario where id_user=%s;"
                params=request.args.get(id_user)
                DataBaseConnection_4.execute_query(sql,params)
                return {"msg": "Actores eliminado con éxito"}, 200           
               
            
            
    ##---------------------------------------##
    # se tendria que eliminar esto para que quede mas prolijo el trabajo 
    
   