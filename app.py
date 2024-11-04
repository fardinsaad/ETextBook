from controllers.user_controller import UserController
from controllers.admin_controller import AdminController
from controllers.faculty_controller import FacultyController
from models.book_model import BookModel

class App:
    def __init__(self):
        self.user_controller = UserController()
        self.admin_controller = AdminController()
        self.book_model = BookModel()

    def check(self):
        ebook = {
            'textBookID': 2,
            'title': 'Database Management System',
            'userID': 1,
            'chapterID': "chap01",
            'chapterTitle': 'Introduction',
            'sectionID': "Sec01",
            'sectionTitle': 'RDBMS',
            'contentblockID': "Block01",
            'blockType': 'activity',
            'content': 'ACT01',
            'activityID': 'ACT01',
            'questionID': 'Q1',
            'question': 'What is 2+2?',
            'OP1': '4',
            'OP1_EXP': 'EXP-1',
            'OP1_Label': 'Correct',
            'OP2': '2',
            'OP2_EXP': 'EXP-2',
            'OP2_Label': 'Incorrect',
            'OP3': '3',
            'OP3_EXP': 'EXP-3',
            'OP3_Label': 'Incorrect',
            'OP4': '4',
            'OP4_EXP': 'EXP-4',
            'OP4_Label': 'Incorrect'
        }
        self.book_model.addActivtyTransaction(ebook)

    def run(self):
        # self.check()
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

