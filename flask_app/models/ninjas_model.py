from flask_app.config.mysqlconnections import connectToMySQL
from flask_app import DATABASE

class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']

    @classmethod
    def create_ninja(cls,data):
        query = """
            INSERT INTO ninjas (first_name, last_name, age, dojo_id)
            VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s)
            """
        results = connectToMySQL(DATABASE).query_db(query,data)
        return results
    
    @classmethod
    def ninjas_in_dojo(cls,data):
        query = """
            SELECT * FROM ninjas
            WHERE dojo_id = %(id)s
            """
        results = connectToMySQL(DATABASE).query_db(query,data)
        all_ninjas = []
        for row_from_db in results:
            ninjas_instance = cls(row_from_db)
            all_ninjas.append(ninjas_instance)
        return all_ninjas