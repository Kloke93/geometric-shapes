"""
Author: Tomas Dal Farra
Date: 06/10/2022
Description: File for 'Circle' class
"""
from shape import Shape
from turtle import Turtle, Screen


PI = 3.14159


class Circle(Shape):
    """
    This class represents a circle with all 'Shape' methods
    *Shape is an abstract class
    Every circle has a
    """
    def __init__(self, rgb: tuple, radius: float):
        """
        Initializer of Circle
        :param rgb: tuple with values red-green-blue between 0 and 255
        :param radius: radius of the circle instance
        """
        super().__init__(rgb)
        self.radius = radius

    def get_radius(self) -> float:
        """
        Gets radius of the Rectangle
        :return: radius of the rectangle instance
        """
        return self.radius

    def set_radius(self, radius: float):
        """
        Sets radius of the Rectangle
        :return: None
        """
        self.radius = radius

    def get_area(self) -> float:
        """
        Calculates circle area (π * r^2)
        :return: returns instance circle area
        """
        return round((self.radius**2) * PI, 2)

    def get_perimeter(self):
        """
        Calculates circle perimeter (2 * π * r)
        :return: returns instance circle perimeter
        """
        return round(2 * PI * self.radius, 2)

    def draw(self):
        """
        Draws the Circle to screen; units are scaled from 1 to 18 pixels
        """
        screen = Screen()
        screen.colormode(255)
        t = Turtle(visible=False)
        t.fillcolor(self.rgb)
        t.speed(0)
        radius = self.radius * 18
        screen.tracer(0)
        t.penup()
        t.goto(0, -radius)
        t.pendown()
        t.begin_fill()
        t.circle(radius)
        t.end_fill()
        screen.update()
        screen.mainloop()


if __name__ == "__main__":
    _rgb = (212, 43, 89)
    _circle1 = Circle(_rgb, 3)
    assert _circle1.get_radius() == 3
    _circle1.set_radius(2)
    assert _circle1.get_area() == _circle1.get_perimeter()
