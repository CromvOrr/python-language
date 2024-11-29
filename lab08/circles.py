# 8.3
from points import Point
import math


class Circle:

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("Radius must be non-negative")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):
        return f"Circle({self.pt.x}, {self.pt.y}, {self.radius})"

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):
        return math.pi * self.radius ** 2

    def move(self, x, y):
        return Circle(self.pt.x + x, self.pt.y + y, self.radius)

    def cover(self, other):
        if not isinstance(other, Circle):
            raise ValueError("Argument must be an instance of Circle")

        dist = math.sqrt((self.pt.x - other.pt.x) ** 2 + (self.pt.y - other.pt.y) ** 2)
        new_radius = max(self.radius, other.radius, (dist + self.radius + other.radius) / 2)
        if dist == 0:
            new_x, new_y = self.pt.x, self.pt.y
        else:
            new_x = self.pt.x + (other.pt.x - self.pt.x) * (new_radius - self.radius) / dist
            new_y = self.pt.y + (other.pt.y - self.pt.y) * (new_radius - self.radius) / dist

        return Circle(new_x, new_y, new_radius)

    @classmethod
    def from_points(cls, points):
        if len(points) != 3:
            raise ValueError("Exactly three points are required")

        pt1, pt2, pt3 = points
        d = 2 * (pt1.x * (pt2.y - pt3.y) + pt2.x * (pt3.y - pt1.y) + pt3.x * (pt1.y - pt2.y))
        if d == 0:
            raise ValueError("Points cannot be collinear")

        ux = ((pt1.x ** 2 + pt1.y ** 2) * (pt2.y - pt3.y) +
              (pt2.x ** 2 + pt2.y ** 2) * (pt3.y - pt1.y) +
              (pt3.x ** 2 + pt3.y ** 2) * (pt1.y - pt2.y)) / d
        uy = ((pt1.x ** 2 + pt1.y ** 2) * (pt3.x - pt2.x) +
              (pt2.x ** 2 + pt2.y ** 2) * (pt1.x - pt3.x) +
              (pt3.x ** 2 + pt3.y ** 2) * (pt2.x - pt1.x)) / d

        radius = math.sqrt((ux - pt1.x) ** 2 + (uy - pt1.y) ** 2)
        return cls(ux, uy, radius)

    @property
    def top(self):
        return self.pt.y + self.radius

    @property
    def left(self):
        return self.pt.x - self.radius

    @property
    def bottom(self):
        return self.pt.y - self.radius

    @property
    def right(self):
        return self.pt.x + self.radius

    @property
    def width(self):
        return self.radius * 2

    @property
    def height(self):
        return self.radius * 2

    @property
    def topleft(self):
        return Point(self.left, self.top)

    @property
    def bottomleft(self):
        return Point(self.left, self.bottom)

    @property
    def topright(self):
        return Point(self.right, self.top)

    @property
    def bottomright(self):
        return Point(self.right, self.bottom)
