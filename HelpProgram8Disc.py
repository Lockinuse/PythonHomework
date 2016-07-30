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
#  This module defines the discriminant and is named Disc.discriminant.
#
#********************************************************************
# This is a package/module. When you import it
def quadratic(coeffA, coeffB, coeffC):
# So, you need to have agruments in order for this file to work with your program. def quadratic(coeffA, coeffB, coeffC)
# is what you need.

#    coeffA = int(input()) You already asked for this in the main function.
#    coeffB = int(input())
#    coeffC = int(input())

    discriminant = (coeffB**2) - (4*coeffA*coeffC)
    return discriminant
#    print (discriminant) - You don't need this print statement. The return function ends the function there.
# It won't even read the print statement or the rest of the program the def userInfo: etc.
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

#So, you do not want to have the below as it will run twice as you have it in the main program already.
#You will have two Name Fred Kumi, etc in your output.
#def userInfo():
#    print('Name:     Fred Kumi')
#    print('Course:   Programming Fundamentals I')
#    print('Program:  Eight')
#    print()
    # End of userInfo

#Call functions
#userInfo()
# quadratic() This does not need to be here as it is causing the function to error out

#End of Disc module
