import copy

class Shape:
    def __init__(self, x=0, y=0, color="black"):
        self.x = x
        self.y = y
        self.color = color

    def clone(self):
        return copy.deepcopy(self)

    def draw(self):
        print(f"Drawing shape at ({self.x}, {self.y}) with color {self.color}")

class Circle(Shape):
    def __init__(self, x=0, y=0, color="black", radius=1):
        super().__init__(x, y, color)
        self.radius = radius

    def clone(self):
        return copy.deepcopy(self)

    def draw(self):
        print(f"Drawing Circle at ({self.x}, {self.y}), radius={self.radius}, color={self.color}")

class Rectangle(Shape):
    def __init__(self, x=0, y=0, color="black", width=1, height=1):
        super().__init__(x, y, color)
        self.width = width
        self.height = height

    def clone(self):
        return copy.deepcopy(self)

    def draw(self):
        print(f"Drawing Rectangle at ({self.x}, {self.y}), size=({self.width}x{self.height}), color={self.color}")

if __name__ == "__main__":
    circle1 = Circle(10, 20, "red", radius=5)
    circle2 = circle1.clone()
    circle2.x = 30
    circle2.color = "blue"

    rect1 = Rectangle(5, 5, "green", width=10, height=20)
    rect2 = rect1.clone()
    rect2.height = 40

    print("Originals:")
    circle1.draw()
    rect1.draw()

    print("\nClones:")
    circle2.draw()
    rect2.draw()
