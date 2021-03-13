class Employee:
    company = "Google"
    salary = 100

Sherry = Employee()
Hamza = Employee()

# Creating instance attribute salary for both the objects
# Sherry.salary = 300
# Hamza.salary = 400
Sherry.salary = 45
print(Sherry.salary)
print(Hamza.salary)

# Below line throws an error as address is not present in instance/class 
# print(Hamza.address) 