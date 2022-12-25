def num_1_2():
    print("Пункты 1 и 2")
    import pandas as pd
    data = pd.read_csv('insurance.csv', sep=',')
    print(data.describe())


def num_3():
    print("Пункт 3")
    import pandas as pd
    import matplotlib.pyplot as plt
    data = pd.read_csv('insurance.csv', sep=',')
    data.hist(color='green', edgecolor='black')
    plt.show()


def num_4():
    print("Пункт 4")
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    import scipy.stats as sts
    data = pd.read_csv('insurance.csv', sep=',')
    mean_bmi = np.mean(data['bmi'])
    moda_bmi = sts.mode(data['bmi'])
    med_bmi = np.median(data['bmi'])
    std_bmi = data['bmi'].std()
    raz_bmi = data['bmi'].max() - data['bmi'].min()
    q1_bmi = np.percentile(data['bmi'], 25, interpolation='midpoint')
    q3_bmi = np.percentile(data['bmi'], 75, interpolation='midpoint')
    iqr_bmi = q3_bmi - q1_bmi

    mean_charges = np.mean(data['charges'])
    moda_charges = sts.mode(data['charges'])
    med_charges = np.median(data['charges'])
    std_charges = data['charges'].std()
    raz_charges = data['charges'].max() - data['charges'].min()
    q1_charges = np.percentile(data['charges'], 25, interpolation='midpoint')
    q3_charges = np.percentile(data['charges'], 75, interpolation='midpoint')
    iqr_charges = q3_charges - q1_charges

    fig, ax = plt.subplots(2, 2, figsize=(15, 4))
    ax[0][0].hist(mean_bmi,
                  label='Среднее',
                  bins=5,
                  color='yellow',
                  edgecolor='black')
    ax[0][0].hist(med_bmi,
                  label='Медиана',
                  bins=5,
                  color='green',
                  edgecolor='black')
    ax[0][0].hist(moda_bmi[0],
                  label='Мода',
                  bins=5,
                  color='blue',
                  edgecolor='black')
    ax[0][0].legend()

    ax[0][1].hist(mean_charges, label='Среднее', color='yellow', edgecolor='black')
    ax[0][1].hist(med_charges, label='Медиана', color='green', edgecolor='black')
    ax[0][1].hist(moda_charges[0], label='Мода', color='blue', edgecolor='black')
    ax[0][1].legend()

    ax[1][0].hist(raz_bmi,
                  label='Размах',
                  bins=1,
                  color='yellow',
                  edgecolor='black')
    ax[1][0].hist(std_bmi,
                  label='Ст. отклонение',
                  bins=1,
                  color='green',
                  edgecolor='black')
    ax[1][0].hist(iqr_bmi,
                  label='Межкварт. размах',
                  bins=1,
                  color='blue',
                  edgecolor='black')
    ax[1][0].legend()

    ax[1][1].hist(raz_charges,
                  label='Размах',
                  bins=1,
                  color='yellow',
                  edgecolor='black')
    ax[1][1].hist(std_charges,
                  label='Ст. отклонение',
                  bins=1,
                  color='green',
                  edgecolor='black')
    ax[1][1].hist(iqr_charges,
                  label='Межкварт. размах',
                  bins=1,
                  color='blue',
                  edgecolor='black')
    ax[1][1].legend()
    plt.show()

    print(f'''bmi
    Среднее = {mean_bmi}
    Мода = {moda_bmi}
    Медиана = {med_bmi}
    Стандартное отклонение = {std_bmi}
    Размах = {raz_bmi}
    Межквартальный размах = {iqr_bmi}''')
    print(f'''charges
    Среднее = {mean_charges}
    Мода = {moda_charges}
    Медиана = {med_charges}
    Стандартное отклонение = {std_charges}
    Размах = {raz_charges}
    Межквартальный размах = {iqr_charges}''')


def num_5():
    print("Пункт 5")
    import pandas as pd
    import matplotlib.pyplot as plt
    data = pd.read_csv('insurance.csv', sep=',')
    fig, ax = plt.subplots(2, 2, figsize=(15, 4))
    ax[0][0].boxplot([data['age']],
                     labels=['age'])
    ax[0][1].boxplot([data['bmi']],
                     labels=['bmi'])
    ax[1][0].boxplot([data['children']],
                     labels=['children'])
    ax[1][1].boxplot([data['charges']],
                     labels=['charges'])
    plt.grid()
    plt.show()


def num_6():
    print("Пункт 6")
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    data = pd.read_csv('insurance.csv', sep=',')
    s_means = []
    for _ in range(300):
        samples = data['bmi'].sample(np.random.randint(data['bmi'].min(), data['bmi'].max()))
        s_mean = np.mean(samples)
        s_means.append(s_mean)
    data1 = pd.DataFrame(s_means)
    plt.hist(s_means, edgecolor='black')
    plt.title(f'Среднее = {float(data1.mean())}\nСтандартное отклонение = {float(data1.std())}')
    plt.show()


def num_7():
    print("Пункт 7")
    import pandas as pd
    import numpy as np
    data = pd.read_csv('insurance.csv', sep=',')
    print('bmi')
    mean_bmi = np.mean(data['bmi'])
    std_bmi = data['bmi'].std()
    mean_charges = np.mean(data['charges'])
    std_charges = data['charges'].std()
    SE = std_bmi / data['bmi'].size ** 0.5
    print(mean_bmi - 1.96 * SE, mean_bmi + 1.96 * SE)
    SE = std_bmi / data['bmi'].size ** 0.5
    print(mean_bmi - 2.58 * SE, mean_bmi + 2.58 * SE)

    print('\ncharges')
    SE = std_charges / data['charges'].size ** 0.5
    print(mean_charges - 1.96 * SE, mean_charges + 1.96 * SE)
    SE = std_charges / data['charges'].size ** 0.5
    print(mean_charges - 2.58 * SE, mean_charges + 2.58 * SE)


def num_8():
    print("Пункт 8")
    from scipy.stats import kstest
    import pandas as pd
    import matplotlib.pyplot as plt
    import statsmodels.api as sm
    data = pd.read_csv('insurance.csv', sep=',')
    figure, axes = plt.subplots(2, 2, figsize=(10, 8))
    axes[0][0].hist(data['bmi'], edgecolor='black')
    sm.qqplot(data['bmi'], line='s', ax=axes[0, 1])
    axes[1][0].hist(data['charges'], edgecolor='black')
    sm.qqplot(data['charges'], line='s', ax=axes[1, 1])
    figure.suptitle('Multiple', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()
    print(kstest(data['bmi'], 'norm'))
    print(kstest(data['charges'], 'norm'))


if __name__ == '__main__':
    num_6()
