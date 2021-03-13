with open("Log File.txt") as f:
    Content = f.read()

if "Python" in Content:#.lower bhi laga sakta ha
    print("Yes")
else:
    print("No")