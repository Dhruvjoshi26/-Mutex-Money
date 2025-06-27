import threading

class BankAccount:
    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            print(f"[{self.account_id}] Depositing {amount}")
            self.balance += amount
            print(f"[{self.account_id}] New balance after deposit: {self.balance}")

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                print(f"[{self.account_id}] Withdrawing {amount}")
                self.balance -= amount
                print(f"[{self.account_id}] New balance after withdrawal: {self.balance}")
            else:
                print(f"[{self.account_id}] Withdrawal of {amount} failed due to insufficient funds.")

    def transfer_to(self, target_account, amount):
        first, second = (self, target_account) if id(self) < id(target_account) else (target_account, self)
        with first.lock:
            with second.lock:
                if self.balance >= amount:
                    print(f"[{self.account_id}] Transferring {amount} to [{target_account.account_id}]")
                    self.balance -= amount
                    target_account.balance += amount
                    print(f"[{self.account_id}] New balance: {self.balance}")
                    print(f"[{target_account.account_id}] New balance: {target_account.balance}")
                else:
                    print(f"[{self.account_id}] Transfer failed due to insufficient funds.")