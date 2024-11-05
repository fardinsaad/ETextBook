from database.db_connection import Database

class UserModel:
    def __init__(self):
        self.db = Database()

    def add_user(self, user):
        userID, firstName, lastName, email, password, role = user['userID'], user['firstName'], user['lastName'], user['email'], user['password'], user['role']
        query = "INSERT INTO User (userID, firstName, lastName, email, password, role) VALUES (%s, %s, %s, %s, %s, %s)"
        try:
            cursor = self.db.execute_query(query, (userID, firstName, lastName, email, password, role))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            self.db.connection.commit()
            print(f"User '{userID}' created successfully!")
            return 1
        except Exception as e:
            print(f"Failed to create User '{userID}': {e}")
            return 0

    def get_user_by_userID(self, userID):
        query = "SELECT * FROM User WHERE userID = %s"
        try:
            cursor = self.db.execute_query(query, (userID,))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            return cursor.fetchone()
        except Exception as e:
            print(f"Failed to get User '{userID}': {e}")
            return None
    
    def get_all_users(self):
        query = "SELECT * FROM User"
        cursor = self.db.execute_query(query)
        return cursor.fetchall()
