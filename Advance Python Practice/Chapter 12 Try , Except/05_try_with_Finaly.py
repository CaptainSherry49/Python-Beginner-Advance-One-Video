try:
    i = int(input("Enter a number:\n"))
    c =  1/i
except Exception as e:
    print(e)
else:
    print("This will not print when the code is wrong")
finally:
    print("Finally tab bhi print hojata ha jab program exit bhi hojai to ya har hal ma exeute hoga")