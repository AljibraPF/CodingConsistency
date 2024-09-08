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
    



circleshape = Circle(10)
print(f"Result Of Circle Area: {circleshape.calc_area()}")
print(f"Result of Circle Perimeter: {circleshape.calc_perimeter()}")

squareshape = Rectangle(5,5)
print(f"Result Of Circle Area: {squareshape.calc_area()}")
print(f"Result Of Circle Area: {squareshape.calc_perimeter()}")

