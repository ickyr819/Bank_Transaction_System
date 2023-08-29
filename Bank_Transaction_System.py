class Account:
    def __init__(self, number, name):
        self.number = number
        self.name = name
        self.balance = 0
        self.transaction=[]
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("必須為正值")
        self.balance += amount
        self.transaction.append(f"存款：+ {str('{:,}'.format(amount))}")
    def withdraw(self, amount):
        if amount < 1 :
            raise ValueError("必須大於0")
        if amount < self.balance:
            self.balance -= amount
        else:
            raise ValueError("餘額不足")
        self.transaction.append(f"提款：- {str('{:,}'.format(amount))}")

    def transfer(self, amount, target_account):
        if amount < 1 :
            raise ValueError("必須大於0")
        if amount > self.balance :
            raise ValueError("餘額不足")
        self.balance -= amount
        self.transaction.append(f"轉出：- {str('{:,}'.format(amount))} 至 {target_account.name} ")
        target_account.balance += amount
        # target_account.transaction.append(f"轉入：+ {str('{:,}'.format(amount))} 來自 {self.name}")

    def get_transaction(self):
        return self.transaction
        
GPacc = Account ("131-454-088" , "Ricky Ko")
TANGacc = Account ("520-777-168" , "Ben Tang")
GPacc.deposit(88888888)
GPacc.withdraw(16888888)
GPacc.transfer(1,TANGacc)

print("交易紀錄：")
for transaction in GPacc.get_transaction():
    print(transaction)
for transaction in TANGacc.get_transaction():
    print(transaction)

print(GPacc.name + ", 您的銀行存款剩餘：" + str("{:,}".format(GPacc.balance)) + str(" 元"))
# print(TANGacc.name + ", 您的銀行餘額剩餘：" + str("{:,}".format(TANGacc.balance)) + str(" 元"))
