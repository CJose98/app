from ..models.auth.user_model import User
from flask import request, session, jsonify,render_template

class UserController:

    @classmethod
    def login(cls):
        if request.method == 'POST':
            
            data = request.json
            user = User(
                correo = data.get('correo'),
                password = data.get('password')
            )

            if User.is_registered(user):   # TRUE O FALSE (TRUE se encontro el user en la base de datos)

                # Almacena el correo y el nombre de usuario en la sesión
                session['correo'] = data.get('correo')

                # Obtén el nombre de usuario del objeto user y almacénalo en la sesión
                correo = session.get('correo')                         

                # método para obtener el usuario a partir del correo en la sesión
                b_user = User()
                b_user.correo = correo
                b_user = User.get(b_user)  # Utiliza el método get para obtener el usuario completo
                nombre = b_user.nombre # Obtiene el id del usuario encontrado
                session['nombre'] = nombre 

                return jsonify({"message": "Sesion iniciada"}), 200
            else:
                return jsonify({"message": "Usuario o contraseña incorrectos"}), 401
        else:
            return render_template("home.html")  # user=user) 

    @classmethod
    def user_logeado(cls):
        correo = session.get('correo')
        nombre = session.get('nombre')
        print("USER LOGEADO*****", nombre)

        user = User.get(User(correo = correo))
        if user is None:
            return {"message": "Usuario no encontrado"}, 404
        else:
            return render_template("user_logeado.html", nombre=nombre, correo=correo)  # user=user) 
        

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
    def grid(cls):
            return render_template("grid.html")
    
        
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
                    return jsonify({"message": "Modificado el usuario"}), 200   #retornamos el numero
                else:
                    return jsonify({"message": "Error al modificar el nombre"}), 400 #401 no es
            else:
                return jsonify({"message": "Usuario no Modificado"}), 404
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
                    return jsonify({"message": "Modificado el nombre"}), 200   #retornamos el numero
                else:
                    return jsonify({"message": "Error al Modificar"}), 400 #401 no es
            else:
                return jsonify({"message": "Usuario no Modificado"}), 404
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
                    return jsonify({"message": "Apellido Creado"}), 200   #retornamos el numero
                else:
                    return jsonify({"message": "Error al Modificar"}), 400 #401 no es
            else:
                return jsonify({"message": "Usuario no Modificado"}), 404
        else:
            return jsonify({"message": "Error 400"}), 400 
        

    """MODIFICAR CORREO"""
    @classmethod
    def mod_correo(cls):

        if request.method == 'PUT':
            
            data = request.json
            correoo = data.get('n_correo') # es con coma o sin coma

            correo = session.get('correo')

            # método para obtener el usuario a partir del correo en la sesión
            user = User()
            user.correo = correo
            user = User.get(user)  # Utiliza el método get para obtener el usuario completo

            if user:
                id_usuario = user.id_usuario # Obtiene el id del usuario encontrado
                print("correo", correo, "id user:", id_usuario)


                if User.mod_correo({"correo": correoo, "id_usuario": id_usuario}):   # TRUE O FALSE (TRUE se encontro el user en la base de datos)
                    return jsonify({"message": "Correo Modificado"}), 200   #retornamos el numero
                else:
                    return jsonify({"message": "Error al Modificar"}), 400 #401 no es
            else:
                return jsonify({"message": "Correo no encontrado"}), 404
        else:
            return jsonify({"message": "Error 400"}), 400 
        
    """MODIFICAR PASSWORD"""
    @classmethod
    def mod_password(cls):

        if request.method == 'PUT':
            
            data = request.json
            a_password = data.get('a_password') # es con coma o sin coma
            n_password = data.get('n_password') # es con coma o sin coma

            correo = session.get('correo')

            # método para obtener el usuario a partir del correo en la sesión
            user = User()
            user.correo = correo
            user = User.get(user)  # Utiliza el método get para obtener el usuario completo

            password = user.password # Obtiene el id del usuario encontrado

            if n_password:
                id_usuario = user.id_usuario # Obtiene el id del usuario encontrado
                print("password", n_password, "id user:", id_usuario)


                if User.mod_contra({"password": n_password, "id_usuario": id_usuario}):   # TRUE O FALSE (TRUE se encontro el user en la base de datos)
                    return jsonify({"message": "Contra Modificada"}), 200   #retornamos el numero
                else:
                    return jsonify({"message": "Error al Modificar"}), 400 #401 no es
            else:
                return jsonify({"message": "Password no Modificado"}), 404
        else:
            return jsonify({"message": "Error 400"}), 400 


    
