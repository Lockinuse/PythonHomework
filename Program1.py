#***************************************************************
#
#  Author:            Breanna Plimpton
#
#  Program #:         1
#
#  File Name:         Program1.py
#
#  Course:            COSC 1336 Programming Fundamentals I 
#
#  Due Date:          06/06/2016
#
#  Instructor:        Fred Kumi 
#
#  Chapter:           Chapter #2
#
#  Description:
#     This is my first program!
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
    
    amount = 32500.00
    twiceMonth = amount / 24
    biWeekly = amount / 26
    
    
    print('Annual Salary           = ', amount)
    print('When paid twice a month = ', twiceMonth)
    print('When paid bi-weekly     = ', biWeekly)
    
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
    print('Program:  1')
    print()
    # End of userInfo


# Call functions
userInfo()
main()

# End of Program 1
