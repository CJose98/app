from flask import Blueprint, render_template

sala_bp = Blueprint('sala_bp',__name__)



#ingresar a la vista
@sala_bp.route("/", methods=['GET'])
def home():
    """Landing page route."""
    return render_template("index.html")
sala_bp.route('/mostrar_sala/<int:customer_id>', methods = ['GET'])
sala_bp.route('/crear_sala/')