from database.db_connection import Database

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
                SELECT cb.blockID, cb.blockType
                FROM ContentBlock cb
                LEFT JOIN content_user_activity cua ON cb.blockID = cua.blockID AND cb.sectionID = cua.sectionID AND cb.chapterID = cua.chapterID AND cb.textBookID = cua.textBookID
                WHERE cb.sectionID = %s AND cb.chapterID = %s AND cb.textBookID = %s AND (cua.courseID = %s OR cua.courseID IS NULL) AND (cua.isHidden_block = 'no' OR cua.isHidden_block IS NULL) ORDER BY cb.blockID
                """
        cursor = self.db.execute_query(query, (sectionID, chapterID, textBookID, courseID))
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
