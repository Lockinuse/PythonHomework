#********************************************************************
#
#  Author:            Breanna Plimpton
#
#  Program #:         8
#
#  File Name:         Program8.py
#
#  Course:            COSC 1336 Programming Fundamentals I 
#
#  Due Date:          07/04/16
#
#  Instructor:        Fred Kumi 
#
#  Chapter:
#
#  Description:
#     This program will find the two answers of a quadratic equation
#
#********************************************************************

import math
import Disc

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
    coeffA = int(input('Enter the coefficient A: '))
    coeffB = int(input('Enter the coefficient B: '))
    coeffC = int(input('Enter the coefficient C: '))
    
    disc = Disc.quadratic(coeffA, coeffB, coeffC)

    if disc < 0:
        print("This equation has no real solution")
    elif disc == 0:
        OnlyAnswer = (-coeffB + math.sqrt(disc)) / (2 * coeffA)
        print("This equation has one solutions: ", OnlyAnswer)
    else:
        Answer1 = (-coeffB + math.sqrt(disc)) / (2 * coeffA)
        Answer2 = (-coeffB - math.sqrt(disc)) / (2 * coeffA)
        print("This equation has two solutions: ", Answer1, " and", Answer2)

    print('\nDiscriminant is: ', disc)
    
   # End of main
   
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
    print('Program:  8')
    print()
    # End of userInfo

#Call functions
userInfo()
main()

# End of Program 8
