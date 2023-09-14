from flask import Blueprint, render_template, request, jsonify

from ..controllers.auth_controller import UserController

auth_bp = Blueprint('auth_bp', __name__)

#ingresar a la vista http://127.0.0.1:5000/auth/login
@auth_bp.route('/login', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':

        result, status_code = UserController.login()  # Llama a la función login desde el controlador
        if status_code == 200:
            return jsonify({"message": "Sesion iniciada"}), 200
        else:
            return jsonify({"message": "Usuario o contraseña incorrectos"}), 401
    else:
        return render_template("home.html")
    



auth_bp.route('/user_logeado', methods=['GET'])(UserController.show_profile)  #html de logeado

auth_bp.route('/registro', methods=['GET'])(UserController.show_register)    #html de registro

auth_bp.route('/logout', methods=['GET'])(UserController.logout)            # nada X