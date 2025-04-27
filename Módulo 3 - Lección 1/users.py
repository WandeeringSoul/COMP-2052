from flask_login import UserMixin


usuarios = {
    'Luis': {'id': '1', 'username': 'Luis', 'password': '1234'},
    'Samuel': {'id': '2', 'username': 'Samuel', 'password': 'abcd'}
}


class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def get_id(self):
        return self.id


def get_user_by_id(user_id):

    for user in usuarios.values():
        if user['id'] == user_id:
            return User(user['id'], user['username'], user['password'])
    return None


def get_user_by_username(username):

    user = usuarios.get(username)
    if user:
        return User(user['id'], user['username'], user['password'])
    return None


def validate_user(username, password):

    user = usuarios.get(username)
    return user and user['password'] == password
