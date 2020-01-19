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


person = Person('Joey', 23, 'Male', 6.0)

person.eat()
person.walk()
print(person.name)
# O/p:
# Eating
# Walking
# Joey

person2 = Person('Chandler', 24, 'Male', 6.2)
print("Name is", person2.name)
print("Age is", person2.age)
# O/p:
# Name is Chandler
# Age is 24
