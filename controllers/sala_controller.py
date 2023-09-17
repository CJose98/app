from ..models.auth.user_model import User
from ..models.auth.sala_model import Sala
from flask import request, session, jsonify,render_template

class SalaController:

    @classmethod
    def show_sala(cls):
        correo = session.get('correo')
        sala = Sala.get(User(correo = correo))
        if sala is None:
            return {"message": "Usuario no encontrado"}, 404
        else:
            return sala.serialize(), 200 #cambiar debe redigir a la pagina
    
    @classmethod
    def logout(cls):
        session.pop('correo', None)
        return {"message": "Sesion cerrada"}, 200