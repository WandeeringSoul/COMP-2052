from flask import Flask, request, jsonify

app = Flask(__name__)

usuarios = []


@app.route('/info', methods=['GET'])
def info():
    return jsonify({
        "sistema": "Gestión de usuarios y productos",
        "versión": "1.0",
        "autor": "Samuel Molina Delgado",
        "estado": "Activo"
    }), 200


@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    datos = request.get_json()

    if not datos:
        return jsonify({"error": "No se proporcionaron datos JSON"}), 400

    nombre = datos.get('nombre')
    correo = datos.get('correo')

    if not nombre or not correo:
        return jsonify({"error": "Faltan datos requeridos: nombre y correo"}), 400

    nuevo_usuario = {
        "nombre": nombre,
        "correo": correo
    }
    usuarios.append(nuevo_usuario)

    return jsonify({"mensaje": "Usuario creado exitosamente", "usuario": nuevo_usuario}), 201


@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify({"usuarios": usuarios}), 200


if __name__ == '__main__':
    app.run(debug=True)
