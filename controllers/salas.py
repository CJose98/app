from flask import request, render_template

from app.database.database import DatabaseConnection, DatabaseConnection_2

from ..database import DataBaseConnection_4

from flask import jsonify
class salas_discord:
    def __init__(self,id_Sala=None,Nombre_sala=None):
            self.id_Sala=id_Sala
            self.Nombre_sala=Nombre_sala
            
    @classmethod
    def crear_sala():
               sql="insert into user_1.salas (Nombre_sala) values(%s);"
               params=request.args.get('nombre_sala','')
               DataBaseConnection_4.execute_query(sql,params)
               return {"msg":"Sala creada con exito "},201
    @classmethod
    def mostrar_salas():
               sql="SELECT * FROM user_1.salas where id_Salas=%s;"
               results = DataBaseConnection_4.fetch_all(sql)
               salas=[]
               for result in results:
                salas.append({"Id_Sala":result[0],
                              "Nombre Sala":result[1]
                              })
                return salas,200
               
    @classmethod
    def mod_sala(id_sala):
              sql=" UPDATE salas SET Nombre_sala= %s WHERE id_Salas=%s;"
              params=request.args.get('Nombre_sala',''),id_sala
              DataBaseConnection_4.execute_query(sql,params)
              return{"msg":"sala actualizad correctamente"},200
    @classmethod
    def eliminarSala(id_sala):
                sql="delete from user_1.salas where id_Salas=%s; "
                params=id_sala
                params=DataBaseConnection_4.execute_query(sql,params)
                return {"msg": "Sala eliminada con éxito"}, 204 