from flask import Blueprint, render_template, request, jsonify

from ..controllers.canal_controller import CanalController

canal_bp = Blueprint('canal_bp', __name__)


canal_bp.route('/crear_canal', methods=['GET', 'POST'])(CanalController.crear_canal)#vrear controller

canal_bp.route('/show_canal/<int:servi_id>', methods=['GET'])(CanalController.show_canal)#vrear controller
