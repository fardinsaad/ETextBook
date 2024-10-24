from controllers.user_controller import UserController
from controllers.admin_controller import AdminController

class App:
    def __init__(self):
        self.user_controller = UserController()
        self.admin_controller = AdminController()

    def run(self):
        while True:
            self.user_controller.user_view.display_menu()
            choice = self.user_controller.user_view.get_user_input("Enter choice (1-5): ")

            if choice == '1':
                self.admin_controller.login()
            elif choice == '2':
                self.faculty_controller.login()
            elif choice == '3':
                self.TA_controller.login()
            elif choice == '4':
                self.student_controller.login()
            elif choice == '5':
                self.user_controller.user_view.display_message("Thank you! Hope to see you again!")
                break
            else:
                self.user_controller.user_view.display_message("Invalid choice! Please try again.")

if __name__ == "__main__":
    app = App()
    app.run()
