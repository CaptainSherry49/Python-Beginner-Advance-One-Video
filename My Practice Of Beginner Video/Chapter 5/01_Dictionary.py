Simple_Dictionary = {"Fast":"Quick",
        "Applause":"Cheer",
        "Crystal":"Rare Shiny Stone",
        "Flat":"A straight Line",
        "List_Mark":[1,2,3,4,5]
}
# we can strore any type of data in Dictionary like String, Integer, List, or another Dictionary

# Accessing Dictionary's Value using keys
print(Simple_Dictionary["Crystal"])
print(Simple_Dictionary["List_Mark"])

# Changing Dictionary Values
Simple_Dictionary["List_Mark"] = [23,56,23,45]
print(Simple_Dictionary)