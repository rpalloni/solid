# LSP: an interface getting a base class has to work with
# all its subclasses

# in a computer program, if S is a subtype of T,
# then objects of type T may be replaced with
# objects of type S without altering any of
# the desired properties of the program
# RULE: A subclass has everything the superclass has

class Rectangle:
    def __init__(self, width, height):
        self._height = height # private attrs
        self._width = width

    # controlled access: getWidth() and setWidth()
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f'Width: {self.width}, height: {self.height}'


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    # enforce same dimension
    @Rectangle.width.setter
    def width(self, value):
        self._width = _height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = _height = value


def use_it(rc):
    w = rc.width
    rc.height = 10  # unpleasant side effect
    expected = int(w * 10)
    print(f'Expected an area of {expected}, got {rc.area}')


rc = Rectangle(2, 3)
use_it(rc)

sq = Square(5)
use_it(sq)

# use_it() function only works with class Rectangle
# and not with subclasses -> LSP violated
