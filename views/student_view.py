class StudentView:
    @staticmethod
    def navbar_menu(user, title):
        print(f"\n\nAdmin: {user[2]} {user[3]} | {title}")
    
    @staticmethod
    def display_menu():
        print(f"\n\n1. Enroll in a course")
        print(f"2. Sign in")
        print(f"3. Go back")
    @staticmethod
    def display_landing_page_menu():
        print(f"\n\n1. View a section")
        print(f"2. View participation activity points")
        print(f"3. Logout")
