def num_1():
    print("Пункт 1")
    import pandas as pd
    from sklearn import preprocessing
    from sklearn.manifold import TSNE
    import matplotlib.pyplot as plt
    import seaborn as sns
    import time

    data = pd.read_csv('zoo.csv')
    class_name = pd.read_csv('class_type.csv')
    d = data.drop(['class_type', 'animal_name'], axis=1)

    scaler = preprocessing.MinMaxScaler()
    d = pd.DataFrame(scaler.fit_transform(d), columns=d.columns)

    start_time = time.time()
    t = TSNE(n_components=2, perplexity=50, random_state=123)
    tsne_features = t.fit_transform(d)
    data = d.copy()

    data['x'] = tsne_features[:, 0]
    data['y'] = tsne_features[:, 1]
    print("--- %s seconds ---" % (time.time() - start_time))

    fig = plt.figure()
    plt.title(f'perplexity = 50')
    sns.scatterplot(x='x',
                    y='y',
                    hue=class_name['class_type'],
                    data=data,
                    palette='bright')
    plt.show()


def num_2():
    print("Пункт 2")
    import pandas as pd
    import umap
    import matplotlib.pyplot as plt
    import seaborn as sns

    data = pd.read_csv('zoo.csv')
    class_name = pd.read_csv('class_type.csv')
    n = (5, 25, 50)
    _d = (0.1, 0.6)
    u = dict()
    for i in range(len(n)):
        for j in range(len(_d)):
            u[(n[i], _d[j])] = (umap.UMAP(n_neighbors=n[i], min_dist=_d[j], random_state=123).fit_transform(data))
            fig = plt.figure()
            sns.scatterplot(x=u[(n[i], _d[j])][:, 0],
                            y=u[(n[i], _d[j])][:, 1],
                            hue=class_name['class_type'],
                            data=data,
                            palette='bright')
            plt.title(f'n_neighbors = {n[i]}, min_dist = {_d[j]}')
            plt.show()


def num_3():
    print("Пункт 3")
    import pandas as pd
    from sklearn import preprocessing
    from sklearn.manifold import TSNE
    import time
    data = pd.read_csv('zoo.csv')
    d = data.drop(['class_type', 'animal_name'], axis=1)

    scaler = preprocessing.MinMaxScaler()
    d = pd.DataFrame(scaler.fit_transform(d), columns=d.columns)

    start_time = time.time()
    t = TSNE(n_components=2, perplexity=50, random_state=123)
    tsne_features = t.fit_transform(d)
    data = d.copy()

    data['x'] = tsne_features[:, 0]
    data['y'] = tsne_features[:, 1]
    print("t-SNE --- %s seconds" % (time.time() - start_time))

    import umap

    um = dict()
    start_time = time.time()
    um[15, 0.1] = (umap.UMAP(n_neighbors=15, min_dist=0.1, random_state=123).fit_transform(data))
    print("UMAP --- %s seconds" % (time.time() - start_time))


if __name__ == '__main__':
    num_1()
