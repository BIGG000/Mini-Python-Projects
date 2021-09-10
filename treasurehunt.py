print('''
  ,d                                                                       
  88                                                                       
MM88MMM 8b,dPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88       88 8b,dPPYba,  
  88    88P'   "Y8 a8P_____88 ""     `Y8 I8[    "" 88       88 88P'   "Y8  
  88    88         8PP""""""" ,adPPPPP88  `"Y8ba,  88       88 88          
  88,   88         "8b,   ,aa 88,    ,88 aa    ]8I "8a,   ,a88 88          
  "Y888 88          `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP'Y8 88          
  ''')

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
import random
print('!!! Welcome to the Treasue Hunt Advanture Game !!! \nYour Life is on YOUR CHOICES \nChoice Wisely it about the matter of life \n;)')
print('Your Mission is to Find the Treasure and cross the deadly hudles.')

def tresure_hunt():

    colors = ['red','yellow','blue']
    random_number = random.randint(0, 2)

    choice1 = input("You are on the Crossroad, So where you want to go 'LEFT' and 'RIGHT'? ").lower()

    if choice1 == 'left':
        choice2 = input("Great You Passed first Huddle\nNow you in front of the river and you have to cross it.\nThe boat is on the way(you can 'wait'), or You can 'Swim' ").lower()
        if choice2 == 'wait':
            print("Now you are on the Island and it has a Castle, to go inside the castle you have to choose between the 3 doors, Choice wisely.")
            choice3 = input("The Door 1 is 'Red', \nThe Door 2 is 'Yellow', \nand The Last Door is 'Blue'\n").lower()
            computer_picks = colors[random_number]
            if choice3 != computer_picks:
                print(f"You DIE LOSER, The Treasure is in the Door {computer_picks}")
            else:
                print("You found the treasue... Great You are now Rich")
        else:
            print("You are eaten by Crocodiles... So Badly Hurt !!!")
    else:
        print("Ohooo!!! You fall into the hole and died...")
tresure_hunt()

while True:
    answer = input('Do you want to Play Again ?\n').lower()
    if answer != 'yes':
        print("Good Bye")
        quit()
    else:
        tresure_hunt()