# NATHAN SARIC - 06/07/2019 

# This program analyzes three text files, each containing a speech given by a government leader,
# and returns several key information to the user including: the number of characters, sentences,
# words, unique words, the percentage of unique words, and the longest word used.
# Furthermore, the frequency of occurrence of each unique word used is saved to a new text file.

# OPTIONAL ANALYSIS: This program also outputs the top ten words of over five letters in length that occur
# most often in the speech.
# [BONUS] The most used word over 5 letters in length that occurs in all three speeches: PEOPLE (47 occurrences)

def readFile(fileName):
    """
    This function opens and reads a text file.
    """
    inFile = open(fileName, "r")
    fileContentsList = inFile.read()
    inFile.close()
    return fileContentsList
    
def cleanText(text):
    """
    This function cleans up the text file by replacing line feeds, hyphens, and double spaces with a single space
    while also converting all upper case letters to lower case letters. Furthermore, all non-alphabetic characters
    are removed, except for single spaces.
    """
    cleanString = " "
    cleanText = text.replace("\n" , " ")            # Replace line feed with single space
    cleanText2 = cleanText.replace("-" , " ")       # Replace hypen with single space
    for aChar in cleanText2 :                       # Remove non-alphabetic characters
        if aChar.isalpha() or aChar == " " :    
            cleanString = cleanString + aChar
    finalText = cleanString.lower()                 # Convert upper case letters to lower case letters
    while finalText.count("  ") > 0 :
        finalText = finalText.replace("  " , " ")   # Replace double space with single space
    return finalText

def splitText(string):
    """
    This function uses the 'split' string method to split the text into a list,
    using a single space as the delimiter.
    """
    textList = []
    textList = string.split(" ")
    return textList

def sortedList(textList):
    """
    This function alphabetically sorts the list.
    """
    filteredList = filter(None, textList)
    sortedList = sorted(filteredList)
    return sortedList

def uniqueWords(textList):
    """
    This function converts the sorted list to a set of unique words, alphabetically sorted.
    """
    uniqueWords = set(textList)
    sortedUniqueWords = sorted(uniqueWords)
    return sortedUniqueWords

def numCharacters(stuffInFile):
    """
    This function returns a list containing all the characters used in the text. 
    """
    characterList = list(stuffInFile)
    return characterList

def numSentences(stuffInFile):
    """
    This function calculates the number of sentences used in the text by summing the number of
    periods, exclamation marks, and question marks. 
    """
    period = stuffInFile.count(".")
    exclamationMark = stuffInFile.count("!")
    questionMark = stuffInFile.count("?")
    numSentences = period + exclamationMark + questionMark
    return numSentences

def uniqueWordPercentage(uniqueWordList, cleanedTextAsList):
    """
    This function calculates and returns the percentage of unique words used in the text
    by dividing the number of unique words by the total number of words. 
    """
    lengthUniqueWords = len(uniqueWordList)
    lengthAllWords = len(cleanedTextAsList)
    percentOfUnique = lengthUniqueWords / lengthAllWords * 100
    return percentOfUnique

def longestWord(uniqueWordList):
    """
    This function finds the longest unique word used in the text.
    """
    longestWord = max(uniqueWordList, key=len)      # Using the max() BIF to identify the maximum value
    return longestWord

def dictionaryList(cleanedTextAsList, uniqueWordList):
    """
    This function creates a dictionary that stores each unique word as the key,
    along with its frequency -- or number of occurrences in the text, as the value.
    """
    dictionary = {}     # This dictionary stores all unique words
    for aVal in uniqueWordList :
        lineDict = {aVal : (cleanedTextAsList.count(aVal))}
        dictionary.update(lineDict)
    return dictionary

def writeDictionary(fileName, fileContents):
    """
    This function writes the contents of the dictionary into a new text file;
    providing a 'key : value' pair on every line. The 'key : value' pairs are alphabetically sorted.
    """
    outFile = open(fileName, "w")
    sortedDict = sorted(fileContents.items())
    for key, value in sortedDict :
        outFile.write(str(key) + " " + str(value) + "\n")
    outFile.close()
    
def mostUsedWords(dictionary):
    """
    This function returns a list of tuples containing the ten most frequent words in the text,
    greater than five letters long, when supplied a dictionary.
    """
    fiveOrMoreDict = {} # This dictionary stores all unique words containing more than five letters
    for key, value in dictionary.items() :
        if len(key) > 5 :
            fiveOrMoreDict[key] = value
    # Sorts the dictionary from greatest frequency to least frequency, then returns only the first ten 'word , frequency' pairs
    topTenWords = sorted(fiveOrMoreDict.items(), key=lambda item: -item[1])[:10]
    return topTenWords

def main():
    allSpeeches = ("PMHarperBerlinWall.txt" , "PresObamaBerlinSpeech.txt" , "PresObamaInauguralAddress.txt")
    speechName = ("Harper's Berlin Speech: " , "Obama's Berlin Speech: " , "Obama's Inaugural Address: ")
    speechDict = ("PMHarperBerlinWallDict.txt" , "PresObamaBerlinSpeechDict.txt" , "PresObamaInauguralAddressDict.txt")
    # The for loop is set to iterate main three times, one for each speech
    for i in range(3):
        try:
            stuffInFile = readFile(allSpeeches[i])
        except IOError :
            print("A problem was encountered when trying to open or read the supplied file! Exiting program.")
            return
        except ValueError :
            print("The supplied file does not contain any text! Exiting program.")
            return
        # Method used to clean the text file and create a dictionary to store unique words and their frequency 
        cleanedString = cleanText(stuffInFile)
        textAsString = splitText(cleanedString)
        cleanedTextAsList = sortedList(textAsString)
        uniqueWordList = uniqueWords(cleanedTextAsList)
        dictionary = dictionaryList(cleanedTextAsList, uniqueWordList)
        # Method used to calculate the number of characters, sentences, the percentage of unique words, and the longest word used,
        # also writes the dictionary to a text file, and writes a list of tuples of the top ten words containing more than five letters
        numOfCharacters = numCharacters(stuffInFile)
        numOfSentences = numSentences(stuffInFile)
        percentUnique = uniqueWordPercentage(uniqueWordList, cleanedTextAsList)
        longWord = longestWord(uniqueWordList)
        dictFile = writeDictionary(speechDict[i], dictionary)
        wordsUsedMost = mostUsedWords(dictionary)
        # Method used to display the key information calculated above to the user as output 
        print("\n" + speechName[i])
        print(str(len(numOfCharacters)) + " characters.")
        print(str(numOfSentences) + " sentences.")
        print(str(len(cleanedTextAsList)) + " words.")
        print(str(len(uniqueWordList)) + " unique words.")
        print("{0:2.1f}% of the words are unique.".format(percentUnique))
        print("The longest word is: " + longWord)
        print("\nMost used words over 5 letters are: ")
        for word, number in wordsUsedMost :
            print(str(word) + ": " + str(number) + " times")
        print("~" * 46)

main()
