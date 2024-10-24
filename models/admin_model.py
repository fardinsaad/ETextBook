from database.db_connection import Database

class AdminModel:
    def __init__(self):
        self.db = Database()

    def get_user(self, userID, password):
        query = "SELECT * FROM users WHERE userID = %s AND password = %s"
        cursor = self.db.execute_query(query, (userID, password))
        return cursor.fetchone()

    def get_all_users(self):
        query = "SELECT id, username FROM users"
        cursor = self.db.execute_query(query)
        return cursor.fetchall()
