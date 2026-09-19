class Car:
    def __init__(self,n,p,s) -> None:
        self.name=n
        self.price=p
        self.status=s

class RentalSystem:
    def __init__(self) -> None:
        self.cars=[]
    def show_cars(self):
        print("Available cars: ")
        for car in self.cars:
            print(f"""{car.name} 
                       {car.price}$/day
                       {car.status}
 """)
    def search_car(self,car_name):
        target_car=None
        for car in self.cars:
            if car.name==car_name:
                target_car=car
        if target_car:
            print("The car is available")
        else:
            print("the car is not available")
    def rent_car(self,car_name):
        for car in self.cars:
            if car.name==car_name:
                car.status="rented"
        print("The car was rented succesfully")
    def retun_car(self,car_name):
        for car in self.cars:
            if car==car_name:
                car.status="available"
        print("The car is de nouveau available")
    def calculate_price(self,car_name,days):
        target_car=None
        for car in self.cars:
            if car.name==car_name:
                target_car=car
        if target_car:
            print(f"""
                {target_car.name} 
                {target_car.price * days} $
    """)

RentalObject=RentalSystem()
def System():
    print("welcome to the renting system")
    while True:
        operation=input("Choose operation : ")
        print("""
              1. Show cars
                2. Search car
                3. Rent car
                4. Calculate price
           """)
        if operation==1:
            RentalObject.show_cars()
        elif operation==2:
            car_name=input(f"Whats the name of the car you want to rent: ")
            RentalObject.search_car(car_name)
        elif operation==3:
            car_name=input(f"Whats the name of the car you want to rent: ")
            RentalObject.rent_car(car_name)
        elif operation==4:
            car_name=input(f"Whats the name of the car you want to rent: ")
            days=input("For wow many days u want to rent this car")
            RentalObject.calculate_price(car_name,days)
