from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'mi_clave_secreta'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


usuarios = {
    'Luis': {'id': '1', 'username': 'Luis', 'password': generate_password_hash('1234'), 'role': 'admin'},
    'Samuel': {'id': '2', 'username': 'Samuel', 'password': generate_password_hash('abcd'), 'role': 'user'}
}


class User(UserMixin):
    def __init__(self, id, username, password, role):
        self.id = id
        self.username = username
        self.password = password
        self.role = role

    def get_id(self):
        return self.id

    def is_admin(self):
        return self.role == 'admin'


def get_user_by_id(user_id):
    for user in usuarios.values():
        if user['id'] == user_id:
            return User(user['id'], user['username'], user['password'], user['role'])
    return None


def get_user_by_username(username):
    user = usuarios.get(username)
    if user:
        return User(user['id'], user['username'], user['password'], user['role'])
    return None


def validate_user(username, password):
    user = usuarios.get(username)
    return user and check_password_hash(user['password'], password)


@login_manager.user_loader
def load_user(user_id):
    return get_user_by_id(user_id)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = get_user_by_username(username)

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Credenciales inválidas')

    return render_template('login.html')


@app.route('/dashboard')
@login_required
def dashboard():
    if current_user.is_admin():
        return render_template('admin_dashboard.html')
    return render_template('user_dashboard.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
