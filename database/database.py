import mysql.connector

"""
La clase DatabaseConnection cuenta con métodos para realizar consultas
a la base de datos. En particular queremos hacer mención del atributo 
de clase _connection, el cual nos permitirá mantener una única conexión a 
la base de datos durante toda la ejecución de la aplicación.
"""
class DatabaseConnection:
    _connection = None
    @classmethod
    def get_connection(cls):
        if cls._connection is None:
                cls._connection = mysql.connector.connect(
                    host='localhost', #'127.0.0.1',
                    user='root',
                    port = "3306",
                    password='root',
                    database='sales'
            )
        return cls._connection
    """ 
    el método execute_query, el cual creará un cursor, ejecutará 
    la consulta indicada en el parámetro query y finalizará la transacción. 
    Finalmente, devolverá el cursor para que otros métodos puedan interactuar con él.
    """
    @classmethod
    def execute_query(cls, query, params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute(query, params)
        cls._connection.commit()
        return cursor
    
    """
    Los métodos que vemos aquí permiten devolver los resultset correspondientes 
    a las consultas ejecutadas con el método que vimos previamente. Estos pueden 
    ser para una única fila o para todas. Por supuesto, podríamos crear un 
    tercer método que permita obtener una cantidad determinada.
    """
    @classmethod
    def fetch_all(cls, query, params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute(query, params)
        return cursor.fetchall()

    @classmethod
    def fetch_one(cls, query, params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute(query, params)
        return cursor.fetchone()
    """
    Por último, necesitaremos una manera de cerrar la conexión que establecimos.
    Mediante esta clase se plantea emplear una única conexión para gestionar la
    comunicación con la base de datos, lo cual puede traer beneficios y desventajas. 
    """
    @classmethod
    def close_connection(cls):
        if cls._connection is not None:
            cls._connection.close()
            cls._connection = None

class DatabaseConnection_2:
    _connection = None
    @classmethod
    def get_connection(cls):
        if cls._connection is None:
                cls._connection = mysql.connector.connect(
                    host='localhost', #'127.0.0.1',
                    user='root',
                    port = "3306",
                    password='root',
                    database='production'
            )
        return cls._connection
    """ 
    el método execute_query, el cual creará un cursor, ejecutará 
    la consulta indicada en el parámetro query y finalizará la transacción. 
    Finalmente, devolverá el cursor para que otros métodos puedan interactuar con él.
    """
    @classmethod
    def execute_query(cls, query, params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute(query, params)
        cls._connection.commit()
        return cursor
    """
    Los métodos que vemos aquí permiten devolver los resultset correspondientes 
    a las consultas ejecutadas con el método que vimos previamente. Estos pueden 
    ser para una única fila o para todas. Por supuesto, podríamos crear un 
    tercer método que permita obtener una cantidad determinada.
    """
    @classmethod
    def fetch_all(cls, query, params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute(query, params)
        return cursor.fetchall()

    @classmethod
    def fetch_one(cls, query, params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute(query, params)
        return cursor.fetchone()
    """
    Por último, necesitaremos una manera de cerrar la conexión que establecimos.
    Mediante esta clase se plantea emplear una única conexión para gestionar la
    comunicación con la base de datos, lo cual puede traer beneficios y desventajas. 
    """
    @classmethod
    def close_connection(cls):
        if cls._connection is not None:
            cls._connection.close()
            cls._connection = None
class DataBaseConnection1:
    _connection=None
    @classmethod
    def get_connection(cls):
        if cls._connection is None:
            cls._connection=mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                port="3306",
                password="123456",
                database="sakila",
                )
            return  cls._connection
    @classmethod
    def execute_query(cls,query,params=None):
        cursor=cls.get_connection().cursor()
        cursor.execute(query,params)
        cls._connection.commit()
        return cursor
    @classmethod
    def fetch_one(cls,query,params=None):
        cursor=cls.get_connection().cursor()
        cursor.execute(query,params)
        return cursor.fetchone()
    @classmethod
    def fetch_all(cls,query,params=None):
            
        cursor=cls.get_connection().cursor()
        cursor.execute(query,params)
        return cursor.fetchall()
    @classmethod
    def close_connection(cls):
        if cls._connection is not None:
            cls._connection.close()
            cls._connection =None
class DataBaseConnection_4:
    _connection=None
    @classmethod
    def get_connection(cls):
        if cls._connection is None:
            cls._connection=mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                port="3306",
                password="123456",
                database="user_1",
                )
            return  cls._connection
    @classmethod
    def execute_query(cls,query,params=None):
        cursor=cls.get_connection().cursor()
        cursor.execute(query,params)
        cls._connection.commit()
        return cursor
    @classmethod
    def fetch_one(cls,query,params=None):
        cursor=cls.get_connection().cursor()
        cursor.execute(query,params)
        return cursor.fetchone()
    @classmethod
    def fetch_all(cls,query,params=None):
            
        cursor=cls.get_connection().cursor()
        cursor.execute(query,params)
        return cursor.fetchall()
    @classmethod
    def close_connection(cls):
        if cls._connection is not None:
            cls._connection.close()
            cls._connection =None            