"""
Author: Tomas Dal Farra
Date: 06/10/2022
Description: Exercise 'OOP'
"""
from container import Container


my_container = Container()
my_container.generate(100)
print(f"total area: {my_container.sum_areas()}")
print(f"total perimeter: {my_container.sum_perimeters()}")
# 255^3 possible colors so probably the list with only 100 won't have any repetition
colors = my_container.count_colors()
print(f"colors {colors}")
# for i in colors:
#     if colors.get(i) > 1:
#         print(i, colors.get(i))
