class Person:
    # Class Attribute
    name = None
    age = None
    gender = None
    height = None

    # Constructor
    def __init__(self, name, age, gender, height):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height

    # Instance Method
    def getDetails(self):
        print("----------------------")
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.height)
        print("----------------------")

    # Destructor
    def __del__(self):
        print("Destroying an instance of Person. Name: " + self.name)


# name = input()
# age = input()
# gender = input()
# height = input()
#
# hasan = Person(name, age, gender, height)
arafat = Person("Arafat Rahman", 80, "Male", "5.6")

# hasan.getDetails()
# arafat.getDetails()
del arafat  # Delete the Object

# print(arafat.getDetails())
