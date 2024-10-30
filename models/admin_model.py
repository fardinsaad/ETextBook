from database.db_connection import Database
from datetime import datetime

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
    def addFaculty(self, firstName, lastName, email, password):
        query = "INSERT INTO User (userID, firstName, lastName, email, password, role) VALUES (%s, %s, %s, %s, %s, %s)"
        current_time = datetime.now()
        userID = firstName[:2]+lastName[:2]+current_time.strftime("%m")+current_time.strftime("%y")
        try:
            cursor = self.db.execute_query(query, (userID, firstName, lastName, email, password, "Faculty"))
            print("Faculty with userId: ", userID, " is created!!")
            return cursor
        except Exception as e:
            print(f"Faculty account not created. Try again!.")        

    def add(self, user):
        query = "INSERT INTO User VALUES(1, 'FAUL','PAGOL','CHAGOL')"
        # cursor = self.db.execute_query(query, (userID, password))
        # user = cursor.fetchone()
        # return user
