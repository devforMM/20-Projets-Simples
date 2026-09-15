class Account:
    def __init__(self,id,owner) -> None:
        self.id=id
        self.owner=owner
        self.balance=0
        self.transactions=[]
    def deposit(self,amount):
        self.balance+=amount
        self.transactions.append(
            Transaction("Deposit",amount)
        )

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            self.transactions.append(
            Transaction("Deposit",amount)
        )
        else:
            return "You dont have enough Money in your account"
    def  check_balance(self):
        return f"Your currenct balance: {self.balance}"
    def transaction_history(self):
        print("Your Transacation history")
        for transaction in self.transactions:
            print(f"""
                  TRANSACTION
                  type: {transaction.type}
                  amount: {transaction.amount}
""")
    def transfer_money(self,receiver_id,amount):
            self.balance-=amount
            self.transactions.append(
                Transaction("Transfer",amount)
            )



        

class Transaction:
    def __init__(self,type,amount) -> None:
        self.type=type
        self.amount=amount






def Minibank():
    while True:
        print(
        """You have those options 1
        1. Create account
        2. Deposit
        3. Withdraw
        4. Transfer
        5. Check balance
        6. Transaction history
        7. Exit""")
        operation=int(input("Chose a number between the options: "))
        if operation==1:
            owner=input("Enter your name: ")
            id=input("Choose an id : ")
            new_account=Account(id,owner)
        elif operation==2:
            amount=float(input("Enter the amount to deposit: "))
            new_account.deposit(amount)
        elif operation==3:
            amount=float(input("Enter the amount to withdraw: "))
            new_account.withdraw(amount)
        elif operation==4:
            new_account.transfer_money(0,amount)
        elif operation==5:
            new_account.check_balance()

        elif operation==6:
            new_account.transaction_history()

        elif operation==7:
            break

    



        


