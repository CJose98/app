from flask import jsonify
from werkzeug.exceptions import HTTPException
class CustomException(Exception):
    
    def __init__(self, status_code, name = "Custom Error", description = 'Error'): 
        super().__init__()
        self.description = description
        self.name = name
        self.status_code = status_code

    def get_response(self):
        response = jsonify({
            'error': {
                'code': self.status_code,
                'name': self.name,
                'description': self.description,
            }
        })
        response.status_code = self.status_code
        return response
class UserNotFound(Exception):
    
    def __init__(self, status_code, name = "UserNotFound", description = 'Error'): 
        super().__init__()
        self.description = description
        self.name = name
        self.status_code = 404

    def UserNotFound(self):
       response=jsonify({
          
        "error": {
        "code": self.status_code,
        "name": self.name,
        "description": "User with id {id_usuario} not found"
        }
        }
        )
       response.status_code=self.status_code
       return response
class BadRequest(HTTPException):
    def __init__(self, description = "Solicitud incorrecta"):
        super().__init__(description)
        self.status_code = 400
    def get_response(self):
        response = jsonify({
                'error': {
                    'code': self.code,
                    'description': self.description,
                    }
                    })
        response.status_code = self.status_code
        return response    
class InsufficientStorage(HTTPException)    :
    def __init__(self,description='Espacio de Almacenamiento insuficiente'):
      super().__init__(description)
      self.status_code=507
    def get_response(self):
      response=jsonify({
         'error':{'code':self.code,
                  'description':self.description,
         }
      })
      response.status_code=self.status_code
      return response   
   