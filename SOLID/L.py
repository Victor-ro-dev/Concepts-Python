"""The "L" in SOLID stands for the Liskov Substitution Principle. This principle says that objects of a derived class should be able to replace objects of the base class without altering the program’s behavior. In other words, if a child class inherits from a parent class, it must maintain the same expected behavior, without causing errors or unexpected results. This guarantees that the system is more reliable and easier to maintain."""


from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

    @abstractmethod
    def validate_payment(self, payment_details):
        pass

class CreditCardPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of {amount}")

    def validate_payment(self, payment_details):
        print(f"Validating credit card payment details: {payment_details}")

class PayPalPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of {amount}")

    def validate_payment(self, payment_details):
        print(f"Validating PayPal payment details: {payment_details}")


# Example usage
if __name__ == "__main__":
    credit_card_payment = CreditCardPayment()
    credit_card_payment.process_payment(100)
    credit_card_payment.validate_payment({"card_number": "1234-5678-9012-3456"})

    paypal_payment = PayPalPayment()
    paypal_payment.process_payment(200)
    paypal_payment.validate_payment({"email": "teste@gmail.com"})


