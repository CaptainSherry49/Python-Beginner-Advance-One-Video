def Table():
    user = int(input("Enter the number for table:\n"))
    for i in range(1,11):
        multiply = (str(user) + "x" +  str(i)) + "=" + str(user*i) 
        print(multiply)

Table()
# (str(num) + "X" + str(i) + "=" + str(num * i))