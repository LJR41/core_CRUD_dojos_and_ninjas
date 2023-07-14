from flask_app.config.mysqlconnections import connectToMySQL
from flask_app import DATABASE

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def display_dojo(cls):
        query = """
            SELECT * FROM dojos
            """
        results = connectToMySQL(DATABASE).query_db(query)
        all_dojos = []
        for row_from_db in results:
            dojos_instance = cls(row_from_db)
            all_dojos.append(dojos_instance)
        return all_dojos
    
    @classmethod
    def create_dojo(cls,data):
        query = """
            INSERT INTO dojos (name)
            VALUES (%(name)s)
            """
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def show_dojo(cls,data):
        query = """
            SELECT * FROM dojos
            WHERE id = %(id)s
            """
        results = connectToMySQL(DATABASE).query_db(query,data)
        if results:
            dojo_instance = cls(results[0])
            return dojo_instance
        return results
