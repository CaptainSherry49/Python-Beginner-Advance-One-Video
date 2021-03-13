def Function_recursive(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n* Function_recursive(n-1)


F = Function_recursive(6)
print(F)