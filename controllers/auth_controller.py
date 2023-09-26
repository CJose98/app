from ..models.auth.user_model import User
from flask import request, session, jsonify,render_template

class UserController:

    @classmethod
    def login(cls):
        data = request.json
        user = User(
            correo = data.get('correo'),
            password = data.get('password')
        )

        if User.is_registered(user):   # TRUE O FALSE (TRUE se encontro el user en la base de datos)
            session['correo'] = data.get('correo')
            return jsonify({"message": "Sesion iniciada"}), 200
        else:
            return jsonify({"message": "Usuario o contraseña incorrectos"}), 401

    @classmethod
    def user_logeado(cls):
        correo = session.get('correo')
        user = User.get(User(correo = correo))
        if user is None:
            return {"message": "Usuario no encontrado"}, 404
        else:
            return render_template("user_logeado.html", user=user) 
        

    """ CREAR REGISTRO """
    @classmethod
    def show_register(cls):
        
        if request.method == 'POST':
            
            data = request.json
            user = User(
                    nombre = data.get('nombre'),
                    apellido = data.get('apellido'),
                    correo = data.get('correo'),
                    password = data.get('password'),
                    nombre_user = data.get('nombre_user'),
                    fecha_nac = data.get('fecha_nac')
            )

            if User.crear_usuario(user):   # TRUE O FALSE (TRUE se encontro el user en la base de datos)
                return jsonify({"message": "Registro completado"}), 200   #retornamos el numero
            else:
                return jsonify({"message": "Error al registrarse"}), 400 #401 no es
        else:
            return render_template("registro.html")


    """ MOSTRAR PERFIL """
    @classmethod
    def mostrar_perfil(cls):
        correo = session.get('correo')
        user = User.get(User(correo = correo))
        if user is None:
            return {"message": "Usuario no encontrado"}, 404
        else:
            return user.serialize(), 200
        

    """MOSTRAR METODOS"""
    @classmethod
    def perfil_float(cls):
            return render_template("perfil_float.html")
    
    @classmethod
    def mod_img_perfil(cls):
         return render_template("mod_img_perfil.html")
    @classmethod
    def editar_user_name(cls):
         return render_template("editar_user_name.html")
    @classmethod
    def editar_user(cls):
         return render_template("editar_user.html")
    @classmethod
    def editar_apellido(cls):
         return render_template("editar_apellido.html")
    @classmethod
    def editar_correo(cls):
         return render_template("editar_correo.html")
    @classmethod
    def editar_contraseña(cls):
            return render_template("editar_contraseña.html")
    
        
    @classmethod
    def logout(cls):
        session.pop('correo', None)
        return {"message": "Sesion cerrada"}, 200
    
    

    """MODIFICAR FOTO"""
    @classmethod
    def mod_foto(cls):

        if request.method == 'PUT':
            
            data = request.json
            img_perfil = data.get('n_foto') # es con coma o sin coma"""

            correo = session.get('correo')

            if not correo:
                return jsonify({"message": "Acceso no autorizado"}), 401

            # método para obtener el usuario a partir del correo en la sesión
            user = User()
            user.correo = correo
            user = User.get(user)  # Utiliza el método get para obtener el usuario completo


            if user:
                id_usuario = user.id_usuario # Obtiene el id del usuario encontrado
                print("img_perfil", img_perfil, "id user:", id_usuario)


                if User.mod_perfil({"img_perfil": img_perfil, "id_usuario": id_usuario}):   # TRUE O FALSE (TRUE se encontro el user en la base de datos)
                    return jsonify({"message": "Servidor Creado"}), 200   #retornamos el numero
                else:
                    return jsonify({"message": "Error al modificar"}), 500
            else:
                return jsonify({"message": "Usuario no encontrado"}), 404
        else:
            return jsonify({"message": "Método no permitido"}), 405
        
            
        

        
    """MODIFICAR USUARIO"""
    @classmethod
    def mod_usuario(cls):

        if request.method == 'PUT':
            
            data = request.json
            nombre_user = data.get('n_user') # es con coma o sin coma

            correo = session.get('correo')

            # método para obtener el usuario a partir del correo en la sesión
            user = User()
            user.correo = correo
            user = User.get(user)  # Utiliza el método get para obtener el usuario completo

            if user:
                id_usuario = user.id_usuario # Obtiene el id del usuario encontrado
                print("nombre_user", nombre_user, "id user:", id_usuario)


                if User.mod_user({"nombre_user": nombre_user, "id_usuario": id_usuario}):   # TRUE O FALSE (TRUE se encontro el user en la base de datos)
                    return jsonify({"message": "Servidor Creado"}), 200   #retornamos el numero
                else:
                    return jsonify({"message": "Error al crear"}), 400 #401 no es
            else:
                return jsonify({"message": "Usuario no encontrado"}), 404
        else:
            return jsonify({"message": "Error 400"}), 400 
        

    """MODIFICAR NOMBRE"""
    @classmethod
    def mod_nombre(cls):

        if request.method == 'PUT':
            
            data = request.json
            nombre = data.get('n_nombre') # es con coma o sin coma

            correo = session.get('correo')

            # método para obtener el usuario a partir del correo en la sesión
            user = User()
            user.correo = correo
            user = User.get(user)  # Utiliza el método get para obtener el usuario completo

            if user:
                id_usuario = user.id_usuario # Obtiene el id del usuario encontrado
                print("nombre", nombre, "id user:", id_usuario)


                if User.mod_nombre({"nombre": nombre, "id_usuario": id_usuario}):   # TRUE O FALSE (TRUE se encontro el user en la base de datos)
                    return jsonify({"message": "Servidor Creado"}), 200   #retornamos el numero
                else:
                    return jsonify({"message": "Error al crear"}), 400 #401 no es
            else:
                return jsonify({"message": "Usuario no encontrado"}), 404
        else:
            return jsonify({"message": "Error 400"}), 400 
        

    """MODIFICAR APELLIDO"""
    @classmethod
    def mod_apellido(cls):

        if request.method == 'PUT':
            
            data = request.json
            apellido = data.get('n_apellido') # es con coma o sin coma

            correo = session.get('correo')

            # método para obtener el usuario a partir del correo en la sesión
            user = User()
            user.correo = correo
            user = User.get(user)  # Utiliza el método get para obtener el usuario completo

            if user:
                id_usuario = user.id_usuario # Obtiene el id del usuario encontrado
                print("apellido", apellido, "id user:", id_usuario)


                if User.mod_apellido({"apellido": apellido, "id_usuario": id_usuario}):   # TRUE O FALSE (TRUE se encontro el user en la base de datos)
                    return jsonify({"message": "Servidor Creado"}), 200   #retornamos el numero
                else:
                    return jsonify({"message": "Error al crear"}), 400 #401 no es
            else:
                return jsonify({"message": "Usuario no encontrado"}), 404
        else:
            return jsonify({"message": "Error 400"}), 400 
        

    """MODIFICAR CORREO"""
    @classmethod
    def mod_correo(cls):

        if request.method == 'PUT':
            
            data = request.json
            correo = data.get('n_correo') # es con coma o sin coma

            correo = session.get('correo')

            # método para obtener el usuario a partir del correo en la sesión
            user = User()
            user.correo = correo
            user = User.get(user)  # Utiliza el método get para obtener el usuario completo

            if user:
                id_usuario = user.id_usuario # Obtiene el id del usuario encontrado
                print("correo", correo, "id user:", id_usuario)


                if User.mod_apellido({"correo": correo, "id_usuario": id_usuario}):   # TRUE O FALSE (TRUE se encontro el user en la base de datos)
                    return jsonify({"message": "Servidor Creado"}), 200   #retornamos el numero
                else:
                    return jsonify({"message": "Error al crear"}), 400 #401 no es
            else:
                return jsonify({"message": "Usuario no encontrado"}), 404
        else:
            return jsonify({"message": "Error 400"}), 400 
        
    """MODIFICAR PASSWORD"""
    @classmethod
    def mod_password(cls):

        if request.method == 'PUT':
            
            data = request.json
            password = data.get('n_password') # es con coma o sin coma

            correo = session.get('correo')

            # método para obtener el usuario a partir del correo en la sesión
            user = User()
            user.correo = correo
            user = User.get(user)  # Utiliza el método get para obtener el usuario completo

            if user:
                id_usuario = user.id_usuario # Obtiene el id del usuario encontrado
                print("password", password, "id user:", id_usuario)


                if User.mod_contra({"password": password, "id_usuario": id_usuario}):   # TRUE O FALSE (TRUE se encontro el user en la base de datos)
                    return jsonify({"message": "Servidor Creado"}), 200   #retornamos el numero
                else:
                    return jsonify({"message": "Error al crear"}), 400 #401 no es
            else:
                return jsonify({"message": "Usuario no encontrado"}), 404
        else:
            return jsonify({"message": "Error 400"}), 400 


    
