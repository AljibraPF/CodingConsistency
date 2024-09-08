import math

class PHShape:
    def calc_area(self):
        pass

    def calc_perimeter(self):
        pass

class Circle(PHShape):
    def __init__(self,radius) -> None:
        self.radius = radius
    
    def calc_area(self):
        return math.pi * self.radius**2
    
    def calc_perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(PHShape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def calc_area(self):
        return self.length * self.width
    
    def calc_perimeter(self):
        return 2 * (self.length + self.width)
    
class Triangle(PHShape):
    def __init__(self,base,height,s1,s2,s3):
        self.base = base
        self.height = height
        self.s1 = s1
        self.s2 = s2
        self. s3 = s3
    
    def calc_area(self):
        return 0.5 * self.base * self.height
    
    def calc_perimeter(self):
        return self.s1 + self.s2 + self.s3
    



circleshape = Circle(10)
print(f"Result Of Circle Area: {circleshape.calc_area()}")
print(f"Result of Circle Perimeter: {circleshape.calc_perimeter()}")

squareshape = Rectangle(5,5)
print(f"\nResult Of Rectangle Area: {squareshape.calc_area()}")
print(f"Result Of Rectangle Perimeter: {squareshape.calc_perimeter()}")

triangshape = Triangle(5,6,7,2,5)
print(f"\nResult Of Triangle Area: {triangshape.calc_area()}")
print(f"Result Of Triangle Perimeter: {triangshape.calc_perimeter()}")

#Practice to try and use inheritance classes



