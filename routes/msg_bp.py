from flask import Blueprint, render_template, request, jsonify

from ..controllers.sala_controller import SalaController

msg_bp = Blueprint('sala_bp', __name__)