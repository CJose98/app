from flask import Blueprint, render_template, request, jsonify

from ..controllers.sala_controller import SalaController

sala_bp = Blueprint('sala_bp', __name__)


"""sala_bp.route('/user_logeado', methods=['GET'])(UserController.show_profile)  #html de logeado"""

sala_bp.route('/sala', methods=['GET'])(SalaController.show_sala)         #html de registro

sala_bp.route('/logout', methods=['GET'])(SalaController.logout)            # nada X
#se crea la bp para crear la sala(servidor) que no estaba echo - fijarse (crear _user )
sala_bp.route('/crear_servidor',methods=['PUT'])(SalaController.crear_servidor)# este bp faltaba
sala_bp.route('/crear_user', methods=['GET'])(SalaController.crear_user)            # html editar
