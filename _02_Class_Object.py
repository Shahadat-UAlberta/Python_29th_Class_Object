"""
1. Class
2. Object
3. Attribute

4. Constructor
5. Instance Method
"""


class Person:
    # Class Attribute
    name = None
    age = None
    gender = None
    height = None


         # Instance Method
    def getDetails(self):
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
arafat.name = "Arafat Rahman"
arafat.age = 80
arafat.gender = "Male"
arafat.height = "5.6"

hasan.getDetails()
arafat.getDetails()
