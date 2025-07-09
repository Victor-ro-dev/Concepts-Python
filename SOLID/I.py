
"""The "I" in SOLID stands for the Interface Segregation Principle. This principle says that a class should not be forced to implement interfaces that it does not use. In other words, it is better to have many small and specific interfaces than one big and generic interface. This way, classes implement only the methods that really make sense for them, making the code cleaner, more flexible, and easier to maintain."""

"""Without Interface Segregation Principle"""
class IPaymentProcessor:
    def process_payment(self, amount):
        pass

    def validate_payment(self, payment_details):
        pass

    def refund_payment(self, amount):
        pass

    def generate_invoice(self, amount):
        pass


"""With Interface Segregation Principle"""
class IPaymentProcessor:
    def process_payment(self, amount):
        pass

class IRefundablePaymentProcessor:
    def refund_payment(self, amount):
        pass

class IValidationPaymentProcessor:
    def validate_payment(self, payment_details):
        pass