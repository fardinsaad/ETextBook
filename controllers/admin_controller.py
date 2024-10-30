import re
from models.admin_model import AdminModel
from views.admin_view import AdminView
from views.user_view import UserView

class AdminController:
    def __init__(self):
        self.admin_model = AdminModel()
        self.admin_view = AdminView()
        self.user_view = UserView()
        self.admin = None
    
    def is_valid_email(email):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'  
        if re.match(email_regex, email):
            return True
        else:
            return False
    
    def isValid(self, firstName, lastName, email, password):
        return len(firstName)>1 and len(lastName) and self.is_valid_email(email) and len(password)>0
    def create_faculty_acount(self):
        self.admin_view.navbar_menu(self.admin, "Create a Faculty Account")
        firstName = self.admin_view.get_text_input("A. First Name: ")
        lastName = self.admin_view.get_text_input("B. Last Name: ")
        email = self.admin_view.get_text_input("C. E-mail: ")
        password = self.admin_view.get_password_input("D. Password: ")

        self.admin_view.display_message("1. Add User")
        self.admin_view.display_message("2. Go Back")
        choice = self.admin_view.get_text_input("Enter Choice (1-2): ")
        if choice == '1':
            if(self.isValid(firstName, lastName, email, password)):
                self.admin_model.addFaculty(firstName, lastName, email, password)
            else:
                self.admin_view.display_message("Invalid input!!!")
            self.landing_page()
        elif choice == '2':
            self.landing_page()
        else:
            self.admin_view.display_message("Invalid choice!")


    def landing_page(self):
        self.admin_view.navbar_menu(self.admin, "Landing Page")
        self.admin_view.landing_page_menu()
        choice = self.admin_view.get_text_input("Enter Choice (1-6): ")
        if choice == '1': # Create a faculty account
            self.create_faculty_acount()
        elif choice == '6':
            print("\nYou are logged out.")
            pass
        else:
            self.admin_view.display_message("Invalid choice!")

    def login(self):
        self.admin_view.display_message("\n\nAdmin | Login")
        userID = self.admin_view.get_text_input("A. Enter user ID: ")
        password = self.admin_view.get_password_input("B. Enter password: ")
        self.admin_view.display_menu()
        choice = self.admin_view.get_text_input("Enter Choice (1-2): ")
        if choice == '1':
            user = self.admin_model.get_user(userID, password)
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