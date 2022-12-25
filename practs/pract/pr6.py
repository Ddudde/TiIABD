import pandas as pd
import numpy as np
import scipy.stats as sts
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('pr6/ECDCCases.csv')
colors = ['pink','white']
sns.heatmap(data.isna(), cmap=sns.color_palette(colors))
plt.show()
for column in data.columns:
    missing = np.mean(data[column].isna()*100)
    print(f"{column}:{round(missing,1)}%")
D = data.drop(['geoId','Cumulative_number_for_14_days_of_COVID-19_cases_per_100000'], axis=1)

imputer = SimpleImputer(missing_values=np.nan, strategy='median')
imputer = imputer.fit(D[['popData2019']])
D['popData2019'] = imputer.transform(D[['popData2019']])

imputer1 = SimpleImputer(missing_values=np.nan, strategy='constant', fill_value = 'other')
imputer1 = imputer1.fit(D[['countryterritoryCode']])
D['countryterritoryCode'] = imputer1.transform(D[['countryterritoryCode']])

print("Удалены два признака и заполнены столбцы:")
for column in D.columns:
    missing = np.mean(D[column].isna()*100)
    print(f"{column}:{round(missing,1)}%")

print(D.describe())
print("Вывод высокой смертности:")
filter = D['deaths'] > 3000
data_filter = D[['dateRep', 'countriesAndTerritories', 'deaths']].loc[filter]
print(data_filter)
D1=D
D1.drop_duplicates(inplace=True)

data1 = pd.read_csv('pr6/bmi.csv')
print("Критерий Шапиро-Уилка:")
north = data1.loc[data1['region'] == 'northwest']
south = data1.loc[data1['region'] == 'southwest']
res1 = sts.shapiro(north['bmi'])
res2 = sts.shapiro(south['bmi'])
print(res1, '\n', res2)

print("Критерий Бартлетта")
disp = sts.bartlett(res1,res2)
print(disp)

print("t критерий Стьюдента")
t_res = sts.ttest_ind(res1,res2)
print(t_res)

print("Хи квадрат(проверка равномерного распределения)")
d = {'Points': [1, 2, 3, 4, 5, 6],
'Полученный': [97, 98, 109, 95, 97, 104],
'Ожидаемый': [100, 100, 100, 100, 100, 100]}
data = pd.DataFrame(data=d)
data1 = sts.chisquare(data['Полученный'])
print(data1)

data = pd.DataFrame({'Женат': [89,17,11,43,22,1],
                   'Гражданский брак': [80,22,20,35,6,4],
                    'Не состоит в отношениях': [35,44,35,6,8,22]})
data.index = ['Полный рабочий день','Частичная занятость','Временно не работает','На домохозяйстве','На пенсии','Учёба']

data1 = sts.chi2_contingency(data)
print(data1)