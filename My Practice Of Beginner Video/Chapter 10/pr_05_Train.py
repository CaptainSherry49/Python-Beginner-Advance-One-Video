#Fare =  The money paid for a journey on public transport.

class Train:
    def __init__(self, name , fare , Seats):
        self.name = name
        self.fare = fare
        self.Seats = Seats
    def Train_info(self):
        print(f"The name of Train from Rawalpindi to Karachi is {self.name}")
        print(f"The fare of {self.name} is {self.fare}")
    
    def getStatus(self):
        print(f"The Seats in {self.name} are {self.Seats}")

    
    def book_ticket(self):
        if (self.Seats>0):
            print(f"Your ticket is booked your seat number is {self.Seats}")
            self.Seats = self.Seats -1
        else:
            print("Sorry this train is full")


Info_of_Train = Train("Khyber Mail: 1324","1500","243")
Info_of_Train.Train_info()
Info_of_Train.getStatus
Info_of_Train.book_ticket()
Info_of_Train.getStatus