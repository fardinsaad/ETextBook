import re
from models.ta_model import TAModel
from models.book_model import BookModel
from views.ta_view import TAView
from views.user_view import UserView

class TAController:
    def __init__(self):
        self.ta_model = TAModel()
        self.ta_view = TAView()
        self.user_view = UserView()
        self.book_model = BookModel()
        self.user = None
        self.ebook = {}

    def view_students(self, courseID):
        self.user_view.navbar_menu(self.user, "View Students")
        students = self.ta_model.get_students_by_courseID(courseID)
        if not students:
            self.user_view.display_message("No students enrolled in this course!")
        else:
            self.ta_view.display_students(students)
        self.user_view.display_message("\n1. Go back")
        choice = self.user_view.get_text_input("Enter choice (1): ")
        if choice == '1':
            self.active_course()
        else:
            self.user_view.display_message("Invalid choice!")
            self.view_students()

    def ischapterIDValid(self, chapterID):
        pattern = r'^chap\d+$'
        return bool(re.match(pattern, chapterID))
       
    def issectionIDValid(self, sectionID):
        pattern = r'^Sec\d+$'
        return bool(re.match(pattern, sectionID))
    
    def isValidBlockID(self, contentblockID):
        pattern = r'^Block\d+$'
        return bool(re.match(pattern, contentblockID))
    
    def isValidActivityID(self, activityID):
        pattern = r'^ACT\d+$'
        return bool(re.match(pattern, activityID))

    def isValidQuestionID(self, questionID):
        pattern = r'^Q\d+$'
        return bool(re.match(pattern, questionID))


    def create_text(self, blockType, action):
        self.user_view.navbar_menu(self.user, "Add Text")
        content = self.user_view.get_text_input("Enter Text: ")
        self.user_view.display_message("1. Add")
        self.user_view.display_message("2. Go Back")
        choice = self.user_view.get_text_input("Enter Choice (1-2): ")
        
        if choice == '1':
            # values: textBookID, title, chapterID, chapterTitle, sectionID, sectionTitle, contentblockID, type, text
            self.ebook['blockType'] = blockType
            self.ebook['content'] = content
            if action == "create":
                isSucceed = self.ta_model.addContentTransaction(self.ebook)
                if isSucceed == 0:
                    self.landing_page()
                else:
                    self.create_content_block()
            elif action == "modify":
                isSucceed = self.ta_model.modifyContentTransaction(self.ebook, "text")
                if isSucceed == 0:
                    self.landing_page()
                else:
                    self.modify_content_block()
        elif choice == '2':
            if action == "create":
                self.create_content_block()
            elif action == "modify":
                self.modify_content_block()
        else:
            self.user_view.display_message("Invalid choice!")
                
    def create_picture(self, type, action):
        self.user_view.navbar_menu(self.user, "Add Picture")
        content = self.user_view.get_text_input("Enter Picture: ")
        self.user_view.display_message("1. Add")
        self.user_view.display_message("2. Go Back")
        choice = self.user_view.get_text_input("Enter Choice (1-2): ")
        self.ebook['blockType'] = type
        self.ebook['content'] = content
        if choice == '1':
            # values: textBookID, title, chapterID, chapterTitle, sectionID, sectionTitle, contentblockID, type, text
            if action == "create":
                isSucceed = self.ta_model.addContentTransaction(self.ebook)
                if isSucceed == 0:
                    self.landing_page()
                else:
                    self.create_content_block()
            elif action == "modify":
                isSucceed = self.book_model.modifyContentTransaction(self.ebook, "picture")
                if isSucceed == 0:
                    self.landing_page()
                else:
                    self.modify_content_block()
        elif choice == '2':
            if action == "create":
                self.create_content_block()
            elif action == "modify":
                self.modify_content_block()
        else:
            self.user_view.display_message("Invalid choice!")   
                
    def create_question(self, action):
        self.user_view.navbar_menu(self.user, "Add Question")
        questionID = self.user_view.get_text_input("A. Enter Question ID: ")
        question = self.user_view.get_text_input("B. Enter Question Text: ")
        option1 = self.user_view.get_text_input("C. Enter Option 1: ")
        option1Explanation = self.user_view.get_text_input("D. Enter Option 1 Explanation: ")
        option1Label = self.user_view.get_text_input("E. Enter Option 1 Label(Correct/Incorrect): ")
        option2 = self.user_view.get_text_input("F. Enter Option 2: ")
        option2Explanation = self.user_view.get_text_input("G. Enter Option 2 Explanation: ")
        option2Label = self.user_view.get_text_input("H. Enter Option 2 Label(Correct/Incorrect): ")
        option3 = self.user_view.get_text_input("I. Enter Option 3: ")
        option3Explanation = self.user_view.get_text_input("J. Enter Option 3 Explanation: ")
        option3Label = self.user_view.get_text_input("K. Enter Option 3 Label(Correct/Incorrect): ")
        option4 = self.user_view.get_text_input("L. Enter Option 4: ")
        option4Explanation = self.user_view.get_text_input("M. Enter Option 4 Explanation: ")
        option4Label = self.user_view.get_text_input("N. Enter Option 4 Label(Correct/Incorrect): ")
        
        if(self.isValidQuestionID(questionID)):
            self.user_view.display_message("1. Save")
            self.user_view.display_message("2. Cancel")
            choice = self.user_view.get_text_input("Enter Choice (1-2): ")
            if choice == '1':
                self.ebook['questionID'] = questionID
                self.ebook['question'] = question
                self.ebook['OP1'] = option1
                self.ebook['OP1_EXP'] = option1Explanation
                self.ebook['OP1_Label'] = option1Label
                self.ebook['OP2'] = option2
                self.ebook['OP2_EXP'] = option2Explanation
                self.ebook['OP2_Label'] = option2Label
                self.ebook['OP3'] = option3
                self.ebook['OP3_EXP'] = option3Explanation
                self.ebook['OP3_Label'] = option3Label
                self.ebook['OP4'] = option4
                self.ebook['OP4_EXP'] = option4Explanation
                self.ebook['OP4_Label'] = option4Label
                if action == "create":
                    isSucceed = self.ta_model.addActivtyTransaction(self.ebook)
                elif action == "modify":
                    isSucceed = self.book_model.modifyContentTransaction(self.ebook, "activity")
                if isSucceed == 0:
                    self.landing_page()
                else:
                    print("\nQuestion was saved successfully!")
                    self.create_activity("activity", action)
            elif choice == '2':
                self.create_activity("activity", action)
            else:
                self.user_view.display_message("Invalid choice!")
        else:
            self.user_view.display_message("Invalid Question ID format")
            self.create_question(action)

    def create_activity(self, type, action):
        self.user_view.navbar_menu(self.user, "Add Activity")
        activityID = self.user_view.get_text_input("Enter Unique Activity ID: ")
        if (self.isValidActivityID(activityID)):
            self.user_view.display_message("1. Add Question")
            self.user_view.display_message("2. Go back")
            choice = self.user_view.get_text_input("Enter Choice (1-2): ")
            if choice == '1':
                self.ebook['blockType'] = type
                self.ebook['activityID'] = activityID
                self.ebook['content'] = activityID
                if action == "create":
                    self.create_question("create")
                elif action == "modify":
                    self.create_question("modify")
            elif choice == '2':
                if action == "create":
                    self.create_content_block()
                elif action == "modify":
                    self.modify_content_block()
            else:
                self.user_view.display_message("Invalid choice!")
        else:
            self.user_view.display_message("Invalid Activity ID format")
            self.create_activity(type, action)
              
    def create_content_block(self):
        self.user_view.navbar_menu(self.user, "Add New Content Block")
        contentblockID = self.user_view.get_text_input("Enter Content Block ID: ")
        if(self.isValidBlockID(contentblockID)):
            self.user_view.display_message("1. Add Text")
            self.user_view.display_message("2. Add Picture")
            self.user_view.display_message("3. Add Activity")
            self.user_view.display_message("4. Go Back")
            choice = self.user_view.get_text_input("Enter Choice (1-4): ")
            self.ebook['contentblockID'] = contentblockID
            if choice == '1':
                self.create_text("text", "create")
            elif choice == '2':
                self.create_picture("picture", "create")
            elif choice == '3':
                self.create_activity("activity", "create")
            elif choice == '4':
                self.create_section()
            else:
                self.user_view.display_message("Invalid choice!")
        else:
            self.user_view.display_message("Invalid Content Block ID format")
            self.create_content_block()
            
    def modify_content_block(self):
        self.user_view.navbar_menu(self.user, "Modify Content Block")
        contentblockID = self.user_view.get_text_input("Enter Content Block ID: ")
        if(self.isValidBlockID(contentblockID)):
            self.user_view.display_message("1. Add Text")
            self.user_view.display_message("2. Add Picture")
            self.user_view.display_message("3. Add New Activity")
            self.user_view.display_message("4. Go Back")
            self.user_view.display_message("5. Landing Page")
            choice = self.user_view.get_text_input("Enter Choice (1-5): ")
            self.ebook['contentblockID'] = contentblockID
            if choice == '1':
                self.create_text("text", "modify")
            elif choice == '2':
                self.create_picture("picture", "modify")
            elif choice == '3':
                self.create_activity("activity", "modify")
            elif choice == '4':
                self.modify_section()
            elif choice == '5':
                self.landing_page()
            else:
                self.user_view.display_message("Invalid choice!")
        else:
            self.user_view.display_message("Invalid Content Block ID format")
            self.modify_content_block()
            

    def create_section(self):
        self.user_view.navbar_menu(self.user, "Add New Section")
        sectionID = self.user_view.get_text_input("Enter Section Number: ")
        sectionTitle = self.user_view.get_text_input("Enter Section Title: ")
        if self.issectionIDValid(sectionID):
            self.user_view.display_message("1. Add New Content Block")
            self.user_view.display_message("2. Go Back")
            choice = self.user_view.get_text_input("Enter Choice (1-2): ")
            if choice == '1':
                self.ebook['sectionID'] = sectionID
                self.ebook['sectionTitle'] = sectionTitle
                self.create_content_block()
            elif choice == '2':
                self.create_chapter()
            else:
                self.user_view.display_message("Invalid choice!") 
        else:
            self.user_view.display_message("Invalid Section ID format")
            self.create_section()
         
    def create_chapter(self):
        self.user_view.navbar_menu(self.user, "Add New Chapter")
        chapterID = self.user_view.get_text_input("Enter Unique Chapter ID: ")
        chapterTitle = self.user_view.get_text_input("Enter Chapter Title: ")
        if self.ischapterIDValid(chapterID):
            self.user_view.display_message("\n1. Add New Section")
            self.user_view.display_message("2. Go Back")
            choice = self.user_view.get_text_input("Enter Choice (1-2): ")
            if choice == '1':
                self.ebook['chapterID'] = chapterID
                self.ebook['chapterTitle'] = chapterTitle  
                self.create_section()
            elif choice == '2':
                self.active_course()
            else:
                self.user_view.display_message("Invalid choice!")
                self.create_chapter()
        else:
            self.user_view.display_message("Invalid Chapter ID format")
            self.create_chapter()     
            
    def delete_content_block(self):
        self.user_view.navbar_menu(self.user, "Delete Content Block")
        contentblockID = self.user_view.get_text_input("Enter Content Block ID: ")
        self.user_view.display_message("1. Delete")
        self.user_view.display_message("2. Go Back")
        choice = self.user_view.get_text_input("Enter Choice (1-2): ")
        if choice == '1':
            if(self.isValidBlockID(contentblockID)):
                self.ebook['contentblockID'] = contentblockID
                isSucceed = self.ta_model.deleteContentBlock(self.ebook)
                if isSucceed == 1:
                    self.modify_section()
                else:
                    self.user_view.display_message("Invalid Conten Bolck ID!")
                    self.delete_content_block()
            else:
                self.user_view.display_message("Invalid Content Block ID format")
                self.delete_content_block()
        elif choice == '2':
            self.modify_section()
        else:
            self.user_view.display_message("Invalid choice!")
            self.delete_content_block()
            
    def hide_content_block(self):
        self.user_view.navbar_menu(self.user, "Hide Content Block")
        contentblockID = self.user_view.get_text_input("Enter Content Block ID: ")
        self.user_view.display_message("1. Hide")
        self.user_view.display_message("2. Go Back")
        choice = self.user_view.get_text_input("Enter Choice (1-2): ")
        if choice == '1':
            if(self.isValidBlockID(contentblockID)):
                self.ebook['contentblockID'] = contentblockID
                isSucceed = self.ta_model.hideContentBlock(self.ebook)
                if isSucceed == 1:
                    self.modify_section()
                else:
                    self.user_view.display_message("Content Block was not hidden!")
                    self.hide_content_block()
            else:
                self.user_view.display_message("Invalid Content Block ID format")
                self.hide_content_block()
        elif choice == '2':
            self.modify_section()
        else:
            self.user_view.display_message("Invalid choice!")
            self.hide_content_block()
                
    def modify_section(self):
        self.user_view.navbar_menu(self.user, "Modify Section")
        sectionID = self.user_view.get_text_input("Enter Section Number: ")
        if self.issectionIDValid(sectionID):
            print("\n")
            self.user_view.display_message("1. Add New Content Block")
            self.user_view.display_message("2. Modify Content Block")
            self.user_view.display_message("3. Delete Content Block")
            self.user_view.display_message("4. Hide Content Block")
            self.user_view.display_message("5. Go Back")
            choice = self.user_view.get_text_input("Enter Choice (1-5): ")
            self.ebook['sectionID'] = sectionID
            query = "SELECT title FROM Section WHERE sectionID = %s AND chapterID = %s AND textBookID = %s"
            params = (sectionID, self.ebook['chapterID'], self.ebook['textBookID'])
            sectionTitle = self.book_model.getdata(query, params)
            if sectionTitle and len(sectionTitle) > 0:
                self.ebook['sectionTitle'] = sectionTitle[0][0]
            else:
                self.user_view.display_message("Invalid Section ID!")
                self.modify_section()
                return
            if choice == '1':
                self.create_content_block()
            elif choice == '2':
                self.modify_content_block()
            elif choice == '3':
                self.delete_content_block()
            elif choice == '4':
                self.hide_content_block()
            elif choice == '5':
                self.modify_chapter()
            else:
                self.user_view.display_message("Invalid choice!")
        else:
            self.user_view.display_message("Invalid Section ID format")
            self.modify_section()
            
            
    def modify_chapter(self):   
        self.user_view.navbar_menu(self.user, "Modify Chapter")
        chapterID = self.user_view.get_text_input("Enter Unique Chapter ID: ")
        if self.ischapterIDValid(chapterID):
            self.user_view.display_message("1. Add New Section")
            self.user_view.display_message("2. Modify Section")
            self.user_view.display_message("3. Go Back")
            choice = self.user_view.get_text_input("Enter Choice (1-3): ")
            self.ebook['chapterID'] = chapterID
            query = "SELECT title FROM Chapter WHERE chapterID = %s AND textBookID = %s"
            params = (chapterID, self.ebook['textBookID'])
            chapterTitle = self.book_model.getdata(query, params)
            if chapterTitle and len(chapterTitle) > 0:
                self.ebook['chapterTitle'] = chapterTitle[0][0]
            else:
                self.user_view.display_message("Invalid Chapter ID!")
                self.modify_chapter()
                return
            if choice == '1':
                self.create_section()
            elif choice == '2':
                self.modify_section()
            elif choice == '3':
                self.active_course()
            else:
                self.user_view.display_message("Invalid choice!")
        else:
            self.user_view.display_message("Invalid Chapter ID format")
            self.modify_chapter()

    def active_course(self):
        self.user_view.navbar_menu(self.user, "Go to Active Course")
        courseID = self.user_view.get_text_input("Enter course ID: ")
        self.ebook['courseID'] = courseID
        validTA = self.ta_model.is_ta_in_course(self.user[0], courseID)
        if not validTA:
            self.user_view.display_message("You are not a TA in this course!")
            self.active_course()
            return
            
        textBookID = self.book_model.get_textbookID_by_courseID(courseID)
        if textBookID:
            self.ebook['textBookID'] = textBookID[0]
        else:
            self.user_view.display_message("Course ID does not exist!")
            self.active_course()
            return
        
        self.user_view.display_message("\n1. View Students")
        self.user_view.display_message("2. Add New Chapter")
        self.user_view.display_message("3. Modify Chapters")
        self.user_view.display_message("4. Go Back")
        choice = self.user_view.get_text_input("Enter choice (1-4): ")
        if choice == '1':
            self.view_students(courseID)
        elif choice == '2':
            self.create_chapter()
        elif choice == '3':
            self.modify_chapter()
        elif choice == '4':
            self.landing_page()
        else:
            self.user_view.display_message("Invalid choice!")
            self.active_course()
        

    def view_courses(self):
        self.user_view.navbar_menu(self.user, "View Courses")
        courses = self.ta_model.get_courses_by_userID(self.user[0])
        self.ta_view.display_courses(courses)
        self.user_view.display_message("\n1. Go back")
        choice = self.user_view.get_text_input("Enter choice (1): ")
        if choice == '1':
            self.landing_page()
        else:
            self.user_view.display_message("Invalid choice!")
            self.view_courses()

    def change_password(self):
        self.user_view.navbar_menu(self.user, "Change Password")
        old_password = self.user_view.get_password_input("A. Enter current password: ")
        new_password = self.user_view.get_password_input("B. Enter new password: ")
        confirm_password = self.user_view.get_password_input("C. Confirm new password: ")

        self.user_view.display_message("1. Update")
        self.user_view.display_message("2. Go back")
        
        choice = self.user_view.get_text_input("Enter Choice (1-2): ")
        if choice == '1':
            if new_password != confirm_password:
                self.user_view.display_message("new and confirm Passwords  do not match!")
                self.change_password()
            else:
                self.ta_model.update_password(self.user[0], new_password)
                self.user_view.display_message("Password updated successfully!")
                self.landing_page()
        if choice == '2':
            self.landing_page()

    def landing_page(self):
        self.user_view.navbar_menu(self.user, "Landing Page")
        self.ta_view.display_landing_page_menu()
        choice = self.user_view.get_text_input("Enter choice (1-4): ")
        if choice == '1':
            self.active_course()
        elif choice == '2':
            self.view_courses()
        elif choice == '3':
            self.change_password()
        elif choice == '4':
            pass
        else:
            self.user_view.display_message("Invalid choice!")
            self.landing_page()
    
    def login(self):
        self.user_view.display_message("\nTA | Login")
        userID = self.user_view.get_text_input("A. Enter user ID: ")
        password = self.user_view.get_password_input("B. Enter password: ")
        self.user_view.get_user_signInMenu()
        choice = self.user_view.get_text_input("Enter Choice (1-2): ")
        if choice == '1':
            user = self.ta_model.get_ta_by_id_password(userID, password)
            if user:
                self.user = user
                self.ebook['userID'] = self.user[0]
                self.landing_page()
            else:
                self.user_view.display_message("Login incorrect.")
                self.login()
        elif choice == '2':
            pass
        else:
            self.user_view.display_message("Invalid choice!")
    
    