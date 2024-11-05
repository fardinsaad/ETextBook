from database.db_connection import Database

class FacultyModel:
    def __init__(self):
        self.db = Database()
    def get_user(self, userID, password):
        query = "SELECT * FROM User WHERE userID = %s AND password = %s"
        cursor = self.db.execute_query(query, (userID, password))
        user = cursor.fetchone()
        return user

