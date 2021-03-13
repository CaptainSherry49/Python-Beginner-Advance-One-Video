import random


def gameWin(Computer, you):
    if Computer == you:
        return None
    elif Computer == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif Computer == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif Computer == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

print("Computer Turn : Snake(s), water(w), Gun(g)?")
randomNo  = random.randint(1,3)
print(randomNo)
if randomNo==1:
    Computer = 's'
elif randomNo==2:
    Computer = 'w'
elif randomNo==3:
    Computer = 'g'

you = input("Player's Turn : Snake(1), water(2), Gun(3)?")

a = gameWin(Computer , you)
print(f"Computer Choose {Computer}")
print(f"You Choose {you}")

if a == None:
    print("Game is Tie:")
if a:
    print("You Win")
else:
    print("You Lose")