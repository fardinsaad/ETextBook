from models.user_model import UserModel
from views.user_view import UserView

class UserController:
    def __init__(self):
        self.user_model = UserModel()
        self.user_view = UserView()

    def register_user(self):
        username = self.user_view.get_user_input("Enter username: ")
        password = self.user_view.get_password_input("Enter password: ")
        if self.user_model.add_user(username, password):
            self.user_view.display_message("User registered successfully!")
        else:
            self.user_view.display_message("Registration failed!")

    def login_user(self):
        username = self.user_view.get_user_input("Enter username: ")
        password = self.user_view.get_password_input("Enter password: ")
        user = self.user_model.get_user(username, password)
        if user:
            self.user_view.display_message(f"Welcome, {username}!")
        else:
            self.user_view.display_message("Invalid credentials!")

    def view_all_users(self):
        users = self.user_model.get_all_users()
        self.user_view.display_users(users)
