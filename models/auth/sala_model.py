from ...database import DatabaseConnection

class Sala:

    def __init__(self, **kwargs):
        self.id_servidor = kwargs.get('id_servidor')
        self.nombre_servidor = kwargs.get('nombre_servidor') 
        self.propietario_id = kwargs.get('propietario_id')                     #propietario_id,#falta poner el propietario

    def serialize(self):
        return  {
            "id_servidor": self.id_servidor,
            "nombre_servidor": self.nombre_servidor,
            "propietario_id": self.propietario_id
        }

    @classmethod
    def get(cls, user):

        query = """SELECT servidores.id_servidor, servidores.nombre_servidor, servidores.propietario_id
                FROM Discor.servidores
                INNER JOIN Discor.user_servi
                ON servidores.id_servidor = user_servi.servidor_id
                WHERE user_servi.usuario_id =  %(id_usuario)s""" #  ver q sea una lista
                            
        params = user  #los datos del usuario logeado   #{"correo": user.correo} 
        result = DatabaseConnection.fetch_all(query, params=params) #fetch_all (DEBE OBTENER UNA LISTA) 
    
        if result:
            if len(result) == 1:
                # Si solo hay un resultado, devuélvelo como un solo objeto
                return cls(
                    id_servidor=result[0][0],
                    nombre_servidor=result[0][1],
                    propietario_id=result[0][2]
                )
            else:
                # Si hay múltiples resultados, devuélvelos como una lista de objetos
                return [cls(
                    id_servidor=row[0],
                    nombre_servidor=row[1],
                    propietario_id=row[2]
                ) for row in result]

        return []#None

        

    @classmethod
    def crear_servidor(cls, params):              
            query  = """INSERT INTO Discor.servidores (nombre_servidor, propietario_id) VALUES (%(nombre_servidor)s,%(propietario_id)s)"""
            #params = serv.__dict__
            DatabaseConnection.execute_query(query, params=params)
            return True









    

    
    """if result is not None:
            return cls(
                id_servidor = result[0],
                nombre_servidor = result[1]
            )
        return None"""
    






    