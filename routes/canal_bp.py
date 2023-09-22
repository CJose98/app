from flask import Blueprint, render_template, request, jsonify

from ..controllers.canal_controller import CanalController

canal_bp = Blueprint('sala_bp', __name__)
canal_bp.route('/crear_canal', methods=['GET'])(CanalController.mostrar_todo)#vrear controller