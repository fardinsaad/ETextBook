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
        self.user = None
        self.userID = None
        self.ebooks = {}
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
            self.enroll()

    def view_participation_activity_points(self):
        self.user_view.display_message("\nStudent | View Participation Activity Points")
        total_score = self.student_model.get_participation_activity_point_by_userID(self.user[0])
        print("Your Current Participation Activity Point:", total_score)
        self.user_view.display_message("1. Go back")
        choice = self.user_view.get_text_input("Enter Choice (1): ")
        if choice == '1':
            self.landing_page()
        else:
            self.user_view.display_message("Invalid choice!")
    def view_activity_rep(self, ebookIdx, textBookID, courseID, chapterID, sectionID, blockID, blockIdx, activity, activity_data, qo_no):
        try:
            question = activity_data[qo_no]
            print(f"Question {qo_no+1}: {activity_data[qo_no][1]}")
            print(f"Options:")
            print(f"\t {1}. {question[2]}")
            print(f"\t {2}. {question[5]}")
            print(f"\t {3}. {question[8]}")
            print(f"\t {4}. {question[11]}")
            choice = self.user_view.get_text_input("Enter Choice (1-4): ")
            verdicts = ["", question[4], question[7], question[10], question[13]]
            points = 1
            if verdicts[int(choice)] == 'Correct':
                print("\033[92mCorrect!\033[0m")
                points = 3
            else:
                print('\033[31mIncorrect!\033[0m')
            print(f"Explanations for every choiche:")
            print(f"\t {1}. {question[4]}: {question[3]}")
            print(f"\t {2}. {question[7]}: {question[6]}")
            print(f"\t {3}. {question[10]}: {question[9]}")
            print(f"\t {4}. {question[13]}: {question[12]}")
            uToken = self.student_model.get_uToken_by_courseID(courseID)
            self.userID = self.user[0]
            result = self.student_model.get_student_activity_score(self.userID, textBookID, uToken, chapterID, sectionID, blockID, activity, question[0])
            if(result):
                self.student_model.update_student_activity(self.userID, textBookID, uToken, chapterID, sectionID, blockID, activity, question[0], points)
                print(f"\033[92mAlready attempted! Previous score: {result}, New score: {points}\033[0m")
            else:
                self.student_model.add_student_activity(self.userID, textBookID, uToken, chapterID, sectionID, blockID, activity, question[0], points)
                print(f"\033[92m New Score: {points}\033[0m") 
        except IndexError:
            print('\033[31mNo questions found!\033[0m')
            self.view_content_block(ebookIdx['textBookID'], ebookIdx['chapterID'], ebookIdx['sectionID'], blockIdx+1)
        self.user_view.display_message("1. Next/Submit")
        self.user_view.display_message("2. Go back")
        choice = self.user_view.get_text_input("Enter Choice (1-2): ")
        if choice == '1':
            self.view_activity_rep(ebookIdx, textBookID, courseID, chapterID, sectionID, blockID, blockIdx, activity, activity_data, qo_no+1)
        elif choice == '2':
            if(qo_no == 0):
                print("Going back to content block")
                print(textBookID, chapterID, sectionID, blockIdx)
                self.view_content_block(ebookIdx['textBookID'], ebookIdx['chapterID'], ebookIdx['sectionID'], blockIdx+1)
            else:
                self.view_activity_rep(ebookIdx, textBookID, courseID, chapterID, sectionID, blockID, blockIdx, activity, activity_data, qo_no-1)
        else:
            self.user_view.display_message("Invalid choice!")
            self.view_activity_rep(ebookIdx, textBookID, courseID, chapterID, sectionID, blockID, blockIdx, activity, activity_data, qo_no)
            
        

    def view_activity(self, textBookID, chapterID, sectionID, blockID, activity):
        ebookIdx = {
            'textBookID': textBookID,
            'chapterID': chapterID,
            'sectionID': sectionID,
            'blockID': blockID,
        }
        print(f"Activity {activity}")
        blockIdx = blockID
        courseID = self.ebooks[textBookID]['ebook'][1]
        blockID = self.ebooks[textBookID]['chapters'][chapterID]['sections'][sectionID]['contentblocks'][blockID][0]
        sectionID = self.ebooks[textBookID]['chapters'][chapterID]['sections'][sectionID]['section'][0]
        chapterID = self.ebooks[textBookID]['chapters'][chapterID]['chapter'][0]
        courseID = self.ebooks[textBookID]['ebook'][1]
        textBookID = self.ebooks[textBookID]['ebook'][0]
        activity_data = self.student_model.get_questions_by_blockID(blockID, sectionID, chapterID, courseID, textBookID, activity)
        self.view_activity_rep(ebookIdx, textBookID, courseID, chapterID, sectionID, blockID, blockIdx, activity, activity_data, 0)

    def view_content_block(self, textBookID, chapterID, sectionID, blockID):
        contentblock = None
        print("sd", textBookID, chapterID, sectionID, blockID, type(textBookID), type(chapterID), type(sectionID), type(blockID))
        try:
            contentblock = self.ebooks[textBookID]['chapters'][chapterID]['sections'][sectionID]['contentblocks'][blockID]
            print(f"Content Blocks for Section {sectionID+1}:")
            blockType, content = contentblock[1], contentblock[2]
            print(f"Block {blockID+1}: {blockType}")
            if(blockType == 'activity'):
                self.view_activity(textBookID, chapterID, sectionID, blockID, content)
            else:
                print(content)
        except IndexError:
            print('\033[31mNo content blocks found!\033[0m')
            self.landing_page()
        if not contentblock:
            print('\033[31mNo content blocks found!\033[0m')
            self.landing_page()
        self.user_view.display_message("1. Next/Submit")
        self.user_view.display_message("2. Go back")
        choice = self.user_view.get_text_input("Enter Choice (1-2): ")
        if choice == '1':
            self.view_content_block(textBookID, chapterID, sectionID,blockID=blockID+1)
        else:
            self.user_view.display_message("Invalid choice!")
            self.view_content_block(textBookID, chapterID, sectionID, blockID)

    def view_block(self, textBookID, chapterID, sectionID):
        self.user_view.display_message("\nStudent | View Block")
        textBookID = int(textBookID.split('.')[-1])-1
        chapterID = int(chapterID.split('.')[-1])-1
        sectionID = int(sectionID.split('.')[-1])-1
        self.view_content_block(textBookID, chapterID, sectionID,0)

    def view_section(self):
        self.user_view.display_message("\nStudent | View Section")
        textBookID = self.user_view.get_text_input("Enter TextBook ID: ")
        chapterID = self.user_view.get_text_input("Enter Chapter ID: ")
        sectionID = self.user_view.get_text_input("Enter Section ID: ")
        
        self.user_view.display_message("1. View Block")
        self.user_view.display_message("2. Go back")
        choice = self.user_view.get_text_input("Enter Choice (1-2): ")
        if choice == '1':
            self.view_block(textBookID, chapterID, sectionID)
        elif choice == '2':
            self.landing_page()
        else:
            self.user_view.display_message("Invalid choice!")
            self.view_section()

    def display_enrolled_courses(self):
        self.ebooks = []
        userID = self.user[0]
        courses = self.student_model.get_enrolled_courses_by_userID(userID=userID)
        
        for i, ebook in enumerate(courses, start=1):
            textBookID, courseID, ebookTitle = ebook
            print(f"E-TextBook-{i}: {ebookTitle}")
            ebook_data = {
                'ebook': ebook,
                'chapters': []
            }
            chapters = self.student_model.get_chapters_by_id(courseID, textBookID)
            for j, chapter in enumerate(chapters, start=1):
                chapterID, chapterTitle = chapter
                print(f"\t Chapter {j}: {chapterTitle}")
                chapter_data = {
                    'chapter': chapter,
                    'sections': []
                }
                sections = self.student_model.get_sections_by_id(chapterID, courseID, textBookID)
                for k, section in enumerate(sections, start=1):
                    sectionID, sectionTitle = section
                    print(f"\t\t Section {j}.{k}: {sectionTitle}")
                    section_data = {
                        'section': section,
                        'contentblocks': []
                    }
                    contentblocks = self.student_model.get_contentblocks_by_id(sectionID, chapterID, courseID, textBookID)
                    for l, contentblock in enumerate(contentblocks, start=1):
                        blockID, blockType, content = contentblock
                        print(f"\t\t\t Block {j}.{k}.{l}: {blockType}")
                        section_data['contentblocks'].append(contentblock)

                    chapter_data['sections'].append(section_data)
                ebook_data['chapters'].append(chapter_data)
            self.ebooks.append(ebook_data)
    def display_notification(self):
        notifications = self.student_model.get_unread_notifications_by_userID(self.user[0])
        if(len(notifications) > 0):
            print("Notification: You have", len(notifications), "new notification(s).")
            for i, notification in enumerate(notifications, start=1):
                print(f"\t{i}. {notification[2]}")    
    def landing_page(self):
        print("Student | Landing Page---------------------------------")
        self.display_notification()
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
            self.user = user
            if user:
                self.userID = user[0]
                print(self.userID, "UserID----------------", type(self.userID))
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

