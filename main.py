
# Class initialization
class BankAccount:
    # Class Attribute
    title = "Bank of America"
    # Initialization function takes customer name, current balance, and minimum balance
    def __init__(self, customer_name: str, current_balance: float, minimum_balance: float):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

# Deposit Function takes BankAccount object and deposit value
def deposit(account: BankAccount, deposit_val: float):
    # Deposits amount into BankAccount object, then provides confirmation message
    account.current_balance += deposit_val
    print(f"\nFor the Customer: {account.customer_name}, ")
    print("Deposit Complete.")

# Withdraw Function takes BankAccount object and withdraw value
def withdraw(account: BankAccount, withdraw_val: float):
    # If withdrawing would fall below minimum value, cancel withdraw and provide cancel message
    if (account.current_balance - withdraw_val) < account.minimum_balance:
        print(f"\nFor the Customer: {account.customer_name}, ")
        print("Insufficient balance to withdraw again...")
        return
    # If withdraw is possible, continue and provide confirmation message
    else:
        account.current_balance -= withdraw_val
        print(f"\nFor the Customer: {account.customer_name}, ")
        print("Withdraw Complete.")

# Custom display of BankAccount object including bank title
def print_customer_information(account: BankAccount):
    print(f"\nBank: {account.title}\nCustomer: {account.customer_name}"
          f"\nCurrent Balance: {account.current_balance}\nMinimum Balance: {account.minimum_balance}")


# Validation Below

# Create two instances of the BankAccount class
customer_one = BankAccount("Ivan Ivanov", 350.77, 200.00)
customer_two = BankAccount("Greg Gregoriv", 350.00, 200.00)

# Print information from both instances using custom def
print_customer_information(customer_one)
print_customer_information(customer_two)

# Deposit $100 into Ivan's account, then display updated account
deposit(customer_one, 100)
print_customer_information(customer_one)

# Withdraw $100 from Greg's account
withdraw(customer_two, 100)
# Prove that Withdraw limit exists with minimum balance.
withdraw(customer_two, 100)
# Display updated account with only $100 withdrawn
print_customer_information(customer_two)
