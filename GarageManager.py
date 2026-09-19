import json

def get_car(cars,car_name):
    car_names=[car["name"] for car in cars]
    position=car_names.index(car_name)
    return cars.pop(position)

class MyGarage:
    def __init__(self) -> None:
        self.cars=[]
        self.repaired=[]
        self.under_reperation=[]
    def update_cars(self,cars):
        with open("cars.json","w") as file:
            json.dump(cars,file)

    def add_car(self,name,owner):
        car={
            "name":name,
            "owner":owner,
            "status":"Normal"
        }
        self.cars.append(car)
        self.update_cars(self.cars)

    def create_repair(self,car_name,problem,repair,cost):
        car=get_car(self.cars,car_name)
        car["Problem"]=problem
        car["Repair"]=repair
        car["Cost"]=cost
        car["status"]="under reparation"
        self.cars.append(car)
        self.update_cars(car)

    def close_repair(self,car_name):
        car=get_car(self.cars,car_name)
        car["Problem"]=None
        car["repair"]=None
        car["Cost"]=None
        car["status"]="repaired"
        self.cars.append(car)
        self.update_cars(self.cars)


garage=MyGarage()

def system():
    print("Welcome to MygarageSystem")
    while True:
        print("""
            Add vehicle
            Create repair
            Close repair
            Calculate repair cost
            Show customer history

""")
        operation=input("choose an operation: ")
        if operation==1:
            owner_name=input("Enter your name:  ")
            car_name=input("Enter the car name: ")
            garage.add_car(car_name,owner_name)

        elif operation==2:
            car_name=input("enter the car name")
            problem=input("Enter the problem")
            repair=input("enter the repair")
            cost=input("enter the cost")
            garage.create_repair(car_name,problem,repair,cost)
        elif operation==3:
            car_name=input("enter the car name: ")
            garage.close_repair(car_name)


        else:
            break


    

