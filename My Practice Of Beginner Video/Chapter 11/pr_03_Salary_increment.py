class Employee:
    salary = 21000
    Increment = 1.5

    @property
    def salaryAfterIncrement(self):
        return self.salary*self.Increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,sai):
        self.Increment = sai/self.salary

E = Employee()
print(E.salaryAfterIncrement)
print(E.Increment)
E.salary = 30000
print(E.salaryAfterIncrement)
print(E.Increment)