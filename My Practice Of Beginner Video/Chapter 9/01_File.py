# Use Open Function to read the Content of a File!
f = open("Sample.txt",'r') # 'r' is by default 
Content = f.read()
# Content = f.read(10) # Read First 10 Character of a File
print(Content)
f.close()


# We can also use "f.readlines" to read  a file , readlines function will read the files lines by lines


# Modes of Opening a File
# 1. "r"  read 
# 2. "w"  write
# 3. "a"  append
# 4. "+"  update
