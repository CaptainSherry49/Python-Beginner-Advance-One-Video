n = int(input("Enter your number:\n"))

table = [n*i for i in range(1,11)]
print(table)

with open("tables.txt","a") as f:
    f.write(str(table))