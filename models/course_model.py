from database.db_connection import Database

class CourseModel:
    def __init__(self):
        self.db = Database()

    def add_course(self, course):
        courseID, title, textBookID, userID, startDate, endDate, courseType = course['courseID'], course['title'], course['textBookID'], course['userID'], course['startDate'], course['endDate'], course['courseType']
        query = "INSERT INTO Course (courseID, title, textBookID, userID, startDate, endDate, courseType) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        try:
            cursor = self.db.execute_query(query, (courseID, title, textBookID, userID, startDate, endDate, courseType))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            self.db.connection.commit()
            print(f"Course '{courseID}' created successfully!")
            return 1
        except Exception as e:
            print(f"Failed to create Course '{courseID}': {e}")
            return 0
    def add_active_course(self, course):
        uToken, courseID, coursecapacity = course['uToken'], course['courseID'], course['coursecapacity']
        query = "INSERT INTO ActiveCourse (uToken, courseID, coursecapacity) VALUES (%s, %s, %s)"
        try:
            cursor = self.db.execute_query(query, (uToken, courseID, coursecapacity))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            self.db.connection.commit()
            print(f"Active Course '{courseID}' created successfully!")
            return 1
        except Exception as e:
            print(f"Failed to create Active Course '{courseID}': {e}")
            return 0
    def get_course_by_id(self, courseID):
        query = "SELECT * FROM Course WHERE courseID = %s"
        try:
            cursor = self.db.execute_query(query, (courseID,))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            return cursor.fetchone()
        except Exception as e:
            print(f"Failed to get Course '{courseID}': {e}")
            return None
    def get_active_course_by_uToken(self, uToken):
        query = "SELECT * FROM ActiveCourse WHERE uToken = %s"
        try:
            cursor = self.db.execute_query(query, (uToken,))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            return cursor.fetchone()
        except Exception as e:
            print(f"Failed to get Active Course of uToken '{uToken}': {e}")
            return None
    def is_valid_studentID_uToken_for_ActiveEnrollment(self, studentID, uToken):
        query = "SELECT * FROM ActiveEnrollment WHERE uToken = %s AND studentID = %s"
        try:
            cursor = self.db.execute_query(query, (uToken, studentID))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            result = cursor.fetchone()
            return result is not None  # Return True if a record is found, otherwise False
        except Exception as e:
            print(f"Failed to get Active Course of uToken '{uToken}': {e}")
            return False
   
        
