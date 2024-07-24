import math
from typing import Tuple, Union


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union["Vector", float]) -> Union[float, "Vector"]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: Tuple[float, float],
        end_point: Tuple[float, float]
    ) -> "Vector":
        x_diff = round(end_point[0] - start_point[0], 2)
        y_diff = round(end_point[1] - start_point[1], 2)
        return cls(x_diff, y_diff)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> float:
        dot_product = self * other
        length_self = self.get_length()
        length_other = other.get_length()
        cos_angle = dot_product / (length_self * length_other)
        angle = math.degrees(math.acos(cos_angle))
        return round(angle)

    def get_angle(self) -> float:
        return round(math.degrees(math.atan2(self.y, self.x)))

    def rotate(self, degrees: float) -> "Vector":
        radians = math.radians(degrees)
        x_new = self.x * math.cos(radians) - self.y * math.sin(radians)
        y_new = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(round(x_new, 2), round(y_new, 2))
