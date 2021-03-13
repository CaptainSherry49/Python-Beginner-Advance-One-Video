class Employee:
    company = "Google"
    salary = 100

Sherry = Employee()
Hamza = Employee()
Sherry.salary = 300
Hamza.salary = 400

print(Sherry.company)
print(Hamza.company)
Employee.company = "YouTube"
print(Sherry.company)
print(Hamza.company)
print(Sherry.salary)
print(Hamza.salary)