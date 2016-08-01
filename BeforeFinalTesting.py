class Dog:

    def __init__(self, Breed, Name, Age):
        self.Breed = Breed
        self.Name = Name
        self.Age = Age

    def get_Breed(self):
        return self.Breed

    def get_Name(self):
        return self.Name

    def get_Age(self):
        return self.Age

Breed = input("What breed if your dog: ")
Name = input("What is your dogs name: " )
Age = input("How old is your dog: ")

dog1 = Dog(Breed, Name, Age)
print("You have entered", (dog1.get_Name()))# You don't use self outside the class. dog1 is self

