from ...database import DatabaseConnection
#from .user_role_model import UserRoleModel
#from .user_status_model import UserStatusModel
from flask import json

class Sala:

    def __init__(self, **kwargs):
        self.id_servidor = kwargs.get('id_servidor')
        self.nombre_servidor = kwargs.get('nombre_servidor')

    def serialize(self):
        return  {
            "id_servidor": self.id_servidor,
            "nombre_servidor": self.nombre_servidor
            
            #"status": UserStatusModel.get(UserStatusModel(status_id = self.status_id)).serialize(),
            #"role": UserRoleModel.get(UserRoleModel(role_id = self.role_id)).serialize()
        }

    @classmethod
    def get(cls, sala):
        query = """SELECT servidores.id_servidor, servidores.nombre_servidor
                FROM Discor.servidores INNER JOIN Discor.usuarios
                ON servidores.id_servidor = usuarios.id_usuario
                WHERE usuarios.correo = %(correo)s""" #  ver q sea una lista
                            
        params = sala.__dict__
        result = DatabaseConnection.fetch_one(query, params=params) #fetch_all (DEBE OBTENER UNA LISTA O NO )


        if result is not None:
            return cls(
                id_servidor = result[0],
                nombre_servidor = result[1]
            )
        return None



    