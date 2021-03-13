def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("this is not good Sherry")

a =  increment(465)
print(a)