#from ..models.actor_model import Actor
#from ..routes.actor_bp import Actor
from flask import request, render_template

from app.database.database import DatabaseConnection, DatabaseConnection_2

from ..database import DataBaseConnection_4

from flask import jsonify

print("Hola mundo! 2")


class App_Discor:
    def __init__(self,id_user=None,Apellido=None,Nombre=None,Correo=None,password=None,Nombre_usuario=None,Fecha_nac=None):
            #Contructor
            self.id_user=id_user
            self.Apellido=Apellido
            self.Nombre=Nombre
            self.Correo=Correo
            self.password=password#cambniar despuesde cambia db Password
            self.Nombre_usuario=Nombre_usuario
            self.Fecha_nac=Fecha_nac
    
    @classmethod
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
    @classmethod
    def crear_us():
             sql="insert into user_1.usuario (Apellido,Nombre,Correo,Contraseña,Nombre_usuario,Fecha_nac)values(%s,%s,%s,%s,%s,%s);"
             params=request.args.get('Apellido',''),request.args.get('Nombre',''),request.args.get('Correo',''),
             request.args.get('Contraseña',''),request.args.get('Nombre_usuario',''),request.args.get('Fecha_nac','')
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
    
   