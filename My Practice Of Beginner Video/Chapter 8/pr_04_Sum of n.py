# # Sum(n) = sum(n-1) + n
def recursive(n):
    if (n==1):
        return 1
    return (recursive(n-1) + n)

sum = recursive(3)
print(sum)

# def Mysum(n):
#     if (n == 1):
#         return 1
#     return n + Mysum(n-1)

# n = int(input("Enter the range whose sum you want to see:\n"))
# print(Mysum(n))