"""The "D" in SOLID stands for the Dependency Inversion Principle. This principle says that high-level modules should not depend on low-level modules; both should depend on abstractions. In other words, instead of a class depending directly on another concrete class, it should depend on interfaces or abstract classes. This makes the system more flexible, easier to modify and test, because the dependencies can be replaced without altering the main code."""

from abc import ABC, abstractmethod

# Good example: Both depend on abstraction
class IMessageService(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailService(IMessageService):
    def send(self, message):
        print(f"Email sent: {message}")

class SMSService(IMessageService):
    def send(self, message):
        print(f"SMS sent: {message}")

class Notification:
    def __init__(self, service: IMessageService):
        self.service = service
    def notify(self, message):
        self.service.send(message)


# Example usage
if __name__ == "__main__":

    email_service = EmailService()
    sms_service = SMSService()

    notification = Notification(email_service)
    notification.notify("Hello via Email!")

    notification = Notification(sms_service)
    notification.notify("Hello via SMS!")
