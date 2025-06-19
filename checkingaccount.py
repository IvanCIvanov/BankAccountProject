from bankaccount import BankAccount

class CheckingAccount(BankAccount):
    # Subclass title
    account_title = "Checking Account"

    # Sent its initialization up to parent class
    def __init__(self, customer_name: str, current_balance: float, minimum_balance: float):
        super().__init__(customer_name, current_balance, minimum_balance)
    # Include variable for transfer limit
    transfer_limit = 1000

    def transfer(self, recipient_account, amount):
        if amount > self.transfer_limit:
            print(f"Transfer failed: Amount exceeds limit of {self.transfer_limit}")
        elif amount > self.current_balance:
            print(f"Transfer failed: Insufficient balance of {self.current_balance}")
        else:
            self.current_balance -= amount
            self.current_balance = round(self.current_balance, 2)
            recipient_account.current_balance += amount
            recipient_account.current_balance = round(recipient_account.current_balance, 2)
            print(f"Transferred ${amount} from {self.customer_name} to {recipient_account.customer_name}")
