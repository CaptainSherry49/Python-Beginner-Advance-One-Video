def Greater(num1,num2,num3):
    if num1 > num2 and num3:
        print(f"{num1} is Greater")
    elif num2 > num1 and num3:
        print(f"{num2} is Greater")
    elif num3 > num1 and num2:
        print(f"{num3} is Greater")

Greater(100,49,99)