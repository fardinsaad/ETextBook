from database.db_connection import Database

class AdminModel:
    def __init__(self):
        self.db = Database()

    def get_user(self, userID, password):
        query = "SELECT * FROM User WHERE userID = %s AND password = %s"
        cursor = self.db.execute_query(query, (userID, password))
        user = cursor.fetchone()
        return user
    def get_all_users(self):
        query = "SELECT * FROM User"
        users = self.db.fetch_results(query=query)
        return users
    def add(self, user):
        query = "INSERT INTO User VALUES(1, 'FAUL','PAGOL','CHAGOL')"
        # cursor = self.db.execute_query(query, (userID, password))
        # user = cursor.fetchone()
        # return user
