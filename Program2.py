#***************************************************************
#
#  Author:            Breanna Plimpton
#
#  Program #:         2
#
#  File Name:         Program2.py
#
#  Course:            COSC 1336 Programming Fundamentals I 
#
#  Due Date:          06/08/2016
#
#  Instructor:        Fred Kumi 
#
#  Chapter:           Chapter #2
#
#  Description:
#     This is my second program!
#
#***************************************************************

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
    
    test1 = int(input("Enter your first test score: "))
    test2 = int(input("Enter your second test score: "))
    test3 = int(input("Enter your third test score: "))
    test4 = int(input("Enter your forth test score: "))
    test5 = int(input("Enter your fifth test score: "))

    AverageofTests = (test1 + test2 + test3 + test4 + test5) / 5

    print('average', AverageofTests)
    
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
    print('Program:  2')
    print()
    # End of userInfo


# Call functions
userInfo()
main()

# End of Program 1
