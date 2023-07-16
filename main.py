import random
import time

print ("___________________________" + "\n"
    + "|                          |" + "\n"
    + "|   Double Six Dice Game   |" + "\n"
    + "|__________________________|" + "\n")

player1 = input("enter the name of the player one : ")
player2 = input("enter the name of the player two : ")
print("\n----------------------------------------\n")

counter1 = 0
counter2 = 0

print("turn of ", player1, ":\n")

while True:
    dice1 = number=random.randint(1,6)
    dice2 = number=random.randint(1,6)
    counter1 += 1
    print(player1, ":", dice1, "|", dice2 )
    time.sleep(1)
    if dice1 == 6 and dice2 == 6:
        print(player1, "have do a double six in", counter1, "try")
        break

print("\n----------------------------------------\n")
print("turn of ", player2, ":\n")

while True:
    dice1 = number=random.randint(1,6)
    dice2 = number=random.randint(1,6)
    counter2 += 1
    print(player2, ":", dice1, "|", dice2 )
    time.sleep(1)
    if dice1 == 6 and dice2 == 6:
        print(player2, "have do a double six in", counter2, "try")
        break

print("\n----------------------------------------\n")

if counter1 == counter2:
    print("Equality between", player1, "and", player2)
    print("\n----------------------------------------\n")
elif counter1 > counter2:
    print(player2, "win")
    print("\n----------------------------------------\n")
elif counter2 > counter1:
    print(player1, "win")
    print("\n----------------------------------------\n")
