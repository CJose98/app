from flask import Blueprint, render_template, request, jsonify

from ..controllers.canal_controller import CanalController

canal_bp = Blueprint('canal_bp', __name__)
canal_bp.route('/crear_canal', methods=['GET'])(CanalController.crear_canal)#vrear controller
# canal_bp.route('/eliminar_canal',methods=['DELETE'])(CanalController.eliminar_canal)
# canal_bp.route('/mod_canal',methods=['PUT'])(CanalController.mod_canal))