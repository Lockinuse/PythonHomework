# ********************************************************************
#
#  Author:            <Your name>
#
#  Program #:         7
#
#  File Name:         Program7.py
#
#  Course:            COSC 1336 Programming Fundamentals I
#
#  Due Date:          06/29/16
#
#  Instructor:        Fred Kumi
#
#  Chapter:           Chapter 4
#
#  Description:
#
# ********************************************************************

# ***************************************************************
#
#  Function:     main
#
#  Description:  The main function of the program
#
#  Parameters:   None
#
#  Returns:      Nothing
#
# **************************************************************
def main():
    inFile = open('Program7.txt', 'r')

    lineRead = inFile.readline()
    TotalOfRaises = 0
    AmountOfRaises = 0
    TotalBeforeRaises = 0
    TotalAfterRaises = 0

    while lineRead != '':
        words = lineRead.split()

        for word in words:
            Salary = float(word)
            if Salary <= 50000.00:
                PayRaise = (Salary * 0.055)
            elif 50000.01 <= Salary <= 60000:
                PayRaise = (Salary * 0.07)
            else:
                PayRaise = (Salary * 0.04)
            print("Your current pay is this:", format(Salary, ".2f"))
            print("Your pay raise is: ", format(PayRaise, ".2f"))
            NewSalary = Salary + PayRaise
            TotalBeforeRaises = TotalBeforeRaises + Salary
            TotalAfterRaises = TotalAfterRaises + NewSalary
            TotalOfRaises = TotalOfRaises + PayRaise
            AmountOfRaises = AmountOfRaises + 1

        lineRead = inFile.readline()
    print("The total amount of all the raises is :", format(TotalOfRaises, ".2f"))
    print("The average raise is :", format(TotalOfRaises/AmountOfRaises, ".2f"))
    print("The total faculty payroll before the raise is :", format(TotalBeforeRaises, ".2f"))
    print("The total faculty payroll after the raise is :", format(TotalAfterRaises, ".2f"))

    # Close the file.
    inFile.close()


# ***************************************************************
#
#  Function:     userInfo
#
#  Description:  Prints Programmer's information
#
#  Parameters:   None
#
#  Returns:      Nothing
#
# **************************************************************
def userInfo():
    print('Name:     Fred Kumi')
    print('Course:   Programming Fundamentals I')
    print('Program:  Seven')
    print()
    # End of userInfo


# Call functions
userInfo()
main()
