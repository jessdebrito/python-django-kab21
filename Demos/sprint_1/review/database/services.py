# Importação absoluta: parte do repositorio de trabalho ( ( from main import users //
#                                                     from database.db import users)
# Importação relativa: import a partir de onde estou/arquivo (from .db import users)

from database.db import users

def creat_user(username, telefone, password):
    next_id = len(users) + 1
    new_user = {"username": username, "telefone": telefone, "password": password, "id": next_id }
    users.append(new_user)
    return new_user

def get_all_users():
    return users

def get_user_by_id(id):
    try:
        user = [u for u in users if u['id']  == id] [0]
        return user
    except IndexError:
        return f"O usuário com o id {id} não existe."

def delete_user_by_id(id):
    for user in users:
        if user['id'] == id:
            users.remove(user)
    return user

def update_user(id, **kwargs):
    found_user: dict = get_user_by_id(id)
    for key, value in found_user.items():
        found_user[key] = kwargs.get(key, value)
    return found_user
