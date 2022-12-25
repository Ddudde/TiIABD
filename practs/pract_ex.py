import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.cluster import DBSCAN
import plotly.graph_objects as go
from sklearn.metrics import silhouette_score
from sklearn.neighbors import NearestNeighbors
from matplotlib import pyplot as plt

data = pd.read_csv('weather-check.csv')


def getRepToNum(uni):
    rez = {}
    for i in range(len(uni)):
        rez[uni[i]] = i
    return rez


def toNum(par):
    rep = getRepToNum(pd.unique(data[par]))
    # print(rep)
    data[par].replace(rep, inplace=True)
    # print(data)


def delUndef():
    global data
    data1 = data
    for i in range(len(data.index)):
        if str(data.loc[i]).replace(" - ", "").__contains__("-"):
            data1.drop(index=[i], inplace=True)
    data = data1


if __name__ == '__main__':
    global data
    data.rename(columns={'Do you typically check a daily weather report?': 'param1'}, inplace=True)
    data.rename(columns={'How do you typically check the weather?': 'param2'}, inplace=True)
    data.rename(columns={'A specific website or app (please provide the answer)': 'param3'}, inplace=True)
    data.rename(columns={
        'If you had a smartwatch (like the soon to be released Apple Watch), how likely or unlikely would you be to check the weather on that device?': 'param4'},
        inplace=True)
    data.rename(columns={'Age': 'param5'}, inplace=True)
    data.rename(columns={'What is your gender?': 'param6'}, inplace=True)
    data.rename(columns={'How much total combined money did all members of your HOUSEHOLD earn last year?': 'param7'},
                inplace=True)
    data.rename(columns={'US Region': 'param8'}, inplace=True)
    # keys = data.keys()[1:]
    # print(str(data.loc[0]).replace(" - ", "").__contains__("-"))
    # data.drop(index=[0], inplace=True)

    # print(data)

    # print(len(data.index))
    delUndef()
    data.drop("RespondentID", axis=1, inplace=True)
    # print(data)
    keys = data.keys()
    for i in range(len(keys)):
        toNum(keys[i])

    # models = []
    # score1 = []
    # score2 = []
    # for i in range(2, 10):
    #     model = KMeans(n_clusters=i, random_state=123, init='k-means++').fit(data)
    #     models.append(model)
    #     score1.append(model.inertia_)
    #     score2.append(silhouette_score(data, model.labels_))

    # plt.grid()
    # plt.plot(np.arange(2, 10), score1, marker='o')
    # plt.show()
    # plt.grid()
    # plt.plot(np.arange(2, 10), score2, marker='o')
    # plt.show()

    neighbors = NearestNeighbors(n_neighbors=3)
    neighbors_fit = neighbors.fit(data)
    distances, indices = neighbors_fit.kneighbors(data)
    distances = np.sort(distances, axis=0)
    distances = distances[:, 1]
    plt.plot(distances)
    plt.show()

    # model1 = KMeans(n_clusters=2, random_state=123, init='k-means++')
    # model1.fit(data)
    # print(model1.cluster_centers_)
    # labels = model1.labels_
    # data['Claster'] = labels
    # print(data['Claster'].value_counts())

    # fig = go.Figure(data=[
    #     go.Scatter3d(x=data['param8'],
    #                  y=data['param7'],
    #                  z=data['param4'],
    #                  mode='markers',
    #                  marker_color=data['Claster'],
    #                  marker_size=8)
    # ])
    # fig.show()

    # model2 = AgglomerativeClustering(2, compute_distances=True)
    # model2.fit(data)
    # labels = model2.labels_
    # data['Claster'] = labels
    # data['Claster'].value_counts()

    # fig = go.Figure(data=[
    #     go.Scatter3d(x=data['param8'],
    #                  y=data['param7'],
    #                  z=data['param4'],
    #                  mode='markers',
    #                  marker_color=data['Claster'],
    #                  marker_size=4)
    # ])
    # fig.show()

    model3 = DBSCAN(eps=5, min_samples=3).fit(data)
    labels = model3.labels_
    data['Claster'] = labels
    # print(data['Claster'].keys())
    print(data['Claster'])

    inc = 0
    inc1 = 0

    for (x, y) in enumerate(data['Claster']):
        if y == -1:
            inc += 1
        if y == 0:
            inc1 += 1

    print(inc)
    print(inc1)

    fig = go.Figure(data=[
        go.Scatter3d(x=data['param8'],
                     y=data['param7'],
                     z=data['Claster'],
                     mode='markers',
                     marker_color=data['Claster'],
                     marker_size=4)
    ])
    fig.show()
