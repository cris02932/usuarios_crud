from config.mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"

        resultado_query = connectToMySQL('usuario_crud').query_db(query)

        lista_usuarios = []

        for elemento in resultado_query:
            lista_usuarios.append(cls(elemento))

        return lista_usuarios

    @classmethod
    def save(cls, datos):
        query = "INSERT INTO usuarios (nombre, apellido, email, created_at, updated_at) VALUES (%(nombre)s, %(apellido)s, %(email)s, NOW(), NOW());"

        return connectToMySQL('usuario_crud').query_db(query, datos)

    @classmethod
    def get_by_id(cls, id):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"

        datos = {
            "id": id
        }

        resultado = connectToMySQL('usuario_crud').query_db(query, datos)

        return cls(resultado[0])

    @classmethod
    def update(cls, datos):
        query = "UPDATE usuarios SET nombre = %(nombre)s, apellido = %(apellido)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"

        return connectToMySQL('usuario_crud').query_db(query, datos)

    @classmethod
    def delete(cls, id):
        query = "DELETE FROM usuarios WHERE id = %(id)s;"

        datos = {
            "id": id
        }

        return connectToMySQL('usuario_crud').query_db(query, datos)
