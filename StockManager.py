class Stock:
    def __init__(self) -> None:
        self.products=[]
    def add_product(self,name,price,qte):
        new_product=Prodcut(
            name=name,price=price,qte=qte
        )
        self.products.append(new_product)
        print("The Product was added succesfully")

    def update_stock(self,target_product,new_quantity):
        for prod in self.products:
            if prod==target_product:
                prod.qte=new_quantity
        print("The Stock was succesfully updated")
        
    def search_product(self,product_name):
        target_product=None
        for product in self.products:
            if  product.name==product_name:
             target_product=product
        if target_product:
            print(f"Product: {target_product.name} Price: {target_product.price} Stock: {target_product.qte} ")

        else:
            print("The product that you are searching for is not available")

    def remove_product(self,product_name):
        for product in self.products:
            if product.name==product_name:
                self.products.remove(product)
        print(" Product deleted succesfully")

    def show_products(self):
        f"""
        ####### Products #############         
        """
        for prodcut in self.products:
            print(f" {prodcut.name}   {prodcut.price}$   Stock: {prodcut.qte} ")
        
    def stock_value(self):
        value=0
        for prod in self.products:
            value+=prod.price*prod.quantity
        print(f"The Stock Value is : {value}")

    def low_stock(self):
        low_stock=[]
        for prod in self.products:
            if prod.quantity<1:
                low_stock.append(prod)
        print("The low stock products:")
        for p in low_stock:
            print(
                f"Product: {p.name} Quantity:{p.quantity}"
            )
    
        
    

class Prodcut:
    def __init__(self,name,price,qte) -> None:
        self.name=name
        self.price=price,
        self.quantity=qte


My_stock=Stock()

def stock_manager():
    while True:
        print(""" Available operations:
        1. Add product
        2. Remove product
        3. Update stock
        4. Search product
        5. Show low stock
        6. Calculate stock value
        7. Show products
        8. Exit 
             """)
        operation=int(input("Choose an Operation : "))
        if operation==1:
            product_name=input("Enter the name of the Product you want to add: ")
            quantity=input("Enter the quantity of your Product: ")
            price=input("Enter the price of your product")
            My_stock.add_product(product_name,price,quantity)

        elif operation==2:
            product_name=input("Enter the name of the product you want to delete")
            My_stock.remove_product(product_name)
        elif operation==3:
            product_name=input("Enter the name of the product you want to delete")
            update_quantity=input("Enter the update quantity")
            My_stock.update_stock(product_name,update_quantity)
        elif operation==4:
            product_name=input("Enter the name of the product you want to delete")
    
        elif operation==5:
            My_stock.low_stock()
        elif operation==6:
           My_stock.stock_value()
        elif operation==7:
            My_stock.show_products()
        else:
            break




    

