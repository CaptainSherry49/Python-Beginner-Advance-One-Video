# Single Inheretence



class Employee:  # Base class
    Company = "Google"

    def showdetails(self):
        print("This is an employee")

class Programmer(Employee):  # child Class , derived Class
    Company = "youtube"
    language = "Python"
# Is class ko ab Employee class ka sara attributes lana ka right ha
    def getlang(self):
        print(f"The language of Programmer is {self.language}")
# agar is chid class k pas apna koi attribute hoga to ya osa impliment kara ga warna to ya inheritence (class Programmer(Employee):) kar k  base class ka pas search kara ga 
e = Employee()
p = Programmer()
e.showdetails() 
p.showdetails() 
print(p.Company)