import math


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # What is y!r and y!r?
    # In the __repr__ method of your Vector
    # class , the !r is used within the f-string to indicate that the values of self.x and self.y should be
    # formatted using the repr() function.It means that the values will be represented as strings using
    # their repr representations rather than their str representations.
    #
    # For example,
    # if self.x is an integer 5, then self.x!r would format it as the string '5' (using repr(5)), ensuring
    # that the result is a valid Python expression that could recreate the value.
    # {self.x!r}: Formats self.x using repr(self.x).
    # {self.y!r}: Formats self.y using repr(self.y).
    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'

    def __abs__(self):
        return math.hypot(self.x, self.y)

    # implementation of __bool__ is simple: it returns False if the
    # magnitude of the vector is zero, True otherwise.
    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
