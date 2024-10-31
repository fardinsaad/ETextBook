import re
from models.admin_model import AdminModel
from views.admin_view import AdminView
from views.user_view import UserView
from models.book_model import BookModel

class AdminController:
    def __init__(self):
        self.admin_model = AdminModel()
        self.admin_view = AdminView()
        self.user_view = UserView()
        self.book_model = BookModel()
        self.admin = None
    
    # def is_valid_email(email):
    #     email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'  
    #     return bool(re.match(email_regex, email))
    
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
    
    def extract_primary_chapter_id(self, chapter_id):
        pattern = r'^chap(\d+)$'
        match = re.match(pattern, chapter_id)
        if match:
            primary_chapter_id = match.group(1)
            return primary_chapter_id
        else:
            raise ValueError("Invalid chapter ID format")
        
    def issectionIDValid(self, sectionID):
        pattern = r'^Sec\d+$'
        return bool(re.match(pattern, sectionID))
    
    def isValidBlockID(self, contentblockID):
        pattern = r'^Block\d+$'
        return bool(re.match(pattern, contentblockID))
    
    def isValidActivityID(self, activityID):
        pattern = r'^ACT\d+$'
        return bool(re.match(pattern, activityID))

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
            if(self.isValid(firstName, lastName, password)):
                self.admin_model.addFaculty(firstName, lastName, email, password)
            else:
                self.admin_view.display_message("Invalid input!!!")
            self.landing_page()
        elif choice == '2':
            self.landing_page()
        else:
            self.admin_view.display_message("Invalid choice!")
            
    def create_text(self, type, blockID):
        self.admin_view.navbar_menu(self.admin, "Add Text")
        text = self.admin_view.get_text_input("Enter Text: ")
        self.admin_view.display_message("1. Add")
        self.admin_view.display_message("2. Go Back")
        self.admin_view.display_message("3. Landing Page")
        while True:
            choice = self.admin_view.get_text_input("Enter Choice (1-3): ")
            if choice == '1':
                decide = self.book_model.addContentBlock(blockID, type, text)
                if decide == 0:
                    self.create_text(type, blockID)
                else:
                    self.create_content_block()
            elif choice == '2':
                self.create_content_block()
            elif choice == '3':
                self.landing_page()
            else:
                self.admin_view.display_message("Invalid choice!")
                

    
    def create_picture(self, type, blockID):
        self.admin_view.navbar_menu(self.admin, "Add Picture")
        picture = self.admin_view.get_text_input("Enter Picture: ")
        self.admin_view.display_message("1. Add")
        self.admin_view.display_message("2. Go Back")
        self.admin_view.display_message("3. Landing Page")
        while True:
            choice = self.admin_view.get_text_input("Enter Choice (1-3): ")
            if choice == '1':
                decide = self.book_model.addContentBlock(blockID, type, picture)
                if decide == 0:
                    self.create_picture(type, blockID)
                else:
                    self.create_content_block()
            elif choice == '2':
                self.create_content_block()
            elif choice == '3':
                self.landing_page()
            else:
                self.admin_view.display_message("Invalid choice!")   
                
    def create_question(self, type, activityID):
        self.admin_view.navbar_menu(self.admin, "Add Question")
        questionID = self.admin_view.get_text_input("A. Enter Question ID: ")
    
    def create_activity(self, type, blockID):
        self.admin_view.navbar_menu(self.admin, "Add Activity")
        activityID = self.admin_view.get_text_input("Enter Unique Activity ID: ")
        if (self.isValidActivityID(activityID)):
            self.admin_view.display_message("1. Add Question")
            self.admin_view.display_message("2. Go back")
            self.admin_view.display_message("3. Landing Page")
            while True:
                choice = self.admin_view.get_text_input("Enter Choice (1-3): ")
                if choice == '1':
                    decide = self.book_model.addContentBlock(blockID, type, activityID)
                    self.create_question("question", activityID)
                elif choice == '2':
                    self.create_content_block()
                elif choice == '3':
                    self.landing_page()
                else:
                    self.admin_view.display_message("Invalid choice!")
        else:
            self.admin_view.display_message("Invalid Activity ID format")
            self.create_activity(type, blockID)
        
            
    def create_content_block(self):
        self.admin_view.navbar_menu(self.admin, "Add New Content Block")
        contentblockID = self.admin_view.get_text_input("Enter Content Block ID: ")
        if(self.isValidBlockID(contentblockID)):
            self.admin_view.display_message("1. Add Text")
            self.admin_view.display_message("2. Add Picture")
            self.admin_view.display_message("3. Add Activity")
            self.admin_view.display_message("4. Go Back")
            self.admin_view.display_message("5. Landing Page")
            while True:
                choice = self.admin_view.get_text_input("Enter Choice (1-5): ")
                if choice == '1':
                    self.create_text("text", contentblockID)
                elif choice == '2':
                    self.create_picture("picture", contentblockID)
                elif choice == '3':
                    self.create_activity("activity", contentblockID)
                elif choice == '4':
                    self.create_section()
                elif choice == '5':
                    self.landing_page()
                else:
                    self.admin_view.display_message("Invalid choice!")
        else:
            self.admin_view.display_message("Invalid Content Block ID format")
            self.create_content_block()

    def create_section(self):
        self.admin_view.navbar_menu(self.admin, "Add New Section")
        sectionID = self.admin_view.get_text_input("Enter Section Number: ")
        sectionTitle = self.admin_view.get_text_input("Enter Section Title: ")
        if self.issectionIDValid(sectionID):
            primarySectionNumber = sectionID
            prefix = sectionID[:-2]    # Get "SEC" (all except the last two characters)
            number = int(sectionID[-2:])  # Convert the last two characters to an integer (e.g., 05 -> 5)
    
            # Decrement the numeric part by 1
            secondary_number = number - 1

            # Format back to two digits and combine with the prefix
            secondarySectionNumber = f"{prefix}{secondary_number:02d}"  # Ensures two-digit format
            decide = self.book_model.addSection(sectionID, sectionTitle, primarySectionNumber, secondarySectionNumber)
            if decide == 0:
                self.create_section()
            else:
                print("\n")
                self.admin_view.display_message("1. Add New Content Block")
                self.admin_view.display_message("2. Go Back")
                self.admin_view.display_message("3. Landing Page")
                while True:
                    choice = self.admin_view.get_text_input("Enter Choice (1-3): ")
                    if choice == '1':
                        self.create_content_block()
                        break
                    elif choice == '2':
                        self.create_chapter()
                        break
                    elif choice == '3':
                        self.landing_page()
                        break
                    else:
                        self.admin_view.display_message("Invalid choice!") 
        else:
            self.admin_view.display_message("Invalid Section ID format")
            self.create_section()

    def create_chapter(self):
        self.admin_view.navbar_menu(self.admin, "Add New Chapter")
        chapterID = self.admin_view.get_text_input("Enter Unique Chapter ID: ")
        chapterTitle = self.admin_view.get_text_input("Enter Chapter Title: ")
        if self.ischapterIDValid(chapterID):
            primarychapterID = self.extract_primary_chapter_id(chapterID)
            secondarychapterID = int(primarychapterID) - 1 
            #print(chapterID, primarychapterID, chapterTitle, secondarychapterID)
            decide = self.book_model.addChapter(chapterID, int(primarychapterID), chapterTitle, secondarychapterID)
            if decide == 0:
                self.create_chapter()
            else:
                print("\n")
                self.admin_view.display_message("1. Add New Section")
                self.admin_view.display_message("2. Go Back")
                self.admin_view.display_message("3. Landing Page")
                while True:
                    choice = self.admin_view.get_text_input("Enter Choice (1-3): ")
                    if choice == '1':
                        self.create_section()
                        break
                    elif choice == '2':
                        self.create_etextbook()
                        break
                    elif choice == '3':
                        self.landing_page()
                        break
                    else:
                        self.admin_view.display_message("Invalid choice!")
        else:
            self.admin_view.display_message("Invalid Chapter ID format")
            self.create_chapter()        

    def create_etextbook(self):
        self.admin_view.navbar_menu(self.admin, "Create E-textbook")
        title = self.admin_view.get_text_input("Enter E-textbook Title: ")
        textBookID = self.admin_view.get_text_input("Enter Unique E-textbook ID: ")
        # Add validity checks for textBookID ********
        decide = self.book_model.addEtextbook(textBookID, title)
        if decide == 0:
            self.create_etextbook()
        else:
            print("\n")
            self.admin_view.display_message("1. Add New Chapter")
            self.admin_view.display_message("2. Go Back")
            while True:
                choice = self.admin_view.get_text_input("Enter Choice (1-2): ")
                if choice == '1':
                    self.create_chapter()
                    break
                elif choice == '2':
                    self.landing_page()
                    break
                else:
                    self.admin_view.display_message("Invalid choice!")



    def landing_page(self):
        self.admin_view.navbar_menu(self.admin, "Landing Page")
        self.admin_view.landing_page_menu()
        choice = self.admin_view.get_text_input("Enter Choice (1-6): ")
        if choice == '1': # Create a faculty account
            self.create_faculty_acount()
        elif choice == '2': # Create E-textbook
            self.create_etextbook()
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

