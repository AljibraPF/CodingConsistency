#Class for bankaccount, initialazation isn't yet finished
class BankAccount:
    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Successfully withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Account balance: ${self.balance:.2f}")


#29/11/2024
#Initiliazation

def main():
    print("Welcome to the ATM System")
    account = BankAccount(account_number="123456789", owner_name="John Doe", balance=500.0)

    while True:
        print("\nOptions:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Select an option (1-4): ")

        if choice == "1":
            account.check_balance()
        elif choice == "2":
            amount = float(input("Enter the amount to deposit: "))
            account.deposit(amount)
        elif choice == "3":
            amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()