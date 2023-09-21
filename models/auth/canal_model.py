from ...database import DatabaseConnection
#from .user_role_model import UserRoleModel
#from .user_status_model import UserStatusModel
from flask import json, request

class Canal:
     
     def __init__(self, **kwargs):
        self.id_canal = kwargs.get('id_canal')
        self.nombre_canal = kwargs.get('nombre_canal')
        self.servidor_id=kwargs.get('servidor_id')
        self.creador_id=kwargs.get('creador_id')

     def serialize(self):
        return  {
            "id_canal": self.id_canal,
            "nombre_canal": self.nombre_canal,
            "servidor_id":self.servidor_id,
            "creador_id":self.creador_id
            }
     @classmethod
     def crear_canal():
        sql="""INSERT INTO Discord.canales(nombre_canal,serviDor_id,creador_id)VALUES(%s,%s,%s,);"""
        params=request.args.get('nombre_canal',''),request.args.get('servidor_id',''),request.args.get('creador_id','')
        result=DatabaseConnection.execute_query(sql,params)
        if result==None:
            return False
        else:
            return True
        
     @classmethod
     def eliminar_canal()  :
         sql="""
            DELETE FROM Discord.canales WHERE id_canal =%s;""" 
         result=DatabaseConnection.execute_query(sql)
         if result==None:
             return False
         else:
             return True

     @classmethod
     def mod_canal(id_canal):
         sql="""
         update Discord.canales set nombre_canal=%s where id_canal=%s;"""
         params=request.args.get('nombre_canal',''),id_canal
         result=DatabaseConnection.execute_query(sql,params)
         if result==None:
                return False
         else:
                return True