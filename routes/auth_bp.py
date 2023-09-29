from flask import Blueprint, render_template, request, jsonify

from ..controllers.auth_controller import UserController

auth_bp = Blueprint('auth_bp', __name__)

#ingresar a la vista http://127.0.0.1:5000/auth/login

    
auth_bp.route('/login', methods=['GET','POST'])(UserController.login)  

auth_bp.route('/user_logeado', methods=['GET'])(UserController.user_logeado)  

auth_bp.route('/registro', methods=['GET','POST'])(UserController.show_register)   

auth_bp.route('/perfil_float', methods=['GET'])(UserController.perfil_float)         

auth_bp.route('/mostrar_perfil', methods=['GET'])(UserController.mostrar_perfil) 

auth_bp.route('/logout', methods=['GET'])(UserController.logout)   

auth_bp.route('/grid', methods=['GET'])(UserController.grid)





auth_bp.route('/mod_img_perfil', methods=['GET'])(UserController.mod_img_perfil)            # html editar
auth_bp.route('/editar_user_name', methods=['GET'])(UserController.editar_user_name)            # html editar
auth_bp.route('/editar_user', methods=['GET'])(UserController.editar_user)            # html editar
auth_bp.route('/editar_apellido', methods=['GET'])(UserController.editar_apellido)            # html editar
auth_bp.route('/editar_correo', methods=['GET'])(UserController.editar_correo)            # html editar
auth_bp.route('/editar_contraseña', methods=['GET'])(UserController.editar_contraseña)            # html editar



auth_bp.route('/mod_foto', methods=['PUT'])(UserController.mod_foto)            # html modificar
auth_bp.route('/mod_usuario', methods=['PUT'])(UserController.mod_usuario)            # html modificar 
auth_bp.route('/mod_nombre', methods=['PUT'])(UserController.mod_nombre)            # html modificar
auth_bp.route('/mod_apellido', methods=['PUT'])(UserController.mod_apellido)            # html modificar
auth_bp.route('/mod_correo', methods=['PUT'])(UserController.mod_correo)            # html modificar
auth_bp.route('/mod_password', methods=['PUT'])(UserController.mod_password)            # html modificar


