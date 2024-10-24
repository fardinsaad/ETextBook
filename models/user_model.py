from database.db_connection import Database

class UserModel:
    def __init__(self):
        self.db = Database()

    def add_user(self, username, password):
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        return self.db.execute_query(query, (username, password))

    def get_user(self, username, password):
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor = self.db.execute_query(query, (username, password))
        return cursor.fetchone()

    def get_all_users(self):
        query = "SELECT id, username FROM users"
        cursor = self.db.execute_query(query)
        return cursor.fetchall()
