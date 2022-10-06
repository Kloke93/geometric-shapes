"""
Author: Tomas Dal Farra
Date: 06/10/2022
Description: File for 'Square' class
"""
from rectangle import Rectangle


class Square(Rectangle):
    """
    This class represents a square with all 'Rectangle' attributes, because all square is also a rectangle
    Every square has side length, color, perimeter and area
    """

    def __init__(self, rgb: tuple, length: float):
        """
        Initializer for Square, that is also a rectangle
        :param rgb: tuple with values red-green-blue between 0 and 255
        :param length: side length of square
        """
        super().__init__(rgb, length, length)

    def set_length(self, length: float):
        """
        Sets side length of square
        :param length: side length
        """
        super().set_length(length)
        super().set_width(length)

    def set_width(self, length: float):
        """
        Sets width of Square (equal to length)
        :param length: side length of square
        """
        self.set_length(length)


if __name__ == "__main__":
    _black = (0, 0, 0)
    _white = (255, 255, 255)
    _sq1 = Square(_black, 6)
    assert _sq1.get_length() == _sq1.get_width()
    _sq1.set_length(2)
    _sq1.set_width(4)
    assert _sq1.get_length() == _sq1.get_width()
    assert _sq1.get_perimeter() == _sq1.get_area()
    _sq2 = Square(_white, 3)
    _sq3 = _sq1 + _sq2
    assert not isinstance(_sq3, Square)
    assert _sq3.get_area() == 25
    assert _sq3.get_color() == (127.5, 127.5, 127.5)
