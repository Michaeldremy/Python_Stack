class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.balance = balance
        self.int_rate = int_rate
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if (self.balance - amount) < 0:
            self.balance = self.balance - 5
            print("Insufficient funds: Charging a $5 fee")
        else:
            self.balance -= amount
        return self
    def display_account_info(self):
        print("Balance: $%s" % (self.balance))
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance = (self.int_rate * self.balance) + self.balance
        return self
class User:
    def __init__(self, name, email, number):
        self.name = name
        self.email = email
        self.account = BankAccount()
        self.number = number
    def make_deposit(self, amount):
    	self.account.deposit(amount)
    	return self
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        print("User: %s, Account Balance: $%d" % (self.name, self.account.balance))
        return self
michael = User("Michael Python", "michael@python.com", 1987654321)
michael.make_deposit(500).make_withdrawal(150).make_withdrawal(100).make_withdrawal(25).display_user_balance()
