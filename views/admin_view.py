class AdminView:
    @staticmethod
    def display_menu():
        print("\n1. Sign In")
        print("2. Go Back")

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
