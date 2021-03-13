class Employee:
    company = "Amazon"
    Salary = 30000
    SalaryBonus = 1500

    @property
    def TotalSalary(self):
        return self.Salary + self.SalaryBonus


E = Employee()
print(E.TotalSalary)
