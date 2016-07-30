#***************************************************************
#
#  Author:            Breanna Plimpton
#
#  Program #:         5
#
#  File Name:         Program5.py
#
#  Course:            COSC 1336 Programming Fundamentals I 
#
#  Due Date:          06/19/2016
#
#  Instructor:        Fred Kumi 
#
#  Chapter:           Chapter #1-3
#
#  Description:
#     This program gives you a discounted amount after a certain quantity along with your savings
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
    
    CostofUnit = 99
    UnitsSold = int(input("Please enter the total units sold: "))

    if UnitsSold<=9:
        discountapplied = "0%"
        discount = 0
        TotalSavings = 0
        TotalCostAfterDiscount = UnitsSold * 99

    elif UnitsSold<=19:
        discountapplied = "20%"
        discount = (UnitsSold * 99) * .20
        TotalCostAfterDiscount = (UnitsSold * 99) - discount

    elif UnitsSold<=49:
        discountapplied = "30%"
        discount = (UnitsSold * 99) * .30
        TotalCostAfterDiscount = (UnitsSold * 99) - discount

    elif UnitsSold<=69:
        discountapplied = "35%"
        discount = (UnitsSold * 99) * .35
        TotalCostAfterDiscount = (UnitsSold * 99) - discount

    elif UnitsSold<=99:
        discountapplied = "40%"
        discount = (UnitsSold * 99) * .40
        TotalCostAfterDiscount = (UnitsSold * 99) - discount

    else:
        discountapplied = "50%"
        discount = (UnitsSold * 99) * .50
        TotalCostAfterDiscount = (UnitsSold * 99) - discount

    print("The number of units you purchased is ", UnitsSold)
    print("The discount applied to this purchase is ", discountapplied)
    print("The total savings received due to the discount is ", format(discount, '.2f'))
    print("The total cost of your purchase with your discount is ", format(TotalCostAfterDiscount, '.2f'))

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
    print('Program:  5')
    print()
    # End of userInfo


# Call functions
userInfo()
main()

# End of Program 5
