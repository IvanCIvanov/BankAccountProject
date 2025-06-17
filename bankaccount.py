class BankAccount:
    # Class Attribute
    title = "Bank of America"
    # Initialization function takes customer name, current balance, and minimum balance
    def __init__(self, customer_name: str, current_balance: float, minimum_balance: float):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance