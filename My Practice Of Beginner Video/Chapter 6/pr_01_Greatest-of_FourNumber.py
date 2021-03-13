First = int(input("Enter First number:\n"))
Second = int(input("Enter Second number:\n"))
Third = int(input("Enter Third number:\n"))
Fourth = int(input("Enter Fourth number:\n"))

if (First> (Second and Third and Fourth)):
    print(First)
elif (Second>(First and Third and Fourth)):
    print(Second)
elif (Third>(First and Second and Fourth)):
    print(Third)
elif (Fourth>(First and Second and Third)):
    print(Fourth)
else:
    print("I am Optional")
    
