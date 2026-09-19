class HotelSystem:
    def __init__(self) -> None:
        self.rooms=[]
    def add_room(self,id,type,price):
        new_room=Room(
            id,type,price,"Available"
        )
        self.rooms.append(new_room)
        print("The Room was added succesfully")
    
    def book_room(self,room_id,days):
        target_room=None
        for r in self.rooms:
            if r.id==room_id:
                target_room=r
                r.status="unavailable"
        if target_room:
            print(f"Room: {target_room}")
            print(f"number of nights : {days}")
            print(f"price: {days*target_room.price}$ ")
    def cancel_booking(self,room_id):
        for room in self.rooms:
            if room==room_id:
                room.status="Available"
        print("The room booking was canceled") 

       
    
        
        



class Room:
    def __init__(self,id,type,price,status) -> None:
        self.id=id
        self.type=type
        self.price=price
        status=status


system=HotelSystem()

def Hote():
    print("Welcome to hotel system")
    while True:
        operation=int(input("Chose between those options"))
        print("""
           1. add rooom
           2. book room
           3. cancel booking

""")    
        if operation==1:
            id=input("Enter the room id")
            type=input("Enter the type of the room")
            price=input("Enter the price of the room you want to book")
            system.add_room(id,type,price)
        elif operation==2:
            id=input("Enter the id of the room you want to book")
            days=input("Enter the number of days you want to book your room for")
            system.book_room(id,days)
        elif operation==3:
            id=input("Enter the id of the room you want to cancel")
            system.cancel_booking(id)
        else:
            break

