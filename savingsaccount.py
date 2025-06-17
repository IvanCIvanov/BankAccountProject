from bankaccount import BankAccount

class SavingsAccount(BankAccount):
    # Subclass title
    account_title = "Savings Account"
    # Sent its initialization up to parent class
    def __init__(self, customer_name: str, current_balance: float, minimum_balance: float):
        super().__init__(customer_name, current_balance, minimum_balance)
    # Include variable for interest rate
    interest_rate = 0.01