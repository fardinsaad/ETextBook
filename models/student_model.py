from database.db_connection import Database
import datetime

class StudentModel:
    def __init__(self):
        self.db = Database()
    def get_user(self, userID, password):
        query = "SELECT * FROM User WHERE userID = %s AND password = %s"
        cursor = self.db.execute_query(query, (userID, password))
        user = cursor.fetchone()
        return user
    def get_student(self, userID, password):
        query = "SELECT * FROM User WHERE userID = %s AND password = %s AND role = 'Student'"
        cursor = self.db.execute_query(query, (userID, password))
        user = cursor.fetchone()
        return user
    def get_student_by_userID(self, userID):
        query = "SELECT * FROM Student WHERE userID = %s"
        cursor = self.db.execute_query(query, (userID,))
        return cursor.fetchone()
    def get_user_by_FLname_email(self, first_name, last_name, email):
        query = "SELECT * FROM User WHERE email = %s AND firstName = %s AND lastName = %s AND role = 'Student'"
        cursor = self.db.execute_query(query, (email, first_name, last_name))
        return cursor.fetchone()
    
    def get_participation_activity_point_by_userID(self, userID):
        query = "SELECT sum(score) FROM StudentActivity WHERE studentID = %s"
        cursor = self.db.execute_query(query, (userID,))
        result = cursor.fetchone()
        if result and result[0]:  # Check if result is not None and not 0
            return result[0]  # Return the total score
        return 0  # Return 0 if no score is found
    
    def get_enrolled_courses_by_userID(self, userID):
        query = """
                SELECT c.textBookID, c.courseID, c.title
                FROM Course c
                JOIN ActiveCourse ac ON c.courseID = ac.courseID
                JOIN ActiveEnrollment ae ON ac.uToken = ae.uToken
                WHERE ae.studentID = %s AND ae.c_status = 'Enrolled' ORDER BY c.textBookID
                """
        cursor = self.db.execute_query(query, (userID,))
        return cursor.fetchall()

    def get_chapters_by_id(self, courseID, textBookID): 
        query = """
                SELECT ch.chapterID, ch.title
                FROM Chapter ch
                LEFT JOIN content_user_activity cua ON ch.chapterID = cua.chapterID AND ch.textBookID = cua.textBookID
                WHERE ch.textBookID = %s AND (cua.courseID = %s  OR cua.courseID IS NULL) AND (cua.isHidden_chap = 'no' OR cua.isHidden_chap IS NULL) ORDER BY ch.chapterID
                """
        cursor = self.db.execute_query(query, (textBookID, courseID))
        return cursor.fetchall()
    
    def get_sections_by_id(self, chapterID, courseID, textBookID):
        query = """
                SELECT s.sectionID, s.title
                FROM Section s
                LEFT JOIN content_user_activity cua ON s.sectionID = cua.sectionID AND s.chapterID = cua.chapterID AND s.textBookID = cua.textBookID
                WHERE s.chapterID = %s AND s.textBookID = %s AND (cua.courseID = %s OR cua.courseID IS NULL) AND (cua.isHidden_sec = 'no' OR cua.isHidden_sec IS NULL) ORDER BY s.sectionID
                """
        cursor = self.db.execute_query(query, (chapterID, textBookID, courseID))
        return cursor.fetchall()
    
    def get_contentblocks_by_id(self, sectionID, chapterID, courseID, textBookID):
        query = """
                SELECT cb.blockID, cb.blockType, cb.content
                FROM ContentBlock cb
                LEFT JOIN content_user_activity cua ON cb.blockID = cua.blockID AND cb.sectionID = cua.sectionID AND cb.chapterID = cua.chapterID AND cb.textBookID = cua.textBookID
                WHERE cb.sectionID = %s AND cb.chapterID = %s AND cb.textBookID = %s AND (cua.courseID = %s OR cua.courseID IS NULL) AND (cua.isHidden_block = 'no' OR cua.isHidden_block IS NULL) ORDER BY cb.blockID
                """
        cursor = self.db.execute_query(query, (sectionID, chapterID, textBookID, courseID))
        return cursor.fetchall()
    def get_questions_by_blockID(self, blockID, sectionID, chapterID, courseID, textBookID, activityID):
        query = """
                SELECT q.questionID, q.question, q.OP1, q.OP1_EXP, q.OP1_Label, q.OP2, q.OP2_EXP, q.OP2_Label, q.OP3, q.OP3_EXP, q.OP3_Label, q.OP4, q.OP4_EXP, q.OP4_Label
                FROM Question q
                LEFT JOIN content_user_activity cua ON q.questionID = cua.questionID AND q.blockID = cua.blockID AND q.sectionID = cua.sectionID AND q.chapterID = cua.chapterID AND q.textBookID = cua.textBookID
                WHERE q.blockID = %s AND q.sectionID = %s AND q.chapterID = %s AND q.textBookID = %s AND q.activityID = %s AND (cua.courseID = %s OR cua.courseID IS NULL) AND (cua.isHidden_ques = 'no' OR cua.isHidden_ques IS NULL) ORDER BY q.questionID
                """
        cursor = self.db.execute_query(query, (blockID, sectionID, chapterID, textBookID, activityID, courseID))
        return cursor.fetchall()
    def get_unread_notifications_by_userID(self, userID):
        query = "SELECT * FROM Notification WHERE userID = %s AND isRead = FALSE"

        cursor = self.db.execute_query(query, (userID,))
        return cursor.fetchall()
    
    def enroll_student(self, studentID, uToken, c_status):
        query = "INSERT INTO ActiveEnrollment (studentID, uToken, c_status) VALUES (%s, %s, %s)"
        try:
            cursor = self.db.execute_query(query, (studentID, uToken, c_status))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            self.db.connection.commit()
            return 1
        except Exception as e:
            print(f"Failed to enroll student '{studentID}': {e}")
            return 0
    def get_uToken_by_courseID(self, courseID):
        query = "SELECT uToken FROM ActiveCourse WHERE courseID = %s"
        cursor = self.db.execute_query(query, (courseID,))
        result = cursor.fetchone()
        return result[0] if result else None
    def get_student_activity_score(self, userID, textBookID, uToken, chapterID, sectionID, blockID, activityID, questionID):
        query = "SELECT score FROM StudentActivity WHERE studentID = %s AND textBookID = %s AND uToken = %s AND chapterID = %s AND sectionID = %s AND blockID = %s AND activityID = %s AND questionID = %s"
        cursor = self.db.execute_query(query, (userID, textBookID, uToken, chapterID, sectionID, blockID, activityID, questionID))
        result = cursor.fetchone()
        return result[0] if result else None
    def update_student_activity(self, userID, textBookID, uToken, chapterID, sectionID, blockID, activityID, questionID, score):
        current_timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        query = "UPDATE StudentActivity SET score = %s, time_stamp = %s WHERE studentID = %s AND textBookID = %s AND uToken = %s AND chapterID = %s AND sectionID = %s AND blockID = %s AND activityID = %s AND questionID = %s"
        try:
            cursor = self.db.execute_query(query, (score, current_timestamp, userID, textBookID, uToken, chapterID, sectionID, blockID, activityID, questionID))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            self.db.connection.commit()
            return 1
        except Exception as e:
            print(f"Failed to update student activity '{userID}': {e}")
            return 0
    def add_student_activity(self, userID, textBookID, uToken, chapterID, sectionID, blockID, activityID, questionID, score):
        current_timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        query = "INSERT INTO StudentActivity (studentID, textBookID, uToken, chapterID, sectionID, blockID, activityID, questionID, score, time_stamp) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            cursor = self.db.execute_query(query, (userID, textBookID, uToken, chapterID, sectionID, blockID, activityID, questionID, score, current_timestamp))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            self.db.connection.commit()
            return 1
        except Exception as e:
            print(f"Failed to add student activity '{userID}': {e}")
            return 0
         
