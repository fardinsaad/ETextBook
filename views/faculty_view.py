class FacultyView:
    @staticmethod
    def navbar_menu(user, title):
        print(f"\n\nFaculty: {user[2]} {user[3]} | {title}")
    @staticmethod
    def display_menu():
        print(f"\n\n1. Enroll in a course")
        print(f"2. Sign in")
        print(f"3. Go back")

    @staticmethod
    def landing_page_menu():
        print("\n1. Go to Active Course")
        print("2. Go to Evaluation Course")
        print("3. View Courses")
        print("4. Change Password")
        print("5. Logout")
        
    @staticmethod
    def display_message(message):
        print(message)
        
    @staticmethod
    def display_courses(courses):
        print("\nAssigned Courses:")
        for i, course in enumerate(courses, start=1):
            courseID, title, startDate, endDate, courseType = course
            print(f"{i}. Course ID: {courseID} | Title: {title} | Start Date: {startDate} | End Date: {endDate} | Course Type: {courseType}")
        
    @staticmethod
    def display_worklist(worklist):
        print("------------------------------------------------------")
        print("Student ID\tName\t\t\tStatus")
        print("------------------------------------------------------")
    
        # Iterate over the worklist and print each student's details
        for i,student in enumerate(worklist, start = 1):
            student_id, first_name, last_name, status = student
            print(f"{i}. {student_id}\t{first_name} {last_name}\t\t{status}")
            
    @staticmethod
    def display_students(list):
        print("------------------------------------------------------")
        print("Student ID\tName")
        print("------------------------------------------------------")
    
        # Iterate over the worklist and print each student's details
        for i,student in enumerate(list, start=1):
            student_id, first_name, last_name = student
            print(f"{i}. {student_id}\t{first_name} {last_name}")