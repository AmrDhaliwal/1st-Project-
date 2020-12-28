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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice_1 = input('You\'re at a crossroad. Which way do you want to go? Type "left" or "right" \n').lower()
if choice_1 == "left":
    choice_2 = input('You are now at a lake. There is a island in the middle of the lake. Do you "swim" or "wait"? \n').lower()
    if choice_2 == "wait":
        choice_3 = input("You arrive on the island. A house appears on the island with three doors. Which door do you chose? red, blue, or yellow \n").lower()
        if choice_3 == "red":
            print("Room full of fire. You burn to death. GameOver")
        elif choice_3 == "yellow":
                print("Its a room full of treasure. You Win!")
        elif choice_3 == "blue":
                print("Room of mountain lions. You are eaten alive. Game Over")
        else:
            print("You chose a door that does not exist. You vanish. Game over")
    else:
        print("You are attacked and eaten by the Nessy the Lochness monster. Game over")
else:
    print("You fall into the abyss. Game Over")



