# Multilever = 1 Parent , 2 Child
class Person:
    Country = "Pakistan"
    City = "karachi"

    def Breath(self):
        print("person is Breathing")

class Employee(Person):
    Company = "honda"
    salary = 20000

    def Breath(self):
        print("Employee is breathing luckily")

    def getSalary(self):
        print(f"Salary of Employee is {self.salary}")

class Programmer(Person):
    Company = "Fiver"

    # def Breath(self):
    #     print("Programmer is also breathing")

    def getSalary(self):
        print("No salary for Programmer")

P = Person()
E = Employee()
Pr = Programmer()
P.Breath()
E.Breath()
Pr.Breath()
# P.Company() Thows an error
print(E.Company)