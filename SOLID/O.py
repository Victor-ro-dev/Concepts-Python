"""The "O" in SOLID stands for the Open/Closed Principle. This principle says that classes should be open for extension, but closed for modification. In other words, you should be able to add new features to the system without needing to alter the existing code. This is generally done by using inheritance and interfaces, allowing the system to evolve without breaking what is already working."""

from abc import ABC, abstractmethod

class INotificationChannel(ABC): # Interface for notification channels
    @abstractmethod
    def send_notification(self, message: str) -> None:
        pass

class EmailChannel(INotificationChannel): # Extension 1
    def send_notification(self, message: str) -> None:
        print(f"Sending email notification: {message}")

class SMSChannel(INotificationChannel): # Extension 2
    def send_notification(self, message: str) -> None:
        print(f"Sending SMS notification: {message}")

class WhatsAppChannel(INotificationChannel): # Extension 3
    def send_notification(self, message: str) -> None:
        print(f"Sending WhatsApp notification: {message}")

class NotificationService: # Closed for modification
    def __init__(self, channel: INotificationChannel) -> None:
        self.channel = channel

    def notify(self, message: str) -> None:
        self.channel.send_notification(message)

# Example usage
if __name__ == "__main__":
    email_channel = EmailChannel()
    sms_channel = SMSChannel()
    whatsapp_channel = WhatsAppChannel()

    email_service = NotificationService(email_channel)
    email_service.notify("Hello via Email!")

    sms_service = NotificationService(sms_channel)
    sms_service.notify("Hello via SMS!")

    whatsapp_service = NotificationService(whatsapp_channel)
    whatsapp_service.notify("Hello via WhatsApp!")

    