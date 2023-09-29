from flask import Blueprint, render_template, request, jsonify

from ..controllers.msg_controller import MsgController

msg_bp = Blueprint('msg_bp', __name__)


msg_bp.route('/show_msg/<int:id_canal>', methods=['GET'])(MsgController.show_msg)#vrear controller  

msg_bp.route('/guar_msg', methods=['POST'])(MsgController.guar_msg)

msg_bp.route('/eliminar_msg', methods=['DELETE'])(MsgController.eliminar_msg)

"""
msg_bp.route('/mod_msg',methods=['get','put'])(MsgController.mod_msg)
msg_bp.route('/eliminar_msg',methods=['delete'])(MsgController.eliminar_msg)"""
