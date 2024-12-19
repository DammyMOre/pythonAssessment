from decimal import Decimal


class Account:
    def __init__(self, name: str , phone_number:"0000000", balance:"0.00"):
        self.name = name
        self.phone_number = phone_number
        self.balance = self.validate_balance(balance)

    def get_balance(self) -> Decimal:
        return self.balance

    def validate_balance(self,amount:Decimal):
        if amount < Decimal('0.00'):
            return "Invalid amount"
        self.balance = amount
        return self.balance

    def deposit(self,amount:Decimal):
        if amount >= Decimal('0.00'):
            self.balance += amount
            raise valueError



