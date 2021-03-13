class Sample:
    a = "Sherry" # Class Atrribute

obj = Sample()
obj.a = "Furqan"
# Sample.a = "Furqan"  , This will change the class attribute
print(Sample.a)
print(obj.a)


# So the Answer is No because obj creates an instance object not the changing the class attributes