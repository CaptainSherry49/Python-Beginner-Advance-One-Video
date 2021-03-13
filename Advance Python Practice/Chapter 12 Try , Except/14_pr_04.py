a = int(input("Enter a\n"))
b = int(input("Enter b\n"))

try:
    print(a/b)
except ZeroDivisionError:
    print("Infinite")