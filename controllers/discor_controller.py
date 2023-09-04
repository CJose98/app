from flask import request, render_template
from ..database import DatabaseConnection, DatabaseConnection_2
from flask import jsonify


class App_Discor:
    """ codificando """
    def get_usuario(userId):
        return 