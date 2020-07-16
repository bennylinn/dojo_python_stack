class User:
    def __init__(self, name, email, balance):
        self.name = name
        self.email = email
        self.balance = balance

    def make_deposit(self, amount):
        self.balance+= amount

userBenny = User("Benny", "benny@gmail.com", 0)

userBenny.make_deposit(500)
userBenny.balance