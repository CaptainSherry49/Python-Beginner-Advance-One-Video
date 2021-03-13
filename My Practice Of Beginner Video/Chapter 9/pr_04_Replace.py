with open("Donkey.txt") as f:
    Content = f.read()

Content = Content.replace("donkey","######")

with open("Donkey.txt","w") as f:
    f.write(Content)