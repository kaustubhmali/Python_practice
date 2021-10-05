class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __add__(self, other):
        return Shape(self.width + other.width, self.height + other.height)

    def __lt__(self, other):
        return self.area() < other.area()
    

s1 = Shape(2, 3)
s2 = Shape(4, 2)
total_dimensions = s1 + s2
total_area = total_dimensions.area()
print(total_area)
print(s1 > s2)