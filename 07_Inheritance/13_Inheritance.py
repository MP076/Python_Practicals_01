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


class Student(Person):

    rollNum = 0
    marks = 100

    def takeClass(self):
        print("Taking class")


stud = Student('Joey', 18, 'Male', 5.9)
stud.eat()
stud.takeClass()
# Eating
# Taking class
