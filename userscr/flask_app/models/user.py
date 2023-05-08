from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db = "usercr"

    def __init__(self,data):
        self.id = data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def get_all_users(cls):
        query="""
            SELECT * FROM users;
            """
        results = connectToMySQL(cls.db).query_db(query)
        all_users=[]
        for user in results:
            all_users.append(cls(user))
        return all_users    
    @classmethod
    def get_one_user(cls,data):
        query = """
                SELECT * FROM users
                WHERE id = %(id)s;
                """
        results = connectToMySQL(cls.db).query_db(query,data)
        return cls(results[0])    
    @classmethod
    def save_user(cls, data):
        query = """
                INSERT INTO users (first_name, last_name, email)
                VALUES (%(first_name)s, %(last_name)s, %(email)s)
                """
        return connectToMySQL(cls.db).query_db(query, data)
    @classmethod
    def edit_user(cls, data):
        query = """
                UPDATE users
                SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s 
                WHERE id = %(id)s;
                """
        results = connectToMySQL(cls.db).query_db(query,data)
        return results
    
    @classmethod
    def delete_user(cls, data):
        query = """
                DELETE FROM users where id = %(id)s
                """
        results = connectToMySQL(cls.db).query_db(query, data)
        return results
