# 1.
class Person:

    def __init__(self, name, age, gender, height):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height

    def eat(self):
        print("Eating")

    def walk(self):
        print("Walking")

    def getName(self):
        return self.name

    def getAge(self):
        return self.age
