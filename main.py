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

# Create two instances of Checking Account
customer_one_checking = checkingaccount.CheckingAccount("Ivan Ivanov", 350.77, 200.00)
customer_two_checking = checkingaccount.CheckingAccount("Grishma Howale", 350.00, 200.00)

# Create two instances of Savings Account
customer_one_savings = savingsaccount.SavingsAccount("Ivan Ivanov", 1000, 0)
customer_two_savings = savingsaccount.SavingsAccount("Grishma Howale", 1000, 0)

print("\n******** Two Instances of Checking Account and Savings Account ********")

print("\nDisplay Savings Accounts: ")
print_customer_savings(customer_one_savings)
print_customer_savings(customer_two_savings)

print("\nDisplay Checking Accounts: ")
print_customer_checking(customer_one_checking)
print_customer_checking(customer_two_checking)


#Call new methods
print("\n******** Begin Scenario ********")
print("\n******** Applying Interest & Transferring Money ********")
print("\nApplying Interest to customer one Savings...")
print("\nPrevious Amount: $" + str(customer_one_savings.current_balance))
customer_one_savings.apply_interest()
print("\nUpdated Account Balance: ")
print_customer_savings(customer_one_savings)

print("\nAttempting Transfer of money")
customer_one_checking.transfer(customer_two_checking, 600)
print("\nCurrent Accounts status post-failure: ")
print_customer_checking(customer_one_checking)
print_customer_checking(customer_two_checking)

print("\nAttempting Valid Transfer of money")
customer_one_checking.transfer(customer_two_checking, 200)
print("\nCurrent Accounts status post-success: ")
print_customer_checking(customer_one_checking)
print_customer_checking(customer_two_checking)

# Routing Number is protected and should not be accessed in general.
# This display is only to provide proof of functionality,
# and would not be in a standard use case.
print("\n******** Private Accounting Number ********")
print("\n******** Protected Routing Number  ********")
print(f"\nCustomer One Account Number: {customer_one_checking.account_number()}")
print(f"Customer One Routing Number: {customer_one_checking._routing_number}\n")

print(f"Customer Two Account Number: {customer_two_checking.account_number()}")
print(f"Customer Two Routing Number: {customer_two_checking._routing_number}")
