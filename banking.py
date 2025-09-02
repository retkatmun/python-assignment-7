"""
Bank Account Simulation

Task:
- Manage simple bank accounts.
- Store accounts in dictionary { "account_number": {"name": str, "balance": float} }
- Deposit, withdraw, transfer between accounts.
- Use *args for batch deposits/withdrawals.
- Use **kwargs for flexible account creation (e.g., overdraft_limit).

// NOT FOR THIS TASK
Future OOP Extension:
- BankAccount class with methods deposit(), withdraw(), transfer().
- Bank class to manage all accounts.
"""
accounts = {}

def create_account(acc_no, name, **kwargs):
    """Create an account with optional features like overdraft_limit."""
    accounts[acc_no] = {"name": name, "balance": 0.0}
    accounts[acc_no].update(kwargs)

def deposit(acc_no, amount):
    """Deposit money into account.
        return "Account not found!" (if account does not exist)
        return Deposited {amount} into {account name}'s account. if account exists
    """
    if acc_no in accounts:
        accounts[acc_no]["balance"] += amount
        return f"Deposited {amount} into {accounts[acc_no]['name']}'s account."
    return "Account not found"

def withdraw(acc_no, amount):
    """Withdraw money if balance is sufficient. else: insufficient funds"""
    if acc_no in accounts:
        if accounts[acc_no]["balance"] >= amount:
            accounts[acc_no]["balance"] -= amount
            return f"Withdrew {amount} from {accounts[acc_no]['name']}'s account."
        return "Insufficient funds."
    return "Account not found!"

def transfer(from_acc, to_acc, amount):
    """Transfer money between accounts if funds are sufficient"""
    if from_acc in accounts and to_acc in accounts:
        if accounts[from_acc]["balance"] >= amount:
            accounts[from_acc]["balance"] -= amount
            accounts[to_acc]["balance"] += amount
            return f"Transferred {amount} from {accounts[from_acc]['name']} to {accounts[to_acc]['name']}."
        return "Insufficient funds."
    return "One or both accounts not found!"

create_account(101, "Alice")
create_account(102, "Bob")

print(deposit(101, 500))
print(deposit(102, 300))
print(withdraw(101, 200))
print(transfer(101, 102, 100))
print(accounts)

