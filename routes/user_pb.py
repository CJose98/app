from flask import Blueprint, render_template

user_bp=Blueprint('Users')
@user_bp.route('/')
def init():
    return render_template ('login.html')

user_bp.route('/users>', methods = ['GET'])
user_bp.route('/crearUser', methods = ['GET'])
user_bp.route('/ModificarUsuario/<int:id_user>',methods=['GET'])
user_bp.route('/EliminarUser/<int:custome_id>', methods = ['DELETE'])
