#***************************************************************
#
#  Author:            Breanna Plimpton
#
#  Program #:         12
#
#  File Name:         Program12.py
#
#  Course:            COSC 1336 Programming Fundamentals I
#
#  Due Date:          08/01/2016
#
#  Instructor:        Fred Kumi
#
#  Chapter:           Chapter 1-10
#
#  Description:
#     This program returns information about the employess tax rate, net worth for the month and their information.
#
#***************************************************************
import ClassEmployee

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
    employee_name = input("What is your first and last name: ")
    while employee_name != "no":
        employee = ClassEmployee.Employee()  # making an object of the class
        hourly_rate = float(input("What is your hourly rate: "))
        hours_per_week1 = float(input("How many total hours did you work the first week of the month?: "))
        hours_per_week2 = float(input("How many total hours did you work the second week of the month?: "))
        hours_per_week3 = float(input("How many total hours did you work the third week of the month?: "))
        hours_per_week4 = float(input("How many total hours did you work the forth week of the month?: "))
        employee.set_employee_information(employee_name, hourly_rate, hours_per_week1, hours_per_week2, hours_per_week3, hours_per_week4)
        employee.get_employee_information()
        employee.get_monthly_regular_pay()
        employee.get_monthly_overtime_pay()
        employee.display_information()
        employee_name = input("What is your first and last name of the next employee or enter no to exit: ")

main()