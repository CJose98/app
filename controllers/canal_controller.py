from app.database import DatabaseConnection
from ..models.auth.canal_model import Canal

from flask import request, session, jsonify,render_template

class CanalController:
    @classmethod
    def mostrar_todo():
        #        print(request)
        pass
    @classmethod
    def eliminar_canal():
        pass
    @classmethod
    def mod_canal():
        return render_template('../templates\modificar_canal.html')
        pass
    @classmethod
    def crear_canal():
        return render_template('../templates\crear_canal.html')
        pass