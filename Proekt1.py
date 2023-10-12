'''
>>>
Задача: Написать функцию для определения третьей стороны, площади, периметра,
радиуса вписанной и описанной окружности
треугольника по двум сторонам и углу между ними
<<<
'''

import math
def f(a,b,x):
    x = x * math.pi / 180 # Переводим градусную меру угла в радианы
    c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(x)) # Ищем третью сторону треугольника
    s = 0.5 * a * b * math.sin(x) # Ищем площадь треугольника
    p = a + b + c # Ищем периметр треугольника
    r = 2 * s / p
    R = a*b*c / (4 * s)
    return [c, s, p, r, R]
j = False
while j== False:
    a = int(input('Первая сторона >>> '))
    if a < 0:
        print('>>> Ошибка!!! Длина не может быть отрицательной! <<<')
    else:
        j = True
j = False
while j== False:
    b = int(input('Вторая сторона >>> '))
    if b < 0:
        print('>>> Ошибка!!! Длина не может быть отрицательной! <<<')
    else:
        j = True
j = False
while j== False:
    x = int(input('Угол >>> '))
    if x < 0:
        print('>>> Ошибка!!! Угол не может быть отрицательным! <<<')
    else:
        j = True
ar = f(a,b,x)
print(' Третья сторона >>> %4.2f \n Площадь треугольника >>> %4.2f \n Периметр треугольника >>> %4.2f \n Радиус вписанной окружности >>> %4.2f \n Радиус описанной окружности >>> %4.2f' %(ar[0],ar[1],ar[2],ar[3],ar[4]))
    
