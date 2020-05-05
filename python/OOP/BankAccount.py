class BankAccount:
    def __init__(self, int_rate=0.01, balance=0): # don't forget to add some default values for these parameters!
        self.balance = balance
        self.int_rate = int_rate
    def deposit(self, amount):
        self.balance += amount	# your code here
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
michaelAmerica = BankAccount(0.05, 300)
beccaSmash = BankAccount(0.20, 1000)
michaelAmerica.deposit(250).deposit(150).deposit(50).withdraw(2000).yield_interest().display_account_info()
beccaSmash.deposit(500).deposit(350).withdraw(50).withdraw(75).withdraw(50).withdraw(100).yield_interest().display_account_info()
