#***************************************************************
#
#  Author:            Breanna Plimpton
#
#  Program #:         4
#
#  File Name:         Program4.py
#
#  Course:            COSC 1336 Programming Fundamentals I 
#
#  Due Date:          06/15/2016
#
#  Instructor:        Fred Kumi 
#
#  Chapter:           Chapter #1-2
#
#  Description:
#     This program gives you the Gross Pay rate, the deductions and then the ending Net Pay rate after any deductions
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
    
    ID_number = int(input("Please enter your ID Number: "))
    HourlyPayRate = float(input("Please enter your hourly pay rate: "))
    HoursWorked = float(input("Please enter the amount of hours you worked: "))
    OvertimeHours = 0.0
    OvertimePay = 0.0

    if HoursWorked > 40:
        OvertimeHours = HoursWorked - 40
        OvertimePay = (OvertimeHours * HourlyPayRate) * 1.5
        RegularPay = HourlyPayRate * 40

    else:
        RegularPay = HourlyPayRate * HoursWorked

    GrossPay = RegularPay + OvertimePay

    if GrossPay > 500:
        Deductions = (GrossPay * 0.15) + 20

    else:
        Deductions = 20

    GrossPay = RegularPay + OvertimePay - Deductions

    print("Your Netpay is: ", format(GrossPay, '.2f'))

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
    print('Program:  4')
    print()
    # End of userInfo


# Call functions
userInfo()
main()

# End of Program 4
