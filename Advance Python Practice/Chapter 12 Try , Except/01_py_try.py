while(True):
    print("press q to quit")
    a = input("Enter a number:\n")
    if a == "q":
        break
    try:
        a = int(a)
        if a > 87 :
            print("You entered a number greater than a")
        else:
            print("You entered a number Less than a")
    except Exception as e:
        print(f"You make an error, please recheck your Code: {e}")

print("Thanks For Playing this game.")