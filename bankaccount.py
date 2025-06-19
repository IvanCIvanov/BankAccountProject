import random

# Global Dictionary for current live account numbers
account_number_list = []
# Creates a randomized Account Number (Not for large scale, duplicates may arise)
def new_account_number():
    # Create a random account number
    __account_number = random.randint(10000, 99999)
    # Check for duplicate account numbers
    while __account_number in account_number_list:
        __account_number = random.randint(10000, 99999)
    account_number_list.append(__account_number)

    # Return new Private account number
    return __account_number


class BankAccount:
    # Class Attribute
    title = "Bank of America"
    # Protected Routing Number for Bank of America
    _routing_number = 29348484
    # Initialization function takes customer name, current balance, and minimum balance
    def __init__(self, customer_name: str, current_balance: float, minimum_balance: float):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self.__account_number = new_account_number()

    # Allows return of account number in a clean way.
    # Circumvents 'print(client_one_checking._BankAccount__account_number)'
    # Now able to use 'print(client_one_checking.account_number())'
    def account_number(self):
        return self.__account_number