class RestaurantManager:
    def __init__(self) -> None:
        self.orders=[]
    def add_order(self,name,price,qte):
        new_order=Order(name,price,qte)
        self.orders.append(new_order)
        print("The Order was added succesfully")
    def show_order(self,order_name):
        target_order=None
        for ord in self.orders:
            if ord.name==order_name:
                target_order=ord
        if target_order:
              print(f"Order: {target_order.name} {target_order.amount} {target_order.qte}")
        else:
            print("No Order in this ")

    def calculte_bill(self):
        bill=0
        for order in self.orders:
            bill+=order.price
        print(f"your bill is : {bill}$")

    def apply_discount(self):
        bill=0
        for order in self.orders:
            bill+=order.price
        if bill>150:
            print(f"Appliying the discount  of  20 % ")
            print(f"The bill after the discount: {bill * 0.2} ")
    def pay(self):
        bill=0
        for order in self.orders:
            bill+=order.price
        print(f"All the bill was paid succesfully")
    def delete_order(self,order_name):
        for ord in self.orders:
            if ord.name==order_name:
                self.orders.remove(ord)
        
class Order:
    def __init__(self,name,amount,qte) -> None:
        self.name=name
        self.amount=amount
        self.quantity=qte



RestaurantSystem=RestaurantManager()

def orders_management():
    print("Welcome to Restaurant Manager")
    while True:
        print("""
            Add item
            Remove item
            Show order
            Calculate bill
            Apply discount
            Pay
""")
        operation=int(input("Choose an operation between those:")) 
        if operation==1:
            order_name=input("Enter the name of your order: ")
            price=input("Enter the price of your order: ")
            quantity=int(input("Enter the quantity of the order"))
            RestaurantSystem.add_order(order_name,price,quantity)
        elif operation==2:
            order_name=input("Enter the name of the order you want to delete")
            RestaurantSystem.delete_order(order_name)
        elif operation==3:
            order_name=input("Enter the name of the order you want to delete")
            RestaurantSystem.show_order(order_name)
        elif operation==4:
            RestaurantSystem.calculte_bill()
        elif operation==7:
            RestaurantSystem.calculte_bill()
        else:
            break

    

