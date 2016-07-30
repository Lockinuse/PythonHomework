#********************************************************************
#
#  Author:            Elizabeth Arlene Waghalter
#
#  Program #:         8
#
#  File Name:         Program8.py
#
#  Course:            COSC 1336 Programming Fundamentals I 
#
#  Due Date:          07/06/2016
#
#  Instructor:        Fred Kumi 
#
#  Chapter:           Chapters 1-6
#
#  Description:
#  This program determines the discriminant value of coefficients A, B, and C.
#
#********************************************************************

import math
import HelpProgram8Disc
# I changed Import Disc to Import HelpProgram8Disc since I changed your file name to that

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
    
    disc = HelpProgram8Disc.quadratic(coeffA, coeffB, coeffC)
# I changed the above to match the file name along with your function name in your Disc file which is quadratic

    if disc > 0:
        root1 = (-coeffB + math.sqrt(disc))/(2*coeffA)
        # you have a instead of coeffA after the 2
        root2 = (-coeffB - math.sqrt(disc))/(2*coeffA)
        # you have a instead of coeffA after the 2
        print('There are 2 roots: ', root1, root2)

    elif disc == 0:
        root1 = (-coeffB + math.sqrt(disc))/(2*coeffA)
        # you have a instead of coeffA after the 2
        print('There is one root: ', root1)

    elif disc < 0:
        print('There are no solutions to this equation: ')

    else:
        print('The answer to your query lies elsewhere.')
                
    print('\nDiscriminant is: ', disc)

#    Disc.close() - You do not need this as you are not opening a file.
    
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
    print('Name:     Fred Kumi')
    print('Course:   Programming Fundamentals I')
    print('Program:  Eight')
    print()
    # End of userInfo

#Call functions
userInfo()
main()

# End of Program 8
