import re
from models.admin_model import AdminModel
from views.admin_view import AdminView
from models.user_model import UserModel
from views.user_view import UserView
from models.book_model import BookModel
from models.course_model import CourseModel
from models.student_model import StudentModel
from views.student_view import StudentView

class StudentController:
    def __init__(self):
        self.admin_model = AdminModel()
        self.admin_view = AdminView()
        self.user_model = UserModel()
        self.user_view = UserView()
        self.book_model = BookModel()
        self.course_model = CourseModel()
        self.student_model = StudentModel()
        self.student_view = StudentView()
        self.student = None
        self.ebook = {}
    def enroll(self):
        self.user_view.display_message("\nStudent | Enroll in a course")
        first_name = self.user_view.get_text_input("A. Enter first name: ")
        last_name = self.user_view.get_text_input("B. Enter last name: ")
        email = self.user_view.get_text_input("C. Enter email: ")
        course_token = self.user_view.get_text_input("D. Enter course token: ")
        self.user_view.display_message("1. Enroll")
        self.user_view.display_message("2. Go back")
        choice = self.user_view.get_text_input("Enter Choice (1-2): ")
        if choice == '1':
            user = self.student_model.get_user_by_FLname_email(first_name, last_name, email)
            if user:
                course = self.course_model.get_active_course_by_uToken(course_token)
                if course:
                    if self.course_model.is_valid_studentID_uToken_for_ActiveEnrollment(user[0], course[0]):
                        self.user_view.display_message("You are already enrolled in this course!")
                        return
                    self.student_model.enroll_student(user[0], course[0], "Pending")
                    self.user_view.display_message("Enrolled successfully!")
                else:
                    self.user_view.display_message("Course not found!")
            else:
                self.user_view.display_message("User not found!")
        elif choice == '2':
            self.landing_page()
        else:
            self.user_view.display_message("Invalid choice!")

    def view_section(self):
        pass
    def view_participation_activity_points(self):
        self.user_view.display_message("\nStudent | View Participation Activity Points")
        total_score = self.student_model.get_participation_activity_point_by_userID(self.student[0])
        print("Your Current Participation Activity Point:", total_score)
        self.user_view.display_message("1. Go back")
        choice = self.user_view.get_text_input("Enter Choice (1): ")
        if choice == '1':
            self.landing_page()
        else:
            self.user_view.display_message("Invalid choice!")
    def display_enrolled_courses(self):
        userID = self.student[0]
        ebooks = self.student_model.get_enrolled_courses_by_userID(userID=userID)

        for i, ebook in enumerate(ebooks, start=1):
            textBookID, courseID, ebookTitle = ebook
            print(f"E-TextBook-{i}: {ebookTitle}")

            chapters = self.student_model.get_chapters_by_id(courseID, textBookID)
            for j, chapter in enumerate(chapters, start=1):
                chapterID, chapterTitle = chapter
                print(f"\t Chapter {j}: {chapterTitle}")
                sections = self.student_model.get_sections_by_id(chapterID, courseID, textBookID)
                for k, section in enumerate(sections, start=1):
                    sectionID, sectionTitle = section
                    print(f"\t\t Section {j}.{k}: {sectionTitle}")
                    contentblocks = self.student_model.get_contentblocks_by_id(sectionID, chapterID, courseID, textBookID)
                    for l, contentblock in enumerate(contentblocks, start=1):
                        blockType = contentblock[1]
                        print(f"\t\t\t Block {j}.{k}.{l}: {blockType}")
        
    def landing_page(self):
        print("Student | Landing Page")
        self.display_enrolled_courses()
        self.student_view.display_landing_page_menu()
        choice = self.user_view.get_text_input("Enter Choice (1-3): ")
        if choice == '1':
            self.view_section()
        elif choice == '2':
            self.view_participation_activity_points()
        elif choice == '3':
            self.login()
        else:
            self.user_view.display_message("Invalid choice!")
    def signIn(self):
        self.user_view.display_message("\nStudent | Sign In")
        userID = self.user_view.get_text_input("A. Enter user ID: ")
        password = self.user_view.get_password_input("B. Enter password: ")
        self.user_view.get_user_signInMenu()
        choice = self.user_view.get_text_input("Enter Choice (1-2): ")
        if choice == '1':
            user = self.student_model.get_student(userID, password)
            self.student = user
            if user:
                self.landing_page()
            else:
                self.user_view.display_message("Login incorrect.")
                self.signIn()
        elif choice == '2':
            pass
        else:
            self.admin_view.display_message("Invalid choice!")

    def login(self):
        self.user_view.display_message("\n Student | Login")
        self.student_view.display_menu()
        choice = self.user_view.get_text_input("Enter Choice (1-2): ")
        if choice == '1':
            self.enroll()
        elif choice == '2':
            self.signIn()
        elif choice == '3':
            pass
        else:
            self.user_view.display_message("Invalid choice!")

