# Star pattern 3
'''
* * *
*   *
* * *
'''
n = 3
for i in range(3):
    print("* " * n, end="")
    print("*    " * (i-1),end="")
    print("* " * n)