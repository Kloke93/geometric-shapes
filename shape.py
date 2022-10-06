"""
Author: Tomas Dal Farra
Date: 06/10/2022
Description: File for 'Shape' abstract class
"""
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract class to define general shape methods; get and set color, also get area and surface
    """

    @abstractmethod
    def __init__(self, rgb: tuple):
        """
        abstract initializer just for the color of the shape
        :param rgb: tuple with values red-green-blue between 0 and 255
        """
        self.rgb = (0, 0, 0)            # Immediately updated in set_color
        self.set_color(rgb)

    def set_color(self, rgb: tuple):
        """
        Sets red-green-blue color to new values
        :param rgb: tuple with values red-green-blue between 0 and 255
        :return: None
        """
        if any((n > 255 or n < 0) for n in rgb) or (len(rgb) != 3):
            raise ValueError("Not RGB values")
        self.rgb = rgb

    def get_color(self) -> tuple:
        """
        Gets self.rgb from instance
        """
        return self.rgb

    @abstractmethod
    def get_area(self):
        """
        Abstract method to get shape's area
        """
        pass

    @abstractmethod
    def get_perimeter(self):
        """
        Abstract method to get shape's perimeter
        """
        pass

    @abstractmethod
    def draw(self):
        """
        Abstract method to draw shape to screen
        """
        pass


class _ShapeTest(Shape):
    """
    Class just to test Shape class functionalities
    """
    def __init__(self, rgb):
        super().__init__(rgb)

    def get_area(self):
        return None

    def get_perimeter(self):
        return None

    def draw(self):
        return None


if __name__ == "__main__":
    _s_test = _ShapeTest((123, 31, 87))
    assert _s_test.get_color() == (123, 31, 87)
    _s_test.set_color((12, 5, 231))
    assert _s_test.get_color() == (12, 5, 231)
