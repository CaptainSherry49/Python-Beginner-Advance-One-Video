with open("this.txt") as f:
    Content = f.read()

with open("Copy.txt","w") as f:
    f.write(Content)

with open("Copy.txt") as f:
    a = f.read()
    print(a)