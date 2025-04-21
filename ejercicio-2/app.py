from flask import Flask, request, jsonify

app = Flask(__name__)

usuarios = []


@app.route('/info', methods=['GET'])
def info():
    return jsonify({
        "sistema": "Gestor de Usuarios y Productos",
        "version": "1.0",
        "autor": "Samuel"
    }), 200


@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    data = request.get_json()

    nombre = data.get('nombre')
    correo = data.get('correo')

    if not nombre or not correo:
        return jsonify({"error": "Nombre y correo son requeridos"}), 400

    nuevo_usuario = {
        "id": len(usuarios) + 1,
        "nombre": nombre,
        "correo": correo
    }
    usuarios.append(nuevo_usuario)

    return jsonify({"mensaje": "Usuario creado correctamente", "usuario": nuevo_usuario}), 201


@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify({"usuarios": usuarios}), 200


# Ejecutar servidor
if __name__ == '__main__':
    app.run(debug=True)
