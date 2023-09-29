from ...database import DatabaseConnection

class User: 

    def __init__(self, **kwargs):
        self.id_usuario = kwargs.get('id_usuario') 
        self.nombre = kwargs.get('nombre')
        self.apellido = kwargs.get('apellido')
        self.correo = kwargs.get('correo')
        self.password = kwargs.get('password')
        self.nombre_user = kwargs.get('nombre_user')
        self.fecha_nac = kwargs.get('fecha_nac')
        self.img_perfil = kwargs.get('img_perfil')

    def serialize(self):
        return {
            "id_usuario": self.id_usuario,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "correo": self.correo,
            "password": self.password,
            "nombre_user": self.nombre_user,
            "fecha_nac": self.fecha_nac,
            "img_perfil": self.img_perfil 
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
                id_usuario = result[0],
                nombre = result[1],
                apellido = result[2],
                correo = result[3],
                contraseña = result[4],
                nombre_user = result[5],
                fecha_nac = result[6],
                img_perfil = result[7]
            )
        return None
    
    
    @classmethod
    def crear_usuario(cls, user):              
            query  = """INSERT INTO Discor.usuarios (nombre, apellido, correo, password, nombre_user, fecha_nac) VALUES (%(nombre)s,%(apellido)s,%(correo)s,%(password)s,%(nombre_user)s,%(fecha_nac)s)"""
            params = user.__dict__
            DatabaseConnection.execute_query(query, params=params)
            return True
    
    @classmethod
    def mod_perfil(cls, params):            
            query  = """UPDATE Discor.usuarios SET img_perfil = %(img_perfil)s WHERE usuarios.id_usuario = %(id_usuario)s"""
            DatabaseConnection.execute_query(query, params=params)
            return True
    
    @classmethod
    def mod_user(cls, params):            
            query  = """UPDATE Discor.usuarios SET nombre_user = %(nombre_user)s WHERE usuarios.id_usuario = %(id_usuario)s"""
            DatabaseConnection.execute_query(query, params=params)
            return True
    
    @classmethod
    def mod_nombre(cls, params):            
            query  = """UPDATE Discor.usuarios SET nombre = %(nombre)s WHERE usuarios.id_usuario = %(id_usuario)s"""
            DatabaseConnection.execute_query(query, params=params)
            return True
    
    @classmethod
    def mod_apellido(cls, params):            
            query  = """UPDATE Discor.usuarios SET apellido = %(apellido)s WHERE usuarios.id_usuario = %(id_usuario)s"""
            DatabaseConnection.execute_query(query, params=params)
            return True
    @classmethod
    def mod_correo(cls, params):            
            query  = """UPDATE Discor.usuarios SET correo = %(correo)s WHERE usuarios.id_usuario = %(id_usuario)s"""
            DatabaseConnection.execute_query(query, params=params)
            return True
    
    @classmethod
    def mod_contra(cls, params):            
            query  = """UPDATE Discor.usuarios SET password = %(password)s WHERE usuarios.id_usuario = %(id_usuario)s"""
            DatabaseConnection.execute_query(query, params=params)
            return True
