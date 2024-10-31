from database.db_connection import Database
class BookModel:
    def __init__(self):
        self.db = Database()

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
    
    def addEtextbook(self, textBookID, title):
        query = "INSERT INTO ETbook (textBookID, title) VALUES (%s, %s)"
        try:
            cursor = self.db.execute_query(query, (textBookID, title))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            print(f"E-textbook '{title}' created successfully!")
            return 1
        except Exception as e:
            print(f"Failed to create E-textbook '{title}': {e}") 
            return 0

    def addChapter(self, chapterID, primarychapterID, chapterTitle, secondarychapterID):
        query = "INSERT INTO Chapter (chapterID, primaryChapterNumber, title, secondaryChapterNumber) VALUES (%s, %s, %s, %s)"
        try:
            cursor = self.db.execute_query(query, (chapterID, primarychapterID, chapterTitle, secondarychapterID))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            print(f"Chapter '{chapterTitle}' created successfully!")
            return 1
        except Exception as e:
            print(f"Failed to create Chapter '{chapterTitle}': {e}")
            return 0  
    
    def addSection(self, sectionID, sectionTitle, primarySectionNumber, secondarySectionNumber):
        query = "INSERT INTO Section (sectionID, title, primarySectionNumber, secondarySectionNumber) VALUES (%s, %s, %s, %s)"
        try:
            cursor = self.db.execute_query(query, (sectionID, sectionTitle, primarySectionNumber, secondarySectionNumber))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            print(f"Section '{sectionTitle}' created successfully!")
            return 1
        except Exception as e:
            print(f"Failed to create Section '{sectionTitle}': {e}")
            return 0
        
    def addContentBlock(self, blockID, type, content):
        query = "INSERT INTO ContentBlock (blockID, blockType, content) VALUES (%s, %s, %s)"
        try:
            cursor = self.db.execute_query(query, (blockID, type, content))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            print(f"Text block '{blockID}' with '{type}' created successfully!")
            return 1
        except Exception as e:
            print(f"Failed to create Text block '{blockID}' with '{type}': {e}")
            return 0
