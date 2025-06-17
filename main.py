import bankaccount
import savingsaccount
import checkingaccount


# Deposit Function takes BankAccount object and deposit value
def deposit(account: bankaccount.BankAccount, deposit_val: float):
    # Deposits amount into BankAccount object, then provides confirmation message
    account.current_balance += deposit_val
    print(f"\nFor the Customer: {account.customer_name}, ")
    print("Deposit Complete.")

# Withdraw Function takes BankAccount object and withdraw value
def withdraw(account: bankaccount.BankAccount, withdraw_val: float):
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
def print_customer_information(account):
    print(f"\nBank: {account.title}\nCustomer: {account.customer_name}"
          f"\n{account.account_title}: ${account.current_balance}\nMinimum Balance: ${account.minimum_balance}")

def print_customer_savings(account: savingsaccount.SavingsAccount):
    print(f"\nCustomer: {account.customer_name}"
          f"\n{account.account_title} Balance: ${account.current_balance}\nMinimum Balance: ${account.minimum_balance}"
          f"\nCurrent Interest Rate: {account.interest_rate}")

def print_customer_checking(account: checkingaccount.CheckingAccount):
    print(f"\nCustomer: {account.customer_name}"
          f"\n{account.account_title} Balance: ${account.current_balance}\nMinimum Balance: ${account.minimum_balance}"
          f"\nTransfer Limit: ${account.transfer_limit}")
# Validation Below

# Create two instances of the BankAccount class
customer_one_checking = checkingaccount.CheckingAccount("Ivan Ivanov", 350.77, 200.00)
customer_two_checking = checkingaccount.CheckingAccount("Greg Gregoriv", 350.00, 200.00)

customer_one_savings = savingsaccount.SavingsAccount("Ivan Ivanov", 1000, 0)
customer_two_savings = savingsaccount.SavingsAccount("Greg Gregoriv", 1000, 0)

# Print information from both instances using custom def
print_customer_information(customer_one_checking)
print_customer_information(customer_two_checking)

# Deposit $100 into Ivan's account, then display updated account
deposit(customer_one_checking, 100)
print_customer_information(customer_one_checking)

# Withdraw $100 from Greg's account
withdraw(customer_two_checking, 100)
# Prove that Withdraw limit exists with minimum balance.
withdraw(customer_two_checking, 100)
# Display updated account with only $100 withdrawn
print_customer_information(customer_two_checking)


print("\nDisplay Savings Accounts: ")
print_customer_savings(customer_one_savings)
print_customer_savings(customer_two_savings)

print("\nDisplay Checking Accounts: ")
print_customer_checking(customer_one_checking)
print_customer_checking(customer_two_checking)