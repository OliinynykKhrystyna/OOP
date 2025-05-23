from math import pi



class Shape:

    def __init__(self, color="Black"):

        self._color = color  

    

    def get_color(self):

        return self._color

    

    def set_color(self, color):

        self._color = color

    

    def calculate_area(self):

        raise 



class Circle(Shape):

    def __init__(self, radius, color="Black"):

        super().__init__(color)

        self._radius = radius 



    def calculate_area(self):  

        return pi * self._radius ** 2



class Rectangle(Shape):

    def __init__(self, width, height, color="Black"):

        super().__init__(color)

        self._width = width

        self._height = height

    

    def calculate_area(self):  

        return self._width * self._height



class Triangle(Shape):

    def __init__(self, base, height, color="Black"):

        super().__init__(color)

        self._base = base

        self._height = height

    

    def calculate_area(self):  

        return 0.5 * self._base * self._height



shapes = [

    Circle(5, "Red"),

    Rectangle(4, 6, "Blue"),

    Triangle(3, 7, "Green")

]



for shape in shapes:

    print(f"{shape.__class__.__name__} (колір: {shape.get_color()}) має площу {shape.calculate_area():.2f}")
