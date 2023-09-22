from ...database import DatabaseConnection
#from .user_role_model import UserRoleModel
#from .user_status_model import UserStatusModel
from flask import request
from datetime import datetime

class User:

    def __init__(self, **kwargs):
        self.id_mensaje=kwargs.get('id_mensaje')
        self.descripcion_mensaje=kwargs.get('descripcion_mensaje')
        self.fecha_hora=kwargs.get('fecha_hora')
        self.canal_is=kwargs.get('canal_id')
    def serialize(self):
        return {
            'id': self.id_mensaje,
            'descripcionMensaje':  self.descripcion_mensaje ,
            'fechaHora':   str(datetime.now()),
                               
        }    
    @classmethod
    def crear_msg():
        sql="""INSERT INTO Discord.mensajes(descripcion_mensaje,fecha_hora,canal_id)VALUES(%s,%s,%s);"""
        params=request.args.get('descripcion_mensaje',''),request.args.get('fecha_hora',''),request.args.get('canal_id','')
        result=DatabaseConnection.execute_query(sql,params)
        if result == None:
            return False
        else:
             return True
        
    def mostrar_todo(cls):
        sql = """SELECT * FROM mensajes;"""
        result = DatabaseConnection.fetch_one(sql)
        msg=[]
        if result is not  None:
            for resul in result:
                msg.append[{
                    'id_canal':resul[0],
                    'descricion_canal':resul[1],
                    'fecha_hora':resul[2],
                    'canal_id':resul[3]
                    }]
            return msg
        else:
             return {'msg':'no se a creado ningun msg'},400
        