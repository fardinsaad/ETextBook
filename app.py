from controllers.user_controller import UserController
from controllers.admin_controller import AdminController
from controllers.faculty_controller import FacultyController
from controllers.student_controller import StudentController
from controllers.ta_controller import TAController
from models.book_model import BookModel
from models.course_model import CourseModel
from models.student_model import StudentModel
from models.ta_model import TAModel

class App:
    def __init__(self):
        self.user_controller = UserController()
        self.admin_controller = AdminController()
        self.faculty_controller = FacultyController()
        self.student_controller = StudentController()
        self.TA_controller = TAController()
        self.book_model = BookModel()
        self.course_model = CourseModel()
        self.student_model = StudentModel()
        self.ta_model = TAModel()

    def check(self):
        ebook = {
            'textBookID': 2,
            'title': 'Database Management System',
            'userID': 2,
            'chapterID': "chap05",
            'chapterTitle': 'asss',
            'sectionID': "Sec02",
            'sectionTitle': 'plssss',
            'contentblockID': "Block01",
            'blockType': 'activity',
            'content': 'ACT01',
            'activityID': 'ACT01',
            'questionID': 'Q1',
            'question': 'What is 2+10?',
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
        # self.ta_model.addContentTransaction(ebook)
        # self.book_model.addActivtyTransaction(ebook)
        # self.book_model.modifyContentTransaction(ebook, "activity")
        course = {
            'courseID': 2,
            'title': 'Mathematical Analysis',
            'textBookID': 1,
            'userID': 1,
            'startDate': '2021-09-01',
            'endDate': '2021-12-01',
            'courseType': 'Active'
        }
        # self.course_model.add_course(course)
        # ebooks = self.student_model.get_enrolled_courses_by_userID(userID=4)
        # print("Enrolled Courses:", ebooks)
        # print("E-TextBooks:", ebooks[0])
        # for i, ebook in enumerate(ebooks, start=1):
        #     textBookID, courseID, ebookTitle = ebook
        #     print(f"E-TextBook-{i}: {ebookTitle}")
        #     chapters = self.student_model.get_chapters_by_id(courseID, textBookID)
        #     print("Chapters:", chapters)

    def run(self):
        #  self.check()
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

