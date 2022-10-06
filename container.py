"""
Author: Tomas Dal Farra
Date: 06/10/2022
Description: file for shape container class
"""
from random import randint, choice
from rectangle import Rectangle
from square import Square
from circle import Circle


SHAPE_OPTIONS = (Rectangle, Square, Circle)


class Container:
    """
    Geometric shape container for rectangles, squares and circles
    """

    def __init__(self, shapes=None):
        """
        Initializer for Container
        :param shapes: list of shapes
        :type shapes: list
        """
        if shapes is None:
            self.shapes = []
        elif all(isinstance(s, SHAPE_OPTIONS) for s in shapes):
            self.shapes = shapes
        else:
            raise TypeError("Container can only contain shapes")

    def generate(self, x: int) -> None:
        """
        'randomly' generates x number of geometric shapes
        :param x: Number of shapes to create
        :return: None
        """
        if x <= 0 or not isinstance(x, int):
            raise ValueError('Not positive integer')
        for _ in range(x):
            rgb = tuple(randint(0, 255) for _ in range(3))
            new_shape = None
            shape_init = choice(SHAPE_OPTIONS)
            if shape_init == Rectangle:
                new_shape = shape_init(rgb, randint(1, 15), randint(1, 15))
            else:
                new_shape = shape_init(rgb, randint(1, 15))
            self.shapes.append(new_shape)

    def sum_areas(self) -> float:
        """
        Calculates sum of all shapes areas in shape list
        :return: Sum of areas
        """
        n = 0
        for s in self.shapes:
            n += s.get_area()
        return round(n, 2)

    def sum_perimeters(self) -> float:
        """
        Calculates sum of all perimeters in shape list
        :return: Sum of perimeters
        """
        n = 0
        for s in self.shapes:
            n += s.get_perimeter()
        return round(n, 2)

    def count_colors(self):
        """
        how many equal colors there are in shape list
        :return: dictionary where key is a color and value is
        how many shapes has that color
        """
        colors = {}
        for s in self.shapes:
            color = s.get_color()
            if color in colors:
                colors[color] += 1
            else:
                colors[color] = 1
        return colors


if __name__ == "__main__":
    _cont = Container([Square((130, 0, 0), 4), Circle((0, 3, 90), 2)])
    assert _cont.sum_areas() == _cont.sum_perimeters()          # both shape perimeters equal their areas
    _cont.generate(3)
    assert len(_cont.shapes) == 5
    assert all(isinstance(s, SHAPE_OPTIONS) for s in _cont.shapes)
    assert _cont.sum_areas() > 0 and _cont.sum_perimeters() > 0
