from ...database import DatabaseConnection
#from .user_role_model import UserRoleModel
#from .user_status_model import UserStatusModel
from flask import json

class Sala:

    def __init__(self, **kwargs):
        self.id_servidor = kwargs.get('id_servidor')
        self.nombre_servidor = kwargs.get('nombre_servidor')
        self.propietario_id=kwargs.get('nombre_propietario')

    def serialize(self):
        return  {
            "id_servidor": self.id_servidor,
            "nombre_servidor": self.nombre_servidor,
            "propietario_id":self.propietario_id

            #"status": UserStatusModel.get(UserStatusModel(status_id = self.status_id)).serialize(),
            #"role": UserRoleModel.get(UserRoleModel(role_id = self.role_id)).serialize()
        }

    @classmethod
    def get(cls, user):
        query = """SELECT servidores.id_servidor, servidores.nombre_servidor
                FROM Discor.servidores INNER JOIN Discor.usuarios
                ON servidores.propietario_id = usuarios.id_usuario
                WHERE usuarios.correo = %(correo)s""" #  ver q sea una lista
                            
        params = user.__dict__   #los datos del usuario logeado   #{"correo": user.correo} 
        result = DatabaseConnection.fetch_all(query, params=params) #fetch_all (DEBE OBTENER UNA LISTA) 
    
        if result:
            if len(result) == 1:
                # Si solo hay un resultado, devuélvelo como un solo objeto
                return cls(
                    id_servidor=result[0][0],
                    nombre_servidor=result[0][1]
                )
            else:
                # Si hay múltiples resultados, devuélvelos como una lista de objetos
                return [cls(
                    id_servidor=row[0],
                    nombre_servidor=row[1]
                ) for row in result]

        return [] #None
    ##----------------------------------------------------------##
    ##creo las funcion crear 
    @classmethod
    def create_sala(cls):
        sql = """INSERT INTO discord.servidores(nombre_servidor,
        propietario_id)
        values(%s,%s);"""
        params = (Sala.nombre_servidor,Sala.propietario_id)
        DatabaseConnection.execute_query(sql, params)
        
        if params == None:
            return True
        else:
            return False
        
    #-----------------------------------------------------#
    def get_all_salas(cls):
         sql="SELECT * FROM discord.servidores;"
         results = DatabaseConnection.fetch_all(sql)
         salas=[]
         for result in results:
                salas.append({"Id_Servidor":result[0],
                              "Nombre_Servidor":result[1]
                              })
         return salas,200
        

    
    



    