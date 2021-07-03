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
print("Your Random Number is :",random_number)