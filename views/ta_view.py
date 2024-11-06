class TAView:
    @staticmethod
    def navbar_menu(user, title):
        print(f"\nTA: {user[2]} {user[3]} | {title}")

    @staticmethod
    def display_landing_page_menu():
        print(f"\n\n1. Go to Active course")
        print(f"2. View Courses")
        print(f"3. Change Password")
        print(f"4. Logout")

    @staticmethod
    def display_courses(courses):
        print("\nAssigned Courses:")
        for i, course in enumerate(courses, start=1):
            uToken, courseID, title, textBookID = course
            print(f"{i}. Title: {title} | TextBookID: {textBookID} | CourseID: {courseID} | uToken: {uToken}")
    @staticmethod
    def display_students(students):
        print("\nStudentIDs:")
        for i, student in enumerate(students, start=1):
            studentID, = student
            print(f"{i}. {studentID}")