import math
#Some Python Calculations to ease the mind

def cylinder_surface_area(radius, height):
    lateral_area = 2 * math.pi * radius * height
    base_area = 2 * math.pi * radius ** 2
    total_area = lateral_area + base_area
    return total_area

radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))
area = cylinder_surface_area(radius, height)
print(f"The surface area of the cylinder is: {area:.2f}")
