from database.db_connection import Database

class TAModel:
    def __init__(self):
        self.db = Database()
    def get_ta_by_id_password(self, userID, password):
        query = "SELECT * FROM User WHERE userID = %s AND password = %s AND role = 'TA'"
        try:
            cursor = self.db.execute_query(query, (userID, password))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            return cursor.fetchone()
        except Exception as e:
            print(f"Failed to get TA '{userID}': {e}")
            return None
    def update_password(self, userID, password):
        query = "UPDATE User SET password = %s WHERE userID = %s"
        try:
            self.db.execute_query(query, (password, userID))
            self.db.connection.commit()
        except Exception as e:
            print(f"Failed to update password for TA '{userID}': {e}")

    def get_courses_by_userID(self, TAID):
        query = """
                SELECT ac.uToken, c.courseID, c.title, c.textBookID
                FROM ActiveCourseTA acta
                JOIN ActiveCourse ac ON acta.uToken = ac.uToken
                JOIN Course c ON ac.courseID = c.courseID
                WHERE acta.TAID = %s
                """
        try:
            cursor = self.db.execute_query(query, (TAID,))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            return cursor.fetchall()
        except Exception as e:
            print(f"Failed to get courses for TA '{TAID}': {e}")
            return None
    def get_students_by_courseID(self, courseID):
        query = """
                SELECT ae.studentID
                FROM ActiveEnrollment ae
                JOIN ActiveCourse ac ON ae.uToken = ac.uToken
                WHERE ac.courseID = %s AND ae.c_status = 'Enrolled'
                """
        try:
            cursor = self.db.execute_query(query, (courseID,))
            if cursor is None:
                raise Exception("Query Execution Failed!!!!")
            return cursor.fetchall()
        except Exception as e:
            print(f"Failed to get students for course '{courseID}': {e}")
            return None
