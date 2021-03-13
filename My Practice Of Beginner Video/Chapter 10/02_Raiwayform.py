class RailwayForm:
    fromtype = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

SherryApplication = RailwayForm()
SherryApplication.name = "Sherry"
SherryApplication.train = "Pakistan Express"
SherryApplication.printData()