from app.database import DatabaseConnection
from ..models.auth.user_model import User
from ..models.auth.sala_model import Sala
from flask import request, session, jsonify,render_template

class CanalController:
    