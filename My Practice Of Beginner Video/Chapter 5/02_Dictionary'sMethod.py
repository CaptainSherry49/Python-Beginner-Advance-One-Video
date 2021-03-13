Dictionary = {1:"Sherry",
             "Hamza":2,
             3:"Asad",
             "Zulqarnin":4,
             5:"Furqan"
}

print(Dictionary)

# Dictionary Function

# Dictionary Items
print(Dictionary.items())

# Dictionary Keys
print(Dictionary.keys())

# Dictionary Update
var = Dictionary.update({"Me":"it's me Sherry"})
print(var)
# Dictionary Get
print(Dictionary.get(1))

# Dictionary Values
print(Dictionary.values())

# Remove Dictionary's All items
Dictionary.clear()
print(Dictionary)