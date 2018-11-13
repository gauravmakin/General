
import time
import random 

menu = """


To begin, Please choose one of the options below:
1 - Play the Game
2 - Exit
Option: """
DogPic="""
         __.                                              
        .-".'                      .--.            _..._    
      .' .'                     .'    \       .-""  __ ""-. 
     /  /                     .'       : --..:__.-""  ""-. \
    :  :                     /         ;.d$$    sbp_.-""-:_:
    ;  :                    : ._       :P .-.   ,"TP        
    :   \                    \  T--...-; : d$b  :d$b        
     \   `.                   \  `..'    ; $ $  ;$ $        
      `.   "-.                 ).        : T$P  :T$P        
        \..---^..             /           `-'    `._`._     
       .'        "-.       .-"                     T$$$b    
      /             "-._.-"               ._        '^' ;   
     :                                    \.`.         /    
     ;                                -.   \`."-._.-'-'     
    :                                 .'\   \ \ \ \   Woof!        
    ;  ;                             /:  \   \ \ . ;  Hi! Welcome to Celebrity Dogs!       
   ;    \        ;                     ;    "-._:  ;         
  :      `.      :                     :         \/         
  ;       /"-.    ;                    :                    
 :       /    "-. :                  : ;                    
 :     .'        T-;                 ; ;        
 ;    :          ; ;                /  :        
 ;    ;          : :              .'    ;       
:    :            ;:         _..-"\     :       
:     \           : ;       /      \     ;      
;    . '.         '-;      /        ;    :      
;  \  ; :           :     :         :    '-.      
'.._L.:-'           :     ;          ;    . `. 
                     ;    :          :  \  ; :  
                     :    '-..       '.._L.:-'  
                      ;     , `.                
                      :   \  ; :                
                      '..__L.:-'


"""
print(DogPic)


category_chosen = """

Please select a category you would like to comapare and use against the computer in this round:
1 - Intelligence
2 - Exercise
3 - Friendliness
4 - Drool
"""

 

           
def cardsnumber():
    while True:
        print(("Please enter the number of cards you would like to play with"))
        global cardsnumber
        cardsnumber=int(input("Number of cards you would like to play with against the computer: "))
        time.sleep(0.5)
 
        mod = cardsnumber % 2
        if mod > 0 and cardsnumber < 4 or cardsnumber > 30:
            print("Checking")
            print("...")
            time.sleep(0.5)
            print("Please enter a number that is even and is between 4 and 30")

        elif mod > 0 and cardsnumber > 4 and cardsnumber < 30:
            print("Checking")
            print("...")
            time.sleep(0.5)
            print("Number entered is within range but please enter an even number")

        elif mod == 0 and cardsnumber < 4 or cardsnumber > 30:
            print("Checking")
            print("...")
            time.sleep(0.5)
            print(" Number entered is even but please enter a number between 4 and 30")

        else:
            return cardsnumber        
 
def dog_cards ():
    global dogs
    with open('dogs.txt') as dogs:
        dogs = dogs.read().splitlines()
        dogs = [line.split(",") for line in dogs]

    return dogs
    


