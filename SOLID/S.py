
"""The "S" in SOLID stands for the Single Responsibility Principle. This principle says that a class should have only one reason to change. In other words, it should be responsible for just one specific part of the system’s functionality. When a class does many different things, it becomes hard to understand, maintain, and modify. By following SRP, the code becomes more organized, easier to test, and easier to evolve, because each class has a well-defined role."""

class UserManager:
    def save_user(self, user):
        # Logic to save user
        print(f"User {user} saved.")
    def send_welcome_email(self, user):
        # Logic to send welcome email
        print(f"Welcome email sent to {user}.")

class UserRepository:
    def save_user(self, user):
        # Logic to save user in database
        print(f"User {user} saved in repository.")

class EmailService:
    def send_email(self, user):
        # Logic to send email
        print(f"Email sent to {user}.")