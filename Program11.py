#***************************************************************
#
#  Author:            Breanna Plimpton
#
#  Program #:         11
#
#  File Name:         Program11.py
#
#  Course:            COSC 1336 Programming Fundamentals I 
#
#  Due Date:          07/25/2016
#
#  Instructor:        Fred Kumi 
#
#  Chapter:           1 - 9
#
#  Description:
#     This gets the winner and how many times they won in the World
# Series on certain dates
#***************************************************************

BASE_YEAR = 1903

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
    showResults(creatingYearDictionary(), creatingCounterDictionary())

# ***************************************************************
#
#  Function:     userInfo
#
#  Description:  Creates the year dictionary for the years who won the
# Wold Series
#
#  Parameters:   None
#
#  Returns:      year_dict
#
# **************************************************************
def creatingYearDictionary():
    year_dict = {}

    # Open the file for reading
    input_file = open('Program11.txt', 'r')
    lineRead = input_file.readline()

    counter = BASE_YEAR
    while lineRead != '':
        winner = lineRead.rstrip('\n')
        if counter == 1904 or counter == 1994:
            counter += 1
            year_dict[counter] = winner
            counter += 1
        else:
            year_dict[counter] = winner
            counter += 1

        lineRead = input_file.readline()

    input_file.close()
    return year_dict
#***************************************************************
#
#  Function:     userInfo
#
#  Description:  Creates the count dictionary for who won the
# World Series and how many times. It pulls the winners from a
# text file.
#
#  Parameters:   None
#
#  Returns:      count_dict
#
#**************************************************************

def creatingCounterDictionary():
    count_dict = {}

    input_file = open('Program11.txt', 'r')
    lineRead = input_file.readline()

    while lineRead != '':
        winner = lineRead.rstrip('\n')
        if winner in count_dict:
            count_dict[winner] = count_dict[winner] + 1
        else:
            count_dict[winner] = 1

        lineRead = input_file.readline()

    input_file.close()
    return count_dict
#***************************************************************
#
#  Function:     showResults
# 
#  Description:  This function displays the results the program.
#                Do not modify this function. Minus 50% if you do.
#
#  Parameters:   None
#
#  Returns:      Nothing 
#
#**************************************************************
def showResults(year_dict, count_dict):
    
    # Receive user input
    year = int(input('Enter a year in the range 1903-2015: '))

    # Print results
    if year == 1904 or year == 1994:
        print("The world series wasn't played in the year", year)
    elif year < 1903 or year > 2015:
        print('The data for the year', year, \
              'is not included in our database.')
    else:
        winner = year_dict[year]
        wins = count_dict[winner]
        print('The team that won the world series in ', \
              year, ' is the ', winner, '.', sep='')
        print('They won the world series', wins, 'times.')
        
    # End of showResults

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
    print('Program:  11')
    print()
    # End of userInfo

# Call the userInfor and the main functions.
userInfo()
main()

