import random

top_number = input("Enter the number: ")

if top_number.isdigit():
    top_number = int(top_number)

    if top_number <= 0:
        print("Enter a large number then 0 next time.")
        quit()
        
else:
    print("Enter the number next time")
    quit()

random_number = random.randint(0, top_number)
guesses = 0

while True:
    guesses += 1
    user_guess = input(int("Enter a Number: "))
    if user_guess == random_number:
        print("You got it correct")
        break
    elif user_guess > random_number:
        print("You are high on guess number")
    else:
        print("You are low on guess number")
print("You got the answer in ",guesses,"guesses")