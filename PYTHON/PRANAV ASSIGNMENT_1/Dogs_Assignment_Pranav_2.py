from random import randint

def menu():     # This function is for the menu, which displays the 2 possible options for the user to play or quit. 
    print("Welcome to Celebrity Dogs: \n 1. Play the Game \n 2. Quit") # This displays the 2 possible options for the user to choose from.
    choice = input() # I am creating a variable for the user choice, whether it is 1, 2 or some other option. It is taking the choice as an input

    if choice == "1": # The statement is looking, if the user chooses the first option and wants to play the game
        cardsnumber = int(input("Please enter the number of cards you would like to play with :")) # I am creating a new variable for the cardsnumber which is being stored as an integer

        mod = cardsnumber % 2 # I am using this to check if the number entered by the user is an even number or an odd number. It will use a percentage comparison with 2.
        if cardsnumber == 0 and cardsnumber < 4 or cardsnumber > 30: # I am using this IF statement to see that if the user has entered an even number but the number is not entered in range
            print("Please enter a number that is between 4 and 30") # This will tell th user to enter a number between range
            menu()  #This will return the user to the menu

        elif cardsnumber > 0 and cardsnumber < 4 or cardsnumber > 30:#This elif statement will work if the number entered is within range but is not an even number  
            print("Please enter a number that is even and is between 4 and 30") # This will now tell the user that the number entered is within range but is not an even number and the user needs an even number
            menu() #This will return the user to the menu


        else:  #This else statement will work if the number entered is an even number and is within range
            print("Number is even and is within the limits, Starting Game...") #This will tell the user that the number is entered is completely valid and now the cards are about to generate      
                  
            f = open('dogs.txt','r')
            dogs = f.read().splitlines()    # Read lines from file into a list 
            #print(f.read())
            print(dogs)
            print(type(dogs))

            category = ['Exercise', 'Intelligence','Friendliness','Drool']  # Pre defined categories in a list
            
            i = 0
            category_values = []   # List to store values for each category
            
            while i <= cardsnumber-1:
                temp1 = []                      # Temporary list to store random generate values for each category
                temp1.append(randint(1,5))      # Value for Exercise
                temp1.append(randint(1,100))    # Value for Intelligence
                temp1.append(randint(1,10))     # Value for Friendliness
                temp1.append(randint(1,10))     # Value for Drool
                category_values.append(temp1)   # Append random values into another list. This will give you list of lists
                i = i + 1                       # Increment so you only generate values only for the number of cards the user wants to play with
            print(category_values)
            print("1st Value is Exercise\n2nd value is Intelligence \n3rd Value is Friendliness \n4th Value is Drool")
            value = (input("Please choose one of the categories you would like to start with and enter 1,2,3 or 4 based on their position")
            if value in category[][]:
                  print("Thank you for choosing")
                  print("Comparing against the Computer...")
            else:
                  ("Value chosen is not valid, please try again")
            
            
            
                        


    elif choice == "2":
        print ("You are now exiting the program, Thanks for playing!")
        exit

    else:
        print("This is not a valid option, Please try again")
        menu()

menu()
    
    
