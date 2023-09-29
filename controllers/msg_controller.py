from ..models.auth.user_model import User
from ..models.auth.msg_model import Msg
from flask import request, session, jsonify,render_template

class MsgController:

    @classmethod
    def show_msg(cls, id_canal):
        print("id_canal ****:", id_canal)   
        correo = session.get('correo')
        print("correo ****:", correo) 

        user = User(correo=correo) #user = Sala.get(User(correo = correo)) 


        if user is None:
            return {"message": "Usuario no encontrado"}, 404
        else:
            mensaje = Msg.get({"id_canal": id_canal})  # Obtiene una lista de instancias de sala Canal.get({"correo": correo, "servidor_id": servi_id})
            
            if mensaje:
                if isinstance(mensaje, Msg):
                    mensaje = [mensaje]  # Si salas es un solo objeto Sala, se convierte en una lista
                
                # Crear un diccionario que representa las salas
                serialized_mensaje = {}
                for index, mensaje in enumerate(mensaje, start=1):
                    serialized_mensaje[f"mensaje{index}"] = mensaje.serialize()
                return jsonify(serialized_mensaje), 200
            
            if not mensaje:
                return jsonify({"message": "Usuario no tiene mensajes"}), 200
            
            else:
                return jsonify({"message": "No se encontraron los mensajes"}), 404





    """ CREAR MENSAJE"""
    @classmethod
    def guar_msg(cls):
            correo = session.get('correo')
            nombre = session.get('nombre')
            print("DATOS", correo, " , ", nombre)

            if request.method == 'POST':
                
                data = request.json
                descripcion_mensaje = data.get('descripcion_mensaje') # es con coma o sin coma
                id_canal = data.get('id_canal')
                

                correo = session.get('correo')

                # método para obtener el usuario a partir del correo en la sesión
                user = User()
                user.correo = correo
                user = User.get(user)  # Utiliza el método get para obtener el usuario completo

                if user:

                    creador_id = user.id_usuario # Obtiene el id del usuario encontrado
                    print("descripcion_mensaje", descripcion_mensaje, "id_canal", id_canal, "creador_id",creador_id)


                    if Msg.crear_mensaje({"descripcion_mensaje": descripcion_mensaje, "id_canal": id_canal, "creador_id": creador_id}):   # TRUE O FALSE (TRUE se encontro el user en la base de datos)
                        return jsonify({"message": "Mensaje Creado"}), 200   #retornamos el numero
                    else:
                        return jsonify({"message": "Error al crear"}), 400 #401 no es
                else:
                    return jsonify({"message": "Mensaje no encontrado"}), 404
            else:
                return jsonify({"message": " Metodo fatal"}), 401
            


    """ ELIMINAR MENSAJE"""
    @classmethod
    def eliminar_msg(cls):
            correo = session.get('correo')

            if request.method == 'DELETE':
                
                data = request.json
                id_mensaje = data.get('id_mensaje')
                nombre = data.get('nombre')
            

                # método para obtener el usuario a partir del correo en la sesión
                user = User()
                user.correo = correo
                user = User.get(user)  # Utiliza el método get para obtener el usuario completo

                usernombre = user.nombre # Obtiene el id del usuario encontrado 

                print("id_mensaje", id_mensaje, "usernombre", usernombre, "nombre", usernombre)

                if nombre == usernombre:

                    if Msg.eliminar_mensaje({"id_mensaje": id_mensaje}):   # TRUE O FALSE (TRUE se encontro el user en la base de datos)
                        return jsonify({"message": "Mensaje Creado"}), 200   #retornamos el numero
                    else:
                        return jsonify({"message": "Error al eliminar"}), 400 #401 no es
                else:
                    return jsonify({"message": "Usuario no valido para modificar"}), 404
            else:
                return jsonify({"message": " Metodo fatal"}), 401