from flask import Blueprint, render_template, request, jsonify

from ..controllers.sala_controller import SalaController

msg_bp = Blueprint('msg_bp', __name__)
msg_bp.route('/crear_msg', methods=['GET'])(MsgController.crear_msg)#vrear controller