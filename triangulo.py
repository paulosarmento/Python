import math
a = int(input("Lado A? "))
b = int(input("Lado B? "))
c = int(input("Lado C? "))
p = (a + b + c) / 2
area = math.sqrt(p * (p - a) * (p - b) * (p - c))

if a <= 0 or b <= 0 or c <= 0:
    print ("Valor invalido em um dos lados!")
elif a + b > c and a + c > b and b + c > a:

    if a == b and b == c:
        print ("Triangulo Equilatero", area)
    elif a != b and b != c and a != c:
        print ("Triangulo Escaleno", area)
    elif a == b or a == c or b == c:
        print ("Triangulo Isosceles", area)
    if a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == a ** 2 + b ** 2:
        print ("Triangulo Retangulo", area)
else:
    print ("Nao forma um Triangulo!")

