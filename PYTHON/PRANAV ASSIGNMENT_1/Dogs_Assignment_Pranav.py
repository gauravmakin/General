from random import randint

def menu():     # This function is for the menu, which displays the 2 possible options for the user to play or quit. 
    print("Welcome to Celebrity Dogs: \n 1. Play the Game \n 2. Quit") # This displays the 2 possible options for the user to choose from.
    choice = input() # I am creating a variable for the user choice, whether it is 1, 2 or some other option. It is taking the choice as an input

    if choice == "1": # The statement is looking, if the user chooses the first option and wants to play the game
        cardsnumber = int(input("Please enter the number of cards you would like to play with.\nPlease enter even number between 4 and 30:\t")) # I am creating a new variable for the cardsnumber which is being stored as an integer
        mod = cardsnumber % 2 # I am using this to check if the number entered by the user is an even number or an odd number. It will use a percentage comparison with 2.
        if ((mod == 0) and (cardsnumber < 4 or cardsnumber > 30)): # I am using this IF statement to see that if the user has entered an even number but the number is not entered in range
            print("Please enter a number that is between 4 and 30. Please execute program again") # This will tell th user to enter a number between range
            exit

        elif ((mod != 0) and (cardsnumber < 4 or cardsnumber > 30)):#This elif statement will work if the number entered is within range but is not an even number  
            print("Please enter a number that is even and is between 4 and 30. Please execute program again") # This will now tell the user that the number entered is within range but is not an even number and the user needs an even number
            exit
        else:  #This else statement will work if the number entered is an even number and is within range
            print("Number is even and is within the limits, Starting Game...") #This will tell the user that the number is entered is completely valid and now the cards are about to generate      
            return cardsnumber
        
    elif choice == "2":
        print ("You are now exiting the program, Thanks for playing!")
        exit

    else:
        print("This is not a valid option, Please execute program again.")
        exit


def read_file():                        # Function to read file
    f = open('dogs.txt','r')
    dogs = f.read().splitlines()
    f.close()
    return dogs

def check_number(cardsnumber):
    mod = cardsnumber % 2 # I am using this to check if the number entered by the user is an even number or an odd number. It will use a percentage comparison with 2.
    if (mod or cardsnumber > 4 or cardsnumber < 30):
        return cardsnumber
    else:
        print('Goodbye')
        pass
           
def create_category_values(cardsnumber2):    # Function to randomly generate values for the 4 categories for each card
    i = 0
    category_values = []   # List to store values for each category
    cardsnumber = cardsnumber2

    while i < cardsnumber:
        temp1 = []                      # Temporary list to store random generate values for each category
        temp1.append(randint(1,5))      # Value for Exercise
        temp1.append(randint(1,100))    # Value for Intelligence
        temp1.append(randint(1,10))     # Value for Friendliness
        temp1.append(randint(1,10))     # Value for Drool
        category_values.append(temp1)   # Append random values into another list. This will give you list of lists
        i = i + 1                       # Increment so you only generate values only for the number of cards the user wants to play with

    return category_values


def create_deck(dogs, cardsnumber):     # Function to create list with 2 elements. Each element is a list of cards i.e. Item 1 are Players cards and Item 2 are computers cards
    deck = []
    deck_length = int(cardsnumber/2)
    players_deck = dogs[:deck_length]
    computers_deck = dogs[deck_length:cardsnumber]
    deck.append(players_deck)
    deck.append(computers_deck)
    return deck


def create_category_deck(category_values, cardsnumber):     # Function to create a list of 2 elements. Each element is a list of 4 random values for the categories
    deck = []
    deck_length = int(cardsnumber/2)
    players_deck = category_values[:deck_length]
    computers_deck = category_values[deck_length:cardsnumber]
    deck.append(players_deck)
    deck.append(computers_deck)
    return deck


def display_single_card(index, deck, category, category_values):    # Function to display a single card
    print('\n\tCard In Hand')
    print('\nDog: \t', deck[index])
    print('Attributes:')
    category_length = len(category)
    
    i = 0
    while i < category_length:
        print('  ', category[i], ' - \t', category_values[i])
        i = i + 1

