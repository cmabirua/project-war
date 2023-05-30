import math

class Cylinder:
    pi = math.pi

    def __init__(self, height=2, radius=3):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.pi * self.radius**2 * self.height

    def surface_area(self):
        return 2 * self.pi * self.radius * (self.radius + self.height)

my_cylinder = Cylinder()
print(my_cylinder.surface_area())
print(my_cylinder.volume())


