class AdminView:
    @staticmethod
    def navbar_menu(user, title):
        print(f"\n\nAdmin: {user[2]} {user[3]} | {title}")

    @staticmethod
    def display_menu():
        print("\n1. Sign In")
        print("2. Go Back") 

    @staticmethod
    def landing_page_menu():
        print("\n1. Create a Faculty Account")
        print("2. Create E-textbook")
        print("3. Modify E-textbook")
        print("4. Create New Active Course")
        print("5. Create New Evaluation Course")
        print("6. Logout")

    @staticmethod
    def get_text_input(prompt):
        return input(prompt)

    @staticmethod
    def get_password_input(prompt):
        import getpass
        return getpass.getpass(prompt)

    @staticmethod
    def display_message(message):
        print(message)

    @staticmethod
    def display_users(users):
        print("\nRegistered Users:")
        for user_id, username in users:
            print(f"ID: {user_id}, Username: {username}")
