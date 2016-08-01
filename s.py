class Employee:
    def __init__(self):
        self.__hourly_rate = 7.25
        self.__regular_hours = 0.0
        self.__overtime_hours = 0.0

    def set_employee_information(self, employee_name, hourly_rate, hours_per_month):
        self.employee_name = employee_name
        self.__hourly_rate = hourly_rate
        self.hours_per_month = hours_per_month

input("What is your first and last name?: ")
input("What is your hourly rate: ")
input("How many total hours did you work this month?: ")