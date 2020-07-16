class User:
    def __init__(self, name, email, branch, balance):
        self.name = name
        self.email = email
        self.account = BankAccount(branch, balance)

    def make_deposit(self, amount):
        self.account+= amount
        return self

    def make_withdrawal(self, amount):
        self.account-= amount
        return self
        
    def display_user(self):        
        print(self.account.balance)

class BankAccount:
    def __init__(self, branch, balance):
        self.branch = branch
        self.balance = balance

userBenny = User("Benny", "benny@gmail.com", "CIBC", 0)
userGuido = User('Guido', "guido@python.com", "TD", 0)
userMonty = User("Monty", "monty@python.com", "BMO", 0)


userBenny.display_user()