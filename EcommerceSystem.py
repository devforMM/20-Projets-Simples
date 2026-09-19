import json


def search_user(users,user_name):
    user_names=[user["name"] for user in users]
    postion=user_names.index(user_name)
    return users.pop(postion)



class Commerce:
    def __init__(self) -> None:
        self.products=[]
        self.users=[]

    def update_users(self,users):
        with open("Users.json" ,"w") as file:
            json.dump(users,file)

    def update_stock(self,products):
        with open("Products.json","w") as file:
            json.dump(products,file)



    def search_product(self,product_name):
        target_product=[prod for prod in self.products if prod.name==product_name]
        if target_product:
            print(f""" Product_name: {target_product[0].name} 
                       Product price: {target_product[0].price}
                       Product Quantity: {target_product[0].quantity}
                    """)
        else:
            print("The Product you are searching for is unavailable")
    def browse_products(self):
        for prod in self.products:
            print(f"""
                    Product_name: {prod.name}
                    Product_price: {prod.price}
                    Product Qauntiy: {prod.price}
""")
    def add_to_cart(self,user_name,name,qte,price):
        user=search_user(self.users,user_name)
        user["cart"]=user["cart"].append(
           { "name":name,
            "quantity":qte,
            "price":price,
            "ordred":False}
        )
        self.users.append(user)
        self.update_users(self.users)
    def remove_from_cart(self,user_name,prod_name):
        user=search_user(self.users,user_name)
        prod_names=[prod.name for prod in self.products]
        position=prod_names.index(prod_name)
        product=self.products[position]
        user["cart"].remove(product)
        self.users.append(user)
        self.update_users(self.users)
    def add_product(self,name,price,qte):
        new_product={
            "name":name,
            "price":price,
            "qte":qte
        }
        self.products.append(new_product)
        self.update_stock(self.products)


            
    
commerce=Commerce()


def system():
    print("Welcome to our Commerce Manager")
    while True:
        operation=int(input("Choose one option between those:"))
        print("""
            1. Browse products
            2. Search
            3. Add to cart
            4. Remove from cart
            5. add product

""")
        if operation==1:
            commerce.browse_products()
        elif operation==2:
            product_name=input("Enter the product name: ")
            commerce.search_product(product_name)
        elif operation==3:
            username=input("Enter your name: ")
            product_informations=input("Enter the Product Informations : Product/quantity/price").split(" ")
            commerce.add_to_cart(username,product_informations[0],product_informations[1],product_informations[2])
        elif operation==4:
            username=input("Enter your name: ")
            product_name=input("Enter the product you want to remove from the cart")
            commerce.remove_from_cart(username,product_name)
        elif operation==5:
            product_informations=input("Enter the product informations: Product/quantity/price ").split(" ")
            commerce.add_product(
                product_informations[0],product_informations[1],product_informations[2]
            )
        else:
            break
    
             


        

        
        
        

        

    
            
        

