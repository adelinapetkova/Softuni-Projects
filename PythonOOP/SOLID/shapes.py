from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, side, height):
        self.height = height
        self.side = side

    def area(self):
        return (self.height*self.side)/2


class AreaCalculator:
    def __init__(self, shapes):
        if not isinstance(shapes, list):
            raise AssertionError("`shapes` should be of type `list`.")
        self.shapes = shapes

    def total_area(self):
        total_sum=0
        for shape in self.shapes:
            total_sum+=shape.area()
        return total_sum


shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)
print("The total area is: ",calculator.total_area())
