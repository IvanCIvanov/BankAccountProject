from bankaccount import BankAccount

class CheckingAccount(BankAccount):
    # Subclass title
    account_title = "Checking Account"

    # Sent its initialization up to parent class
    def __init__(self, customer_name: str, current_balance: float, minimum_balance: float):
        super().__init__(customer_name, current_balance, minimum_balance)
    # Include variable for transfer limit
    transfer_limit = 1000