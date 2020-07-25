class Shape(object):
    def name(self):
        return 'Shape'


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def name(self):
        return 'Circle'

    def area(self):
        result = 3.14 * pow(self.radius, 2)
        return result


class Color(Circle):
    def __init__(self, color, radius):
        self.color = color
        super(Color, self).__init__(radius)

    def colors(self):
        return self.color

obj = Circle(5)
print(super(Circle, obj).name())
obj = Color('Black', 2)
print(super(Color, obj).name())
print(super(Color, obj).area())
print(obj.colors())

colored_circle = Color('Black', 2)
print(colored_circle.area())
