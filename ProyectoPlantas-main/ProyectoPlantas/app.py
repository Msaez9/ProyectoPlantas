# ejecutar pip install flask flask-sqlalchemy flask-migrate flask-cors
# importamos las librerias de flask
from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Cliente
from flask_cors import CORS, cross_origin

# Instanciamos la app
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.url_map.strict_slashes = False
app.config['DEBUG'] = False
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)


Migrate(app, db)

# Creación de ruta por defecto
@app.route('/')
def index():
    return 'Hello world'

# Ruta para consultar todos los clientes
@app.route('/Cliente', methods=['GET'])
# no se sabe si va este antes de definir el metodo: @cross_origin()
def getCliente():
    cliente = Cliente.query.all()
    cliente = list(map(lambda x: x.serialize(), cliente))
    return jsonify(cliente),200

# Ruta para agregar clientes
@app.route('/Cliente', methods=['POST'])
def addCliente():
    cliente = Cliente()
    #asignacion de variables
    rut = request.json.get('rut')
    dv = request.json.get('dv')
    primer_nombre = request.json.get('primer_nombre')
    segundo_nombre = request.json.get('segundo_nombre')
    apellido_paterno = request.json.get('apellido_paterno')
    apellido_materno = request.json.get('apellido_materno')
    direccion = request.json.get('direccion')
    fono = request.json.get('fono')
    correo = request.json.get('correo')
    estado = request.json.get('estado')

    #cliente.rut = rut
    #cliente.dv = dv
    #cliente.primer_nombre = primer_nombre
    #cliente.segundo_nombre = segundo_nombre
    #cliente.apellido_paterno = apellido_paterno
    #cliente.apellido_materno = apellido_materno
    #cliente.direccion = direccion
    #cliente.fono = fono
    #cliente.correo = correo
    #cliente.estado = estado

    Cliente.save(cliente)

    return jsonify(cliente.serialize()),200

# Ruta para consultar un cliente en especifico
@app.route('/Cliente/<id_cliente>', methods=['GET'])
def getCliente(id_cliente):
    #o asi cliente = Cliente.query.get('id_cliente') 
    # lo mismo para los demás metodos
    cliente = Cliente.query.get(id_cliente)   
    return jsonify(cliente.serialize()),200 

# Ruta para borrar un cliente en especifico
@app.route('/cliente/<id_cliente>', methods=['DELETE'])
def deleteCliente(id_cliente):
    cliente = Cliente.query.get(id_cliente)
    Cliente.delete(cliente)
    return jsonify(cliente.serialize()), 200

# Ruta para modificar un cliente en específico
@app.route('/cliente/<id_cliente>', methods=['PUT'])
def updateCliente(id_cliente):
    cliente = Cliente.query.get(id_cliente)

    #rut = request.json.get('rut')
    #dv = request.json.get('dv')
    #primer_nombre = request.json.get('primer_nombre')
    #segundo_nombre = request.json.get('segundo_nombre')
    #apellido_paterno = request.json.get('apellido_paterno')
    #apellido_materno = request.json.get('apellido_materno')
    #direccion = request.json.get('direccion')
    #fono = request.json.get('fono')
    #correo = request.json.get('correo')
    #estado = request.json.get('estado')

    #cliente.rut = rut
    #cliente.dv = dv
    #cliente.primer_nombre = primer_nombre
    #cliente.segundo_nombre = segundo_nombre
    #cliente.apellido_paterno = apellido_paterno
    #cliente.apellido_materno = apellido_materno
    #cliente.direccion = direccion
    #cliente.fono = fono
    #cliente.correo = correo
    #cliente.estado = estado

    cliente.rut = request.json.get('rut')
    cliente.dv = request.json.get('dv')
    cliente.primer_nombre = request.json.get('primer_nombre')
    cliente.segundo_nombre = request.json.get('segundo_nombre')
    cliente.apellido_paterno = request.json.get('apellido_paterno')
    cliente.apellido_materno = request.json.get('apellido_materno')
    cliente.direccion = request.json.get('direccion')
    cliente.fono = request.json.get('fono')
    cliente.correo = request.json.get('correo')
    cliente.estado = request.json.get('estado')

    Cliente.save(cliente)

    return jsonify(cliente.serialize()),200


# Configuracion de puertos
if __name__ == '__main__':
    app.run(port=5000, debug=True)