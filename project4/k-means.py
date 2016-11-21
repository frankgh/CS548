import csv
import argparse
import numpy as np
from time import time
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
import matplotlib.pyplot as plt


def bench_k_means(estimator, name, data):
    t0 = time()
    estimator.fit(data)

    print('%12s %13.2fs %15i %15.3f %15s'
          % (name, (time() - t0), estimator.inertia_,
             metrics.silhouette_score(data, estimator.labels_, metric='euclidean', sample_size=len(data)),
             estimator.n_iter_))
    # print('Labels')
    # print(estimator.labels_)


def read_csv_file():
    X = None
    labels = None
    count = 0

    with open(args.input_file, 'rb') as csvfile:
        data_reader = csv.reader(csvfile)
        for row in data_reader:

            if count == 0:
                labels = row
            else:
                if X is None:
                    X = np.array([row])
                else:
                    X = np.append(X, [row], axis=0)

            count += 1

    return X, labels


def cluster_data():
    X, labels = read_csv_file()

    # scale the data
    X = scale(X)
    n_clusters = int(args.n_clusters) if args.n_clusters else 2

    # print(kmeans.labels_)

    print('%12s %14s %15s %15s %15s' % ('init', 'time', 'inertia', 'silhouette', 'iterations'))
    k_means = KMeans(init='k-means++', n_clusters=n_clusters, random_state=0, n_init=100)
    bench_k_means(k_means, name="k-means++", data=X)
    pca = PCA(n_components=n_clusters).fit(X)
    bench_k_means(KMeans(init=pca.components_, n_clusters=n_clusters, random_state=0, n_init=1),
                  name="PCA-based", data=X)

    start_time = time()
    reduced_data = PCA(n_components=2).fit_transform(X)
    kmeans = KMeans(init='k-means++', n_clusters=n_clusters, random_state=0, n_init=10)
    kmeans.fit(reduced_data)
    bench_k_means(k_means, name='PCA-based 2', data=X)
    print("--- %s seconds ---" % (time() - start_time))

    print('Labels')
    print(kmeans.labels_)

    # Step size of the mesh. Decrease to increase the quality of the VQ.
    h = .02  # point in the mesh [x_min, x_max]x[y_min, y_max].

    # Plot the decision boundary. For that, we will assign a color to each
    x_min, x_max = reduced_data[:, 0].min() - 1, reduced_data[:, 0].max() + 1
    y_min, y_max = reduced_data[:, 1].min() - 1, reduced_data[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

    # Obtain labels for each point in mesh. Use last trained model.
    Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.figure(1)
    plt.clf()
    plt.imshow(Z, interpolation='nearest',
               extent=(xx.min(), xx.max(), yy.min(), yy.max()),
               cmap=plt.cm.Paired,
               aspect='auto', origin='lower')

    plt.plot(reduced_data[:, 0], reduced_data[:, 1], 'k.', markersize=2)
    # Plot the centroids as a white X
    centroids = kmeans.cluster_centers_
    plt.scatter(centroids[:, 0], centroids[:, 1],
                marker='x', s=169, linewidths=3,
                color='w', zorder=10)
    plt.title('K-means clustering on the patients dataset (PCA-reduced data)\n'
              'Centroids are marked with white cross')
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xticks(())
    plt.yticks(())
    plt.show()


parser = argparse.ArgumentParser(description='Generate k clusters using the k-means clustering algorithm.')
parser.add_argument('-i', dest='input_file', metavar='input_file', help='path for the input file', required=True)
parser.add_argument('-k', dest='n_clusters', metavar='n_clusters', help='The number of clusters')
args = parser.parse_args()

cluster_data()
