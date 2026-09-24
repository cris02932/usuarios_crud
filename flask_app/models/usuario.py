from config.mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self, data):
        self.id=data['id']
        self.nombre=data['nombre']
        self.apellido=data['apellido']
        self.email=data['email']
        self.created_at=['created_at']
        self.updated_at=['updated_at']


    @classmethod
    def get_all(cls):

        query = "SELECT * FROM usuarios;"

        resultado_query= connectToMySQL('usuario_crud').query_db(query)
        print(resultado_query)

        lista_usuarios = []

        for elemento in resultado_query:
            lista_usuarios.append(cls(elemento))

        return lista_usuarios

    @classmethod
    def save (cls, datos):
        query = "INSERT INTO usuarios (nombre, apellido, email, created_at, updated_at) VALUES (%(nombre)s, %(apellido)s, %(email)s, NOW(), NOW());"

        return connectToMySQL('usuario_crud').query_db(query, datos)

        