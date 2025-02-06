#!/usr/bin/python3

class BaseGeometry:
    """Base class with integer_validator and area methods."""

    def area(self):
        """Raises an exception for unimplemented area method."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the integer value."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry)
    """Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a rectangle with width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"
    
class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize a square with the given size."""
        self.integer_validator("size", size)
        self.__size = size

        super().__init__(size, size)

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Return the string representation of the square."""
        return f"[Square] {self.__size}/{self.__size}"
