import math

def num_1():
    print("Второй пункт")
    a = input()
    match a:
        case "Треугольник":
            print("OK")
            print("Введите основание и высоту")
            b = int(input())
            c = int(input())
            d = 0.5 * b * c
            e = {'a': a, 'b': d}
            print(e)
        case "Прямоугольник":
            print("OK")
            print("Введите длины сторон")
            b = int(input())
            c = int(input())
            d = b * c
            e = {'a': a, 'b': d}
            print(e)
        case "Круг":
            print("OK")
            print("Введите радиус")
            b = int(input())
            c = math.pi * (b ** 2)
            d = {'a': a, 'b': c}
            print(d)
        case _:
            print("Not Found")


def num_2():
    print("Третий пункт")
    print("Введите первое число")
    a = int(input())
    f = True
    while f:
        f = False
        print("Применяется ли модуль к числу? Y-Да. N-Нет")
        e = input()
        match e:
            case "Y":
                print("OK")
                a = abs(a)
            case "N":
                print("OK")
            case _:
                print("Not Found")
                f = True
    print("Введите второе число")
    b = int(input())
    f = True
    while f:
        f = False
        print("Применяется ли модуль к числу? Y-Да. N-Нет")
        e = input()
        match e:
            case "Y":
                print("OK")
                a = abs(a)
            case "N":
                print("OK")
            case _:
                print("Not Found")
                f = True
    f = True
    d = 0
    while f:
        f = False
        print("Выберите операцию. +, -, /, //, *, ** - возведение в степень")
        c = input()
        match c:
            case "+":
                print("OK")
                d = a + b
            case "-":
                print("OK")
                d = a - b
            case "/":
                print("OK")
                d = a / b
            case "//":
                print("OK")
                d = a // b
            case "*":
                print("OK")
                d = a * b
            case "**":
                print("OK")
                d = a ** b
            case _:
                print("Not Found")
                f = True
    print(d)


def num_3():
    print("Четвёртый пункт")
    print("Введите a, b, c")
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    d = (p * (p - a) * (p - b) * (p - c))
    print(math.sqrt(d))


if __name__ == '__main__':
    num_3()
