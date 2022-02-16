class Figure:
    unit = 100
    def __init__(self):
        pass
    def calculate_area(self):
        pass
    def info(self):
        pass


class Circle(Figure):
    def __init__(self, __radius):
        self.__radius=__radius
    def calculate_area(self):
        return f"{self.__radius}"
    def info(self):
        print(f"Radius: {self.__radius}\nArea: {self.calculate_area()}\n")



class Triangle(Figure):
    def __init__(self, __side_a, __side_b):
        self.side_a = __side_a
        self.side_b = __side_b
    def calculate_area(self):
        return self.side_b * self.side_a
    def info(self):
        print(f"Side(a): {self.side_a}\nSide(b):{self.side_b}\nArea:{self.calculate_area()}\n")
sd1 = Circle(2)
sd2 = Circle(6)

AS1 = Triangle(4, 5)
AS2 = Triangle(8, 4)
AS3 = Triangle(9, 1)

tr = [AS1, AS2, AS3]
cr = [sd1, sd2]


for i in tr:
    i.info()

for o in cr:
    o.info()