import random
Number = random.randint(1,9)
#print(Number)
chances = 0
while chances < 5:
    guess = int(input("enter your guess:"))
    if guess == Number:
        print("Congratualations you can read minds")
        break
    chances += 1
if not chances < 5: 
    print (" Haha! You Suck!")