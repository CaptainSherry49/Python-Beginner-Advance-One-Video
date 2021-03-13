try:
    i = int(input("Enter a number:\n"))
    c =  1/i
except Exception as e:
    print(e)
else:
    print("This will not print when the code is wrong")