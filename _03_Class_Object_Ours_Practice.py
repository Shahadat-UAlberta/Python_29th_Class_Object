class Person:
    # Class Attribute
    name = None
    age = None
    gender = None
    height = None

    # Constructor
    def __init__(self,
       print("----------------------")
       print(self.name)
       print(self.age)
       print(self.gender)
       print(self.height)
       print("----------------------")

hasan = Person()
hasan.name = "Hasan Mahmud"
hasan.age = 100
hasan.gender = "Male"
hasan.height = "5.9"


arafat = Person()
arafat.name = "Hasan Mahmud"
arafat.age = 80
arafat.gender = "Male"
arafat.height = "5.6"

