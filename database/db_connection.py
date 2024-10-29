import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG
from threading import Lock

class Database:
    _instance = None  # Singleton instance
    _lock = Lock()  # For thread safety

    def __new__(cls):
        """Create a single instance of Database class (Thread-safe Singleton)."""
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    try:
                        cls._instance = super(Database, cls).__new__(cls)
                        cls._instance.connection = mysql.connector.connect(**DB_CONFIG)
                        if cls._instance.connection.is_connected():
                            print("Connected to MySQL database")
                        else:
                            print("Failed to connect to MySQL database")
                    except Error as e:
                        print(f"Error connecting to MySQL: {e}")
                        cls._instance = None
        return cls._instance

    def execute_query(self, query, values=None):
        """Execute a query and return the cursor object or None."""
        if not self.connection.is_connected():
            print("Database connection is closed.")
            return None

        try:
            cursor = self.connection.cursor()
            cursor.execute(query, values)
            return cursor
        except Error as e:
            print(f"Error executing query: {e}")
            return None

    def fetch_results(self, query, values=None):
        """Execute a query and fetch all results."""
        cursor = self.execute_query(query, values)
        if cursor:
            try:
                results = cursor.fetchall()
                return results
            except Error as e:
                print(f"Error fetching results: {e}")
                return None
            finally:
                cursor.close()
        else:
            print("No cursor returned. Query execution failed or no data.")

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Database connection closed.")

