# Star Pattern 2
'''
    *
   ***
  *****
'''
n = 3
for i in range(3):
    print(" " * (n-i-1),end="")
    print("*" * (2*i+1),end="")
    print(" " * (n-3-1))
