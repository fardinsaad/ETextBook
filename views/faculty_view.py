class FacultyView:
    @staticmethod
    def navbar_menu(user, title):
        print(f"\n\nAdmin: {user[2]} {user[3]} | {title}")
    @staticmethod
    def display_menu():
        print(f"\n\n1. Enroll in a course")
        print(f"2. Sign in")
        print(f"3. Go back")
