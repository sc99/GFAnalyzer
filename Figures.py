from enum import Enum


class Figures(Enum):
    TRIANGLE = "Triangle", 3
    SQUARE = "Square", 4
    RECTANGLE = "Rectangle", 4
    PENTAGON = "Pentagon", 5
    HEXAGON = "Hexagon", 6
    CIRCLE = "Circle", 10

    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    def __init__(self, _: str, approx_length: int = None):
        self._approx_length_ = approx_length

    def __str__(self):
        return self.value

    @property
    def approx_length(self):
        return self._approx_length_

