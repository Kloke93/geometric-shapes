"""
Author: Tomas Dal Farra
Date: 06/10/2022
Description: File for 'Rectangle' class
"""
from shape import Shape
from turtle import Turtle, Screen


class Rectangle(Shape):
    """
    This class represents a rectangle with all 'Shape' methods
    *Shape is an abstract class
    Every rectangle has a perimeter, an area, length, width and color
    """

    def __init__(self, rgb: tuple, length: float, width: float):
        """
        Initializer of Rectangle
        :param rgb: tuple with values red-green-blue between 0 and 255
        :param length: length of the rectangle sides horizontally
        :param width: length of the rectangle sides vertically
        """
        super().__init__(rgb)
        self.length = length
        self.width = width

    def get_length(self) -> float:
        """
        Gets length of the Rectangle
        :return: length of the rectangle instance
        """
        return self.length

    def get_width(self) -> float:
        """
        Gets width of the Rectangle
        :return: width of the rectangle instance
        """
        return self.width

    def set_length(self, length: float):
        """
        Sets length of the Rectangle
        :return: None
        """
        self.length = length

    def set_width(self, width: float):
        """
        Sets width of the Rectangle
        :return: None
        """
        self.width = width

    def get_area(self) -> float:
        """
        Gets area of rectangle by calculating (length x width)
        :return: Area of rectangle
        """
        return round(self.length * self.width, 2)

    def get_perimeter(self) -> float:
        """
        Gets perimeter of rectangle by calculating (2 x length + 2 x width)
        :return: Perimeter of rectangle
        """
        return round(2 * self.length + 2 * self.width, 2)

    def __add__(self, other_rect):
        """
        Defining a sum between two rectangles.
        It has to respect the sum between areas
        :param other_rect: another Rectangle instance
        :type other_rect: Rectangle
        :return: new Rectangle with sum of some characteristics
        :rtype: Rectangle
        """
        if not isinstance(other_rect, Rectangle):
            raise TypeError("Can only add Rectangle to another Rectangle")
        # rgb is the result of the rounded average (one decimal digit) of the sum red = red1+red2; green = ... etc
        rgb = tuple(map(lambda x, y: round((x + y) / 2, 1), self.rgb, other_rect.get_color()))
        coef = self.length / other_rect.get_length()        # coefficient for how much one length has to change
        length = round(self.length, 1)
        width = round(self.width + other_rect.get_width() / coef, 3)
        return Rectangle(rgb, length, width)

    def draw(self):
        """
        Draws the rectangle to screen; units are scaled from 1 to 25 pixels
        """
        screen = Screen()
        screen.colormode(255)
        t = Turtle(visible=False)
        t.fillcolor(self.rgb)
        t.speed(0)
        length = self.length * 25
        width = self.width * 25
        screen.tracer(0)
        t.penup()
        t.goto(-(length//2), width//2)
        t.pendown()
        t.begin_fill()
        for i in range(0, 4):
            if i % 2 == 0:
                t.forward(length)
            else:
                t.forward(width)
            t.right(90)
        t.end_fill()
        screen.update()
        screen.mainloop()


if __name__ == "__main__":
    _black = (0, 0, 0)
    _white = (255, 255, 255)
    _rect1 = Rectangle(_black, 2, 4)
    assert _rect1.get_length() == 2
    assert _rect1.get_width() == 4
    _rect1.set_length(3)
    _rect1.set_width(6)
    assert _rect1.get_length() == 3
    assert _rect1.get_width() == 6
    assert _rect1.get_area() == _rect1.get_perimeter()
    _rect2 = Rectangle(_white, 4, 5)
    _rect3 = _rect1 + _rect2
    assert _rect3.get_area() == 38
    assert _rect3.get_color() == (127.5, 127.5, 127.5)