def display_players_cards(cardsnumber, deck, category, category_values):    # Function to display all the players cards
    print('\n\nYour cards are - ')
    deck_length = int(cardsnumber/2)
    category_length = len(category)

    i = 0
    while i < deck_length:
        print('\n', i+1, 'Dog: \t', deck[i])
        print('   Attributes:')
        category_length = len(category)
        j = 0
        while j < category_length:
            print('  ', category[j], ' - \t', category_values[i][j])
            j = j + 1
        i = i + 1


def play_game(cardsnumber, deck, category, category_values):
#    return null
    # Need to display players top card here
    selected_attribute =  int(input('\n1 for Exercise.\n2 for Intelligence\n3 for Friendliness and\n4 for Drool\nEnter your Category: '))
    if selected_attribute >= 1 and selected_attribute <= 3:
        print(selected_attribute)
        players_dog = deck[0][0]
        print(players_dog)
        players_value = category_values[0][0][selected_attribute-1]
        print(players_value)

        computers_dog = deck[1][0]
        print(computers_dog)
        computers_value = category_values[1][0][selected_attribute-1]
        print(computers_value)

        if (players_value >= computers_value):
            print('Player Wins Hand')   # Player gets the card
            
            # Add computers card to list
            deck[0].append(deck[1][0])
            category_values[0].append(category_values[1][0])

            # Remove lost card from list
            deck[1].pop(0)
            category_values[1].pop(0)

            print(deck[0])
            print(category_values[0])
            print(deck[1])
            
        else:
            # Computer gets the card
            print('Computer Wins Hand')
            
            # Add players card to computers deck
            deck[1].append(deck[0][0])
            category_values[1].append(category_values[0][0])

            # Remove top card from players deck
            deck[0].pop(0)
            category_values[0].pop(0)

            print(deck[1])
            print(category_values[1])
            print(deck[0])

    elif selected_attribute == 4:         # Drool is descending order
        print(selected_attribute)
        print(selected_attribute)
        players_dog = deck[0][0]
        print(players_dog)
        players_value = category_values[0][0][selected_attribute-1]
        print(players_value)

        computers_dog = deck[1][0]
        print(computers_dog)
        computers_value = category_values[1][0][selected_attribute-1]
        print(computers_value)
        
        if (players_value <= computers_value):
            print('Player Wins Hand')   # Player gets the card

            # Add computers card to list
            deck[0].append(deck[1][0])
            category_values[0].append(category_values[1][0])

            # Remove lost card from list
            deck[1].pop(0)
            category_values[1].pop(0)

            print(deck[0])
            print(category_values[0])
            print(deck[1])
            
        else:
            # Computer gets the card
            print('Computer Wins Hand')
            
            # Add players card to computers deck
            deck[1].append(deck[0][0])
            category_values[1].append(category_values[0][0])

            # Remove top card from players deck
            deck[0].pop(0)
            category_values[0].pop(0)

            print(deck[1])
            print(category_values[1])
            print(deck[0])

    else:
        #Wrong Selection
        print('Invalid Selection. Please execute program again.')
        exit

#-----------------------------------------------------------------------#
#                    MAIN PROGRAM                                       #
#-----------------------------------------------------------------------#


cardsnumber = int(menu())

dogs = read_file()
category = ['Exercise', 'Intelligence', 'Friendliness', 'Drool']  # Pre defined categories in a list

category_values = create_category_values(cardsnumber)
print(category_values)
dogs_deck = create_deck(dogs, cardsnumber)
print(dogs_deck)
category_deck = create_category_deck(category_values, cardsnumber)
print(category_deck)
#display_players_cards(cardsnumber, dogs_deck[0], category, category_values)
while (len(dogs_deck[0]) != 0 or len(dogs_deck[1]) != 0):
    play_game(cardsnumber, dogs_deck, category, category_deck)

if len(dogs_deck[0]) == 0:
    print('Computer Wins')
else:
    print('Player Wins')

#display_single_card(0,dogs_deck[0], category, category_values[0])

#play_game()
