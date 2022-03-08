class BankAccount:
    accounts = []
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account(self):
        return f"{self.balance}"

    def yeild_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account()


class User:
    def __init__(self, name):
        self.name = name
        self.account = {
            "checking" : BankAccount(.05,3000),
            "savings" : BankAccount(.05,5000)
        }
        

    def display_user(self):
        print(f"User: {self.name}, Checking Balance: {self.account['checking'].display_account()}")
        print(f"User: {self.name}, Savings Balance: {self.account['savings'].display_account()}")
        return self

    # def transfer_money(self,amount,user):
    #     self.amount -= amount
    #     user.amount += amount
    #     self.display_user()
    #     user.display_user()
    #     return self


mav = User("Maverick")
mav.display_user()

mav.account['checking'].deposit(300)
mav.account['savings'].deposit(600)
mav.display_user()


"""
Output:
User: Maverick, Checking Balance: 3100
User: Maverick, Savings Balance: 5000
"""