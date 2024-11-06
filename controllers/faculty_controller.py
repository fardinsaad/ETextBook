import re
from models.faculty_model import FacultyModel
from views.faculty_view import FacultyView
from views.user_view import UserView

class FacultyController:
    def __init__(self):
        self.faculty_view = FacultyView()
        self.user_view = UserView()
        self.faculty_model = FacultyModel()
        self.user = None
        self.ebook = {}
        
        
    def go_active_course(self):
        self.faculty_view.navbar_menu(self.user, "Go to Active Course")
        courseID = self.user_view.get_text_input("A. Enter course ID: ")
        course = self.faculty_model.getcoursebyid(courseID)
        
    
    def landing_page(self):
        self.faculty_view.navbar_menu(self.user, "Landing Page")
        self.faculty_view.landing_page_menu()
        choice = self.user_view.get_text_input("Enter choice (1-5): ")
        if choice == '1':
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            print("You are logged out!")
        else:
            self.faculty_view.display_message("Invalid choice!")
            self.landing_page()
        

    def login(self):
        self.faculty_view.display_message("\n\nFaculty | Login")
        userID = self.user_view.get_text_input("A. Enter user ID: ")
        password = self.user_view.get_password_input("B. Enter password: ")
        self.user_view.get_user_signInMenu()
        choice = self.user_view.get_text_input("Enter Choice (1-2): ")
        if choice == '1':
            user = self.faculty_model.get_user(userID, password)
            self.faculty = user
            if user:
                self.landing_page()
            else:
                self.faculty_view.display_message("Login incorrect.")
                self.login()
        elif choice == '2':
            pass
        else:
            self.faculty_view.display_message("Invalid choice!")