from ...database import DatabaseConnection
#from .user_role_model import UserRoleModel
#from .user_status_model import UserStatusModel

class User:

    def __init__(self, **kwargs):
        self.id_user = kwargs.get('id_user')
        self.nombre = kwargs.get('nombre')
        self.apellido = kwargs.get('apellido')
        self.correo = kwargs.get('correo')
        self.contraseña = kwargs.get('contraseña')
        self.nombre_user = kwargs.get('nombre_user')
        self.fecha_nac = kwargs.get('fecha_nac')

    def serialize(self):
        return {
            "id_user": self.id_user,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "correo": self.correo,
            "contraseña": self.contraseña,
            "nombre_user": self.nombre_user,
            "fecha_nac": self.fecha_nac  #faltaba sacar la coma
            #"status": UserStatusModel.get(UserStatusModel(status_id = self.status_id)).serialize(),
            #"role": UserRoleModel.get(UserRoleModel(role_id = self.role_id)).serialize()
        }

    @classmethod
    def is_registered(cls, user):   
        query = """SELECT id_user FROM user_1.usuario 
        WHERE correo = %(correo)s and nombre_user = %(nombre_user)s"""
        params = user.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return True
        return False
    
    @classmethod
    def get(cls, user):
        query = """SELECT * FROM user_1.usuario 
        WHERE correo = %(correo)s"""
        params = user.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(
                id_user = result[0],
                nombre = result[1],
                apellido = result[2],
                correo = result[3],
                contraseña = result[4],
                nombre_user = result[5],
                fecha_nac = result[6]
            )
        return None