import random
import numpy as np


def num_1():
    print("Первый пункт")
    f = True
    sum1 = 0
    sum2 = 0
    while f:
        print("Введите число")
        a = int(input())
        sum1 += a
        sum2 = sum2 + (a ** 2)
        print("Сумма чисел равна: " + repr(sum1))
        if sum1 == 0:
            print("Сумма квадратов чисел равна: " + repr(sum2))
            f = False


def num_2():
    print("Второй пункт")
    print("Введите число N")
    a = int(input())
    b = ""
    if a > 0:
        b = "1"
        for i in range(2, a+1):
            c = " " + repr(i)
            b += c * i
    print(b)


def num_3():
    print("Третий пункт")
    x = np.random.rand(random.randint(1, 4), random.randint(1, 4))
    print(x)
    a = []
    for i in x:
        for j in i:
            a.append(j)
    print(a)


def num_4():
    print("Четвёртый пункт")
    a = [1, 2, 3, 4, 2, 1, 3, 4, 5, 6, 5, 4, 3, 2]
    b = ['a', 'b', 'c', 'c', 'c', 'b', 'a', 'c', 'a', 'a', 'b', 'c', 'b', 'a']
    x = {'a' : 0, 'b' : 0, 'c' : 0}
    for i in range(0, len(a)):
        x[b[i]] += a[i]
    print(x)


def num_5():
    print("Пятый пункт")
    from sklearn.datasets import fetch_california_housing
    data = fetch_california_housing(as_frame=True)
    print(data)


def num_6():
    print("Шестой пункт")
    from sklearn.datasets import fetch_california_housing
    data = fetch_california_housing(as_frame=True)
    import pandas as pd
    x = pd.concat([data.frame, data.target], axis=1)
    print(x)


def num_7():
    print("Седьмой пункт")
    from sklearn.datasets import fetch_california_housing
    data = fetch_california_housing(as_frame=True)
    import pandas as pd
    x = pd.concat([data.frame, data.target], axis=1)
    x.info()


def num_8():
    print("Восьмой пункт")
    from sklearn.datasets import fetch_california_housing
    data = fetch_california_housing(as_frame=True)
    import pandas as pd
    x = pd.concat([data.frame, data.target], axis=1)
    print(x.isna().sum())


def num_9():
    print("Девятый пункт")
    from sklearn.datasets import fetch_california_housing
    data = fetch_california_housing(as_frame=True)
    import pandas as pd
    x = pd.concat([data.frame, data.target], axis=1)
    print(x.loc[(x['HouseAge'] > 50) & (x['Population'] > 2500)])


def num_10():
    print("Десятый пункт")
    from sklearn.datasets import fetch_california_housing
    data = fetch_california_housing(as_frame=True)
    import pandas as pd
    x = pd.concat([data.frame, data.target], axis=1)
    print(x['MedHouseVal'].max())
    print(x['MedHouseVal'].min())


def f(d):
    mean = d.mean()
    return mean


def num_11():
    print("Одиннадцатый пункт")
    from sklearn.datasets import fetch_california_housing
    data = fetch_california_housing(as_frame=True)
    import pandas as pd
    x = pd.concat([data.frame, data.target], axis=1)
    print(x.apply(f))


if __name__ == '__main__':
    num_3()
    num_4()
    num_5()
    num_6()
    num_7()
    num_8()
    num_9()
    num_10()
    num_11()
