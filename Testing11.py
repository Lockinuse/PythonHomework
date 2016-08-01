import BeforeFinalTesting

Breed = input("What breed if your dog: ")
Name = input("What is your dogs name: " )
Age = input("How old is your dog: ")

dog = BeforeFinalTesting.Dog(Breed, Name, Age)

print("You have entered", (dog.get_Name()), "as your dogs name" )# You don't use self outside the class. dog1 is self
print("You have entered", (dog.get_Name()), "as your dogs name" )# You don't use self outside the class. dog1 is self
