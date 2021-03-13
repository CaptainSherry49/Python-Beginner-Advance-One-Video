# multiple inheritence = 2 Parents 1 Child
class Employee:
    Company = "Addidas"
    BarCode = 2134

class Freelancer:
    Company = "BeingGuru" 
    level = 0

    def UpgradeLevel(self):
        self.level = self.level +1

class Programmer(Employee,Freelancer): #Multiple
    name = "Sherry"

p = Programmer
print(p.name)
print(p.Company) #jo nhi class hm na child ma pehla likhi hogi os ka method or attributes ko priority hasil hogi
print(p.level)