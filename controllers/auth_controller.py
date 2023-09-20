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
    def show_profile(cls):
        correo = session.get('correo')
        user = User.get(User(correo = correo))
        if user is None:
            return {"message": "Usuario no encontrado"}, 404
        else:
            return render_template("user_logeado.html", user=user)
            #return user.serialize(), 200 #cambiar debe redigir a la pagina

    @classmethod
    def show_register(cls):
            return render_template("registro.html")
    
    @classmethod
    def logout(cls):
        session.pop('correo', None)
        return {"message": "Sesion cerrada"}, 200
    
    @classmethod
    def perfil_float(cls):
            return render_template("perfil_float.html")
    
    @classmethod
    def editar_contraseña(cls):
            return render_template("editar_contraseña.html")
    
    @classmethod
    def crear_user(cls):
            return render_template("crear_user.html")
    