#********************************************************************
#
#  Author:            Breanna Plimpton
#
#  Program #:         9
#
#  File Name:         Program9.py
#
#  Course:            COSC 1336 Programming Fundamentals I 
#
#  Due Date:          07/11/16
#
#  Instructor:        Fred Kumi 
#
#  Chapter:           1 - 7
#
#  Description:
#     This program reads and displays the contents
#     of a file.
#********************************************************************

#***************************************************************
#
#  Function:     main
# 
#  Description:  The main function of the program
#
#  Parameters:   None
#
#  Returns:      Nothing 
#
#**************************************************************
def main():

    rainfallNumbers = []
    inFile = open('program9.txt', 'r')
    
    lineRead = inFile.readline()       # Read first record
    while lineRead != '':              # While there are more records
        words = lineRead.split()        # Split the records into substrings
        annualRainfall = float(words[0])
        print(format(annualRainfall, '.2f'))
        rainfallNumbers.append(annualRainfall)

        lineRead = inFile.readline()    # Read next record
       
    # Close the file.
    inFile.close() # Close file
    rainfall(rainfallNumbers)


def rainfall(rainfallNumbers):
    months = [ "January", "February", "March", "April", "May", "June", "July", "August", "September", "November", "December"]
    smallestRainfall = min(rainfallNumbers)
    smallestIndex = rainfallNumbers.index(smallestRainfall)
    smallestMonth = months[smallestIndex]
    print("The smallest rainfall is in", smallestMonth, "having", smallestRainfall)

    largestRainfall = max(rainfallNumbers)
    largestIndex = rainfallNumbers.index(largestRainfall)
    largestMonth = months[largestIndex]
    print("The largest rainfall is in,", largestMonth, "having", largestRainfall)

    totalRainfall = totalrainfall(rainfallNumbers)

    average = calculationsRainfall(rainfallNumbers, totalRainfall)
    print("The average rainfall for this year is", format(average, '.2f'))

    # i=0
    # for month in months:
        # print(month, ":", rainfallNumbers[i])
        # i+=1


def totalrainfall(rainfallNumbers):
    totalRainfall = 0
    for totalvalue in rainfallNumbers:
        totalRainfall += totalvalue
    print("The total rainfall for this year is", format(totalRainfall, '.2f'))
    return totalRainfall


def calculationsRainfall(rainfallNumbers, totalRainfall):
    averageRainfall = totalRainfall / len(rainfallNumbers)
    return averageRainfall


#***************************************************************
#
#  Function:     userInfo
# 
#  Description:  Prints Programmer's information
#
#  Parameters:   None
#
#  Returns:      Nothing 
#
#**************************************************************
def userInfo():
    print('Name:     Breanna Plimpton')
    print('Course:   Programming Fundamentals I')
    print('Program:  9')
    print()
    # End of userInfo

# Call functions.
userInfo()
main()
