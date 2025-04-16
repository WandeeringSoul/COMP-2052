from flask import Flask, render_template

app = Flask(__name__)


productos = [
    {"id": 1, "nombre": "Laptop", "precio": 1200},
    {"id": 2, "nombre": "Mouse", "precio": 25}
]

usuarios = [
    {"id": 1, "nombre": "Luis", "rol": "Administrador"},
    {"id": 2, "nombre": "Samuel", "rol": "Usuario"}
]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/productos')
def mostrar_productos():
    return render_template('productos.html', productos=productos)


@app.route('/usuarios')
def mostrar_usuarios():
    return render_template('usuarios.html', usuarios=usuarios)


if __name__ == '__main__':
    app.run(debug=True)
