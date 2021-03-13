with open("poems.txt") as f:
    a = f.read()
    if "Twinkle" in a:
        print("Yes this is Present")
    else:
        print("No this is not Present")