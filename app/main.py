import math
from typing import Union


class Vector:
<<<<<<< HEAD
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(
            self,
            other: Union[int, float, "Vector"]) -> Union[float, "Vector"]:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
=======
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(
        self,
        other: Union[int, float, "Vector"]
    ) -> Union[float, "Vector"]:
        if isinstance(other, (int, float)):
            return Vector(
                self.x * other,
                self.y * other
            )
        elif isinstance(other, Vector):
            return (
                self.x * other.x
                + self.y * other.y
            )
>>>>>>> 2625d576cfcf7892d634247c1d4b8f182ac9983f
        else:
            return NotImplemented

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple[float, float],
        end_point: tuple[float, float]
    ) -> "Vector":
        return cls(
<<<<<<< HEAD
            end_point[0] - start_point[0], end_point[1] - start_point[1]
=======
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
>>>>>>> 2625d576cfcf7892d634247c1d4b8f182ac9983f
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        dot_product = self * other
        len_self = self.get_length()
        len_other = other.get_length()
        cos_angle = dot_product / (len_self * len_other)
        angle_radians = math.acos(cos_angle)
        angle_degrees = math.degrees(angle_radians)
        return round(angle_degrees)

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)
<<<<<<< HEAD
        new_x = self.x * cos_theta - self.y * sin_theta
        new_y = self.x * sin_theta + self.y * cos_theta
=======
        new_x = (
            self.x * cos_theta - self.y * sin_theta
        )
        new_y = (
            self.x * sin_theta + self.y * cos_theta
        )
>>>>>>> 2625d576cfcf7892d634247c1d4b8f182ac9983f
        return Vector(new_x, new_y)
