from ...database import DatabaseConnection
#from .user_role_model import UserRoleModel
#from .user_status_model import UserStatusModel
from flask import request

class User:

    def __init__(self, **kwargs):
        self.id_usuario = kwargs.get('id_usuario')
        self.nombre = kwargs.get('nombre')
        self.apellido = kwargs.get('apellido')
        self.correo = kwargs.get('correo')
        self.password = kwargs.get('password')
        self.nombre_user = kwargs.get('nombre_user')
        self.fecha_nac = kwargs.get('fecha_nac')
        self.img_perfil = kwargs.get('fecha_nac')

    def serialize(self):
        return {
            "id_usuario": self.id_usuario,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "correo": self.correo,
            "password": self.password,
            "nombre_user": self.nombre_user,
            "fecha_nac": self.fecha_nac,
            "img_perfil": self.img_perfil  #faltaba sacar la coma
            #"status": UserStatusModel.get(UserStatusModel(status_id = self.status_id)).serialize(),
            #"role": UserRoleModel.get(UserRoleModel(role_id = self.role_id)).serialize()
        }

    @classmethod
    def is_registered(cls, user):   
        query = """SELECT id_usuario FROM Discor.usuarios 
        WHERE correo = %(correo)s and password = %(password)s"""
        params = user.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return True
        return False
    
    @classmethod
    def get(cls, user):
        query = """SELECT * FROM Discor.usuarios 
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
                fecha_nac = result[6],
                img_perfil = result[7]
            )
        return None
    ##------------------se crea los metodos de creacion y modificacion de items ----#

    @classmethod
    def crear_usuario(cls):
        sql="""INSERT INTO Discor.usuarios (nombre,
                            apellido,
                            correo,
                            password,
                            nombre_user,
                            fecha_nac,
                            img_perfil)
        VALUES(%s,%s,%s,%s,%s,%s,%s,);"""
        params=request.args.get("nombre",""),
        request.args.get("apellido",""),
        request.args.get("correo",""),
        request.args.get("password",""),
        request.args.get("nombre_user",""),
        request.args.get("fecha_nac",""),
        request.args.get("img_perfil","")

        result=DatabaseConnection.execute_query(sql,params)

        if result == None:
            return False
        else:
            return True
    @classmethod
    def modificar_contra(id_usuario):
        sql="""UPDATE Discor.usuarios SET password = %s WHERE id_usuario = %s;"""
        params=request.args.get('password',''),id_usuario
        result=DatabaseConnection.execute_query(sql,params)
        if result == None:
            return False
        else:
             return True
        
    @classmethod
    def modificar_nombre(id_usuario):
        sql="""UPDATE Discor.usuarios SET nombre = %s WHERE id_usuario=%s;"""
        params=request.args.get('nombre',''),id_usuario
        result=DatabaseConnection.execute_query(sql,params)
        if result == None:
            return False
        else:
             return True
        
    @classmethod
    def modificar_nombre_user(id_usuario):
        sql="""UPDATE Discor.usuarios SET nombre_user = %s WHERE id_usuario=%s;"""
        params=request.args.get('nombre_user',''),id_usuario
        result=DatabaseConnection.execute_query(sql,params)
        if result == None:
            return False
        else:
             return True
        
    @classmethod
    def modificar_apellido(id_usuario):
        sql="""UPDATE Discor.usuarios SET apellido = %s WHERE id_usuario=%s;"""
        params=request.args.get('apellido',''),id_usuario
        result=DatabaseConnection.execute_query(sql,params)
        if result == None:
            return False
        else:
             return True
    @classmethod
    def modificar_correo(id_usuario):
        sql="""UPDATE Discor.usuarios SET correo = %s WHERE id_usuario=%s;"""
        params=request.args.get('correo',''),id_usuario
        result=DatabaseConnection.execute_query(sql,params)
        if result == None:
            return False
        else:
             return True
    

    @classmethod
    def modificar_img_perfil(id_usuario):
        sql="""UPDATE Discor.usuarios SET img_perfil = %s WHERE id_usuario=%s;"""
        params=request.args.get('img_perfil',''),id_usuario
        result=DatabaseConnection.execute_query(sql,params)
        if result == None:
            return False
        else:
             return True
        
    @classmethod
    def modificar_fecha_nac(id_usuario):
        sql="""UPDATE Discor.usuarios SET fecha_nac = %s WHERE id_usuario=%s;"""
        params=request.args.get('fecha_nac',''),id_usuario
        result=DatabaseConnection.execute_query(sql,params)
        if result == None:
            return False
        else:
             return True      
        
        
    