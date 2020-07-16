class User:
    def __init__(self, name, email, balance):
        self.name = name
        self.email = email
        self.balance = balance

    def make_deposit(self, amount):
        self.balance+= amount
        return self

    def make_withdrawal(self, amount):
        self.balance-= amount
        return self
        
    def display_user(self):
        print(self.name+", Balance: "+str(self.balance))

userBenny = User("Benny", "benny@gmail.com", 0)
userGuido = User('Guido', "guido@python.com", 0)
userMonty = User("Monty", "monty@python.com", 0)

userBenny.make_deposit(500).make_deposit(500).make_deposit(500).make_withdrawal(500).display_user()

userGuido.make_deposit(500).make_deposit(500).make_withdrawal(500).make_withdrawal(500).display_user()

userMonty.make_deposit(500).make_withdrawal(500).make_withdrawal(500).make_withdrawal(500).display_user()
