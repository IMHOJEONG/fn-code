from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width;
        self.height = height;

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class AreaCalculator:
    def calculate_area(self, shape: Shape):
        return shape.area()
        
rectangle = Rectangle(5, 4)
circle = Circle(3)

calculator = AreaCalculator()
print(f"사각형 면적은?: {calculator.calculate_area(rectangle)}")
print(f"원 면적은?: {calculator.calculate_area(circle)}")

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base;
        self.height = height;

    def area(self):
        return 0.5 * self.base * self.height
    
triangle = Triangle(6, 4)
print(f"삼각형 면적은?: {calculator.calculate_area(triangle)}")
