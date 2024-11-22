# 7.5
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
