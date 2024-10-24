import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG

class Database:
    _instance = None  # To hold the singleton instance

    def __new__(cls):
        """Create a single instance of Database class."""
        if cls._instance is None:
            try:
                cls._instance = super(Database, cls).__new__(cls)
                cls._instance.connection = mysql.connector.connect(**DB_CONFIG)
                if cls._instance.connection.is_connected():
                    print("Connected to MySQL database")
            except Error as e:
                print(f"Error connecting to MySQL: {e}")
                cls._instance = None
        return cls._instance

    def execute_query(self, query, values=None):
        """Execute a query and return the result."""
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, values)
            self.connection.commit()
            return cursor
        except Error as e:
            print(f"Error executing query: {e}")
            return None
