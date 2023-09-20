from app.database import DatabaseConnection
from ..models.auth.user_model import User
from ..models.auth.sala_model import Sala
from flask import request, session, jsonify,render_template

class SalaController:

    @classmethod
    def show_sala(cls):
        correo = session.get('correo')                         
        user = User(correo=correo)#user = Sala.get(User(correo = correo))
        if user is None:
            return {"message": "Usuario no encontrado"}, 404
        else:
            salas = Sala.get(user)  # Obtiene una lista de instancias de sala

            if salas:
                if isinstance(salas, Sala):
                    salas = [salas]  # Si salas es un solo objeto Sala, se convierte en una lista

                """serialized_salas = [sala.serialize() for sala in salas]"""
                
                # Crear un diccionario que representa las salas
                serialized_salas = {}
                for index, sala in enumerate(salas, start=1):
                    serialized_salas[f"sala{index}"] = sala.serialize()
                return jsonify(serialized_salas), 200
            else:
                return jsonify({"message": "No se encontraron salas"}), 404
    
    @classmethod
    def logout(cls):
        session.pop('correo', None)
        return {"message": "Sesion cerrada"}, 200
    
    @classmethod
    def crear_servidor():
        crear=Sala.create_sala()
        if crear == None:
            return{"Error":"Ingrese Nombre servidor"},400
        else:
            return {'Msg':'Servidor creado con exito'},200
        
    @classmethod
    def crear_user(cls):
            return render_template("crear_user.html")
        

        
    
