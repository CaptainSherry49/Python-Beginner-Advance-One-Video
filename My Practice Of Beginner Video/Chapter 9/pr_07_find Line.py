Content = True
i = 1


with open("Log File.txt") as f:
    while Content:
        Content = f.readline()
        if "Python" in Content:
            print(Content)
            print("Yes")
            print(i)
        i += 1