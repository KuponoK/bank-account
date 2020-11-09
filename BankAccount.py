# bank account class
class BankAccount:

    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = balance
    
# deposit function 
    def deposit(self, amount):
        self.balance += amount