class Employee:
    def __init__(self):
        self.__hourly_rate = 7.25
        self.__regular_hours = 0.0
        self.__overtime_hours = 0.0

    def set_employee_information(self, employee_name, hourly_rate, hours_per_week1, hours_per_week2, hours_per_week3, hours_per_week4):
        self.__employee_name = employee_name
        self.__hourly_rate = hourly_rate

        if hours_per_week1 > 40:
            self.__regular_hours += 40
            self.__overtime_hours += hours_per_week1 - 40
        else:
            self.__regular_hours += hours_per_week1

        if hours_per_week2 > 40:
            self.__regular_hours += 40
            self.__overtime_hours += hours_per_week2 - 40
        else:
            self.__regular_hours += hours_per_week2

        if hours_per_week3 > 40:
            self.__regular_hours += 40
            self.__overtime_hours += hours_per_week3 - 40
        else:
            self.__regular_hours += hours_per_week3

        if hours_per_week4 > 40:
            self.__regular_hours += 40
            self.__overtime_hours += hours_per_week4 - 40
        else:
            self.__regular_hours += hours_per_week4

    def get_employee_information(self):
        employee_information = {
            "Employee Name" : self.__employee_name,
            "Hourly Rate" : self.__hourly_rate,
            "Regular Hours" : self.__regular_hours,
            "Overtime Hours" : self.__overtime_hours
        }
        return employee_information

    def get_monthly_regular_pay(self):
        monthly_regular_pay = self.__regular_hours * self.__hourly_rate
        return monthly_regular_pay

    def get_monthly_overtime_pay(self):
        monthly_overtime_pay = self.__overtime_hours * (self.__hourly_rate * 1.5)
        return monthly_overtime_pay

    def get_monthly_gross_pay(self):
        monthly_gross_pay = self.get_monthly_regular_pay() + self.get_monthly_overtime_pay()
        return monthly_gross_pay

    def __get_monthlytax(self):
        if self.get_monthly_gross_pay() <= 2000.00:
            monthlytax = self.get_monthly_gross_pay() * .10
        elif 2000.00 < self.get_monthly_gross_pay() <= 3500.00:
            monthlytax = self.get_monthly_gross_pay() * .15
        elif 3500.00 < self.get_monthly_gross_pay() <= 6000.00:
            monthlytax = self.get_monthly_gross_pay() * .28
        elif 6000.00 < self.get_monthly_gross_pay() <= 10000.00:
            monthlytax = self.get_monthly_gross_pay() * .31
        else:
            monthlytax = self.get_monthly_gross_pay() * .36
        return monthlytax

    def __get_monthlypayaftertax(self):
        monthlypay_aftertax = self.get_monthly_gross_pay() - self.__get_monthlytax()
        return monthlypay_aftertax

    def display_information(self):
        print("The employees name is: ", self.__employee_name)
        print("The total regular hours worked is: ", self.__regular_hours)
        print("The total overtime hours worked is: ", self.__overtime_hours)
        print(self.__employee_name, "has a pay rate of:  ", format(self.__hourly_rate, ".2f"))
        print(self.__employee_name, "has a monthly regular pay this month of: ", format(self.get_monthly_regular_pay(), ".2f"))
        print(self.__employee_name, "has a monthly overtime pay this month of: ", format(self.get_monthly_overtime_pay(), ".2f"))
        print(self.__employee_name, "has a monthly gross pay of: ", format(self.get_monthly_gross_pay(), ".2f"))
        print(self.__employee_name, "has this monthly tax of: ", format(self.__get_monthlytax(), ".2f"))
        print(self.__employee_name, "has a net monthly pay of: ", format(self.__get_monthlypayaftertax(), ".2f"))





