print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right".').lower()
if choice1 == "right":
    print(" you fell in to a hole. game over")
if choice1 == "left":
    choice2 = input('you\'ve come to a lake, there is an island in the middle of the lake. '
          'type "wait"to wait for a boat. type "swim" to swim across.').lower()

    if choice2 == "wait":
        choice3 = input("you arrive at the island unharmed. there is house with 3 doors. one red,one yellow and one blue. which color do you choıce ?").lower()
        if choice3 == "red":
            print("it's a room full of fire. Game over")

        elif choice3 == "yellow":
            print("you found the treasure. You win !")

        elif choice3 == "blue":
            print("you enter a room of beasts. Game over")

        else:
            print("you choose a door that doesnt exist. Game over")


    else:
        print("you got attacked by an angry trout.Game Over")
else:
    print("you fell in to a hole. game over")

