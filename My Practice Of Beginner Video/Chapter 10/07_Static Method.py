class Employee:
    company = "Google"

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The time is 9AM in the morning")

Sherry = Employee()
Sherry.salary = 100000
Sherry.getSalary("Thanks!") # Employee.getSalary(Sherry)
Sherry.greet() # Employee.greet()
Sherry.time()

