#initialise the class
class BankAccount:
    def __init__(self,initial_balance = 0.0):
        self.current_balance = initial_balance


    def deposit(self,amount):
        self.current_balance = amount + self.current_balance
        return self.current_balance

    def withdraw(self,amount):
        if self.current_balance >= amount:
            self.current_balance =  amount - self.current_balance
            return True
        else:
            return False
        

    def display_balance(self):
        return print(f"Current Balance: ${self.current_balance:.2f}")