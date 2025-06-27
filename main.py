import threading
from bank_account import BankAccount

acc1 = BankAccount("ACC001", 1000)
acc2 = BankAccount("ACC002", 500)

def transaction_deposit(account, amount):
    account.deposit(amount)

def transaction_withdraw(account, amount):
    account.withdraw(amount)

def transaction_transfer(source, target, amount):
    source.transfer_to(target, amount)

threads = [
    threading.Thread(target=transaction_deposit, args=(acc1, 200)),
    threading.Thread(target=transaction_withdraw, args=(acc2, 100)),
    threading.Thread(target=transaction_transfer, args=(acc1, acc2, 300)),
    threading.Thread(target=transaction_transfer, args=(acc2, acc1, 150)),
    threading.Thread(target=transaction_deposit, args=(acc2, 400)),
    threading.Thread(target=transaction_withdraw, args=(acc1, 500)),
]

for t in threads:
    t.start()

for t in threads:
    t.join()

print("\nFinal Account Balances:")
print(f"{acc1.account_id}: {acc1.balance}")
print(f"{acc2.account_id}: {acc2.balance}")