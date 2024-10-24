from models.admin_model import AdminModel
from views.admin_view import AdminView
from views.user_view import UserView

class AdminController:
    def __init__(self):
        self.admin_model = AdminModel()
        self.admin_view = AdminView()
        self.user_view = UserView()

    def login(self):
        self.admin_view.display_message("\n\nAdmin | Login")
        userID = self.admin_view.get_text_input("A. Enter user ID: ")
        password = self.admin_view.get_password_input("B. Enter password: ")
        self.admin_view.display_menu()
        choice = self.admin_view.get_text_input("Enter Choice (1-2)")
        if choice == '1':
            user = True#self.admin_model.get_user(userID, password)
            if user:
                self.admin_view.display_message(f"Welcome, {userID}!")
                #need to route admin landing page
                exit()
            else:
                self.admin_view.display_message("Login incorrect.")
                self.login()
        elif choice == '2':
            pass
        else:
            self.admin_view.display_message("Invalid choice!")

        

    # def view_all_users(self):
    #     users = self.user_model.get_all_users()
    #     self.user_view.display_users(users)
