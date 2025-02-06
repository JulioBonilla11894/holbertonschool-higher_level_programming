#!/usr/bin/env python3

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Abstract base class for all shapes."""

    @abstractmethod
    def area(self):
        """Method to calculate the perimeter of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Method to calculate the perimeter of the shape."""
        pass

class Circle(Shape):
    """Concrete Circle class."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """Concrete Rectangle class."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

def shape_into(shape):
    """Print the area and perimeter of a shape."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
