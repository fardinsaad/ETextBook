class FacultyView:
    @staticmethod
    def navbar_menu(user, title):
        print(f"\n\nAdmin: {user[2]} {user[3]} | {title}")
    @staticmethod
    def display_menu():
        print(f"\n\n1. Enroll in a course")
        print(f"2. Sign in")
        print(f"3. Go back")

    @staticmethod
    def landing_page_menu():
        print("\n1. Go to Active Course")
        print("2. Go to Evaluation Course")
        print("3. View Courses")
        print("4. Change Password")
        print("5. Logout")
        
    @staticmethod
    def display_message(message):
        print(message)