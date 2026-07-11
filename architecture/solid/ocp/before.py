class Rectangle:
    def __init__(self, width, height):
        self.width = width;
        self.height = height;

class Circle:
    def __init__(self, radius):
        self.radius = radius

class AreaCalculator:
    def calculate_area(self, shape):
        if isinstance(shape, Rectangle):
            return shape.width * shape.height
        elif isinstance(shape, Circle):
            return 3.14 * shape.radius ** 2
        else:
            raise ValueError("지원되지 않는 도형")
        
rectangle = Rectangle(5, 4)
circle = Circle(3)

calculator = AreaCalculator()
print(f"사각형 면적은?: {calculator.calculate_area(rectangle)}")
print(f"원 면적은?: {calculator.calculate_area(circle)}")