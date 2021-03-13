class Programmer:
    Company = "Microsoft"

    def __init__(self,name,product):
        self.name = name
        self.product = product

    def getinfo(self):
        print(f"The name of a Programmer is {self.name} and Product is {self.product}")


Sherry = Programmer("Sherry","Skype")
Zulqarnain = Programmer("Zulqarnain","GitHub")
Sherry.getinfo()
Zulqarnain.getinfo()