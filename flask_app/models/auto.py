from flask_app.config.bd import connectToMySQL
from flask import flash

class Auto:
    db_name = 'trackingcar'

    def __init__(self,db_data):
        self.id_auto = db_data['id_auto']
        self.placa = db_data['placa']
        self.marca = db_data['marca']
        self.modelo = db_data['modelo']
        self.usuarios_id_usuario = db_data['usuarios_id_usuario']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.nombre = db_data['nombre']
        self.apellido = db_data['apellido']
        self.id_proceso = db_data['id_proceso']
        self.abcmotor = db_data['abcmotor']
        self.abcfrenos = db_data['abcfrenos']
        self.suspension = db_data['suspension']
        self.liquidos = db_data['liquidos']
        self.luces = db_data['luces']
        self.autos_id_auto = db_data['autos_id_auto']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO autos (placa, marca, modelo, usuarios_id_usuario) VALUES (%(placa)s,%(marca)s,%(modelo)s,%(usuarios_id_usuario)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def save_prcesos(cls,data):
        query = "INSERT INTO procesos (abcmotor, abcfrenos, suspension, liquidos, luces, autos_id_auto) VALUES ('None','None','None','None','None',%(autos_id_auto)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM autos;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        all_autos = []
        for row in results:
            all_autos.append( cls(row) )
        return all_autos

    @classmethod
    def get_all2(cls):
        query = "SELECT * FROM usuarios INNER JOIN autos ON usuarios.id = autos.usuarios_id_usuario;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        all_autos_clientes = []
        for row in results:
            all_autos_clientes.append(cls(row) )
        return results

    @classmethod
    def get_all3(cls):
        query = "SELECT * FROM usuarios JOIN autos ON usuarios.id_usuario = autos.usuarios_id_usuario LEFT JOIN procesos ON autos.id_auto = procesos.autos_id_auto;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        all_autos_clientes_procesos = []
        for row in results:
            all_autos_clientes_procesos.append(cls(row) )
        return all_autos_clientes_procesos

    @classmethod
    def get_all4(cls,data):
        query = "SELECT * FROM usuarios JOIN autos ON usuarios.id_usuario = autos.usuarios_id_usuario LEFT JOIN procesos ON autos.id_auto = procesos.autos_id_auto WHERE id_usuario = %(id_usuario)s;"
        results =  connectToMySQL(cls.db_name).query_db(query,data)
        all_autos_clientes_procesos = []
        for row in results:
            all_autos_clientes_procesos.append(cls(row) )
        return all_autos_clientes_procesos



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
