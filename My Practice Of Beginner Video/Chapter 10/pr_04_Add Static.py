class Calculator:

    # Constructor
    def __init__(self,num):
        self.number = num
    # Method
    def Square(self):
        print(f"The Square of {self.number} is {self.number **2}")

    def Cube(self):
        print(f"The Cube of {self.number} is {self.number **3}")


    @staticmethod
    def greet():
        print("Hello Sherry")


    def Square_Root(self):
        print(f"The Square root of {self.number} is {self.number **0.5}")

a = Calculator(9)
a.greet()
a.Square()
a.Square_Root()
a.Cube()