# multiply the length value by 2.54
# 1 inch = 2.54cm
def Converting():
    user = int(input("Enter number to convert inches to Cms:\n"))
    Formula = user * 2.54
    return (f"{user} inches into Centimeter is {Formula}")

C = Converting()
print(C)