from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstract class for animals."""
    
    @abstractmethod
    def sound(self):
        """Abstract method that must be implemented by subclasses."""
        pass

class Dog(Animal):
    """Dog class that implements the sound method."""
    
    def sound(self):
        """Returns the sound of a dog."""
        return "Bark"

class Cat(Animal):
    """Cat class that implements the sound method."""
    
    def sound(self):
        """Returns the sound of a cat."""
        return "Meow"
