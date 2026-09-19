class TrackingSystem:
    def __init__(self) -> None:
        self.expenses=[]
    def add_expense(self,cat,amount):
        new_expense=Expense(cat,amount)
        self.expenses.append(new_expense)
        print("Expense added succesfully")

    
    def  show_expenses(self):
        print("Expenses")
        for exepense in self.expenses:
            print(f"Category:  {exepense.cat}  amount: {exepense.amount} date : {exepense.date} ")

    def total_spent(self):
        total=0
        for exp in self.expenses:
            total+=exp.amount
        print(f"The total is : {total}")

    def biggest_exepense(self):
        bigest_exp=self.expenses[0]
        for exp in self.expenses[1:]:
            if exp.amount>bigest_exp.amount:
                bigest_exp=exp
        print(f"Your biggest exepense is :{bigest_exp.amount}")
    def spending_by_category(self):
        dictionnaire={}
        for exp in self.expenses:
            if exp.cat in dictionnaire.keys():
                dictionnaire[exp.cat]+=exp.amount
            else:
                dictionnaire[exp.cat]=exp.amount
        print("Spending by categories")
        for k,v in dictionnaire.items():
            print(f"""
                    category: {k} - spending: {v}
""")           



from datetime import datetime


class Expense:
    def __init__(self,cat,amount) -> None:
        self.category=cat
        self.amount=amount
        self.date= datetime.now().strftime("%Y/%m/%d")


Mysystem=TrackingSystem()

def library_manager(operation):
    print("""
        1. Add expense
        2. Show expenses
        3. Total spent
        4. Spending by category
        5. Biggest expense
        6. Delete expense
        7. Save
""")
    operation=int(input("Select Operation between all those operations: "))
    while True:
        if operation==1:
            category=input("enter your expense category: ")
            amount=input("enter the amount of the expense")
            Mysystem.add_expense(category,float(amount))
        elif operation==2:
            Mysystem.show_expenses()
        elif operation==3:
            Mysystem.total_spent()
        elif operation==4:
            Mysystem.spending_by_category()
        elif operation==4:
            Mysystem.biggest_exepense()
        elif operation==5:
            Mysystem.biggest_exepense()
        else:
            break





