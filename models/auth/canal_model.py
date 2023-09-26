from ...database import DatabaseConnection
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
    def get(cls, params):
        query = """SELECT canales.id_canal, canales.nombre_canal, canales.servidor_id, canales.creador_id
                FROM Discor.canales INNER JOIN Discor.usuarios
                ON canales.creador_id = usuarios.id_usuario
                WHERE usuarios.correo = %(correo)s AND canales.servidor_id = %(servidor_id)s"""
                            
        #params = (user, id_servi)  
        result = DatabaseConnection.fetch_all(query, params=params) #   =params
    
        if result:
            print("result ***********", result)
            if len(result) == 1:
                # Si solo hay un resultado, devuélvelo como un solo objeto
                return cls(
                    id_canal = result[0][0],
                    nombre_canal = result[0][1],
                    servidor_id = result[0][2],
                    creador_id = result[0][3]
                )
            else:
                # Si hay múltiples resultados, devuélvelos como una lista de objetos
                return [cls(
                    id_canal=row[0],
                    nombre_canal=row[1],
                    servidor_id=row[2],
                    creador_id=row[3]
                ) for row in result]

        return []#None
     

    @classmethod
    def crear_canal(cls, params):              
            query  = """INSERT INTO Discor.canales (nombre_canal, servidor_id, creador_id ) VALUES (%(nombre_canal)s,%(servidor_id)s,%(creador_id)s)""" #le damos distintos canales y servidores a user_1
            DatabaseConnection.execute_query(query, params=params)
            return True
