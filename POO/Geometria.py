from abc import ABC, abstractmethod
from math import pi as PI

class Geometria:
    @abstractmethod
    def area(self):
        raise NotImplementedError

    @abstractmethod
    def perimetro(self):
        raise NotImplementedError

class Quadrado(Geometria):
    def __init__(self, lado: int):
        self.lado = lado

    def area(self):
        return self.lado * self.lado
    
    def perimetro(self):
        return 4 * self.lado

class Retangulo(Geometria):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * (self.base + self.altura)

class Circulo(Geometria):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return PI * self.raio * self.radio
    
    def perimetro(self):
        return 2 * PI * self.raio