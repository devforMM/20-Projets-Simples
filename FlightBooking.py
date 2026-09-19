class Flight:
    def __init__(self,n,d1,d2,s,p) -> None:
        self.name=n
        self.depart=d1
        self.destination=d2
        self.available_seats=s
        self.price=p


class FlightSystem:
    def __init__(self) -> None:
        self.flights=[]
    def  search_flight(self,name):
        target_flight=name
        for flight in self.flights:
            if flight.name==name:
                target_flight=flight
        if target_flight:
            print(f"""
               Flight: {target_flight.name}
               {target_flight.depart}->{target_flight.destination}
               Seats: {target_flight.available_seats}

""")

        else:
            print("The Flight you are searching for is not available in our system")

    def book_seat(self,name,seats):
        for flight in self.flights:
            if flight.name==name:
                difference=flight.available_seats-seats
                if difference>-1:
                    flight.available_seats-=seats
                    print("Reservation done with succes")
                else:
                    print("Not enough seats in our system")
    def available_seats(self):
        for flight in self.flights:
            if flight.available_seats>0:
                print(f"""
                   Flight : {flight.name}
                   Available seats; {flight.available_seats}
        
""")
            
        

system=FlightSystem()
def flight_booking():
    print("Welcome to the flight system")
    while True:
        operation=int(input("Choose an operation; "))
        print("""
            Search flight
            Book seat
            Show available seats""")
        if operation==1:
            name=input("Enter the name of the flight you want to search for: ")
            system.search_flight(name)
        elif operation==2:
            name=input("enter the name of the flight")
            seats=input("enter the number of seats you want to book")
            system.book_seat(name,seats)
        elif operation==3:
            system.available_seats()
        else:
            break


        

    
          

    