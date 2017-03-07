class BankAccount(object):
    '''
    This class defines withdraw and deposit and takes no parameters
    '''
    def withdraw():
        pass

    def deposit():
        pass


class SavingsAccount(BankAccount):
    '''
    This class inherits from BankAccount and initializes balance to 500, whereby you cannot withdraw beyond 500 
    '''
    def __init__(self):
        self.balance = 500

    def deposit(self, amount):
        if amount < 0:
            return "Invalid deposit amount"
        else:
            self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount < 0:
            return "Invalid withdraw amount"
        elif amount > self.balance:
            return "Cannot withdraw beyond the current account balance"
        elif (self.balance - amount) < 500:
            return "Cannot withdraw beyond the minimum account balance"
        else:
            self.balance -= amount
        return self.balance


class CurrentAccount(BankAccount):
    '''
    This class inherits from bankaccount and initializes balance to 0
    '''
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount < 0:
            return "Invalid deposit amount"
        else:
            self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount < 0:
            return "Invalid withdraw amount"
        elif self.balance < amount:
            return "Cannot withdraw beyond the current account balance"
        else:
            self.balance -= amount
        return self.balance    