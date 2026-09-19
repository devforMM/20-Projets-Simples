import json
from datetime import datetime
def get_medecine(medecines,medecine_name):
        medecines_names=[m["name"] for m in medecines]
        position=medecines_names.index(medecine_name)
        medecine=medecines.pop(position)
        return medecine
    
class Pharamacie:
    def __init__(self) -> None:
        self.medecines=[]

    def update_stock(self,medecines):
        with open("Stock.json") as file:
            json.dump(medecines,file)
    def add_medecin(self,name,price,stock,expiration):
        medecine={
            "name":name,
            "price":price,
            "stock":stock,
            "expiration":expiration
        }
        self.medecines.append(medecine)
        self.update_stock(self.medecines)
    def sell_medecine(self,Medecine_name,qte):
        medecine=get_medecine(self.medecines,Medecine_name)
        if medecine["quantity"]-qte>=1:
            medecine["quantity"]-=qte
            self.medecines.append(medecine)
            self.update_stock(self.medecines)
    def shpw_low_stock(self):
         print("low stock: ")
         for med in self.medecines:
              if med["quantiy"]<=3:
                   print(f"Medecine {med["name"]} {med["quantity"]} {med["stock"]}")
    def exepired_medecine(self):
         print("Expired medecines")
         for m in self.medecines:
              if  datetime.strptime(m["expiration"],"%Y-%m-%d") - datetime.now():
                   print(f"Name: {m["name"]}  Expiration date: {m["expiration"]}  ")

    def search_medecin(self,medecin_name):
         medecine=get_medecine(self.medecines,medecin_name)
         print(f"Medecine {medecine["name"]} Price: {medecine["price"]}  Stock:{medecine["stock"]} expiration: {medecine["expiration"]} ")

                       
              
    





    