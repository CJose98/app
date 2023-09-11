#from ..models.actor_model import Actor
#from ..routes.actor_bp import Actor
from flask import request, render_template

from app.database.database import DatabaseConnection, DatabaseConnection_2

from ..database import DataBaseConnection_4

from flask import jsonify

print("Hola mundo! 2")


class App_Discor:
    def __init__(self,id_user=None,Apellido=None,Nombre=None,Correo=None,Contraseña=None,Nombre_usuario=None,Fecha_nac=None):
            #Contructor
            self.id_user=id_user
            self.Apellido=Apellido
            self.Nombre=Nombre
            self.Correo=Correo
            self.Contraseña=Contraseña
            self.Nombre_usuario=Nombre_usuario
            self.Fecha_nac=Fecha_nac
    
    @classmethod
    def todos_users ():
              sql="SELECT * FROM user_1.usuario;"
              results=DataBaseConnection_4.fetch_all(sql)
              Usuarios=[]
              for result in results:
                   Usuarios.append({"Id_Usuario":result[0],
                          "Apellido ":result[1],
                          "Nombre":result[2],
                          "Correo":[3],
                          "Pass":[4],
                          "Nombre Usuario":[5],
                          "fecha Nacimiento":[6],
                          })
              return Usuarios,200  
    @classmethod
    def crear_us():
             sql="insert into user_1.usuario (Apellido,Nombre,Correo,Contraseña,Nombre_usuario,Fecha_nac)values(%s,%s,%s,%s,%s,%s);"
             params=request.args.get('Apellido',''),request.args.get('Nombre',''),request.args.get('Correo',''),
             request.args.get('Contraseña',''),request.args.get('Nombre_usuario',''),request.args.get('Fecha_nac','')
             DataBaseConnection_4.execute_query(sql,params)
             return {'msg':'Usuario Creado con exito'},201
    @classmethod
    def mod_user(id_user):
                sql="UPDATE usuario SET password=%s WHERE user_id= %s;"
                params=request.args.get('password',''),id_user
                DataBaseConnection_4.execute_query(sql,params)
                return {'msg':'Usuario Modificado  con exito'},201
    @classmethod
    def eliminarUs(id_user):
                sql="delete from usuario where id_user=%s;"
                params=request.args.get(id_user)
                DataBaseConnection_4.execute_query(sql,params)
                return {"msg": "Actores eliminado con éxito"}, 200           
               
            
            
    ##---------------------------------------##
    # se tendria que eliminar esto para que quede mas prolijo el trabajo 
    
    #http://127.0.0.1:5000/obtenerCliente/2
    def get_cliente(customer_id):
                    sql = "SELECT customer_id, first_name, last_name, email, phone, street, city, state, zip_code FROM sales.customers WHERE customer_id = %s;"
                    params = customer_id,
                    result = DatabaseConnection.fetch_one(sql, params)
                    if result is not None:
                        return {
                            "id": result[0],
                            "nombre": result[1],
                            "apellido": result[2],
                            "Email": result[3],
                            "Telefono": result[4],
                            "Direccion": result[5],
                            "Ciudad": result[6],
                            "Estado": result[7],
                            "Codigo_Postal": result[8],
                        }, 200
                    return {"msg": "No se encontró el actor"}, 404
                
    #http://127.0.0.1:5000/obtenerClientes
    def get_clientes():
                    sql = "SELECT customer_id, first_name, last_name, email, phone, street, city, state, zip_code FROM sales.customers WHERE state = 'NY' LIMIT 2;"
                    results = DatabaseConnection.fetch_all(sql)
                    clientes = []
                    for result in results:
                        clientes.append({
                            "id": result[0],
                            "nombre": result[1],
                            "apellido": result[2],
                            "Email": result[3],
                            "Telefono": result[4],
                            "Direccion": result[5],
                            "Ciudad": result[6],
                            "Estado": result[7],
                            "Codigo_Postal": result[8],
                        })
                    return ({'customers': clientes, 'total': len(clientes)}, 200, {'Content-Type': 'application/json'})

  
     #     http://127.0.0.1:5000/crearCliente?first_name=jose&last_name=colque&email=correo
    def create_cliente():
                #if request.method == 'POST': 
                    nombre = request.args.get('first_name',  default = '')
                    apellido = request.args.get('last_name',  default = '')
                    email = request.args.get('email',  default = '')

                    sql = ("INSERT INTO sales.customers (first_name, last_name, email) VALUES (%s,%s,%s)")
                    cliente     = (nombre, apellido, email)
                    DatabaseConnection.execute_query(sql, cliente)

                    return ({'msg': 'Cliente creado con exito'}, 201, {'Content-Type': 'application/json'})
                
                #else:
                    #return {"error": "Método no permitido para la URL solicitada"}, 405
    
    def registrarForm():
        msg =''
        if request.method == 'POST':
            nombre              = request.form.get("first_name", False)   #ERROR::>>   request.form['first_name']
            apellido            = request.form.get("last_name", False)
            email               = request.form.get("email", False)       
                
            sql         = ("INSERT INTO sales.customers (first_name, last_name, email) VALUES (%s,%s,%s)")
            cliente     = (nombre, apellido, email)
            DatabaseConnection.execute_query(sql, cliente)

            print("1 registro insertado, id")
            
            return render_template('index.html', msg='Formulario enviado')
        else:
            return render_template('index.html', msg = 'Metodo HTTP incorrecto')
    
    

    # http://127.0.0.1:5000/actualizarCliente/1446
    def update_cliente(customer_id):  
        if request.method == 'PUT' or 'GET':  # Check the HTTP method
            nombre              = request.form.get("first_name", default = '')   #ERROR::>>   request.form['first_name']
            apellido            = request.form.get("last_name", default = '')
            email               = request.form.get("email", default = '')    

            sql = "UPDATE sales.customers SET first_name = %s , last_name = %s, email =%s WHERE customers.customer_id = %s;"
            cliente = (nombre, apellido, email, customer_id)
            DatabaseConnection.execute_query(sql, cliente)
                
            return ('Formulario Modificado'),200
        else:
           return ('Metodo HTTP incorrecto'),400



    # http://127.0.0.1:5000/form/1446
    def update_Form(customer_id):
        msg =''
        if request.method == 'PUT' or 'GET':  # Check the HTTP method
            nombre              = request.form.get("first_name", False)   #ERROR::>>   request.form['first_name']
            apellido            = request.form.get("last_name", False)
            email               = request.form.get("email", False)    

            sql = "UPDATE sales.customers SET first_name = %s , last_name = %s, email =%s WHERE customers.customer_id = %s;"
            cliente = (nombre, apellido, email, customer_id)
            DatabaseConnection.execute_query(sql, cliente)

            return render_template('index.html', msg='Formulario Modificado')
        else:
           return render_template('index.html', msg = 'Metodo HTTP incorrecto')
        
    

    #http://127.0.0.1:5000/eliminarCliente/1451            
    def delete_cliente(custome_id):
                    sql = "DELETE FROM sales.customers WHERE customers.customer_id = %s;"
                    params = custome_id,
                    DatabaseConnection.execute_query(sql, params)
                    return ({'msg': 'Cliente eliminado con exito'}, 200, {'Content-Type': 'application/json'})
    


    """*******************************************************************************"""
    """*******************************************************************************"""
    """*******************************************************************************"""
    """*******************************************************************************"""



        #http://127.0.0.1:5000/obtenerProducto/10
    def get_producto(product_id):
                    sql ="""SELECT products.brand_id, brands.brand_name, products.category_id, categories.category_name, products.list_price, products.model_year, products.product_id, products.product_name 
                            FROM brands INNER JOIN products
                            ON brands.brand_id = products.brand_id
                            INNER JOIN categories
                            ON products.category_id = categories.category_id
                            WHERE products.product_id = %s;"""

                    params = product_id,
                    result = DatabaseConnection_2.fetch_one(sql, params)

                    if result is not None:
                        brand = {
                            "brand_id": result[0],
                            "brand_name": result[1],
                        }
                        category = {
                            "category_id": result[2],
                            "category_name": result[3],
                        }

                        return ({'brand': brand, 
                                 'category': category,
                                    "list_price": result[4],
                                    "model_year": result[5],
                                    "product_id": result[6],
                                    "product_name": result[7],
                                }, 200, {'Content-Type': 'application/json'})

                    return {"msg": "No se encontró el actor"}, 404
    


        #http://127.0.0.1:5000/obtenerProductos
    def get_productos():
                    sql ="""SELECT products.brand_id, brands.brand_name, products.category_id, categories.category_name, products.list_price, products.model_year, products.product_id, products.product_name 
                            FROM brands INNER JOIN products
                            ON brands.brand_id = products.brand_id
                            INNER JOIN categories
                            ON products.category_id = categories.category_id
                            WHERE products.brand_id = 1 AND categories.category_id = 1 AND products.list_price = 269.99;"""
                    
                    results = DatabaseConnection_2.fetch_all(sql)
                    productos = []
                    for result in results:
                        brand = {
                            "brand_id": result[0],
                            "brand_name": result[1],
                        }
                        category = {
                            "category_id": result[2],
                            "category_name": result[3],
                        }
                        productos.append({'brand': brand, 
                                    'category': category,
                                    "list_price": result[4],
                                    "model_year": result[5],
                                    "product_id": result[6],
                                    "product_name": result[7],
                                })
                    return ({'productos': productos, 'total': len(productos)}, 200, {'Content-Type': 'application/json'})



        #  http://127.0.0.1:5000/crearProducto?product_name=Trek+Hiperfly+XLR8+-+2019&brand_id=9&category_id=4&model_year=2019&list_price=994.99
        #  http://127.0.0.1:5000/crearProducto?product_name=TrekHiperfly+XLR82019&brand_id=9&category_id=4&model_year=2019&list_price=994.99
    def create_producto():
                    product_name = request.args.get('product_name',  default = '')
                    brand_id = request.args.get('brand_id',  default = '')
                    category_id = request.args.get('category_id',  default = '')
                    model_year = request.args.get('model_year',  default = '')
                    list_price = request.args.get('list_price',  default = '')


                    sql = ("INSERT INTO production.products (product_name, brand_id, category_id, model_year, list_price) VALUES (%s,%s,%s,%s,%s)")
                    productos = (product_name, brand_id, category_id, model_year, list_price)
                    DatabaseConnection.execute_query(sql, productos)

                    return ({'msg': 'Producto creado con exito'}, 201, {'Content-Type': 'application/json'})
    


        # http://127.0.0.1:5000/actualizarProducto/1446
    def modificar_producto(productoId):  

                    product_name = request.args.get('product_name',  default = '')
                    brand_id = request.args.get('brand_id',  default = '')
                    category_id = request.args.get('category_id',  default = '')
                    model_year = request.args.get('model_year',  default = '')
                    list_price = request.args.get('list_price',  default = '')  

                    sql = ("UPDATE production.products SET product_name = %s , brand_id = %s, category_id =%s, model_year =%s, list_price =%s WHERE products.product_id = %s")
                    productos     = (product_name, brand_id, category_id, model_year, list_price, productoId)
                    DatabaseConnection.execute_query(sql, productos)
                
                    return ({'msg': 'Producto modificdo con éxito'}, 200, {'Content-Type': 'application/json'})
        


        #http://127.0.0.1:5000/eliminarProducto/1451            
    def delete_producto(productoId):
                    sql = "DELETE FROM production.products WHERE products.product_id = %s;"
                    params = productoId,
                    DatabaseConnection.execute_query(sql, params)
                    return ({'msg': 'Producto eliminado con éxito'}, 200, {'Content-Type': 'application/json'})
    