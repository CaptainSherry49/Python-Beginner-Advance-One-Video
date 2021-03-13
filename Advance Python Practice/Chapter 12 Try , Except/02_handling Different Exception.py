try:
    a = int(input("Enter a number:\n"))
    c = 1/a
    print(c)
except ValueError as e:
    print("Please enter right value")
except ZeroDivisionError as e:
    print("please don't divided by 0")
print("Thanks for using this code!")