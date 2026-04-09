from circulo import Circulo
import triangulo

c = Circulo(2)
t = triangulo.Triangulo(2, 5)



def imprimir_area(figura):
    print(figura.area())

imprimir_area(t)
imprimir_area(c)