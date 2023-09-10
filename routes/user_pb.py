from flask import Blueprint, render_template

user_bb=Blueprint('Users')

user_bp.route('/todos_user/<int:customer_id>', methods = ['GET'])#(BikeStores.get_cliente)
user_bp.route('/crear_us', methods = ['GET'])#(BikeStores.get_clientes)
user_bp.route('/mod_us/<int:id_user>',methods=['GET'])
user_bp.route('/eliminarCliente/<int:custome_id>', methods = ['DELETE
