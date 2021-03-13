class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    
    @staticmethod
    def Bark():
        user  = int(input("enter the number of Barking:\n"))
        print(f"The Dog is an Animals , also a Pet but Dog is Barking {user} Times")

A = Animals
P = Pets
D = Dog
D.Bark()