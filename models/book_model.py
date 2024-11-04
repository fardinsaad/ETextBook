from database.db_connection import Database
from mysql.connector import Error

class BookModel:
    def __init__(self):
        self.db = Database()

    def getETextBookById(self, textBookID, userID):
        query = "SELECT * FROM ETbook WHERE textBookID = %s and userID = %s"
        try:
            cursor = self.db.execute_query(query, (textBookID, userID,))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            return cursor.fetchone()
        except Exception as e:
            print(f"Failed to get E-textbook with ID {textBookID}: {e}")
            return None
    def addEtextbook(self, textBookID, title, userID):
        print(textBookID, title, userID)
        query = "INSERT INTO ETbook (textBookID, title, userID) VALUES (%s, %s, %s)"
        try:
            cursor = self.db.execute_query(query, (textBookID, title, userID))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            print(f"E-textbook '{title}' created successfully!")
            return 1
        except Exception as e:
            print(f"Failed to create E-textbook '{title}': {e}") 
            return 0

    def getchapterByTextBookId_chapterID(self, textBookID, chapterID, userID):
        query = "SELECT * FROM Chapter WHERE textBookID = %s AND chapterID = %s and userID = %s"
        try:
            cursor = self.db.execute_query(query, (textBookID, chapterID, userID,))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            return cursor.fetchone()
        except Exception as e:
            print(f"Failed to get chapterID with textBookID {chapterID}, {textBookID}: {e}")
            return None
    def addChapter(self, chapterID, chapterTitle, textBookID, userID):
        query = "INSERT INTO Chapter (chapterID, title, textBookID, userID) VALUES (%s, %s, %s, %s)"
        try:
            cursor = self.db.execute_query(query, (chapterID, chapterTitle, textBookID, userID))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            print(f"Chapter '{chapterTitle}' created successfully!")
            return 1
        except Exception as e:
            print(f"Failed to create Chapter '{chapterTitle}': {e}")
            return 0  
    def getSectionByChapterID_SectionID(self, textBookID, chapterID, sectionID, userID):
        query = "SELECT * FROM Section WHERE textBookID=%s AND chapterID = %s AND sectionID = %s AND userID = %s"
        try:
            cursor = self.db.execute_query(query, (textBookID, chapterID, sectionID, userID,))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            return cursor.fetchone()
        except Exception as e:
            print(f"Failed to get Section with chapterID {chapterID}, sectionID {sectionID}: {e}")
            return None
    def addSection(self, sectionID, title, textBookID, chapterID, userID):
        query = "INSERT INTO Section (sectionID, title, textBookID, chapterID, userID) VALUES (%s, %s, %s, %s, %s)"
        try:
            cursor = self.db.execute_query(query, (sectionID, title, textBookID, chapterID, userID))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            print(f"Section '{title}' created successfully!")
            return 1
        except Exception as e:
            print(f"Failed to create Section '{title}': {e}")
            return 0
        
    def getContentBlock(self, blockID, blockType, textBookID, chapterID, sectionID, userID):
        query = "SELECT * FROM ContentBlock WHERE blockID = %s AND blockType = %s AND textBookID = %s AND chapterID = %s AND sectionID = %s AND userID = %s"
        try:
            cursor = self.db.execute_query(query, (blockID, blockType, textBookID, chapterID, sectionID, userID,))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            return cursor.fetchone()
        except Exception as e:
            print(f"Failed to get Text block with ID {blockID}: {e}")
            return None
    def updateContentBlock(self, blockID, blockType, content, textBookID, chapterID, sectionID, userID):
        query = "UPDATE ContentBlock SET content = %s WHERE blockID = %s AND blockType = %s AND textBookID = %s AND chapterID = %s AND sectionID = %s AND userID = %s"
        try:
            cursor = self.db.execute_query(query, (content, blockID, blockType, textBookID, chapterID, sectionID, userID))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            print(f"Text block '{blockID}' with '{type}' updated successfully!")
            return 1
        except Exception as e:
            print(f"Failed to update Text block '{blockID}' with '{type}': {e}")
            return 0
    def addContentBlock(self, blockID, blockType, content, textBookID, chapterID, sectionID, userID):
        query = "INSERT INTO ContentBlock (blockID, blockType, content, textBookID, chapterID, sectionID, userID) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        try:
            cursor = self.db.execute_query(query, (blockID, blockType, content, textBookID, chapterID, sectionID, userID))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            print(f"Text block '{blockID}' with '{type}' created successfully!")
            return 1
        except Exception as e:
            print(f"Failed to create Text block '{blockID}' with '{type}': {e}")
            return 0
        
    def addContentTransaction(self, ebook):
        try:
            self.db.connection.start_transaction()
            if(self.getETextBookById(ebook['textBookID'], ebook['userID']) is None):
                self.addEtextbook(ebook['textBookID'], ebook['title'], ebook['userID'])
            if(self.getchapterByTextBookId_chapterID(ebook['textBookID'], ebook['chapterID'], ebook['userID']) is None):
                self.addChapter(ebook['chapterID'], ebook['chapterTitle'], ebook['textBookID'], ebook['userID'])
            if(self.getSectionByChapterID_SectionID(ebook['textBookID'], ebook['chapterID'], ebook['sectionID'], ebook['userID']) is None):
                self.addSection(ebook['sectionID'], ebook['sectionTitle'], ebook['textBookID'], ebook['chapterID'], ebook['userID'])
            if(self.getContentBlock(ebook['contentblockID'], ebook['blockType'], ebook['textBookID'], ebook['chapterID'], ebook['sectionID'], ebook['userID']) is None):
                self.addContentBlock(ebook['contentblockID'], ebook['blockType'], ebook['content'], ebook['textBookID'], ebook['chapterID'], ebook['sectionID'], ebook['userID'])
            else:
                print("You can not add the content block as it already exists. You can modify it.")
            self.db.connection.commit()
            return 1
        except Error as e:
            if self.db.connection.is_connected():
                self.db.connection.rollback()
                print("Transaction rolled back due to error:", e)
            return 0

    def getQuestionById(self, questionID, activityID, blockID, sectionID, chapterID, textBookID, userID):
        query = "SELECT * FROM Question WHERE questionID = %s AND activityID = %s AND blockID = %s AND sectionID = %s AND chapterID = %s AND textBookID = %s AND userID = %s"
        try:
            cursor = self.db.execute_query(query, (questionID, activityID, blockID, sectionID, chapterID, textBookID, userID,))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            return cursor.fetchone()
        except Exception as e:
            print(f"Failed to get Question with ID {questionID}: {e}")
            return None
    def addQuestion(self, questionID, textBookID, chapterID, sectionID, blockID, activityID, question, OP1, OP1_EXP, OP1_Label, OP2, OP2_EXP, OP2_Label, OP3, OP3_EXP, OP3_Label, OP4, OP4_EXP, OP4_Label, userID):
        query = "INSERT INTO Question (questionID, textBookID, chapterID, sectionID, blockID, activityID, question, OP1, OP1_EXP, OP1_Label, OP2, OP2_EXP, OP2_Label, OP3, OP3_EXP, OP3_Label, OP4, OP4_EXP, OP4_Label, userID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            cursor = self.db.execute_query(query, (questionID, textBookID, chapterID, sectionID, blockID, activityID, question, OP1, OP1_EXP, OP1_Label, OP2, OP2_EXP, OP2_Label, OP3, OP3_EXP, OP3_Label, OP4, OP4_EXP, OP4_Label, userID))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            print(f"Question '{questionID}' created successfully!")
            return 1
        except Exception as e:
            print(f"Failed to create Question '{questionID}': {e}")
            return 0
    
    def getActivtyById(self, activityID, textBookID, chapterID, sectionID, blockID, userID):
        query = "SELECT * FROM Activity WHERE activityID = %s AND textBookID = %s AND chapterID = %s AND sectionID = %s AND blockID = %s AND userID = %s"
        try:
            cursor = self.db.execute_query(query, (activityID, textBookID, chapterID, sectionID, blockID, userID))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            return cursor.fetchone()
        except Exception as e:
            print(f"Failed to get Activity with ID {activityID}: {e}")
            return None
    def addActivity(self, activityID, textBookID, chapterID, sectionID, blockID, userID):
        query = "INSERT INTO Activity (activityID, textBookID, chapterID, sectionID, blockID, userID) VALUES (%s, %s, %s, %s, %s, %s)"
        try:
            cursor = self.db.execute_query(query, (activityID, textBookID, chapterID, sectionID, blockID, userID))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            print(f"Activity '{activityID}' created successfully!")
            return 1
        except Exception as e:
            print(f"Failed to create Activity '{activityID}': {e}")
            return 0
    def addActivtyTransaction(self, ebook):
        try:
            self.db.connection.start_transaction()
            if(self.getETextBookById(ebook['textBookID'], ebook['userID']) is None):
                self.addEtextbook(ebook['textBookID'], ebook['title'], ebook['userID'])
            if(self.getchapterByTextBookId_chapterID(ebook['textBookID'], ebook['chapterID'], ebook['userID']) is None):
                self.addChapter(ebook['chapterID'], ebook['chapterTitle'], ebook['textBookID'], ebook['userID'])
            if(self.getSectionByChapterID_SectionID(ebook['textBookID'], ebook['chapterID'], ebook['sectionID'], ebook['userID']) is None):
                self.addSection(ebook['sectionID'], ebook['sectionTitle'], ebook['textBookID'], ebook['chapterID'], ebook['userID'])
            if(self.getContentBlock(ebook['contentblockID'], ebook['blockType'], ebook['textBookID'], ebook['chapterID'], ebook['sectionID'], ebook['userID']) is None):
                self.addContentBlock(ebook['contentblockID'], ebook['blockType'], ebook['content'], ebook['textBookID'], ebook['chapterID'], ebook['sectionID'], ebook['userID'])
            if(self.getActivtyById(ebook['activityID'], ebook['textBookID'], ebook['chapterID'], ebook['sectionID'], ebook['contentblockID'], ebook['userID']) is None):
                self.addActivity(ebook['activityID'], ebook['textBookID'], ebook['chapterID'], ebook['sectionID'], ebook['contentblockID'], ebook['userID'])
            if(self.getQuestionById(ebook['questionID'], ebook['activityID'], ebook['contentblockID'], ebook['sectionID'], ebook['chapterID'], ebook['textBookID'], ebook['userID']) is None):
                self.addQuestion(ebook['questionID'], ebook['textBookID'], ebook['chapterID'], ebook['sectionID'], ebook['contentblockID'], ebook['activityID'], ebook['question'], ebook['OP1'], ebook['OP1_EXP'], ebook['OP1_Label'], ebook['OP2'], ebook['OP2_EXP'], ebook['OP2_Label'], ebook['OP3'], ebook['OP3_EXP'], ebook['OP3_Label'], ebook['OP4'], ebook['OP4_EXP'], ebook['OP4_Label'], ebook['userID'])
            else:
                print("You can not add the same question ID as it already exists. You can modify it.")
            
            self.db.connection.commit()
            return 1
        except Error as e:
            if self.db.connection.is_connected():
                self.db.connection.rollback()
                print("Transaction rolled back due to error:", e)
            return 0
    