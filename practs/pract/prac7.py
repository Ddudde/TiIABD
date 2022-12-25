import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from pandas import DataFrame

street = np.array([80,98,75,91,78])
garage = np.array([100,82,105,89,102])
day = np.array(['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница'])
np.corrcoef(street,garage)

np.corrcoef(street,garage)[0,1]

plt.grid(True)
plt.title('Диаграмма рассеяния')
plt.xlabel('Число автомобилей')
plt.ylabel('День недели')
plt.scatter(street, day,  marker = 'o', color = 'crimson')
plt.scatter(garage, day,  marker = 'x', color = 'crimson')

data = pd.read_csv('bitcoin.csv')
data

projection = 14
data['predict'] = data['close'].shift(-projection)
data

x = DataFrame(data,columns=['close'])
y = DataFrame(data, columns=['predict'])
x = np.array(x,type(float))[:-projection]
y = np.array(y,type(float))[:-projection]

regression = LinearRegression()
regression.fit(x,y)
regression.predict(x)

regression.coef_

regression.intercept_

regression.predict(data[['close']][-projection:])

regression.score(x,y)

data = pd.read_csv('housePrice.csv')

data['Area'] = pd.to_numeric(data['Area'], errors= 'coerce')
data['Price(USD)'] = pd.to_numeric(data['Price(USD)'], errors= 'coerce')
x = data['Area']
y = data['Price(USD)']

n = np.size(x) # количество точек
  
m_x = np.mean(x)  # среднее значение векторов x и y
m_y = np.mean(y)
  
SS_xy = np.sum(y*x) - n*m_y*m_x # вычисление перекрестного отклонения и отклонения около x
SS_xx = np.sum(x*x) - n*m_x*m_x
  
b_1 = SS_xy / SS_xx # вычисление коэффов регрессии
b_0 = m_y - b_1*m_x

print(f'Коэффициенты: наклон линии регрессии = {b_1}, y-перехват = {b_0}')

plt.scatter(x, y, color='m', marker='o', s=30, alpha=0.5)
y_pred = b_0 + b_1 * x  # пронозируемый вектор
plt.plot(x, y_pred, color='g')

plt.xlabel('x')
plt.ylabel('y')
plt.show()