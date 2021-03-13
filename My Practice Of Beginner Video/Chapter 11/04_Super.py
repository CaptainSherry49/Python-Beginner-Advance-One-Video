# Multilever = 1 Parent , 2 Child
class Person:
    Country = "Pakistan"
    City = "karachi"

    def Breath(self):
        print("person is Breathing")

class Employee(Person):
    Company = "honda"

    def Breath(self):
        print("Employee is breathing luckily")

    def getSalary(self):
        print(f"Salary of Employee is {self.salary}")

class Programmer(Person):
    Company = "Fiver"

    def Breath(self):
        super().Breath() # Super ki waja sa apna bhi method print kara ga or apna parent ka bhi
        print("Programmer is also breathing")


    def getSalary(self):
        print("No salary for Programmer")

P = Person()
E = Employee()
Pr = Programmer()
P.Breath()
E.Breath()
Pr.Breath()


# def __init__():
#     # super().__init__() is tarha ham kisi constructor ko bhi super method k sath use karsakta ha