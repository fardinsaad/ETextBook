import re
from models.faculty_model import FacultyModel
from models.book_model import BookModel
from views.faculty_view import FacultyView
from views.user_view import UserView
from datetime import datetime

class FacultyController:
    def __init__(self):
        self.faculty_view = FacultyView()
        self.user_view = UserView()
        self.faculty_model = FacultyModel()
        self.book_model = BookModel()
        self.user = None
        self.ebook = {}
        
    def isValid(self, firstName, lastName, password):
        # Check each field's length and validate the email format
        return (
            len(firstName.strip()) > 1 and
            len(lastName.strip()) > 1 and
            len(password) > 0
        )
        
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
                isSucceed = self.faculty_model.addContentTransaction(self.ebook)
                if isSucceed == 0:
                    self.landing_page()
                else:
                    self.create_content_block()
            elif action == "modify":
                isSucceed = self.faculty_model.modifyContentTransaction(self.ebook, "text")
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
                isSucceed = self.faculty_model.addContentTransaction(self.ebook)
                if isSucceed == 0:
                    self.landing_page()
                else:
                    self.create_content_block()
            elif action == "modify":
                isSucceed = self.faculty_model.modifyContentTransaction(self.ebook, "picture")
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
                    isSucceed = self.faculty_model.addActivtyTransaction(self.ebook)
                elif action == "modify":
                    isSucceed = self.faculty_model.modifyContentTransaction(self.ebook, "activity")
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

    def delete_activity(self):
        self.user_view.navbar_menu(self.user, "Delete Activity")
        activityID = self.user_view.get_text_input("Enter Activity ID: ")
        if(self.isValidActivityID(activityID)):
            self.ebook['activityID'] = activityID
            self.user_view.display_message("1. Save")
            self.user_view.display_message("2. Cancel")
            choice = self.user_view.get_text_input("Enter Choice (1-2): ")
            if choice == '1':
                isSucceed = self.faculty_model.deleteActivity(self.ebook)
                if isSucceed == 1:
                    self.modify_content_block()
                else:
                    self.modify_content_block()
            elif choice == '2':
                self.modify_content_block()
            else:
                self.user_view.display_message("Invalid choice!")
                self.delete_activity()
        else:
            self.user_view.display_message("Invalid Activity ID format")
            self.delete_activity()

    def hide_activity(self):
        self.user_view.navbar_menu(self.user, "Hide Activity")
        activityID = self.user_view.get_text_input("Enter Activity ID: ")
        if(self.isValidActivityID(activityID)):
            self.ebook['activityID'] = activityID
            self.user_view.display_message("1. Save")
            self.user_view.display_message("2. Cancel")
            choice = self.user_view.get_text_input("Enter Choice (1-2): ")
            if choice == '1':
                isSucceed = self.faculty_model.hideActivity(self.ebook)
                if isSucceed == 1:
                    self.modify_content_block()
                else:
                    self.modify_content_block()
            elif choice == '2':
                self.modify_content_block()
            else:
                self.user_view.display_message("Invalid choice!")
                self.hide_activity()
        else:
            self.user_view.display_message("Invalid Activity ID format")
            self.hide_activity()  
    
    def create_activity(self, type, action):
        self.user_view.navbar_menu(self.user, "Add Activity")
        activityID = self.user_view.get_text_input("Enter Unique Activity ID: ")
        if (self.isValidActivityID(activityID)):
            self.user_view.display_message("1. Add Question")
            self.user_view.display_message("2. Go back")
            choice = self.user_view.get_text_input("Enter Choice (1-2): ")
            if choice == '1':
                self.ebook['activityID'] = activityID
                self.ebook['blockType'] = type
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
            
    def delete_content_block(self):
        self.user_view.navbar_menu(self.user, "Delete Content Block")
        self.user_view.display_message("1. Save")
        self.user_view.display_message("2. Cancel")
        choice = self.user_view.get_text_input("Enter Choice (1-2): ")
        if choice == '1':
            isSucceed = self.faculty_model.deleteContentBlock(self.ebook)
            if isSucceed == 1:
                self.modify_section()
            else:
                self.user_view.display_message("Content Block was not deleted!")
                self.modify_section()
        elif choice == '2':
            self.modify_section()
        else:
            self.user_view.display_message("Invalid choice!")
            self.delete_content_block()
                  
    def hide_content_block(self):
        self.user_view.navbar_menu(self.user, "Hide Content Block")
        self.user_view.display_message("1. Save")
        self.user_view.display_message("2. Cancel")
        choice = self.user_view.get_text_input("Enter Choice (1-2): ")
        if choice == '1':
            isSucceed = self.faculty_model.hideContentBlock(self.ebook)
            if isSucceed == 1:
                self.modify_section()
            else:
                self.user_view.display_message("Content Block was not hidden!")
                self.modify_section()
           
        elif choice == '2':
            self.modify_section()
        else:
            self.user_view.display_message("Invalid choice!")
            self.hide_content_block()
     
    def modify_content_block(self):
        self.user_view.navbar_menu(self.user, "Modify Content Block")
        contentblockID = self.user_view.get_text_input("Enter Content Block ID: ")
        if(self.isValidBlockID(contentblockID)):
            self.user_view.display_message("1. Hide Content Block")
            self.user_view.display_message("2. Delete Content Block")
            self.user_view.display_message("3. Add Text")
            self.user_view.display_message("4. Add Picture")
            self.user_view.display_message("5. Hide Activity")
            self.user_view.display_message("6. Delete Activity")
            self.user_view.display_message("7. Add Activity")
            self.user_view.display_message("8. Go Back")
            choice = self.user_view.get_text_input("Enter Choice (1-8): ")
            self.ebook['contentblockID'] = contentblockID
            if choice == '1':
                self.hide_content_block()
            elif choice == '2':
                self.delete_content_block()
            elif choice == '3':
                self.create_text("text", "modify")
            elif choice == '4':
                self.create_picture("picture", "modify")
            elif choice == '5':
                self.hide_activity()
            elif choice == '6':
                self.delete_activity()
            elif choice == '7':
                self.create_activity("activity", "modify")
            elif choice == '8':
                self.modify_section()
            else:
                self.user_view.display_message("Invalid choice!")
        else:
            self.user_view.display_message("Invalid Content Block ID format")
            self.modify_content_block() 
              
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
                   
    def delete_section(self):
        self.user_view.navbar_menu(self.user, "Delete Section")
        self.user_view.display_message("1. Delete")
        self.user_view.display_message("2. Go Back")
        choice = self.user_view.get_text_input("Enter Choice (1-2): ")
        if choice == '1':
            isSucceed = self.faculty_model.deleteSection(self.ebook)
            if isSucceed == 1:
                self.modify_section()
            else:
                self.modify_section()
        elif choice == '2':
            self.modify_section()
        else:
            self.user_view.display_message("Invalid choice!")
            self.delete_section()
        
    def hide_section(self):
        self.user_view.navbar_menu(self.user, "Hide Section")
        blockID = self.faculty_model.getBlockID_hidden(self.ebook)
        if blockID:
            self.ebook['contentblockID'] = blockID[0]
        else:
            self.user_view.display_message("Section was not hidden!")
            self.modify_section()
            return
        self.user_view.display_message("1. Save")
        self.user_view.display_message("2. Cancel")
        choice = self.user_view.get_text_input("Enter choice(1-2): ")
        if choice == '1':
            isSucceed = self.faculty_model.hideSection(self.ebook)
            if isSucceed == 1:
                self.modify_section()
            else:
                self.user_view.display_message("Section was not hidden!")
                self.modify_section()
        elif choice == '2':
            self.modify_section()
        else:
            self.user_view.display_message("Invalid choice!")
            self.hide_section()    
          
    def modify_section(self):
        self.user_view.navbar_menu(self.user, "Modify Section")
        sectionID = self.user_view.get_text_input("Enter Section Number: ")
        if self.issectionIDValid(sectionID):
            print("\n")
            self.user_view.display_message("1. Hide Section")
            self.user_view.display_message("2. Delete Section")
            self.user_view.display_message("3. Add New Content Block")
            self.user_view.display_message("4. Modify Content Block")
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
                self.hide_section()
            elif choice == '2':
                self.delete_section()
            elif choice == '3':
                self.create_content_block()
            elif choice == '4':
                self.modify_content_block()
            elif choice == '5':
                self.modify_chapter()
            else:
                self.user_view.display_message("Invalid choice!")
        else:
            self.user_view.display_message("Invalid Section ID format")
            self.modify_section()
            
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
               
    def delete_chapter(self):
        self.user_view.navbar_menu(self.user, "Delete Chapter")
        self.user_view.display_message("1. Delete")
        self.user_view.display_message("2. Go Back")
        choice = self.user_view.get_text_input("Enter Choice (1-2): ")
        if choice == '1':
            isSucceed = self.faculty_model.deleteChapter(self.ebook)
            if isSucceed == 1:
                self.modify_chapter()
            else:
                self.modify_chapter()
        elif choice == '2':
            self.modify_chapter()
        else:
            self.user_view.display_message("Invalid choice!")
            self.delete_chapter()
    
    def hide_chapter(self):
        self.user_view.navbar_menu(self.user, "Hide Chapter")
        sectionID = self.faculty_model.getSectionID_hidden(self.ebook)
        if sectionID:
            self.ebook['sectionID'] = sectionID[0]
            blockID = self.faculty_model.getBlockID_hidden(self.ebook)
            if blockID:
                self.ebook['contentblockID'] = blockID[0]
            else:
                self.user_view.display_message("Chapter was not hidden!")
                self.modify_chapter()
                return
        else:
            self.user_view.display_message("Chapter was not hidden!")
            self.modify_chapter()
            return
        
        self.user_view.display_message("1. Save")
        self.user_view.display_message("2. Cancel")
        choice = self.user_view.get_text_input("Enter choice(1-2): ")
        if choice == '1':
            isSucceed = self.faculty_model.hideChapter(self.ebook)
            if isSucceed == 1:
                self.modify_chapter()
            else:
                self.user_view.display_message("Chapter was not hidden!")
                self.modify_chapter()
        elif choice == '2':
            self.modify_chapter()
        else:
            self.user_view.display_message("Invalid choice!")
            self.hide_chapter()
             
    def modify_chapter(self):   
        self.user_view.navbar_menu(self.user, "Modify Chapter")
        chapterID = self.user_view.get_text_input("Enter Unique Chapter ID: ")
        if self.ischapterIDValid(chapterID):
            self.user_view.display_message("1. Hide Chapter")
            self.user_view.display_message("2. Delete Chapter")
            self.user_view.display_message("3. Add New Section")
            self.user_view.display_message("4. Modify Section")
            self.user_view.display_message("5. Go Back")
            choice = self.user_view.get_text_input("Enter Choice (1-5): ")
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
                self.hide_chapter()
            elif choice == '2':
                self.delete_chapter()
            elif choice == '3':
                self.create_section()
            elif choice == '4':
                self.modify_section()
            elif choice == '5':
                if self.ebook['ctype'] == "Active":
                    self.active_course()
                else:
                    self.evaluation_course()
            else:
                self.user_view.display_message("Invalid choice!")
        else:
            self.user_view.display_message("Invalid Chapter ID format")
            self.modify_chapter()  
         
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
                if self.ebook['ctype'] == "Active":
                    self.active_course()
                else:
                    self.evaluation_course()
            else:
                self.user_view.display_message("Invalid choice!")
                self.create_chapter()
        else:
            self.user_view.display_message("Invalid Chapter ID format")
            self.create_chapter()     
                     
    def create_TA(self):
        self.user_view.navbar_menu(self.user, "Add TA")
        firstName = self.user_view.get_text_input("A. Enter First Name: ")
        lastName = self.user_view.get_text_input("B. Enter Last Name: ")
        email = self.user_view.get_text_input("C. Enter Email: ")
        password = self.user_view.get_text_input("D. Enter Password: ")
        if not self.isValid(firstName, lastName, password):
            self.user_view.display_message("Invalid Input!")
            self.create_TA()
            return
        current_time = datetime.now()
        TAID = firstName[:2]+lastName[:2]+current_time.strftime("%m")+current_time.strftime("%y")
        self.user_view.display_message("\n1. Save")
        self.user_view.display_message("2. Cancel")
        choice = self.user_view.get_text_input("Enter choice(1-2): ")
        if choice == '1':
            taId = self.faculty_model.getTAID(firstName, lastName, email)
            if(taId is None):
                self.faculty_model.addTA_to_User(TAID, firstName, lastName, email, password)
                self.faculty_model.addTA_to_Course(self.ebook['uToken'], TAID, self.ebook['courseID'])
            else:
                self.faculty_model.addTA_to_Course(self.ebook['uToken'], taId, self.ebook['courseID'])
            self.landing_page()
        elif choice == '2':
            self.landing_page()
        else:
            self.user_view.display_message("Invalid choice!")
            self.create_ta()
        
    def view_students(self):
        self.user_view.navbar_menu(self.user, "View Students")
        students = self.faculty_model.get_enrolled_students(self.ebook['uToken'], "Enrolled")
        if students:
            print(f"List of students in the course {self.ebook['courseID']}:\n ")
            self.faculty_view.display_students(students)
        else:
            self.faculty_view.display_message("No students found!")
            self.active_course()
            return
        self.user_view.display_message("\n1. Go Back")
        choice = self.user_view.get_text_input("Enter choice (1): ")
        if choice == '1':
            self.active_course()
        else:
            self.user_view.display_message("Invalid choice!")
            self.view_students()
        
    def approve_enrollment(self):
        self.user_view.navbar_menu(self.user, "Approve Enrollment")
        studentID = self.user_view.get_text_input("Enter student ID: ")
        isValidStudent = self.faculty_model.is_valid_student(self.ebook['uToken'], studentID)
        if not isValidStudent:
            self.user_view.display_message("Invalid student ID!")
            self.approve_enrollment()
            return
        self.user_view.display_message("\n1. Save")
        self.user_view.display_message("2. Cancel")
        choice = self.user_view.get_text_input("Enter choice(1-2): ")
        if choice == '1':
            isStatusPending = self.faculty_model.is_status_pending(self.ebook['uToken'], studentID)
            if not isStatusPending:
                self.user_view.display_message(f"{studentID} was already enrolled for {self.ebook['courseID']}! You can't make them enroll again.")
                self.active_course()
                return
            decide = self.faculty_model.approve_enrollment(self.ebook['uToken'], studentID)
            if decide == 1:
                self.user_view.display_message(f"Successful enrollment for student {studentID}")
            else:
                self.user_view.display_message(f"Error in enrolling student {studentID}")
            self.active_course()
        elif choice == '2':
            self.user_view.display_message(f"Going back!")
            self.active_course()
        else:
            self.user_view.display_message("Invalid choice!")
            self.approve_enrollment()
        
    def view_worklist(self):
        self.user_view.navbar_menu(self.user, "View Worklist")
        worklist = self.faculty_model.get_worklist(self.ebook['uToken'])
        if worklist:
            print(f"List of students in the course {self.ebook['courseID']} with their status:\n ")
            self.faculty_view.display_worklist(worklist)
        else:
            self.faculty_view.display_message("No worklist found!")
            self.active_course()
            return
        self.user_view.display_message("\n1. Go Back")
        choice = self.user_view.get_text_input("Enter choice (1): ")
        if choice == '1':
            self.active_course()
        else:
            self.user_view.display_message("Invalid choice!")
            self.view_worklist()
             
    def active_course(self):
        self.user_view.navbar_menu(self.user, "Go to Active Course")
        courseID = self.user_view.get_text_input("Enter course ID: ")
        self.ebook['courseID'] = courseID
        validFaculty = self.faculty_model.is_faculty_in_course(self.user[0], courseID)
        if not validFaculty:
            self.user_view.display_message("You are not a Faculty in this course!")
            self.active_course()
            return
            
        textBookID = self.book_model.get_textbookID_by_courseID(courseID)
        if textBookID:
            self.ebook['textBookID'] = textBookID[0]
        else:
            self.user_view.display_message("Course ID does not exist!")
            self.active_course()
            return
        self.ebook['uToken'] = self.faculty_model.get_uToken_by_courseID(courseID)
        self.ebook['ctype'] = "Active"
        self.user_view.display_message("\n1. View Worklist")
        self.user_view.display_message("2. Approve Enrollment")
        self.user_view.display_message("3. View Students")
        self.user_view.display_message("4. Add New Chapter")
        self.user_view.display_message("5. Modify Chapters")
        self.user_view.display_message("6. Add TA")
        self.user_view.display_message("7. Go Back")
        choice = self.user_view.get_text_input("Enter choice (1-7): ")
        if choice == '1':
            self.view_worklist()
        elif choice == '2':
            self.approve_enrollment()
        elif choice == '3':
            self.view_students()
        elif choice == '4':
            self.create_chapter()
        elif choice == '5':
            self.modify_chapter()
        elif choice == '6':
            self.create_TA()
        elif choice == '7':
            self.landing_page()
        else:
            self.user_view.display_message("Invalid choice!")
            self.active_course()
    
    def evaluation_course(self):
        self.user_view.navbar_menu(self.user, "Go to Evaluation Course")
        courseID = self.user_view.get_text_input("Enter course ID: ")
        self.ebook['courseID'] = courseID
        validFaculty = self.faculty_model.is_faculty_in_e_course(self.user[0], courseID)
        if not validFaculty:
            self.user_view.display_message("You are either not a Faculty in this course or this is not a evaluation course!")
            self.evaluation_course()
            return
        textBookID = self.book_model.get_textbookID_by_courseID(courseID)
        if textBookID:
            self.ebook['textBookID'] = textBookID[0]
        else:
            self.user_view.display_message("Course ID does not exist!")
            self.evaluation_course()
            return
        self.ebook['ctype'] = "Evaluation"
        self.user_view.display_message("1. Add New Chapter")
        self.user_view.display_message("2. Modify Chapters")
        self.user_view.display_message("3. Go Back")
        choice = self.user_view.get_text_input("Enter choice (1-3): ")
        if choice == '1':
            self.create_chapter()
        elif choice == '2':
            self.modify_chapter()
        elif choice == '3':
            self.landing_page()
        else:
            self.user_view.display_message("Invalid choice!")
            self.evaluation_course()
    
    def view_courses(self):
        self.user_view.navbar_menu(self.user, "View Courses")
        courses = self.faculty_model.get_courses_by_userID(self.user[0])
        if courses:
            self.faculty_view.display_courses(courses)
        else:
            self.faculty_view.display_message("No courses found!")
            self.landing_page()
            return
        self.user_view.display_message("\n1. Go Back")
        choice = self.user_view.get_text_input("Enter choice (1): ")
        if choice == '1':
            self.landing_page()
        else:
            self.faculty_view.display_message("Invalid choice!")
            self.view_courses()
            
    def change_password(self):
        self.user_view.navbar_menu(self.user, "Change Password")
        old_password = self.user_view.get_password_input("A. Enter current password: ")
        new_password = self.user_view.get_password_input("B. Enter new password: ")
        confirm_password = self.user_view.get_password_input("C. Confirm new password: ")
        if len(new_password) == 0:
            self.user_view.display_message("Invalid password!")
            self.change_password()
            return
        if new_password != confirm_password:
            self.user_view.display_message("Passwords do not match!")
            self.change_password()
            return
        
        self.user_view.display_message("\n1. Update")
        self.user_view.display_message("2. Go Back")
        choice = self.user_view.get_text_input("Enter choice(1-2): ")
        if choice == '1':
            isSucceed = self.faculty_model.update_password(self.user[0], new_password)
            if isSucceed == 1:
                self.user_view.display_message("\nPassword changed successfully!")
                self.landing_page()
            else:
                self.user_view.display_message("Error in changing password!")
                self.change_password()
        elif choice == '2':
            self.landing_page()
        else:
            self.user_view.display_message("Invalid choice!")
            self.change_password()
    
    def landing_page(self):
        self.user_view.navbar_menu(self.user, "Landing Page")
        self.faculty_view.landing_page_menu()
        choice = self.user_view.get_text_input("Enter choice (1-5): ")
        if choice == '1':
            self.active_course()
        elif choice == '2':
            self.evaluation_course()
        elif choice == '3':
            self.view_courses()
        elif choice == '4':
            self.change_password()
        elif choice == '5':
            print("You are logged out!")
        else:
            self.faculty_view.display_message("Invalid choice!")
            self.landing_page()
        
    def login(self):
        self.user_view.display_message("\n\nFaculty | Login")
        userID = self.user_view.get_text_input("A. Enter user ID: ")
        password = self.user_view.get_password_input("B. Enter password: ")
        self.user_view.get_user_signInMenu()
        choice = self.user_view.get_text_input("Enter Choice (1-2): ")
        if choice == '1':
            user = self.faculty_model.get_user(userID, password)
            #print(user)
            if user:
                self.user = user
                self.ebook['userID'] = user[0]
                self.landing_page()
            else:
                self.user_view.display_message("Login incorrect.")
                self.login()
        elif choice == '2':
            pass
        else:
            self.user_view.display_message("Invalid choice!")