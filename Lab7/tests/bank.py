class BankAccount: 

    def __init__(self, owner, balance = 0): 
        self.owner = owner 
        self.balance = balance 

    def deposit(self, amount): 
        if amount > 0: 
            self.balance += amount 
            return True  
        
        return False 
    def withdraw(self, amount): 
        if 0 < amount <= self.balance: 
            self.balance -= amount
            return True 
         
        return False 
    def get_balance(self): 
        return self.balance  
    
class SavingsAccount(BankAccount): 
    def __init__(self, owner, balance = 0, annual_rate = 0.03): 
        
        super().__init__ (owner, balance)
        self.annual_rate = annual_rate 


    def add_monthly_interest(self): 
        interest = round(self.balance * self.annual_rate / 12, 2) 
        self.balance = self.balance + interest
        return interest
    pass  
pass  

