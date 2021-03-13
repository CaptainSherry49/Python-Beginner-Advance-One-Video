# "renamed_by_Python.txt"
import os


with open("rename.txt") as f:
    a = f.read()

with open("renamed_by_Python.txt","w") as f:
    f.write(a)

os.remove("rename.txt")