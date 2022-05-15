# NATHAN SARIC - 06/14/2019

# This program reads a file containing actual historical weather data for the city of Toronto (at Pearson Airport)
# and performs various searches and sorts on the data in order to rearrange the data chronologically.
# The program outputs key information with regards to minimum, maximum, and median values of
# temperature, rainfall, and snowfall.
# Furthermore, the calculated yearly mean temperatures are saved to a new text file to 'check' for Global Warming!

def readData(filename):
    '''Reads the weather data from the supplied filename. The function returns a list of
dictionaries, where each dictionary consists of the data for a particular month.'''
    fileIn = open(filename, 'r')
    allData = []
    line = fileIn.readline()
    while line != "":
        line = fileIn.readline().strip()
        if line != "":
            values = line.split(',')
            monthData = {}
            monthData['year'] = int(values[0])      # Key names used in dictionary.
            monthData['month'] = int(values[1])
            monthData['meanT'] = float(values[2])
            monthData['maxT'] = float(values[3])
            monthData['minT'] = float(values[4])
            monthData['rain'] = float(values[5])
            monthData['snow'] = float(values[6])
            allData.append(monthData)
    fileIn.close()
    return allData

def showSome(allData):
    '''A convenience function that prints the beginning and end portions of the supplied list.'''
    for i in range(10):
        print(allData[i])
    print("<snip>")
    for i in range(-10, 0):
        print(allData[i])

def getInt(prompt, lowLimit=None, highLimit=None):
    '''A robust function that is sure to return an int value between the two
supplied limits.'''
    numberOK = False
    while not numberOK:
        try:
            userNum = int(input(prompt))
            if lowLimit != None and userNum < lowLimit:
                print("The number must be higher than", lowLimit)
                print("Please try again.")
            elif highLimit != None and userNum > highLimit:
                print("The number must be lower than", highLimit)
                print("Please try again.")
            else:
                numberOK = True
        except ValueError:
            print("Your entry is not a valid integer, please try again.")
    return userNum

def addYearMonthKey(allData):
    '''Calculates and adds a key:value pair to each dictionary in the supplied list.
The key will be named 'yearmonth' and will have a value of (100 * year + month).'''
    for monthData in allData:
        monthData['yearmonth'] = monthData['year'] * 100 + monthData['month']

def insertionSort(allData, key):
    '''Sorts the supplied list of dictionaries in situ into increasing order
by the key name supplied.'''
    for i in range(1, len(allData)):    # Insertion sort used.
        value = allData[i]
        while i > 0 and allData[i-1][key] > value[key] :
            allData[i] = allData[i-1]
            i -= 1                      # i is decrementing.
        allData[i] = value 
        
def findRain(allData, target):
    '''Uses a binary search to locate rainfall amounts in mm from the supplied list of
dictionaries.  target is a date in the 'yearmonth' value format.  The function assumes
that the list has been sorted by increasing date.  The function will raise a ValueError
exception if the year and month in target do not exist in allData.'''
    index = 0
    length = len(allData) - 1
    while not index > length :          # Binary search used.
        mid = int(index + length) // 2
        if allData[mid]["yearmonth"] < target :
            index = mid + 1
        elif allData[mid]["yearmonth"] > target :
            length = mid - 1
        else :
            return allData[mid]["rain"]
    raise ValueError("Error: Cannot find the target {0} in allData.".format(target))

def findMax(allData, key):
    '''Returns the record from allData that has the maximum value for the supplied key.'''
    maximum = allData[0]
    for i in range(1, len(allData)) :
        if (allData[i][key] > maximum[key]) :
            maximum = allData[i]
    return maximum

def findMin(allData, key):
    '''Returns the record from allData that has the minimum value for the supplied key.'''
    minimum = allData[0]
    for i in range(1, len(allData)) :
        if (allData[i][key] < minimum[key]) :
            minimum = allData[i]
    return minimum

def getAnnualSnow(allData):
    '''This function returns a list of dictionaries which consist of the total
snowfall for every year listed in allData.  Each record will consist of
{'year' : ####, 'totalsnow' : ###.#}, where # is a number.  There will be one record per year.
It does not matter if any month records are missing, the total snowfall is still calculated, by
assuminng zero snow for the missing months.'''
    minYear = int(allData[0]["year"])
    snow = [{"year" : minYear , "totalsnow" : 0}]
    for i in range(len(allData)) :
        year = int(allData[i]["year"])
        snowIndex = year - minYear
        if len(snow) - 1 < snowIndex :
            snow.append({"year" : year , "totalsnow" : 0})
        snow[snowIndex]["totalsnow"] += float(allData[i]["snow"])
    return snow

