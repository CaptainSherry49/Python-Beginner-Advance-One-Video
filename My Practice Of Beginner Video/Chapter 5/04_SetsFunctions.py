Set_by_me = {"First","Second","Third","Fourth","Fifth","Sixth"}

# Sets Functions

# Sets Length
print(len(Set_by_me)) # length of Set is 6

# Set Remove
Set_by_me.remove("Third")
print(Set_by_me)

# Set Pop
poped = Set_by_me.pop() #By default last element
print(poped)
print(Set_by_me)

# Set Clear
Set_by_me.clear() # It will clear the list items and return the empty list
print(Set_by_me)

# Adding Element in Set
Set_by_me.add(49)
Set_by_me.add(500)
print(Set_by_me)


# We can add tuple in Set but cannot add list and Dictionary because set is immutable


# Set's Union & Intersection (Dil nhi kiya karna ko)
