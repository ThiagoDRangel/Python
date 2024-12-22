class Rectangle:
    def __init__(self, base: int, height: int) -> None:
        self.base = base
        self.height = height
    
    def calc_area(self) -> int:
        area = (self.base * self.height)
        return area

    def calc_perimetro(self):
        perimetro = 2 * (self.base + self.height)
        return perimetro

rectangle = Rectangle(5, 10)
print("Área:", rectangle.calc_area())
print("Perímetro:", rectangle.calc_perimetro())


