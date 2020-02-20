# 1.
# class Shape:
#     width = 0
#     height = 0
#
#     def area(self):
#         print("Parent class Area")
#
#
# class Rectangle(Shape):
#
#     def __init__(self, w, h):
#         self.width = w
#         self.height = h
#
#
# rect = Rectangle(10, 20)
# rect.area()
# O/p:
# Parent class Area


class Shape:
    width = 0
    height = 0

    def area(self):
        print("Parent class Area")


class Rectangle(Shape):

    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        print("Area of Rectangle:", self.width * self.height)


class Triangle(Shape):

    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        print("Area of Triangle:", (self.width * self.height) / 2)


rect = Rectangle(10, 20)
rect.area()
tri = Triangle(2, 10)
tri.area()
# O/p:
# Area of Rectangle: 200
# Area of Triangle: 10.0
