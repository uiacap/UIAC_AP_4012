from typing import List


class Triangle:
    def __init__(self, legs: List[float]):
        self.legs = sorted(legs)

    def area(self):
        p = sum(self.legs) / 2
        s = (p * (p - self.legs[0]) * (p - self.legs[1]) * (p - self.legs[2])) ** .5
        return round(s, 3)

    def get_type(self):
        if self.legs[0] == self.legs[2]:
            return 'Equilateral'
        elif (self.legs[0] ** 2 + self.legs[1] ** 2) == self.legs[2] ** 2:
            return 'Right'
        elif self.legs[1] in [self.legs[0], self.legs[2]]:
            return 'Isosceles'
        else:
            return None

legs = [float(l) for i, l in enumerate(input().split()) if i&1]

triangle = Triangle(legs)
t_area = triangle.area()
t_type = triangle.get_type()

print(t_area, ',' + t_type if t_type else '', sep='')

