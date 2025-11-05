from utils.bank_account import BankAccount


if __name__ == "__main__":
    account = BankAccount("Alice")
    account.deposit(1000)
    print(account.get_balance())

    account.withdraw(900)
    print(account.get_balance())

    account.set_interest_rate(0.05)
    account.apply_interest()
    print(account.get_balance())