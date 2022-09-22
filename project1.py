#!/usr/bin/python3
"""This is a program made for Project1 python training course"""

#Creates a main method
def main():
   
    #Loops is to know what questions to ask next and to make sure it isnt blank
    loop = 0

    while loop < 5:
        #Ask the user for input
        print("What game should I play? ")
        game = int(input("Enter 1 for RPG, 2 for Action, 3 for RTS, 4 for Crafting: "))
    
        #First if-loop to read values
        if loop == 0:
            if game == 4:
                print(f'You selected category {game}!')
                loop = 1
            elif game == 3:
                print(f'You selected category {game}!')
                loop = 2
            elif game == 2:
                print(f'You selected category {game}!')
                loop = 3
            elif game == 1:
                print(f'You selected categegory {game}!')
                loop = 4
            else:
                print("You insert an incorrect value")
                loop = 0 

        #If loop = 1 then run this section else dont
        if loop == 1:

            #Just setting another variable
            game2 = int(input("Enter 1 for Single Player or 2 for Multiplayer: "))
            
            #Second loop for different questions
            if game2 == 1:
                print(f'You selected category {game}!')
                print("You should play Stardew Valley!")
                loop = 5 
            elif game2 == 2:
                print(f'You selected category {game}!')
                print("You should play Minecraft!")
                loop = 5
            else:
                print("You insert an incorrect value")
                loop = 1 

        #If loop = 2 then run this section else dont
        if loop == 2:

            #Just setting another variable
            game2 = int(input("Enter 1 for Single Player or 2 for Multiplayer: "))

            #Second loop for different questions
            if game2 == 1:
                print(f'You selected category {game}!')
                print("You should play Mount & Blade 2: Bannerlord!")
                loop = 5
            elif game2 == 2:
                print(f'You selected category {game}!')
                print("Starcraft 2!")
                loop = 5
            else:
                print("You insert an incorrect value")
                loop = 2

	#If loop = 3 then run this section else dont
        if loop == 3:

            #Just setting another variable
            game2 = int(input("Enter 1 for Single Player or 2 for Multiplayer: "))

            #Second loop for different questions
            if game2 == 1:
                print(f'You selected category {game}!')
                print("You should play Sekiro: Shadows Die Twice!")
                loop = 5
            elif game2 == 2:
                print(f'You selected category {game}!')
                print("You should play Chivalry 2!")
                loop = 5
            else:
                print("You insert an incorrect value")
                loop = 3

	#If loop = 4 then run this section else dont
        if loop == 4:

            #Just setting another variable
            game2 = int(input("Enter 1 for Single Player or 2 for Multiplayer: "))

            #Second loop for different questions
            if game2 == 1:
                print(f'You selected category {game}!')
                print("You should play Baldur's Gate 3!")
                loop = 5
            elif game2 == 2:
                print(f'You selected category {game}!')
                print("You should play Elden Ring!")
                loop = 5
            else:
                print("You insert an incorrect value")
                loop = 4

main()
