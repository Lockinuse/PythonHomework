#***************************************************************
#
#  Author:            Breanna Plimpton
#
#  Program #:         3
#
#  File Name:         Program3.py
#
#  Course:            COSC 1336 Programming Fundamentals I 
#
#  Due Date:          06/13/2016
#
#  Instructor:        Fred Kumi 
#
#  Chapter:           Chapter #3
#
#  Description:
#     This program gives the values of taxes for certain property values.
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
    
    PropertyValue = float(input("Please enter your property value: "))
    format(PropertyValue, '.2f')
 
    TaxRate = float(input("Please enter your tax rate: "))
    
    AssessedValue = (PropertyValue * 0.6)
    format(AssessedValue, '.2f')
       
    PropertyTax = ((AssessedValue / 100) * TaxRate)
    

    print("Your annual property taxes for this year is: ", format(PropertyTax, '.2f'))
    
    
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
    print('Program:  3')
    print()
    # End of userInfo


# Call functions
userInfo()
main()

# End of Program 3
