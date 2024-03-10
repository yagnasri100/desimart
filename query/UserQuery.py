import mysql.connector
from config import DatabaseManager
from model.UserModel import User
from config.DatabaseManager import DatabaseManager


class UserQuery:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.db_manager = DatabaseManager()

    def add_user(self, user):
        query = "INSERT INTO tbl_user (password, email_id, first_name, last_name, phone_no, address, city, state, zip_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.db_manager.execute_query(query, (
            user.password, user.email, user.firstname, user.lastname, user.phone, user.address, user.city, user.state,
            user.zipcode))

    def get_user(self, user):
        query = "SELECT user_id,email_id,first_name,last_name,password from desimart.tbl_user where email_id=%s and password=%s"
        return self.db_manager.execute_query(query, (user.email, user.password))

    def close(self):
        if self.db_manager:
            self.db_manager.close()
