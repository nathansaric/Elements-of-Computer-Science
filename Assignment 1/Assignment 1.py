# NATHAN SARIC - 07/08/2019
# This program is a simulation of the word game Blink! A game in which players take turns adding a single letter to a growing word fragment,
# trying not to be the one to complete a valid English word. A player also loses if the letter they add to the growing fragment is not
# the beginning of an actual English word. 

# NOTE: I have removed the 'Challenge Mode' functionality as it is redundant in the context of this program.
#       By validating the user input and the current word fragment each round, the program replaces the need
#       for a 'Challenge Mode' by catching the error right away. 

'''
Reads a text file and returns a list of words
that contains all valid English words for the \
purpose of the game.
'''
def loadWords():
    print("Loading word list from file...")
    fileName = open("words.txt", "r")
    wordList = []
    for line in fileName:
        line.strip()
        line.lower()
        wordList.append(line)
    print(str(len(wordList)) + " English words successfully loaded.")
    return wordList

'''
Parameter is the current word fragment
and the created list of words.
The return value is true if the current
word fragment is in the list of words,
and false otherwise.
'''
wordList = loadWords()
def wordCheck(newWord, wordList):
    for line in range(len(wordList)):
        if str(newWord) in str(line):
            return True
        else :
            return False

'''
Parameter is the current word fragment
and the created list of words.
The return value is false if a word in
the list starts with the current word
fragment, and true otherwise.
'''
def fragmentCheck(newWord, wordList):
    for line in wordList:
        if line.startswith(newWord):
            return False
    return True

'''
Paramater is the user-inputted letter.
The return value is true if the letter
is a single, alphabetic character,
and false otherwise.
'''
def inputChecker(newCharacter):
    if len(newCharacter) == 1 and newCharacter.isalpha():
        return True
    else :
        return False

'''
Parameter is the round number and the
number of players.
The function determines which player
goes next using the modulo operator.
'''
def alternateTurns(roundNumber, numPlayers):
    if numPlayers == "2":
        if roundNumber%2 == 1:
            return "Player 1"
        else :
            return "Player 2"
    elif numPlayers == "3":
        if roundNumber%3 == 1:
            return "Player 1"
        elif roundNumber%3 == 2:
            return "Player 2"
        else :
            return "Player 3"

'''
Accepts a yes or no input from the user
and restarts the game if the input is Y
and ends the game if the input is N.
'''
def playAgain():
    userChoice = str(input("Would you like to play again? Y / N: "))
    while True:
        if userChoice == "Y" or userChoice == "y":
            playBlink()
        elif userChoice == "N" or userChoice == "n":
            print("Thanks for playing Nathan's Blink Game!")
            exit()
        else :
            print("The value " + userChoice + " is invalid!\nPlease try again!")
            playAgain()

'''
The main function of the program:
Accepts either a 2 or 3 as input and starts
the corresponding game.
Prompts the user for a letter and checks the
validity of the input each round.
If the input is invalid, the losing player is
printed and the user is prompted to play again. 
'''
def playBlink():
    roundNumber = 1
    newCharacter = ""
    newWord = ""
    print("Welcome to Nathan's Blink Game!")
    numPlayers = str(input("Do you want to play a 2 or 3 player game?")) 
    while numPlayers != "2" and numPlayers != "3":
        numPlayers = input("The value " + str(numPlayers) + " is invalid!\nBlink only supports 2 or 3 player games.\nPlease try again!")

    while True: 
        print("It is " + alternateTurns(roundNumber, numPlayers) + "'s turn.")
        print("The current word fragment is: " + newWord)
        newCharacter = str(input("Enter a letter: "))
        newCharacter = newCharacter.strip()
        newCharacter = newCharacter.lower()
        
        while inputChecker(newCharacter) == False :
            newCharacter = str(input("The value '" + str(newCharacter) + "' is invalid!\nPlease try again!"))
            newCharacter = newCharacter.strip()
            newCharacter = newCharacter.lower()
        newWord += newCharacter

        if len(newWord) > 3 and inputChecker(newCharacter):
            if wordCheck(newWord, wordList):
                print(newWord + " is an English word! " + alternateTurns(roundNumber, numPlayers) + " loses!")
                playAgain()
            elif fragmentCheck(newWord, wordList):
                print("No English word begins with '" + newWord + "' " + alternateTurns(roundNumber, numPlayers) + " loses!")
                playAgain()
        elif len(newWord) <= 3 and inputChecker(newCharacter):
            if fragmentCheck(newWord, wordList):
                print("No English word begins with '" + newWord + "' " + alternateTurns(roundNumber, numPlayers) + " loses!")
                playAgain()
        roundNumber += 1

playBlink()
