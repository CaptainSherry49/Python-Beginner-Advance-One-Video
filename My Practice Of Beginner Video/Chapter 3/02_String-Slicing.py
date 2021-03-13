#Concatination
greeting = "Good Morning, "
name = "Sherry"
Concatination = greeting + name
print(Concatination)
#All above this is Concatination
SLicing_of_String = "This is a String Now this String will be Sliced by Sherry"
print(SLicing_of_String[0:16]) #This is Called Simple Slicing
#In ABove Code 0 is "included" but 16 in "Excluded"
print(SLicing_of_String[41:58])

#Finding Lendth of any String
print(len(SLicing_of_String)) #Current Length of a Variable String is 57

#Extended Slicing
print(SLicing_of_String[:35])
print(SLicing_of_String[0:])

#Negative Slicing
print(SLicing_of_String[-20:]) #-20 to Last Item

#Skiping Value Slicing
print(SLicing_of_String[::2]) #ab ya pori string ki slicing kara ga aik aik value skip kar ka