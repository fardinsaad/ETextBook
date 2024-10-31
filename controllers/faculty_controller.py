import re
from models.faculty_model import FacultyModel
from views.faculty_view import FacultyView
from views.user_view import UserView

class FacultyController:
    def __init__(self):
        self.admin_model = AdminModel()
        self.admin_view = AdminView()
        self.user_view = UserView()
        self.faculty = None
    
    def landing_page(self):
        pass
        # self.admin_view.navbar_menu(self.admin, "Landing Page")
        # self.admin_view.landing_page_menu()
        # choice = self.admin_view.get_text_input("Enter Choice (1-6): ")
        # if choice == '1': # Create a faculty account
        #     self.create_faculty_acount()
        # elif choice == '6':
        #     print("\nYou are logged out.")
        #     pass
        # else:
        #     self.admin_view.display_message("Invalid choice!")

    def login(self):
        self.admin_view.display_message("\n\nFaculty | Login")
        userID = self.admin_view.get_text_input("A. Enter user ID: ")
        password = self.admin_view.get_password_input("B. Enter password: ")
        self.admin_view.display_menu()
        choice = self.admin_view.get_text_input("Enter Choice (1-2): ")
        if choice == '1':
            user = self.faculty_model.get_user(userID, password)
            self.admin = user
            if user:
                self.landing_page()
            else:
                self.admin_view.display_message("Login incorrect.")
                self.login()
        elif choice == '2':
            pass
        else:
            self.admin_view.display_message("Invalid choice!")