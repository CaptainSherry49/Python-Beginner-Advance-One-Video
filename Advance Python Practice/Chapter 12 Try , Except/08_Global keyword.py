a = 54 #Global Variable
def func():
    global a
    print(f"Statement 1 {a}")
    a = 7 # Local Variable
    print(f"Statement 2 {a}")
 
func()
print(f"Statement 3 {a}")