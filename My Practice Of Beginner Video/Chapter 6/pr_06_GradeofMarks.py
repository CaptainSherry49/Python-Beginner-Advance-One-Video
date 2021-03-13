Marks = int(input("Enter your Marks:\n"))
if Marks > 90 and Marks <101:
    print("Your Grade is Ex Congratulations!")
elif Marks > 80 and Marks < 91:
    print("Your Grade is A ")
elif Marks > 70 and Marks < 81:
    print("Your Grade is B ")
elif Marks > 60 and Marks < 71:
    print("Your Grade is C ")
elif Marks == 50 and Marks < 61:
    print("Your Grade is D ")
elif Marks < 50:
    print("Sorry to Say but You are Fail (f)") 
else:
    print("Invalid input")