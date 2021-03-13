Letter = '''Dear <|NAME|>
You are Selected!
Date <|DATE|>
'''
# print(Letter)
Name = input("Enter Your Name\n")
Date = input("Enter Date\n")
Letter = Letter.replace("<|NAME|>",Name)
Letter = Letter.replace("<|DATE|>",Date)

print(Letter)