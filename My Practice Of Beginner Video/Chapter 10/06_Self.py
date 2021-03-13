class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")

Sherry = Employee()
Sherry.salary = 100000
Sherry.getSalary() # Employee.getSalary(Sherry)