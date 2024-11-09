from database.db_connection import Database
from mysql.connector import Error


class FacultyModel:
    def __init__(self):
        self.db = Database()
        
    # DONE
    def get_user(self, userID, password):
        query = "SELECT * FROM User WHERE userID = %s AND password = %s AND role = 'Faculty'"
        cursor = self.db.execute_query(query, (userID, password))
        user = cursor.fetchone()
        return user
    
    # DONE
    def addTA_to_User(self, userID, firstName, lastName, email, password):
        
        query = "INSERT INTO User (userID, firstName, lastName, email, password, role) VALUES (%s, %s, %s, %s, %s, %s)"
        try:
            cursor = self.db.execute_query(query, (userID, firstName, lastName, email, password, "TA"))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            
            self.db.connection.commit()
            print("TA with userId: ", userID, " is created!!")
            return True
        except Exception as e:
            print(f"TA account not created. {e}")
            return False
    # DONE
    def addTA_to_Course(self, uToken, userID, courseID):
        query = "INSERT INTO ActiveCourseTA (uToken, TAID) VALUES (%s, %s)"
        try:
            cursor = self.db.execute_query(query, (uToken, userID))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            
            self.db.connection.commit()
            print("TA with userId: ", userID, " is added to courseID: ", courseID)
            return True
        except Exception as e:
            print(f"TA account not added to course. Try again! {e}")
            return False
    
    def update_password(self, userID, password):
        query = "UPDATE User SET password = %s WHERE userID = %s"
        try:
            cursor = self.db.execute_query(query, (password, userID))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            self.db.connection.commit()
            return 1
        except Exception as e:
            print(f"Failed to update password for Faculty '{userID}': {e}")
            return 0

    def get_courses_by_userID(self, FID):
        query = """
                SELECT courseID, title, startDate, endDate, courseType
                FROM Course c
                WHERE c.userID = %s
                """
        try:
            cursor = self.db.execute_query(query, (FID,))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            return cursor.fetchall()
        except Exception as e:
            print(f"Failed to get courses for Faculty '{FID}': {e}")
            return None
        
    def get_faculty_by_userID(self, userID):
        query = "SELECT * FROM Faculty WHERE userID = %s"
        cursor = self.db.execute_query(query, (userID,))
        return cursor.fetchone()
    # DONE
    def is_faculty_in_course(self, userID, courseID):
        query = """
            SELECT COUNT(*)
            FROM ETextBook.Course c
            WHERE c.userID = %s AND c.courseID = %s
        """
        try:
            cursor = self.db.execute_query(query, (userID, courseID))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            result = cursor.fetchone()
            return result[0] > 0
        except Exception as e:
            print(f"Failed to check if Faculty '{userID}' is in course '{courseID}': {e}")
            return False
    # DONE    
    def get_uToken_by_courseID(self, courseID):
        query = "SELECT uToken FROM ETextBook.ActiveCourse WHERE courseID = %s"
        try:
            cursor = self.db.execute_query(query, (courseID,))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                return None
        except Exception as e:
            print(f"Failed to get uToken for courseID {courseID}: {e}")
            return None
    # DONE
    def get_worklist(self, uToken):
        query = """
            SELECT u.userID, u.firstName, u.lastName, ae.c_status
            FROM ETextBook.ActiveEnrollment ae
            JOIN ETextBook.User u ON ae.studentID = u.userID
            WHERE ae.uToken = %s
        """
        try:
            cursor = self.db.execute_query(query, (uToken,))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            return cursor.fetchall()
        except Exception as e:
            print(f"Failed to get worklist for uToken {uToken}: {e}")
            return None
    # DONE
    def is_valid_student(self, uToken, studentID):
        query = "SELECT COUNT(*) FROM ETextBook.ActiveEnrollment WHERE uToken = %s AND studentID = %s"
        try:
            cursor = self.db.execute_query(query, (uToken, studentID,))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            result = cursor.fetchone()
            return result[0] > 0
        except Exception as e:
            print(f"Failed to check if student '{studentID}' is valid: {e}")
            return False   
    # DONE   
    def is_status_pending(self, uToken, studentID):
        query = """
            SELECT COUNT(*)
            FROM ETextBook.ActiveEnrollment
            WHERE uToken = %s AND studentID = %s AND c_status = 'Pending'
        """
        try:
            cursor = self.db.execute_query(query, (uToken, studentID))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            result = cursor.fetchone()
            return result[0] > 0
        except Exception as e:
            print(f"Failed to check if student '{studentID}' has pending status: {e}")
            return False
    # DONE 
    def approve_enrollment(self, uToken, studentID):
        query = """
            UPDATE ETextBook.ActiveEnrollment
            SET c_status = 'Enrolled'
            WHERE uToken = %s AND studentID = %s
        """
        try:
            cursor = self.db.execute_query(query, (uToken, studentID))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            self.db.connection.commit()
            return 1
        except Exception as e:
            print(f"Failed to approve enrollment for student {studentID}: {e}")
            return 0
    # DONE    
    def get_enrolled_students(self, uToken, status):
        query = """
            SELECT u.userID, u.firstName, u.lastName
            FROM ETextBook.ActiveEnrollment ae
            JOIN ETextBook.User u ON ae.studentID = u.userID
            WHERE ae.uToken = %s AND ae.c_status = %s
        """
        try:
            cursor = self.db.execute_query(query, (uToken, status))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            return cursor.fetchall()
        except Exception as e:
            print(f"Failed to get enrolled students for uToken {uToken}: {e}")
            return None



    # DONE
    def getchapterByTextBookId_chapterID(self, ebook):
        textBookID, chapterID, userID = ebook['textBookID'], ebook['chapterID'], ebook['userID']
        query = "SELECT * FROM Chapter WHERE textBookID = %s AND chapterID = %s"
        try:
            cursor = self.db.execute_query(query, (textBookID, chapterID,))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            return cursor.fetchone()
        except Exception as e:
            print(f"Failed to get chapterID with textBookID {chapterID}, {textBookID}: {e}")
            return None
    # DONE
    def addChapter(self, ebook):
        chapterID, chapterTitle, textBookID, userID = ebook['chapterID'], ebook['chapterTitle'], ebook['textBookID'], ebook['userID']
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
    # DONE
    def getSectionByChapterID_SectionID(self, ebook):
        textBookID, chapterID, sectionID, userID = ebook['textBookID'], ebook['chapterID'], ebook['sectionID'], ebook['userID']
        query = "SELECT * FROM Section WHERE textBookID=%s AND chapterID = %s AND sectionID = %s"
        try:
            cursor = self.db.execute_query(query, (textBookID, chapterID, sectionID,))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            return cursor.fetchone()
        except Exception as e:
            print(f"Failed to get Section with chapterID {chapterID}, sectionID {sectionID}: {e}")
            return None
    # DONE
    def addSection(self, ebook):
        sectionID, title, textBookID, chapterID, userID = ebook['sectionID'], ebook['sectionTitle'], ebook['textBookID'], ebook['chapterID'], ebook['userID']
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
    # DONE
    def getContentBlock(self, ebook):
        blockID, blockType, textBookID, chapterID, sectionID, userID = ebook['contentblockID'], ebook['blockType'], ebook['textBookID'], ebook['chapterID'], ebook['sectionID'], ebook['userID']
        query = "SELECT * FROM ContentBlock WHERE blockID = %s AND blockType = %s AND textBookID = %s AND chapterID = %s AND sectionID = %s"
        try:
            cursor = self.db.execute_query(query, (blockID, blockType, textBookID, chapterID, sectionID,))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            return cursor.fetchone()
        except Exception as e:
            print(f"Failed to get Text block with ID {blockID}: {e}")
            return None
    # DONE
    def addContentBlock(self, ebook):
        blockID, blockType, content, textBookID, chapterID, sectionID, userID = ebook['contentblockID'], ebook['blockType'], ebook['content'], ebook['textBookID'], ebook['chapterID'], ebook['sectionID'], ebook['userID']
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
    # DONE 
    def addContentTransaction(self, ebook):
        try:
            if not self.db.connection.in_transaction:
                self.db.connection.start_transaction()
            if(self.getchapterByTextBookId_chapterID(ebook) is None):
                self.addChapter(ebook)
            if(self.getSectionByChapterID_SectionID(ebook) is None):
                self.addSection(ebook)
            if(self.getContentBlock(ebook) is None):
                self.addContentBlock(ebook)
            else:
                print("You can not add the content block as it already exists. You can modify it.")
            self.db.connection.commit()
            return 1
        except Error as e:
            if self.db.connection.is_connected():
                self.db.connection.rollback()
                print("Transaction rolled back due to error:", e)
            return 0
        
    def getQuestionById(self, ebook):
        questionID, activityID, blockID, sectionID, chapterID, textBookID, userID = ebook['questionID'], ebook['activityID'], ebook['contentblockID'], ebook['sectionID'], ebook['chapterID'], ebook['textBookID'], ebook['userID']
        query = "SELECT * FROM Question WHERE questionID = %s AND activityID = %s AND blockID = %s AND sectionID = %s AND chapterID = %s AND textBookID = %s"
        try:
            cursor = self.db.execute_query(query, (questionID, activityID, blockID, sectionID, chapterID, textBookID,))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            return cursor.fetchone()
        except Exception as e:
            print(f"Failed to get Question with ID {questionID}: {e}")
            return None
        
    def addQuestion(self, ebook):
        questionID, textBookID, chapterID, sectionID, blockID, activityID, question, OP1, OP1_EXP, OP1_Label, OP2, OP2_EXP, OP2_Label, OP3, OP3_EXP, OP3_Label, OP4, OP4_EXP, OP4_Label, userID = ebook['questionID'], ebook['textBookID'], ebook['chapterID'], ebook['sectionID'], ebook['contentblockID'], ebook['activityID'], ebook['question'], ebook['OP1'], ebook['OP1_EXP'], ebook['OP1_Label'], ebook['OP2'], ebook['OP2_EXP'], ebook['OP2_Label'], ebook['OP3'], ebook['OP3_EXP'], ebook['OP3_Label'], ebook['OP4'], ebook['OP4_EXP'], ebook['OP4_Label'], ebook['userID']
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
    # DONE
    def getActivtyById(self, ebook):
        activityID, textBookID, chapterID, sectionID, blockID, userID = ebook['activityID'], ebook['textBookID'], ebook['chapterID'], ebook['sectionID'], ebook['contentblockID'], ebook['userID']
        query = "SELECT * FROM Activity WHERE activityID = %s AND textBookID = %s AND chapterID = %s AND sectionID = %s AND blockID = %s"
        try:
            cursor = self.db.execute_query(query, (activityID, textBookID, chapterID, sectionID, blockID,))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            return cursor.fetchone()
        except Exception as e:
            print(f"Failed to get Activity with ID {activityID}: {e}")
            return None
    # DONE
    def addActivity(self, ebook):
        activityID, textBookID, chapterID, sectionID, blockID, userID = ebook['activityID'], ebook['textBookID'], ebook['chapterID'], ebook['sectionID'], ebook['contentblockID'], ebook['userID']
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
    # DONE
    def addActivtyTransaction(self, ebook):
        try:
            if not self.db.connection.in_transaction:
                self.db.connection.start_transaction()
            if(self.getchapterByTextBookId_chapterID(ebook) is None):
                self.addChapter(ebook)
            if(self.getSectionByChapterID_SectionID(ebook) is None):
                self.addSection(ebook)
            if(self.getContentBlock(ebook) is None):
                self.addContentBlock(ebook)
            if(self.getActivtyById(ebook) is None):
                self.addActivity(ebook)
            if(self.getQuestionById(ebook) is None):
                self.addQuestion(ebook)
            else:
                print("You can not add the same question ID as it already exists. You can modify it.")
            
            self.db.connection.commit()
            return 1
        except Error as e:
            if self.db.connection.is_connected():
                self.db.connection.rollback()
                print("Transaction rolled back due to error:", e)
            return 0
    # DONE
    def is_allowed_to_modify_for_text_picture(self, ebook):
        blockID, blockType, textBookID, chapterID, sectionID, userID = ebook['contentblockID'], ebook['blockType'], ebook['textBookID'], ebook['chapterID'], ebook['sectionID'], ebook['userID']
        query = "SELECT role from User where userID = (SELECT userID FROM ContentBlock WHERE blockID = %s AND blockType = %s AND textBookID = %s AND chapterID = %s AND sectionID = %s)"
        try:
            cursor = self.db.execute_query(query, (blockID, blockType, textBookID, chapterID, sectionID,))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            result = cursor.fetchone()
            if result is None:
                return False
            role = result[0]
            return role != 'Admin'
        except Exception as e:
            print(f"Failed to get Text block with ID {blockID}: {e}")
            return None
    # DONE 
    def is_allowed_to_modify_for_activity_question(self, ebook):
        questionID, activityID, blockID, sectionID, chapterID, textBookID, userID = ebook['questionID'], ebook['activityID'], ebook['contentblockID'], ebook['sectionID'], ebook['chapterID'], ebook['textBookID'], ebook['userID']
        query = "SELECT role from User where userID = (SELECT userID FROM Question WHERE questionID = %s AND activityID = %s AND blockID = %s AND sectionID = %s AND chapterID = %s AND textBookID = %s)"
        try:
            cursor = self.db.execute_query(query, (questionID, activityID, blockID, sectionID, chapterID, textBookID,))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            result = cursor.fetchone()
            if result is None:
                return False
            role = result[0]
            return role != 'Admin'
        except Exception as e:
            print(f"Failed to get Question with ID {questionID}: {e}")
            return None
    # DONE
    def update_modifiedContentBlock(self, ebook):
        blockID, blockType, content, textBookID, chapterID, sectionID, userID = ebook['contentblockID'], ebook['blockType'], ebook['content'], ebook['textBookID'], ebook['chapterID'], ebook['sectionID'], ebook['userID']
        query = "UPDATE ContentBlock SET content = %s, userID = %s WHERE blockID = %s AND blockType = %s AND textBookID = %s AND chapterID = %s AND sectionID = %s"
        try:
            cursor = self.db.execute_query(query, (content, userID, blockID, blockType, textBookID, chapterID, sectionID,))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            print(f"Content block '{blockID}' with '{type}' updated successfully!")
            return 1
        except Exception as e:
            print(f"Failed to update Content block '{blockID}' with '{type}': {e}")
            return 0
    # DONE
    def update_modifiedActivityQuestion(self, ebook):
        questionID, textBookID, chapterID, sectionID, blockID, activityID, question, OP1, OP1_EXP, OP1_Label, OP2, OP2_EXP, OP2_Label, OP3, OP3_EXP, OP3_Label, OP4, OP4_EXP, OP4_Label, userID = ebook['questionID'], ebook['textBookID'], ebook['chapterID'], ebook['sectionID'], ebook['contentblockID'], ebook['activityID'], ebook['question'], ebook['OP1'], ebook['OP1_EXP'], ebook['OP1_Label'], ebook['OP2'], ebook['OP2_EXP'], ebook['OP2_Label'], ebook['OP3'], ebook['OP3_EXP'], ebook['OP3_Label'], ebook['OP4'], ebook['OP4_EXP'], ebook['OP4_Label'], ebook['userID']
        query = "UPDATE Question SET question = %s, userID = %s, OP1 = %s, OP1_EXP = %s, OP1_Label = %s, OP2 = %s, OP2_EXP = %s, OP2_Label = %s, OP3 = %s, OP3_EXP = %s, OP3_Label = %s, OP4 = %s, OP4_EXP = %s, OP4_Label = %s WHERE questionID = %s AND activityID = %s AND blockID = %s AND sectionID = %s AND chapterID = %s AND textBookID = %s"
        try:
            cursor = self.db.execute_query(query, (question, userID, OP1, OP1_EXP, OP1_Label, OP2, OP2_EXP, OP2_Label, OP3, OP3_EXP, OP3_Label, OP4, OP4_EXP, OP4_Label, questionID, activityID, blockID, sectionID, chapterID, textBookID,))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            print(f"Question '{questionID}' updated successfully!")
            return 1
        except Exception as e:
            print(f"Failed to update Question '{questionID}': {e}")
            return 0
    # DONE
    def modifyContentTransaction(self, ebook, type):
        try:
            if not self.db.connection.in_transaction:
                self.db.connection.start_transaction()
            if(self.getContentBlock(ebook) is not None):
                if type == "text" or type == "picture":
                    if self.is_allowed_to_modify_for_text_picture(ebook):
                        self.update_modifiedContentBlock(ebook)
                    else:
                        print("You can not modify the content block as you are not allowed to modify it.")
                elif type == "activity":
                    if self.is_allowed_to_modify_for_activity_question(ebook):
                        self.update_modifiedActivityQuestion(ebook)
                    else:
                        print("You can not modify the content block as you are not allowed to modify it.")
            else:
                print("You can not modify the content block as it does not exist. You can add it.")
            self.db.connection.commit()
            return 1
        except Error as e:
            if self.db.connection.is_connected():
                self.db.connection.rollback()
                print("Transaction rolled back due to error:", e)
            return 0
      
        
    # HIDING AND DELETING EBOOK CONTENT    
    def deleteChapter(self, ebook):
        chapterID = ebook['chapterID']
        textBookID = ebook['textBookID']
        
        query = """
            DELETE c
            FROM Chapter c
            JOIN User u ON u.userID = c.userID
            WHERE c.chapterID = %s AND c.textBookID = %s AND (u.role = 'TA' OR u.role = 'Faculty')
        """
        
        try:
            cursor = self.db.execute_query(query, (chapterID, textBookID))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            if cursor.rowcount == 0:
                print(f"No chapter with ID '{chapterID}' was deleted. You do not have permission to delete it.")
                return 0
            print(f"Chapter '{chapterID}' deleted successfully!")
            self.db.connection.commit()
            return 1
        except Exception as e:
            print(f"Failed to delete chapter '{chapterID}': {e} as you are not allowed to delete it.")
            return 0
        
    def deleteSection(self, ebook):
        chapterID = ebook['chapterID']
        textBookID = ebook['textBookID']
        sectionID = ebook['sectionID']
        
        query = """
            DELETE s
            FROM Section s
            JOIN User u ON u.userID = s.userID
            WHERE s.sectionID = %s AND s.chapterID = %s AND s.textBookID = %s AND (u.role = 'TA' OR u.role = 'Faculty')
        """
        
        try:
            cursor = self.db.execute_query(query, (sectionID, chapterID, textBookID))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            if cursor.rowcount == 0:
                print(f"No section with ID '{sectionID}' was deleted. You do not have permission to delete it.")
                return 0
            print(f"Section '{sectionID}' deleted successfully!")
            self.db.connection.commit()
            return 1
        except Exception as e:
            print(f"Failed to delete section '{sectionID}': {e}")
            return 0
        
    def deleteContentBlock(self, ebook):
        blockID = ebook['contentblockID']
        textBookID = ebook['textBookID']
        chapterID = ebook['chapterID']
        sectionID = ebook['sectionID']
        
        query = """
            DELETE cb
            FROM ContentBlock cb
            JOIN User u ON u.userID = cb.userID
            WHERE cb.blockID = %s AND cb.textBookID = %s AND cb.chapterID = %s AND cb.sectionID = %s 
            AND (u.role = 'TA' OR u.role = 'Faculty')
        """
        
        try:
            cursor = self.db.execute_query(query, (blockID, textBookID, chapterID, sectionID))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            if cursor.rowcount == 0:
                print(f"No content block with ID '{blockID}' was deleted. You do not have permission to delete it.")
                return 0
            print(f"Content block '{blockID}' deleted successfully!")
            self.db.connection.commit()
            return 1
        except Exception as e:
            print(f"Failed to delete Text block '{blockID}': {e}")
            return 0
        
     # HIDING EBOOK CONTENT   
      
    def deleteActivity(self, ebook):
        content = ebook['activityID']
        textBookID = ebook['textBookID']
        chapterID = ebook['chapterID']
        sectionID = ebook['sectionID']
        blockID = ebook['contentblockID']
        
        query = """
            DELETE cb
            FROM ContentBlock cb
            JOIN User u ON u.userID = cb.userID
            WHERE cb.blockID = %s AND cb.textBookID = %s AND cb.chapterID = %s AND cb.sectionID = %s AND cb.content = %s 
            AND (u.role = 'TA' OR u.role = 'Faculty')
        """
        
        try:
            cursor = self.db.execute_query(query, (blockID, textBookID, chapterID, sectionID, content))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            if cursor.rowcount == 0:
                print(f"No activity with ID '{content}' was deleted. You do not have permission to delete it.")
                return 0
            print(f"Activity '{content}' deleted successfully!")
            self.db.connection.commit()
            return 1
        except Exception as e:
            print(f"Failed to delete activity '{content}': {e}")
            return 0  
      
    def iscontentBlockExists_in_content_user_activity(self, ebook):
        blockID = ebook['contentblockID']
        textBookID = ebook['textBookID']
        chapterID = ebook['chapterID']
        sectionID = ebook['sectionID']
        courseID = ebook['courseID']
        
        query = """
            SELECT COUNT(*)
            FROM ETextBook.content_user_activity
            WHERE blockID = %s AND textBookID = %s AND chapterID = %s AND sectionID = %s AND courseID = %s
        """
        
        try:
            cursor = self.db.execute_query(query, (blockID, textBookID, chapterID, sectionID, courseID))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            result = cursor.fetchone()
            return result[0] > 0
        except Exception as e:
            print(f"Failed to check if content block '{blockID}' exists in content_user_activity: {e}")
            return False
    
    def iscontentBlockActivity_in_content_user_activity(self, ebook):
        blockID = ebook['contentblockID']
        textBookID = ebook['textBookID']
        chapterID = ebook['chapterID']
        sectionID = ebook['sectionID']
        activityID = ebook['activityID']
        courseID = ebook['courseID']
        
        query = """
            SELECT COUNT(*)
            FROM ETextBook.content_user_activity
            WHERE blockID = %s AND textBookID = %s AND chapterID = %s AND sectionID = %s AND courseID = %s AND activityID = %s
        """
        
        try:
            cursor = self.db.execute_query(query, (blockID, textBookID, chapterID, sectionID, courseID, activityID))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            result = cursor.fetchone()
            return result[0] > 0
        except Exception as e:
            print(f"Failed to check if content block '{blockID}' exists in content_user_activity: {e}")
            return False
        
    def getSectionID_hidden(self, ebook):
        chapterID = ebook['chapterID']
        textBookID = ebook['textBookID']
        
        query = """
            SELECT sectionID
            FROM ETextBook.Section
            WHERE chapterID = %s AND textBookID = %s
        """
        try:
            cursor = self.db.execute_query(query, (chapterID, textBookID,))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            result = cursor.fetchone()
            return result
        except Exception as e:
            print(f"Failed to get section for chapter '{chapterID}': {e}")
            return None
        
    def getBlockID_hidden(self, ebook):
        chapterID = ebook['chapterID']
        textBookID = ebook['textBookID']
        sectionID = ebook['sectionID']
    
        query = """
            SELECT blockID
            FROM ETextBook.ContentBlock
            WHERE sectionID = %s AND chapterID = %s AND textBookID = %s
        """
        try:
            cursor = self.db.execute_query(query, (sectionID, chapterID, textBookID))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            result = cursor.fetchone()
            return result
        except Exception as e:
            print(f"Failed to get block for chapter '{chapterID}': {e}")
            return None
      
    def checkHiddenStatusforchapter(self, ebook):
        blockID = ebook['contentblockID']
        textBookID = ebook['textBookID']
        chapterID = ebook['chapterID']
        sectionID = ebook['sectionID']
        userID = ebook['userID']
        courseID = ebook['courseID']
        
        query = """
            SELECT isHidden_chap
            FROM ETextBook.content_user_activity
            WHERE blockID = %s AND textBookID = %s AND chapterID = %s AND sectionID = %s AND courseID = %s
        """
        try:
            cursor = self.db.execute_query(query, (blockID, textBookID, chapterID, sectionID, courseID))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            result = cursor.fetchone()
            return result[0]
        except Exception as e:
            print(f"Failed to check hidden status for chapter '{chapterID}': {e}")
            return None
        
    def checkHiddenStatusforsection(self, ebook):
        blockID = ebook['contentblockID']
        textBookID = ebook['textBookID']
        chapterID = ebook['chapterID']
        sectionID = ebook['sectionID']
        userID = ebook['userID']
        courseID = ebook['courseID']
        
        query = """
            SELECT isHidden_sec
            FROM ETextBook.content_user_activity
            WHERE blockID = %s AND textBookID = %s AND chapterID = %s AND sectionID = %s AND courseID = %s
        """
        try:
            cursor = self.db.execute_query(query, (blockID, textBookID, chapterID, sectionID, courseID))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            result = cursor.fetchone()
            return result[0]
        except Exception as e:
            print(f"Failed to check hidden status for section '{sectionID}': {e}")
            return None
       
    def checkHiddenStatusforblock(self, ebook):
        blockID = ebook['contentblockID']
        textBookID = ebook['textBookID']
        chapterID = ebook['chapterID']
        sectionID = ebook['sectionID']
        userID = ebook['userID']
        courseID = ebook['courseID']
        
        query = """
            SELECT isHidden_block
            FROM ETextBook.content_user_activity
            WHERE blockID = %s AND textBookID = %s AND chapterID = %s AND sectionID = %s AND courseID = %s
        """
        try:
            cursor = self.db.execute_query(query, (blockID, textBookID, chapterID, sectionID, courseID))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            result = cursor.fetchone()
            return result[0]
        except Exception as e:
            print(f"Failed to check hidden status for block '{blockID}': {e}")
            return None   
      
    def checkHiddenStatusforactivity(self, ebook):
        activityID = ebook['activityID']
        blockID = ebook['contentblockID']
        textBookID = ebook['textBookID']
        chapterID = ebook['chapterID']
        sectionID = ebook['sectionID']
        userID = ebook['userID']
        courseID = ebook['courseID']
        
        query = """
            SELECT isHidden_act
            FROM ETextBook.content_user_activity
            WHERE blockID = %s AND textBookID = %s AND chapterID = %s AND sectionID = %s AND courseID = %s AND activityID = %s
        """
        try:
            cursor = self.db.execute_query(query, (blockID, textBookID, chapterID, sectionID, courseID, activityID))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            result = cursor.fetchone()
            return result[0]
        except Exception as e:
            print(f"Failed to check hidden status for activity '{activityID}': {e}")
            return None  
      
    def hideChapter(self, ebook):
        blockID = ebook['contentblockID']
        sectionID = ebook['sectionID']
        chapterID = ebook['chapterID']
        textBookID = ebook['textBookID']
        userID = ebook['userID']
        courseID = ebook['courseID']
        
        # calling this method since isChapterExists_in_content_user_activity is the same as this method. So deleted that method.
        if not self.iscontentBlockExists_in_content_user_activity(ebook):
            query = """
                INSERT INTO ETextBook.content_user_activity (userID, courseID, textBookID, chapterID, sectionID, blockID, isHidden_chap)
                VALUES (%s, %s, %s, %s, %s, %s, 'yes')
            """
            try:
                cursor = self.db.execute_query(query, (userID, courseID, textBookID, chapterID, sectionID, blockID, ))
                if cursor is None:
                    raise Exception("Query Execution Failed!!!!")
                print(f"Chapter '{chapterID}' hidden successfully!")
                self.db.connection.commit()
                return 1
            except Exception as e:
                print(f"Failed to hide chapter '{chapterID}': {e}")
                return 0
        else:
            hiddenStatus = self.checkHiddenStatusforchapter(ebook)
            if hiddenStatus == 'yes':
                print(f"Chapter '{chapterID}' is already hidden!")
                return 1
            else:
                query = """
                    UPDATE ETextBook.content_user_activity
                    SET isHidden_chap = 'yes', userID = %s
                    WHERE blockID = %s AND textBookID = %s AND chapterID = %s AND sectionID = %s AND courseID = %s
                """
                
                try:
                    cursor = self.db.execute_query(query, (userID, blockID, textBookID, chapterID, sectionID, courseID))
                    if cursor is None:
                        raise Exception("Query Execution Failed!!!!")
                    print(f"Chapter '{chapterID}' hidden successfully!")
                    self.db.connection.commit()
                    return 1
                except Exception as e:
                    print(f"Failed to hide chapter '{chapterID}': {e}")
                    return 0  
      
    def hideSection(self, ebook):
        blockID = ebook['contentblockID']
        textBookID = ebook['textBookID']
        chapterID = ebook['chapterID']
        sectionID = ebook['sectionID']
        userID = ebook['userID']
        courseID = ebook['courseID']
        
        if not self.iscontentBlockExists_in_content_user_activity(ebook):
            query = """
                INSERT INTO ETextBook.content_user_activity (userID, courseID, textBookID, chapterID, sectionID, blockID, isHidden_sec)
                VALUES (%s, %s, %s, %s, %s, %s, 'yes')
            """
            try:
                cursor = self.db.execute_query(query, (userID, courseID, textBookID, chapterID, sectionID, blockID, ))
                if cursor is None:
                    raise Exception("Query Execution Failed!!!!")
                print(f"Section '{sectionID}' hidden successfully!")
                self.db.connection.commit()
                return 1
            except Exception as e:
                print(f"Failed to hide section '{sectionID}': {e}")
                return 0
        else:
            if self.checkHiddenStatusforsection(ebook) == 'yes':
                print(f"Section '{sectionID}' is already hidden!")
                return 1
            else:
                query = """
                    UPDATE ETextBook.content_user_activity
                    SET isHidden_sec = 'yes', userID = %s
                    WHERE blockID = %s AND textBookID = %s AND chapterID = %s AND sectionID = %s AND courseID = %s
                """
                
                try:
                    cursor = self.db.execute_query(query, (userID, blockID, textBookID, chapterID, sectionID, courseID))
                    if cursor is None:
                        raise Exception("Query Execution Failed!!!!")
                    print(f"Section '{sectionID}' hidden successfully!")
                    self.db.connection.commit()
                    return 1
                except Exception as e:
                    print(f"Failed to hide section '{sectionID}': {e}")
                    return 0
                    
    def hideContentBlock(self, ebook):
        blockID = ebook['contentblockID']
        textBookID = ebook['textBookID']
        chapterID = ebook['chapterID']
        sectionID = ebook['sectionID']
        userID = ebook['userID']
        courseID = ebook['courseID']
        
        if not self.iscontentBlockExists_in_content_user_activity(ebook):
            query = """
                INSERT INTO ETextBook.content_user_activity (userID, courseID, textBookID, chapterID, sectionID, blockID, isHidden_block)
                VALUES (%s, %s, %s, %s, %s, %s, 'yes')
            """
            try:
                cursor = self.db.execute_query(query, (userID, courseID, textBookID, chapterID, sectionID, blockID,))
                if cursor is None:
                    raise Exception("Query Execution Failed!!!!")
                print(f"Content block '{blockID}' hidden successfully!")
                self.db.connection.commit()
                return 1
            except Exception as e:
                print(f"Failed to hide content block '{blockID}': {e}")
                return 0
        else:
            if self.checkHiddenStatusforblock(ebook) == 'yes':
                print(f"Content block '{blockID}' is already hidden!")
                return 1
            else:    
                query = """
                    UPDATE ETextBook.content_user_activity
                    SET isHidden_block = 'yes', userID = %s
                    WHERE blockID = %s AND textBookID = %s AND chapterID = %s AND sectionID = %s AND courseID = %s
                """
                
                try:
                    cursor = self.db.execute_query(query, (userID, blockID, textBookID, chapterID, sectionID, courseID))
                    if cursor is None:
                        raise Exception("Query Execution Failed!!!!")
                    print(f"Content block '{blockID}' hidden successfully!")
                    self.db.connection.commit()
                    return 1
                except Exception as e:
                    print(f"Failed to hide content block '{blockID}': {e}")
                    return 0
                
    def hideActivity(self, ebook):
        blockID = ebook['contentblockID']
        textBookID = ebook['textBookID']
        chapterID = ebook['chapterID']
        sectionID = ebook['sectionID']
        userID = ebook['userID']
        courseID = ebook['courseID']
        activityID = ebook['activityID']
        
        if not self.iscontentBlockActivity_in_content_user_activity(ebook):
            query = """
                INSERT INTO ETextBook.content_user_activity (userID, courseID, textBookID, chapterID, sectionID, blockID, activityID, isHidden_act)
                VALUES (%s, %s, %s, %s, %s, %s, %s, 'yes')
            """
            try:
                cursor = self.db.execute_query(query, (userID, courseID, textBookID, chapterID, sectionID, blockID, activityID, ))
                if cursor is None:
                    raise Exception("Query Execution Failed!!!!")
                print(f"Activity '{activityID}' hidden successfully!")
                self.db.connection.commit()
                return 1
            except Exception as e:
                print(f"Failed to hide activity '{activityID}': {e}")
                return 0
        else:
            if self.checkHiddenStatusforactivity(ebook) == 'yes':
                print(f"Activity '{activityID}' is already hidden!")
                return 1
            else:    
                query = """
                    UPDATE ETextBook.content_user_activity
                    SET isHidden_activity = 'yes', userID = %s
                    WHERE blockID = %s AND textBookID = %s AND chapterID = %s AND sectionID = %s AND courseID = %s AND activityID = %s
                """
                
                try:
                    cursor = self.db.execute_query(query, (userID, blockID, textBookID, chapterID, sectionID, courseID, activityID,))
                    if cursor is None:
                        raise Exception("Query Execution Failed!!!!")
                    print(f"Activity '{activityID}' hidden successfully!")
                    self.db.connection.commit()
                    return 1
                except Exception as e:
                    print(f"Failed to hide activity '{activityID}': {e}")
                    return 0


