class Budget:
    
    def __init__(self, username):
        self.username = username
        self.amount = 0
        self.accountBalance = 0
        self.category = []

    def deposit (self, amount):
        print(f'{amount} has been deposited by {self.username}')
        self.accountBalance += amount
        return self.accountBalance
        

    def withdraw (self, amount):
        print(f'{amount} has been withdrawn by {self.username}')
        self.accountBalance -= amount
        return self.accountBalance

    def balance (self):
        return self.accountBalance

    def transfer (self, category):
        print(f'{self.amount} has been transfered to {self.username}')
 
  



clothing = Budget('Joe')
food = Budget('Joe')
entertainment = Budget('Joe')


clothing.deposit(5000)
clothing.withdraw(2000)
print(clothing.balance())

clothing.transfer('food')

    #def computingBalance(self):

    #    print(self.accountBalance)

    #def transfer(self):
