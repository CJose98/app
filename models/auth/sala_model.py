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
        query = """SELECT salas.id_sala, salas.nombre_sala
                    FROM user_1.salas INNER JOIN user_1.usuario
                    ON salas.id_sala = usuario.id_user
                    WHERE usuario.correo = %(correo)s"""
        
        params = sala.__dict__
        result = DatabaseConnection.fetch_one(query, params=params) 
        #fetch_all (DEBE OBTENER UNA LISTA O NO )
        if result is not None:
            return cls(
                id_servidor = result[0],
                nombre_servidor = result[1]
            )
        #fijate jose si no te falto for result in results
        # sala=[]
        # append.sala{'nombresala':result[1],
        #             'id_sala':result[0]}
        return None



    