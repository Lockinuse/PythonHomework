class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed

    def get_make(self):
        return self.__make

    def get_year_model(self):
        return self.__year_model


year_and_model = input("What is the year and model ")
make = input("what is the make ")

car1 = Car(year_and_model, make)

car1.accelerate()
car1.accelerate()
car1.brake()

year_and_model = input("What is the year and model ")
make = input("what is the make ")

car2 = Car(year_and_model, make)
car2.accelerate()
car2.accelerate()
car2.accelerate()


print("Car #1's information - Year and Model: %s Make: %s Current Speed: %s" % (car1.get_year_model(), car1.get_make(), car1.get_speed()))

print("Car #2's information - Year and Model: %s Make: %s Current Speed: %s" % (car2.get_year_model(), car2.get_make(), car2.get_speed()))
