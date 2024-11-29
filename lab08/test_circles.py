# 8.3
import pytest
from circles import Circle
from points import Point


def test_from_points():
    c1 = Circle.from_points((Point(0, 1), Point(1, 0), Point(0, -1)))
    assert c1.pt.x == 0
    assert c1.pt.y == 0
    assert c1.radius == 1

    c2 = Circle.from_points([Point(3, 10), Point(5.5, 12.5), Point(8, 10)])
    assert c2.pt.x == 5.5
    assert c2.pt.y == 10
    assert c2.radius == 2.5

    with pytest.raises(ValueError, match="Exactly three points are required"):
        Circle.from_points((Point(1, 2), Point(3, 4)))

    with pytest.raises(ValueError, match="Points cannot be collinear"):
        Circle.from_points((Point(-1, 0), Point(0, 0), Point(1, 0)))


def test_bounding_box():
    c = Circle(0, 0, 5)
    assert c.top == 5
    assert c.left == -5
    assert c.bottom == -5
    assert c.right == 5
    assert c.width == 10
    assert c.height == 10

    assert c.topleft == Point(-5, 5)
    assert c.bottomleft == Point(-5, -5)
    assert c.topright == Point(5, 5)
    assert c.bottomright == Point(5, -5)
