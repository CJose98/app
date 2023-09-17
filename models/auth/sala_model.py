from ...database import DatabaseConnection
#from .user_role_model import UserRoleModel
#from .user_status_model import UserStatusModel
from flask import json

class Sala:

    def __init__(self, **kwargs):
        self.id_sala = kwargs.get('id_sala')
        self.nombre_sala = kwargs.get('nombre_sala')

    def serialize(self):
        return  {
            "id_sala": self.id_sala,
            "nombre_sala": self.nombre_sala
            
            #"status": UserStatusModel.get(UserStatusModel(status_id = self.status_id)).serialize(),
            #"role": UserRoleModel.get(UserRoleModel(role_id = self.role_id)).serialize()
        }

    @classmethod
    def get(cls, sala):
        query = """SELECT salas.id_sala, salas.nombre_sala
                    FROM user_1.salas INNER JOIN user_1.usuario
                    ON salas.id_sala = usuario.id_user
                    WHERE usuario.correo = %(correo)s"""
        
        params = sala.__dict__
        result = DatabaseConnection.fetch_one(query, params=params) #fetch_all (DEBE OBTENER UNA LISTA O NO )


        if result is not None:
            return cls(
                id_sala = result[0],
                nombre_sala = result[1]
            )
        return None



    