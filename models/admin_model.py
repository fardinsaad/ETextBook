from database.db_connection import Database

class AdminModel:
    def __init__(self):
        self.db = Database()

    def get_user(self, userID, password):
        query = "SELECT * FROM users WHERE userID = %s AND password = %s"
        cursor = self.db.execute_query(query, (userID, password))
        user = cursor.fetchone()
        return user
    def get_all_users(self):
        query = "SELECT * FROM users"
        users = self.db.fetch_results(query=query)
        return users
