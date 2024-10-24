class BookModel:
    def __init__(self, db):
        self.db = db

    def add_book(self, title, ISBN):
        query = "INSERT INTO books (title, ISBN) VALUES (%s, %s)"
        return self.db.execute_query(query, (title, ISBN))

    def get_book(self, title):
        query = "SELECT * FROM users WHERE title = %s"
        cursor = self.db.execute_query(query, (title))
        return cursor.fetchone()

    def get_all_books(self):
        query = "SELECT title FROM books"
        cursor = self.db.execute_query(query)
        return cursor.fetchall()
