from models.admin_model import AdminModel
from views.admin_view import AdminView
from views.user_view import UserView

class AdminController:
    def __init__(self):
        self.admin_model = AdminModel()
        self.admin_view = AdminView()
        self.user_view = UserView()
        self.admin = None

    def create_faculty_acount(self):
        self.admin_view.navbar_menu(self.admin, "Create a Faculty Account")
        self.admin_view.get_text_input("A. First Name: ")
        self.admin_view.get_text_input("B. Last Name: ")
        self.admin_view.get_text_input("C. E-mail: ")
        self.admin_view.get_text_input("D. Password: ")

        self.admin_view.display_message("1. Add User")
        self.admin_view.display_message("2. Go Back")
        choice = self.admin_view.get_text_input("Enter Choice (1-2): ")
        if choice == '1':
            
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