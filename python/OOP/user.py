class User:
    def __init__(self, name, email, number):
        self.name = name
        self.email = email
        self.account_balance = 0
        self.number = number
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount # the specific user's account increases by the amount of the value received
    	return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self): # This is currently not working.
        print("User: %s, Account Balance: $%d" % (self.name, self.account_balance))	# output: 100
        return self
guido = User("Guido Van Rossum", "guido@python.com", 2531115678)
monty = User("Monty Python", "monty@python.com", 1234567891)
michael = User("Michael Python", "michael@python.com", 1987654321)
guido.make_deposit(100).make_deposit(200).make_deposit(100).make_withdrawal(300).display_user_balance()
monty.make_deposit(50).make_deposit(150).make_withdrawal(25).make_withdrawal(15).display_user_balance()
michael.make_deposit(500).make_withdrawal(150).make_withdrawal(100).make_withdrawal(25).display_user_balance()
