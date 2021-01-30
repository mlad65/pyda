import math
figure = input('Введите тип фигуры:\r\n').lower()
if figure == 'круг':
    r = float(input('Введите радиус круга:\r\n'))
    output = 'Площадь круга: ' + str(math.pi * r * r)
elif figure == 'треугольник':
    a = float(input('Введите длину стороны A:\r\n'))
    b = float(input('Введите длину стороны B:\r\n'))
    c = float(input('Введите длину стороны C:\r\n'))
    p = a + b + c
    output = 'Площадь треугольника: ' + str(math.sqrt(p * (p - a) * (p - b) * (p - c)))
elif figure == 'прямоугольник':
    a = float(input('Введите длину стороны A:\r\n'))
    b = float(input('Введите длину стороны A:\r\n'))
    output = 'Площадь прямоугольника: ' + str(a * b)
print(output)