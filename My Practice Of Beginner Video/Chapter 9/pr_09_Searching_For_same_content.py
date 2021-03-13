file1 = "Copy.txt"
file2 = "this.txt"

with open(file1) as f:
    a = f.read()
with open(file2) as f:
    b = f.read()

if a == b:
    print("Yes Both Files Have Same Content")
else:
    print("No! Both File HAve Not Same Content")