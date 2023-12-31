from ..models.auth.user_model import User
from ..models.auth.sala_model import Sala
from flask import request, session, json, jsonify,render_template

class SalaController:

    @classmethod
    def show_sala(cls):
        correo = session.get('correo')                         
        user = User(correo=correo) #user = Sala.get(User(correo = correo)) 

         # método para obtener el usuario a partir del correo en la sesión
        b_user = User()
        b_user.correo = correo
        b_user = User.get(b_user)  # Utiliza el método get para obtener el usuario completo


        id_usuario = b_user.id_usuario # Obtiene el id del usuario encontrado
        print("Id USUARIO:", id_usuario)

        if user is None:
            return {"message": "Usuario no encontrado"}, 404
        else:
            salas = Sala.get({"id_usuario": id_usuario})  # Obtiene una lista de instancias de sala

            if salas:
                if isinstance(salas, Sala):
                    salas = [salas]  # Si salas es un solo objeto Sala, se convierte en una lista
                
                # Crear un diccionario que representa las salas
                serialized_salas = {}
                for index, sala in enumerate(salas, start=1):
                    serialized_salas[f"sala{index}"] = sala.serialize()
                return jsonify(serialized_salas), 200
            
            if salas:
                return jsonify({"message": "Usuario no tiene servidores"}), 200
            
            else:
                return jsonify({"message": "No se encontraron servidores"}), 404
            
    
    @classmethod
    def crear_servidor(cls):

        if request.method == 'POST':
            
            data = request.json
            servidor = data.get('servidor') # es con coma o sin coma

            correo = session.get('correo')

            # método para obtener el usuario a partir del correo en la sesión
            user = User()
            user.correo = correo
            user = User.get(user)  # Utiliza el método get para obtener el usuario completo

            if user:
                id_usuario = user.id_usuario # Obtiene el id del usuario encontrado
                print("Nombre del servidor", servidor, "Id USUARIO:", id_usuario)


                if Sala.crear_servidor({"nombre_servidor": servidor, "propietario_id": id_usuario}):   # TRUE O FALSE (TRUE se encontro el user en la base de datos)
                    return jsonify({"message": "Servidor Creado"}), 200   #retornamos el numero
                else:
                    return jsonify({"message": "Error al crear"}), 400 #401 no es
            else:
                return jsonify({"message": "Usuario no encontrado"}), 404
        else:
            return render_template("crear_servidor.html")

        

    @classmethod
    def unir_servi(cls):

        if request.method == 'POST':
            
            data = request.json
            servidor_id = data.get('servidor_id') # es con coma o sin coma

            correo = session.get('correo')

            # método para obtener el usuario a partir del correo en la sesión
            user = User()
            user.correo = correo
            user = User.get(user)  # Utiliza el método get para obtener el usuario completo

            if user:
                id_usuario = user.id_usuario # Obtiene el id del usuario encontrado
                print("usuario_id", id_usuario, "servidor_id:", servidor_id)


                if Sala.unir_servi({"usuario_id": id_usuario, "servidor_id": servidor_id}):   # TRUE O FALSE (TRUE se encontro el user en la base de datos)
                    return jsonify({"message": "Servidor Creado"}), 200   #retornamos el numero
                else:
                    return jsonify({"message": "Error al unir"}), 400 #401 no es
            else:
                return jsonify({"message": "Usuario no encontrado"}), 404
        else:
            return jsonify({"message": "Método no permitido"}), 405





    @classmethod
    def logout(cls):
        session.pop('correo', None)
        return {"message": "Sesion cerrada"}, 200

        