def game_against_computer():
    
    playercards = cardsnumber/2
    computercards = cardsnumber/2

    while True:
        player_intelligence = random.randint(1,100) 
        player_exercise = random.randint(1,5)
        player_friendliness = random.randint(1,10)
        player_drool = random.randint(1,10)
   
        computer_intelligence = random.randint(1,100)
        computer_exercise = random.randint(1,5)
        computer_friendliness = random.randint(1,10)
        computer_drool = random.randint(1,10)
        print("Currenty you have :",playercards,"cards in your deck")
        time.sleep(1)
        print("The computer has :",computercards,"cards in their deck")
        time.sleep(1)
        print("Your dog's name is:")
        print(random.choice(dogs))
        time.sleep(0.5)
        print(" 1 - The Intelligence value is : ",player_intelligence)
        time.sleep(1)
        print(" 2 - The Exercise value is: ",player_exercise)
        time.sleep(1)
        print(" 3 - The Friendliness value is: ",player_friendliness)
        time.sleep(1)
        print(" 4 - The Drool value is: ",player_drool)
        time.sleep(1)
        category = int(input("Please Select a category that you would like to compare against the computer: \n 1 for Intelligence \n 2 for Exercise \n 3 for Friendliness \n 4 for Drool \n Please choose: "))
        time.sleep(0.5)
        
            
        if category == 1:
            print("Intelligence Value has been chosen!")
            time.sleep(0.5)
            print("Looking at the Computer's card...")
            time.sleep(1)
            print("Your intelligence value is : ", player_intelligence)
            time.sleep(0.5)
            

            print("The computer's dog was: ")
            print(random.choice(dogs))
            print(" Computer's intelligence value is : ",computer_intelligence)
            time.sleep(0.5)
            if computer_intelligence > player_intelligence:
                print("Computer wins this round!")
                time.sleep(0.5)
                playercards = playercards - 1
                computercards = computercards + 1
                time.sleep(0.5)
                dog_cards()
                y = 1
            elif computer_intelligence <= player_intelligence:               
                print("Congratulations!, you have won this round.")
                time.sleep(0.5)
                playercards = playercards + 1
                computercards = computercards - 1
                dog_cards()
                y = 1
        elif category == 2:
            print("Exercise value has been chosen!")
            print("Looking at the Computer's card...")
            time.sleep(1)
            print("Your exercise value is : ",player_exercise)
            print("The computer's dog was: ")
            print(random.choice(dogs))
            print("Computer's exercise value is : ",computer_exercise)
            time.sleep(0.5)
            
            if computer_exercise > player_exercise:                 
                print("Computer wins this round!")
                time.sleep(0.5)
                playercards = playercards - 1
                computercards = computercards + 1
                dog_cards()
                y = 1
            elif computer_exercise <= player_exercise:
                print("Congratulations!, you have won this round")
                time.sleep(0.5)
                playercards = playercards + 1
                computercards = computercards - 1
                dog_cards()
                y = 1
        elif category == 3:
            print("Friendliness value has been chosen!")
            print("Looking at the Computer's card...")
            time.sleep(1)
            print("Your friendliness value is : ",player_friendliness)
            print("The computer's dog was: ")
            print(random.choice(dogs))
            print("Computer's friendliness value is : ",computer_friendliness)
            time.sleep(0.5)
            
             
            if computer_friendliness > player_friendliness:
                print("Computer wins this round!")
                time.sleep(0.5)
                playercards = playercards- 1
                computercards = computercards + 1
                dog_cards()
                y = 1
            elif computer_friendliness <= player_friendliness:
                print("Congratulations!,you have won this round.")
                time.sleep(0.5)
                playercards = playercards + 1
                computercards = computercards - 1
                dog_cards()
                y = 1
        elif category == 4:
            print("Drool value has been chosen!")
            print("Looking at the Computer's card...")
            time.sleep(1)
            print("Your drool value is : ",player_drool)
            print("The computer's dog was: ")
            print(random.choice(dogs))
            print("Computer's drool value is : ",computer_drool)
            time.sleep(0.5)
            
            if computer_drool > player_drool:
                print("Congratulations you have won this round!")
                time.sleep(0.5)
                playercards = playercards + 1
                computercards = computercards - 1
                dog_cards()
                y = 1
            elif computer_drool <= player_drool:               
                print("Computer wins this round!")
                time.sleep(0.5)
                playercards = playercards - 1
                computercards = computercards + 1
                dog_cards()
                y = 1
        if playercards == cardsnumber:
            print("Congratulations! you have won the game!")
            time.sleep(0.5)
            print("The program is ending...")
            time.sleep(0.5)
            print("Thank you for playing")
            time.sleep(0.5)
            exit(0)
            
        elif computercards == cardsnumber:
            print(" The Computer has won the game, Try again next time!")
            time.sleep(0.5)
            print("Thank you for playing! Please come back! ")
            time.sleep(0.5)
            print("The game is closing")
            time.sleep(0.5)
            print("...")
            time.sleep(0.5)
            exit(0)
            time.sleep(0.5)



        
def menu_final():
    while True:
        userchoice = int(input(menu)) 
        if userchoice == 2:
            print("Thank you for choosing Celebrity Dogs! Come play later!")
            time.sleep(0.5)
            exit(0)
        elif userchoice == 1:
            cardsnumber()
            dog_cards()
            game_against_computer()
        else:
            print("This not a valid option, please try again !")
            time.sleep(0.5)


while True:
    menu_final()

            


