from flask import Blueprint, render_template
from ..controllers.discor_controller import BikeStores


actor_bp = Blueprint('actor_bp',__name__)


#ingresar a la vista
@actor_bp.route("/", methods=['GET'])
def home():
    """Landing page route."""

    return render_template("index.html")

#obtener datos
actor_bp.route('/obtenerCliente/<int:customer_id>', methods = ['GET'])(BikeStores.get_cliente)
actor_bp.route('/obtenerClientes', methods = ['GET'])(BikeStores.get_clientes)
#crear clientes
actor_bp.route('/crearCliente', methods = ['POST'])(BikeStores.create_cliente)
actor_bp.route('/form', methods = ['POST'])(BikeStores.registrarForm)
#actualizar datos
actor_bp.route('/actualizarCliente/<int:customer_id>', methods = ['PUT'])(BikeStores.update_cliente)
actor_bp.route('/form/<int:customer_id>', methods = ['POST', 'GET'])(BikeStores.update_Form)
#eliminar datos
actor_bp.route('/eliminarCliente/<int:custome_id>', methods = ['DELETE', 'GET'])(BikeStores.delete_cliente)


#actor_bp.route('/customers_x_', methods = ['DELETE'])(BikeStores.delete_clientes)


#obtener datos
actor_bp.route('/obtenerProducto/<int:product_id>', methods = ['GET'])(BikeStores.get_producto)
actor_bp.route('/obtenerProductos', methods = ['GET'])(BikeStores.get_productos)
#registrar datos
actor_bp.route('/crearProducto', methods = ['POST'])(BikeStores.create_producto)
#actualizar datos
actor_bp.route('/actualizarProducto/<int:customer_id>', methods = ['PUT'])(BikeStores.modificar_producto)
#eliminar datos
actor_bp.route('/eliminarProducto/<int:custome_id>', methods = ['DELETE'])(BikeStores.delete_producto)







