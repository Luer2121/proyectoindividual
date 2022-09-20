from flask_app.config.bd import connectToMySQL
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash

class Usuario:
    db_name = "trackingcar"

    def __init__(self,data):
        self.id_usuario= data['id_usuario']
        self.nombre = data['nombre'] 
        self.apellido = data['apellido']
        self.correo = data['correo']
        self.clave = data['clave']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def save(cls,data):
        query = "INSERT INTO usuarios (nombre,apellido,correo,clave,perfiles_id_perfil) VALUES(%(nombre)s,%(apellido)s,%(correo)s,%(clave)s,6)"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios WHERE id_usuario != '13';"
        results = connectToMySQL(cls.db_name).query_db(query)
        users = []
        for row in results:
            users.append(cls(row))
        return users

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM usuarios WHERE correo = %(correo)s AND perfiles_id_perfil =5 ;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_by_email2(cls,data):
        query = "SELECT * FROM usuarios WHERE correo = %(correo)s AND perfiles_id_perfil =6 ;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM usuarios WHERE id_usuario = %(id_usuario)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls(results[0])

    @staticmethod
    def validate_register(user):
        is_valid = True
        query = "SELECT * FROM usuarios WHERE correo = %(correo)s;"
        results = connectToMySQL(Usuario.db_name).query_db(query,user)
        if len(results) >= 1:
            flash("Email already taken.","register")
            is_valid=False
        if not EMAIL_REGEX.match(user['correo']):
            flash("Invalid Email!!!","register")
            is_valid=False
        if len(user['nombre']) < 3:
            flash("Nombre minimo 3 caracteres","register")
            is_valid= False
        if len(user['apellido']) < 3:
            flash("Apellido minimo 3 caracteres","register")
            is_valid= False
        if len(user['clave']) < 8:
            flash("Clave minimo 3 caracteres","register")
            is_valid= False

        if user['clave'] != user['confirmar']:
            flash("Clave no coincide","register")
        return is_valid