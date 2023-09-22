from ...database import DatabaseConnection
#from .user_role_model import UserRoleModel
#from .user_status_model import UserStatusModel
from flask import json, request

class User_servi:
    def __init__(self,**kwargs):
        self.id_user_servi=kwargs.get('id_user_servi')
        self.usuario_id=kwargs.get('usuario_id')
        self.servidor_id=kwargs.get('servidor_id')
    def serialize(self)    :
        return{
            'id':self.id_user_servi,
            'usuarioId':self.usuario_id ,
            'servidorId':self.servidor_id
            }
    @classmethod
    def crear_servi():
        sql="""INSERT INTO user_server (usuario_id, servidor_id ) VALUES (%s,%s);"""
        params=request.get('USUARIO_ID',''),request.get('servidor_id','')
        result=DatabaseConnection.execute_query(sql,params)
        if result == None:
            return False
        else:
             return True
        
           
    
        
        