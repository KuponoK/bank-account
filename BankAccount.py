# bank account class
class BankAccount:

    def __init__(self, full_name, account_number, routing_number, balance):
        self.__full_name = full_name
        self.__account_number = account_number
        self.__routing_number = routing_number
        self.__balance = balance
    
# deposit function 
    def deposit(self, amount):
        self.__balance += amount

# withdraw function
    def withdraw(self, amount):
        if (amount <= self.__balance):
            self.__balance -= amount
            print(f'Amount Withdrawn: {amount}')
        else:
            print('Insufficient funds')
            self.__balance -= 10

# get_balance method
    def get_balance(self):
        print(f'You have a balance of {self.__balance}')
        return self.__balance

# add_intrest method
    def add_interest(self):
        interest = self.__balance * 0.00083
        self.__balance += round(interest, 2)

# print_receipt method
    def print_receipt(self):
        print(f'{self.__full_name}\n Account No: {self.__account_number}\n Routing No: {self.__routing_number}\n Balance: {self.__balance}')

# 3 different bank account examples
Po_Kealiinohomoku = BankAccount('Po Kealiinohomoku', 12345678, 87654321, 100)
Po_Kealiinohomoku.deposit(20.50)
Po_Kealiinohomoku.withdraw(10)
Po_Kealiinohomoku.add_interest()
Po_Kealiinohomoku.get_balance()