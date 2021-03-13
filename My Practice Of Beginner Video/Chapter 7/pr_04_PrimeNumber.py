# Prime Number
# A number which is only divided by itself is called Prime Number

num = int(input("Enter the number:\n"))
prime = True
for i in range(2,num):
    if(num%i==0):
        prime = False
        break 
    
if prime:
    print(f"Yes {num} is a Prime number")
else:
    print(f"No! {num} is not the prime number") 