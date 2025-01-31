#!/usr/bin/python3

class Square:
    """Defines a square with private instance attributes 'size' and 'position'."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square with given size and position.

        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple): A tuple of 2 positive integers (x, y). Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0 or if any element in position is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size attribute.

        Ensures that size is an integer and greater than or equal to 0.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If size not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for the position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the position attribute.

        Ensures that position is a tuple of 2 positive integers.

        Args:
            value (tuple): A tuple (x, y) representing the position.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
            ValueError: If any element of position is less than 0.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
            not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character '#' and applies position for indentation."""
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__position[1]):
                print("")

            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
