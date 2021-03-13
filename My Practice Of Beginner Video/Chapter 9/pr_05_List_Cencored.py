words = ["ass","Abuse","kadu","Mote"]

with open("new_replace.txt") as f:
    Content = f.read()

for word in words:
    Content = Content.replace(word,"#$@$%")
    with open("new_replace.txt","w") as f:
        f.write(Content)

