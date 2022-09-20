from flask_app.config.bd import connectToMySQL
from flask import flash

class Proceso:
    db_name = 'trackingcar'

    def __init__(self,db_data):
        self.id_proceso = db_data['id_proceso']
        self.abcmotor = db_data['abcmotor']
        self.abcfrenos = db_data['abcfrenos']
        self.suspension = db_data['suspension']
        self.liquidos = db_data['liquidos']
        self.luces = db_data['luces']
        self.autos_id_auto = db_data['autos_id_auto']
    
    @classmethod
    def save_prcesos(cls,data):
        query = "INSERT INTO procesos (autos_id_auto) VALUES (%(autos_id_auto)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)
        
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM procesos WHERE id_proceso = %(id_proceso)s;"
        print("Probando query: ",query)
        results = connectToMySQL(cls.db_name).query_db(query,data)
        print("Probando results: ",results)
        return cls( results[0] )
#        return results
        
    @classmethod
    def update(cls, data):
        query = "UPDATE procesos SET abcmotor=%(abcmotor)s, abcfrenos=%(abcfrenos)s, suspension=%(suspension)s, liquidos=%(liquidos)s, luces=%(luces)s,  updated_at=NOW() WHERE id_proceso = %(id_proceso)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        print("Los datos son: ",results)
        return connectToMySQL(cls.db_name).query_db(query,data)

    @staticmethod
    def validate_register(auto):
        is_valid = True
        query = "SELECT * FROM autos WHERE placa = %(placa)s;"
        results = connectToMySQL(Auto.db_name).query_db(query,auto)
        if len(results) >= 1:
            flash("Placa ya existe","register")
            is_valid=False
        if len(auto['placa']) < 3:
            flash("Placa minimo 3 caracteres","register")
            is_valid= False
        if len(auto['marca']) < 3:
            flash("Marca minimo 3 caracteres","register")
            is_valid= False
        if len(auto['modelo']) < 3:
            flash("Modelo minimo 3 caracteres","register")
            is_valid= False