def saveAnnualMeanTemp(allData, filename):
    '''This function calculates the mean temperatures for an entire year and saves this
data to the supplied file - one line in the file per year.
It is assumed that each year from 1938 to 2012 has 12 months.'''
    insertionSort(allData, 'yearmonth')
    
    minYear = int(allData[0]["year"])
    annualAverage = {minYear : 0}
    for i in range(len(allData)) :
        year = int(allData[i]["year"])
        index = year - minYear
        lenMean = len(annualAverage) - 1
        if lenMean < index :
            annualAverage[year - 1] = annualAverage[year - 1] / 12
            annualAverage[year] = 0
        annualAverage[year] += float(allData[i]["meanT"])

    maxYear = int(allData[len(allData) - 1]["year"])
    annualAverage[maxYear] = annualAverage[maxYear] / 12
    
    try :
        fileOut = open(filename, "w")
        for key, value in annualAverage.items() :
            fileOut.write(str(key) + " " + str(value) + "\n")
        fileOut.close()
    except OSError as message :
        print(message)
        
def main():
    # Method used to read the data file
    db = readData("TorontoWeatherData.csv") 
    print("Before sorting, as read from file:")
    showSome(db)
    addYearMonthKey(db)
    insertionSort(db, 'yearmonth')
    print("\nAfter sorting by date:")
    showSome(db)

    # Method used to test the binary search by searching for the rainfall amount for a 
    # user-supplied year and month.
    searchYear = getInt("Enter year for rainfall search: ", 1938, 2018)
    searchMonth = getInt("Enter month for rainfall search: ", 1, 12)
    searchYearMonth = 100 * searchYear + searchMonth
    try:
        rainfall = findRain(db, searchYearMonth)
        print("Rainfall was {0} mm.".format(rainfall))
    except ValueError as message:
        print(message)

    # Method used to test the findMax and findMin functions by locating some extremes.
    # These two functions return a single record which is a dictionary.
    maxR = findMax(db, 'maxT')
    print("\nHighest temperature {0} deg C, in month {1}, {2}.".format(maxR['maxT'], maxR['month'], maxR['year']))
    minR = findMin(db, 'minT')
    print("Lowest temperature {0} deg C, in month {1}, {2}.".format(minR['minT'], minR['month'], minR['year']))
    maxR = findMax(db, 'rain')
    print("Highest rainfall {0} mm, in month {1}, {2}.".format(maxR['rain'], maxR['month'], maxR['year']))
    maxR = findMax(db, 'snow')
    print("Highest snowfall {0} cm, in month {1}, {2}.".format(maxR['snow'], maxR['month'], maxR['year']))

    # Method used to test the getAnnualSnow function by locating the minimum, median, and maximum
    # values of annual snowfall.
    annualSnow = getAnnualSnow(db)      # A list of dictionaries, where each dictionary holds the year and the total snowfall for that year.
    insertionSort(annualSnow, 'totalsnow')
    minR = annualSnow[0]
    print("\nLowest annual snowfall {0} cm, in {1}.".format(minR['totalsnow'], minR['year']))
    medR = annualSnow[len(annualSnow) // 2]
    print("Median annual snowfall {0} cm.".format(medR['totalsnow']))    
    maxR = annualSnow[len(annualSnow) - 1]
    print("Highest annual snowfall {0} cm, in {1}.".format(maxR['totalsnow'], maxR['year']))
    
    # Method used to sort the data, again, by mean temperature. This is the only way to obtain the median
    # value, which is defined as the middle of a sorted set of values.
    insertionSort(db, 'meanT')
    minR = db[0]
    print("\nLowest mean temperature {0} deg C, in month {1}, {2}.".format(minR['meanT'], minR['month'], minR['year']))
    medR = db[len(db) // 2]
    print("Median mean temperature {0} deg C.".format(medR['meanT']))
    maxR = db[-1]
    print("Highest mean temperature {0} deg C, in month {1}, {2}.".format(maxR['meanT'], maxR['month'], maxR['year']))

    # Method used to check for Global Warming!
    saveAnnualMeanTemp(db, "YearMeans.txt")
    
main()
