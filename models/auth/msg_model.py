from ...database import DatabaseConnection
from flask import request 
from datetime import datetime

class Msg:

    def __init__(self, **kwargs):
        self.nombre=kwargs.get('nombre')
        self.id_mensaje=kwargs.get('id_mensaje')
        self.descripcion_mensaje=kwargs.get('descripcion_mensaje') 
        self.fecha_hora=kwargs.get('fecha_hora')
        self.canal_id=kwargs.get('canal_id')
        self.creador_id=kwargs.get('creador_id')


    def serialize(self):
        return {
            'nombre': self.nombre,
            'id_mensaje': self.id_mensaje,
            'descripcion_mensaje':  self.descripcion_mensaje,
            'fecha_hora':  self.fecha_hora.strftime('%Y-%m-%d %H:%M:%S'),    #self.fecha_hora,  #'fechaHora':   str(datetime.now())    
            'canal_id': self.canal_id,
            'creador_id': self.creador_id                                 
        }   

    @classmethod
    def get(cls, params):
        query = """SELECT usuarios.nombre, mensajes.*
                FROM Discor.usuarios INNER JOIN Discor.mensajes
                ON usuarios.id_usuario = mensajes.creador_id
                INNER JOIN Discor.canales
                ON canales.id_canal = mensajes.canal_id
                WHERE mensajes.canal_id = %(id_canal)s"""

        result = DatabaseConnection.fetch_all(query, params=params) #   =params
    
        if result:
            print("result ***********", result)
            if len(result) == 1:
                # Si solo hay un resultado, devuélvelo como un solo objeto
                return cls(
                    nombre = result[0][0],
                    id_mensaje = result[0][1],
                    descripcion_mensaje = result[0][2],
                    fecha_hora = result[0][3],
                    canal_id = result[0][4],
                    creador_id = result[0][5]
                )
            else:
                # Si hay múltiples resultados, devuélvelos como una lista de objetos
                return [cls(
                    nombre=row[0],
                    id_mensaje=row[1],
                    descripcion_mensaje=row[2],
                    fecha_hora=row[3],
                    canal_id=row[4],
                    creador_id=row[5]
                ) for row in result]

        return []#None


    @classmethod
    def crear_mensaje(cls, params):              
            query  = """INSERT INTO Discor.mensajes (descripcion_mensaje, canal_id, creador_id) VALUES (%(descripcion_mensaje)s,%(id_canal)s,%(creador_id)s)""" #le damos distintos canales y servidores a user_1
            DatabaseConnection.execute_query(query, params=params)
            return True
    

    @classmethod
    def eliminar_mensaje(cls, params):              
            query  = """DELETE FROM Discor.mensajes WHERE id_mensaje = %(id_mensaje)s""" 
            DatabaseConnection.execute_query(query, params=params)
            return True
    


        

        