"""Part B tests. Your code goes in Lab7/bank.py."""
from bank import BankAccount, SavingsAccount


def test_new_account():
    account = BankAccount("Ana", 100)
    assert account.owner == "Ana"
    assert account.get_balance() == 100


def test_balance_starts_at_0():
    assert BankAccount("Ana").get_balance() == 0


def test_deposit_adds_money():
    account = BankAccount("Ana", 100)
    assert account.deposit(50) is True
    assert account.get_balance() == 150


def test_cannot_deposit_0_or_less():
    account = BankAccount("Ana", 100)
    assert account.deposit(0) is False
    assert account.deposit(-5) is False
    assert account.get_balance() == 100


def test_can_withdraw_exactly_the_balance():
    account = BankAccount("Ana", 100)
    assert account.withdraw(100) is True
    assert account.get_balance() == 0


def test_cannot_withdraw_more_than_the_balance():
    account = BankAccount("Ana", 100)
    assert account.withdraw(101) is False
    assert account.get_balance() == 100


def test_cannot_withdraw_0_or_less():
    account = BankAccount("Ana", 100)
    assert account.withdraw(0) is False
    assert account.withdraw(-5) is False
    assert account.get_balance() == 100


def test_savings_account_is_a_bank_account():
    assert isinstance(SavingsAccount("Ben"), BankAccount)


def test_monthly_interest_amount():
    savings = SavingsAccount("Ben", 1000, 0.06)
    assert savings.add_monthly_interest() == 5.0


def test_monthly_interest_is_added_to_the_balance():
    savings = SavingsAccount("Ben", 1000, 0.06)
    savings.add_monthly_interest()
    assert savings.get_balance() == 1005.0


def test_monthly_interest_rounds_to_cents():
    savings = SavingsAccount("Ben", 100, 0.05)
    assert savings.add_monthly_interest() == 0.42
