from flask import Flask
from flask_cors import CORS
from config import Config
from .routes.auth_bp import auth_bp
from .routes.sala_bp import sala_bp
from .routes.canal_bp import canal_bp
from .routes.msg_bp import msg_bp
from .database import DatabaseConnection


def init_app():
    """Crea y configura la aplicación Flask"""
    
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    
    CORS(app, supports_credentials=True)

    app.config.from_object(Config)
    
    DatabaseConnection.set_config(app.config)

    app.register_blueprint(auth_bp, url_prefix = '/auth')
    app.register_blueprint(sala_bp, url_prefix = '/auth')
    app.register_blueprint(canal_bp, url_prefix = '/auth')
    app.register_blueprint(msg_bp, url_prefix = '/auth')
    
    

    return app