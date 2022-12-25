def num_1():
    print("Пункт 1")
    import pandas as pd
    data = pd.read_csv('gold_price.csv', sep=';')
    print(data)


def num_2():
    print("Пункт 2")
    import pandas as pd
    data = pd.read_csv('gold_price.csv', sep=';')
    print(data.head(), data.info())


def num_3():
    print("Пункт 3")
    import plotly.graph_objs as go
    import plotly.express as px

    data = px.data.gapminder().query("country == 'France'")
    fig = go.Figure(px.bar(data, x='year', y='pop', color='pop'))
    fig.update_traces(marker=dict(line=dict(color='black', width=2)))
    fig.update_layout(title='Диаграмма количества населения во Франции',
                      title_y=0.96,
                      title_x=0.55,
                      title_xanchor='center',
                      title_yanchor='top',
                      title_font_size=20,
                      xaxis_title='Год',
                      yaxis_title='Население',
                      xaxis_title_font_size=16,
                      xaxis_tickfont_size=14,
                      height=700,
                      width=None,
                      margin=dict(l=0, r=0, t=0, b=0))
    fig.update_xaxes(tickangle=315)
    fig.show()


def num_4():
    print("Пункт 4")
    import plotly.graph_objs as go
    import plotly.express as px

    data = px.data.gapminder().query("country == 'France'")
    fig = go.Figure(px.pie(data, values='year', names='pop', color='pop'))
    fig.update_traces(marker=dict(line=dict(color='black', width=2)))
    fig.update_layout(title='Диаграмма количества населения во Франции',
                      title_y=0.96,
                      title_x=0.2,
                      title_xanchor='center',
                      title_yanchor='top',
                      title_font_size=20,
                      xaxis_title='Год',
                      yaxis_title='Население',
                      xaxis_title_font_size=16,
                      xaxis_tickfont_size=14,
                      height=700,
                      width=None,
                      margin=dict(l=0, r=0, t=0, b=0))
    fig.update_xaxes(tickangle=315)
    fig.show()


def num_5():
    print("Пункт 5")
    import plotly.graph_objs as go
    import plotly.express as px

    data = px.data.gapminder().query("country == 'France'")
    fig = go.Figure(
        go.Scatter(x=data['year'],
                   y=data['pop'],
                   line=dict(color='crimson'),
                   marker=dict(color='white')))
    fig.update_traces(marker=dict(line=dict(color='black', width=2)))
    fig.update_xaxes(gridwidth=2, gridcolor='ivory')
    fig.update_yaxes(gridwidth=2, gridcolor='ivory')
    fig.show()


def num_6():
    print("Пункт 6")
    import matplotlib.pyplot as plt
    import plotly.express as px
    import matplotlib.ticker

    data = px.data.gapminder().query("country == 'France'")
    fig = plt.figure(figsize=(9, 7))
    ax = fig.add_subplot()
    plt.grid(True)
    plt.title('Диаграмма количества населения во Франции', fontsize=16)
    plt.xlabel('Год', fontsize=12)
    plt.ylabel('Население', fontsize=14)
    plt.plot(data['year'],
             data['pop'],
             marker='.',
             color='crimson',
             markerfacecolor='white',
             markeredgecolor='black',
             markersize=10)
    ax.patch.set_facecolor('powderblue')
    ax.yaxis.set_major_formatter(matplotlib.ticker.StrMethodFormatter('{x:,.0f}'))

    plt.show()

    data = px.data.gapminder().query("country == 'France'")
    fig = plt.figure(figsize=(6, 4))
    ax = fig.add_subplot()
    vals = data['pop'].values.tolist()
    ax.pie(vals, autopct='%.2f', shadow=True)
    ax.grid()
    plt.show()

    data = px.data.gapminder().query("country == 'France'")
    fig = plt.figure(figsize=(9, 4))
    ax = fig.add_subplot()
    x = data['year']
    y = data['pop']
    ax.bar(x, y)
    ax.yaxis.set_major_formatter(matplotlib.ticker.StrMethodFormatter('{x:,.0f}'))

    ax.grid()
    plt.show()


if __name__ == '__main__':
    num_6()
    # num_4()
    # num_5()
    # num_6()
    # num_7()
    # num_8()
    # num_9()
    # num_10()
    # num_11()
