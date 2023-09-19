from flask import request, render_template
from ..database import DatabaseConnection

from flask import jsonify
class salas_discord:
    def __init__(self,id_sala=None,nombre_sala=None):
            self.id_sala=id_sala
            self.nombre_sala=nombre_sala
            
    @classmethod
    def crear_sala():
               sql="insert into user_1.salas (nombre_sala) values(%s);"
               params=request.args.get('nombre_sala','')
               DatabaseConnection.execute_query(sql,params)
               return {"msg":"Sala creada con exito "},201
    @classmethod
    def mostrar_salas():
               sql="SELECT * FROM user_1.salas where id_sala=%s;"
               results = DatabaseConnection.fetch_all(sql)
               salas=[]
               for result in results:
                salas.append({"Id_sala":result[0],
                              "nombre Sala":result[1]
                              })
                return salas,200
               
    @classmethod
    def mod_sala(id_sala):
              sql=" UPDATE salas SET nombre_sala= %s WHERE id_sala=%s;"
              params=request.args.get('nombre_sala',''),id_sala
              DatabaseConnection.execute_query(sql,params)
              return{"msg":"sala actualizad correctamente"},200
    @classmethod
    def eliminarSala(id_sala):
                sql="delete from user_1.salas where id_sala=%s; "
                params=id_sala
                params=DatabaseConnection.execute_query(sql,params)
                return {"msg": "Sala eliminada con éxito"}, 204 