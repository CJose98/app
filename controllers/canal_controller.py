from ..models.auth.user_model import User
from ..models.auth.canal_model import Canal
from flask import request, session, jsonify,render_template


class CanalController:

    @classmethod
    def show_canal(cls, servi_id):
        #id_servi = servi_id,
        print("id_servi ****:", servi_id)   
        correo = session.get('correo')
        print("correo ****:", correo)                         
        user = User(correo=correo) #user = Sala.get(User(correo = correo)) 
        print("user ****:", user)  


        if user is None:
            return {"message": "Usuario no encontrado"}, 404
        else:
            salas = Canal.get({"servidor_id": servi_id})  # Obtiene una lista de instancias de sala Canal.get({"correo": correo, "servidor_id": servi_id})
            
            if salas:
                if isinstance(salas, Canal):
                    salas = [salas]  # Si salas es un solo objeto Sala, se convierte en una lista
                
                # Crear un diccionario que representa las salas
                serialized_salas = {}
                for index, sala in enumerate(salas, start=1):
                    serialized_salas[f"sala{index}"] = sala.serialize()
                return jsonify(serialized_salas), 200
            
            if not salas:
                return jsonify({"message": "Usuario no tiene canales"}), 200
            
            else:
                return jsonify({"message": "No se encontraron canales"}), 404
            

    @classmethod
    def crear_canal(cls):
        correo = session.get('correo')
        nombre = session.get('nombre')
        print("DATOS", correo, " , ", nombre)

        if request.method == 'POST':
            
            data = request.json
            canal = data.get('canal') # es con coma o sin coma 
            servidor_id = data.get('id_servidor')
            

            correo = session.get('correo')

            # método para obtener el usuario a partir del correo en la sesión
            user = User()
            user.correo = correo
            user = User.get(user)  # Utiliza el método get para obtener el usuario completo

            if user:
                id_usuario = user.id_usuario # Obtiene el id del usuario encontrado
                print("nombre_canal", canal, "servidor_id", servidor_id, "creador_id",id_usuario)


                if Canal.crear_canal({"nombre_canal": canal, "servidor_id": servidor_id, "creador_id": id_usuario}):   # TRUE O FALSE (TRUE se encontro el user en la base de datos)
                    return jsonify({"message": "Canal Creado"}), 200   #retornamos el numero
                else:
                    return jsonify({"message": "Error al crear"}), 400 #401 no es
            else:
                return jsonify({"message": "Usuario no encontrado"}), 404
        else:
            return render_template("crear_canal.html", correo=correo, nombre=nombre)
        
