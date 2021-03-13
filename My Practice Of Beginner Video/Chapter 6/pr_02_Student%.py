Math = int(input("Enter Your Math %:\n"))
Physics = int(input("Enter Your Physics %:\n"))
English = int(input("Enter Your English %:\n"))
Total_Percentage_of_Student = (((Math+Physics+English)/300)*100)

if Math >= 33 and Physics >= 33 and English >=33:
    print("Pass") 
else:
    print("Fail")

if Total_Percentage_of_Student >= 40:
    print("Qualified")
else:
    print("Sorry you are Failed :(")